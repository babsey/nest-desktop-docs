.. _setup-guide:

===================
|setup| Setup Guide
===================

.. toctree::
   :hidden:

   AppImage <appimage>
   Apptainer <apptainer>
   Backends <backends/index>
   Docker Compose <docker-compose>
   Flatpak <flatpak>
   Mamba (Conda) <mamba>
   Python <python>
   Snap <snap>

This guide provides a detailed documentation on how to install and start NEST Desktop.

.. note::
   To enable the full functionality of NEST Desktop, you also need to install backends on your computer. Each backend
   provides an API Server which can forward requests to the simulation engine.

   You can find the detailed information on backend setup :doc:`here <backends/index>`.

----

**Desktop applications**

You are able to use NEST Desktop as Snap, Flatpak or AppImage.

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: Snap |linux| |macOS|
      :columns: 6
      :link: setup-snap
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 4

            |snap|

         .. grid-item::
            :columns: 8

            Install and start NEST Desktop as Snap (with NEST and NESTML Backend).

   .. grid-item-card:: Flatpak |linux|
      :columns: 6
      :link: setup-flatpak
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 4

            |flatpak|

         .. grid-item::
            :columns: 8

            Install and run NEST Desktop as Flatpak (with NEST backends).

   .. grid-item-card:: AppImage |linux|
      :columns: 6
      :link: setup-appimage
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 4

            |AppImage|

         .. grid-item::
            :columns: 8

            Download and start NEST Desktop as AppImage (without any backends).


**Virtualizations**

Docker (or Docker Compose) and Apptainer provide both NEST Desktop and NEST Backend, so you have everything you need
to run NEST Desktop and NEST Backend.

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: Docker Compose |linux| |windows| |macOS|
      :columns: 6
      :link: setup-docker-compose
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 4

            |docker-compose|

         .. grid-item::
            :columns: 8

            Setup NEST Desktop and NEST Simulator with Docker Compose.

   .. grid-item-card:: Apptainer (Former Singularity) |linux|
      :columns: 6
      :link: setup-apptainer
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 4

            |apptainer|

         .. grid-item::
            :columns: 8

            Setup NEST Desktop and NEST Simulator with Apptainer.


**Packages**

Alternatively, you can install NEST Desktop with the ``conda`` or ``pip`` command.

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: Mamba (Conda) |linux| |windows| |macOS|
      :columns: 6
      :link: setup-mamba
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 4

            |conda-forge|

         .. grid-item::
            :columns: 8

            Setup NEST Desktop (without backends) with Mamba (from Conda-forge).

   .. grid-item-card:: Python |linux| |windows| |macOS|
      :columns: 6
      :link: setup-python
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 4

            |python|

         .. grid-item::
            :columns: 8

            Setup NEST Desktop (without backends) from Python Package.