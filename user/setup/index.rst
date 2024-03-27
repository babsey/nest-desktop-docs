.. _setup-guide:

===================
|setup| Setup Guide
===================

.. toctree::
   :hidden:

   AppImage <appimage>
   Apptainer <apptainer>
   Conda <conda>
   Docker Compose <docker-compose>
   Python <python>
   Snap <snap>

This guide provides a detailed documentation on how to install and start both instances: NEST Desktop and NEST
Simulator.

.. note::
   To enable the full functionality of NEST Desktop, you also need to install NEST Simulator on your computer. NEST
   Simulator provides an API Server which can forward requests to the simulation engine. In summary, you have to start
   NEST Server as well.

   You can find the detailed information on NEST Server in
   :doc:`NEST Simulator user documentation <nest-simulator:connect_nest/nest_server>`.

----

**Desktop applications**

You are able to use NEST Desktop as Snap (with NEST Simulator) or as AppImage (without NEST Simulator).

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: Snap |linux| |macOS|
      :columns: 6
      :link: snap
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 4

            |snap|

         .. grid-item::
            :columns: 8

            Install and start NEST Desktop with Snap (with NEST Server).

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

            Download and start NEST Desktop as AppImage (without NEST Server).


**Virtualizations**

Docker (or Docker Compose) and Apptainer provide both NEST Desktop and NEST Simulator, so you have everything you need
to run NEST Desktop and NEST Simulator.

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

            Deploy NEST Desktop and NEST Simulator with Docker Compose.

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

            Deploy NEST Desktop and NEST Simulator with Apptainer.


**Packages**

Alternatively, you can install NEST Desktop with the ``conda`` or ``pip`` command.

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: Conda |linux| |windows| |macOS|
      :columns: 6
      :link: setup-conda
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 4

            |conda|

         .. grid-item::
            :columns: 8

            Deploy NEST Desktop and NEST Simulator with Conda.

   .. grid-item-card:: Python |linux| |windows| |macOS|
      :columns: 6
      :link: setup-python
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 4

            |python-logo|

         .. grid-item::
            :columns: 8

            Install and start only NEST Desktop from Python Package.

----

Once you start NEST Desktop, you can see the start page containing an image of a laptop with the NEST logo on its
screen. At the bottom it shows a short description of NEST Desktop (left) and some useful links and the current version
(right).

.. image:: /_static/img/screenshots/start-page.png
   :target: #
   :width: 100%
