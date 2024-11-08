Build and publish
=================

Currently, we build NEST Desktop for multiple targets and publish them on various platforms.

.. note::
   Please be aware that a lot of steps are already covered by our `GitLab CI process <continuous-integration.html#gitlab>`__.
   Therefore, we recommend to inspect the ``.gitlab-ci.yml`` file together with this chapter.
   It might also be helpful to have a look at the commands defined in ``package.json``.


.. _production-python:

Python
------

.. image:: /_static/img/logo/python-logo.png
   :alt: Python
   :width: 240px
   :target: #production-python


Building and pushing NEST Desktop on `PyPI <https://pypi.org/project/nest-desktop/>`__ is a required step for the
production. After that, Docker Hub can upgrade NEST Desktop in the provided Docker image.

Requirements
  - build, twine

The Python Package Index **nest-desktop** includes an executive command ``nest-desktop`` and a Python library
``nest_desktop``.

Build
^^^^^

The current working directory is ``nest-desktop``.

The building phase contains two steps:

The first step is to build a package of NEST Desktop using ``vite``.

Initially, you have to upgrade the version of NEST Desktop in:

- ``packages.json``
- ``nest_desktop/__init__.py``

Then generate the app package using ``yarn``. It builds the folder ``nest_desktop/app``:

.. code-block:: bash

   yarn build

The second step is to build a pip package for PyPI:

.. code-block:: bash

   yarn clean

The second step is to build the Python packages of `nest-desktop` for PyPI:

.. code-block:: bash

   python3 -m build -o pydist

|

Upload
^^^^^^

Finally, the package is ready for the the publication. You can upload the pip-package of ``nest-desktop`` to PyPI:

.. code-block:: bash

   python3 -m twine upload pydist/*

Do not forget to commit the changes you made and set a new version tag in git.

.. code-block:: bash

   git tag -a v4.0 -m 'v4.0.0'
   git push --tags


.. _production-conda:

Conda
-----

.. image:: /_static/img/logo/conda-logo.png
   :alt: Conda
   :width: 240px
   :target: #production-conda

We have a conda-smithy `repository for nest-desktop <https://github.com/nest-desktop/nest-desktop-conda>`__.
When a new Python package is released, we can change the version in ``meta.yaml`` (|see| the meta content `online
<https://github.com/nest-desktop/nest-desktop-conda/blob/main/recipe/meta.yaml>`__):

.. code-block::

   {% set version = "4.x.y" %}

.. note::
   It is also important to change the ``sha256`` checksum of the source of ``tar.gz`` file.

Then make a pull request on the base branch of this repository.


.. _production-appImage:

AppImage (``.appImage`` package)
---------------------------

In ``package.json``, there are also yarn commands configured to build an Electron app.

.. code-block:: bash

   yarn app:build --linux appImage

Then upload the ``.appImage`` file to the release on https://github.com/nest-desktop/nest-desktop-AppImage.

.. seeAlso::
   If you want to build other Electron packages, please have a look into ``electron-builder.yml`` file.


.. _production-snap:

Snap (``.snap`` package)
------------------------

By default snapcraft runs with 2G memory, which is not enough for building electron. To use snapcraft with larger
memory:

.. code-block:: bash

   SNAPCRAFT_BUILD_ENVIRONMENT_MEMORY=8G snapcraft

Then install the snap file locally:

.. code-block:: bash

   sudo snap install <snap-file> --dangerous

Finally, upload the snap file:

.. code-block:: bash

   snapcraft upload <snap-file>

.. seeAlso::
   For Snap packages, you can find more information in the `Snap repository for nest-desktop
   <https://github.com/nest-desktop/nest-desktop-snap>`__.
