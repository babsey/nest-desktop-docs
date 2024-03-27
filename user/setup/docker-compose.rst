.. _docker-compose:

Docker Compose |linux| |macOS| |windows|
========================================

.. grid:: 2

   .. grid-item::
      :columns: 9

      Docker is a virtualization software packaging applications and its dependencies. Docker Compose is a tool for
      running multi-container applications on Docker which uses the Compose file format.

   .. grid-item::
      :columns: 3

      .. image:: /_static/img/logo/docker-compose-logo.png
         :target: #
         :width: 120px


.. seeAlso::
   For further information, please see the `official page of Docker Compose <https://github.com/docker/compose>`__.

Installation
------------

Docker Compose is available on multiple platforms. This guide demonstrates some of the ways to install it on Linux,
macOS and Windows.

.. tab-set::

   .. tab-item:: Linux |linux|

      Install Docker and Docker Compose in Terminal

      .. code-block:: bash

         apt install docker.io docker-compose

      **Pull and start Docker containers**

      #. Get the configuration file for Docker Compose (`docker-compose.yml
         <https://raw.githubusercontent.com/nest-desktop/nest-desktop/main/docker-compose.yml>`__)

         .. code-block:: bash

            wget https://raw.githubusercontent.com/nest-desktop/nest-desktop/main/docker-compose.yml

      #. Start NEST Desktop and NEST Simulator in a single command:

         .. code-block:: bash

            docker-compose up

   .. tab-item:: macOS |macOS| and Windows |windows|

      Docker Compose is included in Docker Desktop for macOS and Windows. For more information, take a look at the
      `installation guide of Docker Desktop <https://www.docker.com/get-started>`__.

|

Now, the service starts the containers for NEST Desktop and NEST Simulator. You can use NEST Desktop in the web browser
at http://localhost:54286.

**The installation is now complete!** :doc:`Now you can start constructing networks for the simulation!
</user/usage-basic/index>`

.. seeAlso::
   For more information (like running the containers without root password, etc.), please read the full documentation
   of `NEST Desktop Docker <https://github.com/nest-desktop/nest-desktop-docker>`__.
