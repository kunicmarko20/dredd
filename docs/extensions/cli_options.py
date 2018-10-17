import os
import json

from docutils import nodes
from docutils.statemachine import ViewList

from sphinx.util.compat import Directive
from sphinx.util.nodes import nested_parse_with_titles


class CLIOptionsDirective(Directive):
    required_arguments = 1

    def run(self):
        # Load options from given JSON file
        options_path = os.path.join(
            os.path.dirname(self.state.document['source']),
            self.arguments[0],
        )
        with open(options_path) as f:
            options = json.load(f)

        # Generate reStructuredText lines
        lines = []
        for name, attrs in sorted(options.items()):
            ref = name
            heading = f'.. option:: --{name}'
            if 'alias' in attrs:
                ref += f"-{attrs['alias']}"
                heading += f", -{attrs['alias']}"
            desc = f"   {attrs['description']}"
            if 'default' in attrs:
                value = attrs['default']
                value = 'null' if value is None else str(value).lower()
                desc += f' **Default value:** ``{value}``'
            lines += ['', f'.. _{ref}:', '', heading, '', desc, '']

        # Generate docutils nodes
        result = ViewList()
        for line in lines:
            result.append(line, f'<cli-options-directive>')
        node = nodes.section(document=self.state.document)
        nested_parse_with_titles(self.state, result, node)
        return node.children


def setup(app):
    app.add_directive('cli-options', CLIOptionsDirective)
    return {'version': '1.0', 'parallel_read_safe': True}
