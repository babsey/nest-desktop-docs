.. _setup-nest-server:

NEST Server
===========

|nest|

NEST is a simulator for spiking neural network models that focuses on the dynamics, size and structure of neural systems
rather than on the exact morphology of individual neurons. The development of NEST is coordinated by the NEST
Initiative.

NEST is ideal for networks of spiking neurons of any size, for example:
- Models of information processing e.g. in the visual or auditory cortex of mammals,
- Models of network activity dynamics, e.g. laminar cortical networks or balanced random networks,
- Models of learning and plasticity.

.. seeAlso::
   Read the full installation guide of NEST Simulator :doc:`here <nest-simulator:installation/index>`.

The API Server for NEST is referred to as **NEST Server**. We highly recommend installing NEST 3, in which the NEST
server is implemented.

.. note::
   Before you start :code:`nest-server`, you are able to set these environment variables in bash:

   .. code-block:: bash

      export NEST_SERVER_DISABLE_AUTH=1
      export NEST_SERVER_ENABLE_EXEC_CALL=1
      export NEST_SERVER_DISABLE_RESTRICTION=1

   For more information read the full documentation of NEST Server
   :doc:`here <nest-simulator:connect_nest/nest_server>`.


Conda
-----

#. Activate the Conda environment :bdg:`nest`:

   .. code-block:: bash

      conda activate nest

#. Install NEST Simulator and dependencies for the API Server:

   .. code-block:: bash

      conda install nest-simulator flask flask-cors gunicorn restrictedpython

#. Start NEST Server as the back end:

   The API Server for NEST Simulator is referred to as **NEST Server**.

   .. code-block:: bash

      nest-server start

NEST Server is now running at http://localhost:52425.


Python
------

NEST Simulator has no python package but you can install it via conda or on host system:

#. Install the dependencies for the API Server of NEST Simulator:

   .. code-block:: bash

      pip install flask flask-cors gunicorn restrictedpython

#. Start NEST Server as the back end:

   The API Server for NEST Simulator is referred to as **NEST Server**.

   .. code-block:: bash

      nest-server start

NEST Server is now running at http://localhost:52425.


Source install
--------------

#. Download and unpack latest release package of NEST source code:

   .. code-block:: bash

      export NEST_VERSION=3.8
      wget https://github.com/nest/nest-simulator/archive/refs/tags/v${NEST_VERSION}.tar.gz -P /tmp
      cd /tmp && tar -zxvf v${NEST_VERSION}.tar.gz

#. Install requirements for NEST Simulator and NEST Server.

   .. code-block:: bash

      python3 -m pip install --upgrade pip setuptools wheel
      python3 -m pip install -r /tmp/nest-simulator-${NEST_VERSION}/requirements_pynest.txt
      python3 -m pip install -r /tmp/nest-simulator-${NEST_VERSION}/requirements_nest_server.txt

#. Prepare for build:

   .. code-block:: bash

      mkdir /tmp/nest-build && cd $_
      cmake -DCMAKE_INSTALL_PREFIX:PATH=$HOME/opt/nest /tmp/nest-simulator-${NEST_VERSION}
      make -j $(nproc)
      make install

#. Load NEST environment variables in Terminal:

   .. code-block:: bash

      source opt/nest/bin/nest_vars.sh

   .. hint::
      Add this line to `.bashrc`

#. Install NEST Server (in Python or Conda).