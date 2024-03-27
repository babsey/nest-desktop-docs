.. _python:

Python |linux| |macOS| |windows|
================================

.. grid:: 2

   .. grid-item::
      :columns: 9

      PyPI contains packages of NEST Desktop and NEST Simulator. We recommend to install both packages.

   .. grid-item::
      :columns: 3

      .. image:: /_static/img/logo/python-logo.png
         :target: #
         :width: 120px


NEST Simulator
--------------

#. Install NEST Simulator (SKIP THIS STEP IF YOU HAVE NEST 3 INSTALLED.):

   Read the full installation guide of NEST Simulator :doc:`here <nest-simulator:installation/index>`.

   We highly recommend installing NEST 3. With NEST 3, the API server (i.e., NEST Server) is already implemented.

#. Install the dependencies for the API Server of NEST Simulator:

   .. code-block:: bash

      pip install flask flask-cors RestrictedPython gunicorn

#. Start NEST Server as the back end:

   The API Server for NEST Simulator is referred to as **NEST Server**.

   .. code-block:: bash

      nest-server start

NEST Server is now running at http://localhost:52425.

.. note::
   Before you start :code:`nest-server`, you have to set these environment variables in bash:

   .. code-block:: bash

      export NEST_SERVER_DISABLE_AUTH=1
      export NEST_SERVER_ENABLE_EXEC_CALL=1
      export NEST_SERVER_DISABLE_RESTRICTION=1

   For more information read the full documentation of NEST Server
   :doc:`here <nest-simulator:connect_nest/nest_server>`.

NEST Desktop
------------

#. Install NEST Desktop

   NEST Desktop is available on PyPI and can be installed with the ``pip`` command:

   .. code-block:: bash

      pip3 install nest-desktop [--user] [--upgrade]

   For more information, please read the complete installing guide :doc:`here </user/setup/index>`.

#. Start NEST Desktop (in another terminal session):

   .. code-block:: bash

      nest-desktop start

Now NEST Desktop is started. You can use NEST Desktop in the web browser at http://localhost:54286.

**The installation is now complete!**
:doc:`Now you can start constructing networks for the simulation! </user/usage-basic/index>`

.. seeAlso::
   For more information read the full documentation of the command API
   :doc:`here </user/usage-advanced/command-API>`.