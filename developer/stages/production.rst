Build and publish
=================

Currently, we build NEST Desktop for multiple targets and publish them on various platforms.

.. note::
   Please be aware that a lot of steps are already covered by our `GitLab CI process <continuous-integration.html#gitlab>`__.
   Therefore, we recommend to inspect the ``.gitlab-ci.yml`` file together with this chapter.
   It might also be helpful to have a look at the commands defined in ``package.json``.

.. _production-docker:

Docker
-----

.. image:: /_static/img/logo/Moby-logo.png
   :alt: Docker
   :width: 240px
   :target: #production-docker

After building the app to the output folder with the command ``yarn build``, build a docker image

.. code-block::

   docker build -t nest/nest-desktop:latest -f docker/nest-desktop-build/Dockerfile .

Then tag image with other version

.. code-block::

   docker tag nest/nest-desktop:latest nest/nest-desktop:4.0
   docker tag nest/nest-desktop:latest nest/nest-desktop:4.0.0

Finally push all docker images

.. code-block::

   docker push nest/desktop:latest


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

Then generate the app package using ``yarn``. It builds output into the folder ``nest_desktop/app``:

.. code-block:: bash

   yarn build

Clean output files before you perform the second step:

.. code-block:: bash

   yarn clean

The second step is to build the Python packages of `nest-desktop` for PyPI:

.. code-block:: bash

   python3 -m build -o pydist

Upload
^^^^^^

Finally, the package is ready for the the publication. You can upload the pip-package of ``nest-desktop`` to PyPI:

.. code-block:: bash

   python3 -m twine upload pydist/*

Do not forget to commit the changes you made and set a new version tag in git.

.. code-block:: bash

   git tag v4.0 -m 'v4.0.x'
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

.. code-block:: bash

   conda smithy rerender -c auto

Then make a pull request on the upstream repository. The CI will build package for conda-forge.


.. _production-appImage:

AppImage
--------

In ``package.json``, there are also yarn commands configured to build an Electron app.

.. code-block:: bash

   yarn app:build --linux AppImage

Then upload the ``.appImage`` file to the release on https://github.com/nest-desktop/nest-desktop-AppImage.

.. seeAlso::
   If you want to build other Electron packages, please have a look into ``electron-builder.yml`` file.


.. _production-flatpak:

Flatpak
-------

First install flatpak

.. code-block:: bash

   sudo apt install flatpak
   flatpak remote-add --if-not-exists --user flathub https://dl.flathub.org/repo/flathub.flatpakrepo
   sudo apt install gnome-software-plugin-flatpak gnome-software
   sudo apt install flatpak-builder


Change files and version in the ``io.github.nest_desktop.nest-desktop.yml`` file from
https://github.com/nest-desktop/nest-desktop-flathub.

Build and install flatpak in user folder:

.. code-block:: bash

   flatpak-builder --force-clean --user --install-deps-from=flathub --install builddir io.github.nest_desktop.nest-desktop.yml

If it worked locally, then make a pull request on the upstream repository. The CI will build flatpak for flathub.

.. seeAlso::
   For more information, please read the guide https://docs.flatpak.org/en/latest/index.html


.. _production-snap:

Snap
----

First, install snapcraft

.. code-block:: bash

   sudo snap install snapcraft --classic

.. note::
   Running LXD and Docker on the same host can cause connectivity issues. To fix it, please read this:
   https://documentation.ubuntu.com/lxd/en/latest/howto/network_bridge_firewalld/#prevent-connectivity-issues-with-lxd-and-docker


To build and pack NEST Desktop with snapcraft:

.. code-block:: bash

   snapcraft

Then install the snap file locally:

.. code-block:: bash

   sudo snap install <snap-file> --dangerous

Finally, upload the snap file:

.. code-block:: bash

   snapcraft upload <snap-file>

.. seeAlso::
   For Snap packages, you can find more information in the `Snap repository for nest-desktop
   <https://github.com/nest-desktop/nest-desktop-snap>`__.
