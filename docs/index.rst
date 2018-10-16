.. _index:

Dredd — HTTP API Testing Framework
==================================

|npm version| |Build Status| |Windows Build Status| |Dependency Status| |devDependency Status| |Documentation Status| |Coverage Status| |Known Vulnerabilities|

.. figure:: _images/dredd.png
   :alt: Dredd - HTTP API Testing Framework

..

   **Dredd is a language-agnostic command-line tool for validating API description document against backend implementation of the API.**

Dredd reads your API description and step by step validates whether your API implementation replies with responses as they are described in the documentation.

Features
--------

Supported API Description Formats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `API Blueprint <https://apiblueprint.org/>`__
-  `Swagger <https://swagger.io/>`__

Supported Hooks Languages
~~~~~~~~~~~~~~~~~~~~~~~~~

Dredd supports writing :ref:`hooks <hooks>` — a glue code for each test setup and teardown. Following languages are supported:

-  :ref:`Go <hooks-go>`
-  :ref:`Node.js (JavaScript) <hooks-nodejs>`
-  :ref:`Perl <hooks-perl>`
-  :ref:`PHP <hooks-php>`
-  :ref:`Python <hooks-python>`
-  :ref:`Ruby <hooks-ruby>`
-  :ref:`Rust <hooks-rust>`
-  Didn’t find your favorite language? :ref:`Add a new one! <hooks-new-language>`

Supported Systems
~~~~~~~~~~~~~~~~~

-  Linux, macOS, Windows, …
-  `Travis CI <https://travis-ci.org/>`__, `CircleCI <https://circleci.com/>`__, `Jenkins <https://jenkins.io/>`__, `AppVeyor <https://www.appveyor.com/>`__, …

Contents
--------

.. toctree::
   :maxdepth: 1

   installation
   quickstart
   how-it-works
   how-to-guides
   Usage: CLI <usage-cli>
   Usage: JavaScript <usage-js>
   About Hooks <hooks>
   Hooks: Go <hooks-go>
   Hooks: JavaScript (Sandboxed) <hooks-js-sandbox>
   Hooks: Node.js <hooks-nodejs>
   Hooks: Perl <hooks-perl>
   Hooks: PHP <hooks-php>
   Hooks: Python <hooks-python>
   Hooks: Ruby <hooks-ruby>
   Hooks: Rust <hooks-rust>
   Hooks: Other languages <hooks-new-language>
   data-structures
   contributing

Useful Links
------------

-  `GitHub Repository <https://github.com/apiaryio/dredd>`__
-  `Bug Tracker <https://github.com/apiaryio/dredd/issues?q=is%3Aopen>`__
-  `Changelog <https://github.com/apiaryio/dredd/releases>`__

Example Applications
--------------------

-  `Express.js <https://github.com/apiaryio/dredd-example>`__
-  `Ruby on Rails <https://gitlab.com/theodorton/dredd-test-rails/>`__

.. |npm version| image:: https://badge.fury.io/js/dredd.svg
   :target: https://www.npmjs.com/package/dredd
.. |Build Status| image:: https://travis-ci.org/apiaryio/dredd.svg?branch=master
   :target: https://travis-ci.org/apiaryio/dredd
.. |Windows Build Status| image:: https://ci.appveyor.com/api/projects/status/n3ixfxh72qushyr4/branch/master?svg=true
   :target: https://ci.appveyor.com/project/Apiary/dredd/branch/master
.. |Dependency Status| image:: https://david-dm.org/apiaryio/dredd.svg
   :target: https://david-dm.org/apiaryio/dredd
.. |devDependency Status| image:: https://david-dm.org/apiaryio/dredd/dev-status.svg
   :target: https://david-dm.org/apiaryio/dredd?type=dev
.. |Documentation Status| image:: https://readthedocs.org/projects/dredd/badge/?version=latest
   :target: https://dredd.readthedocs.io/en/latest/
.. |Coverage Status| image:: https://coveralls.io/repos/apiaryio/dredd/badge.svg?branch=master
   :target: https://coveralls.io/github/apiaryio/dredd
.. |Known Vulnerabilities| image:: https://snyk.io/test/npm/dredd/badge.svg
   :target: https://snyk.io/test/npm/dredd
