.. _setup-norse-server:

Norse Server
============

|norse|

Norse aims to exploit the advantages of bio-inspired neural components, which are sparse and event-driven - a
fundamental difference from artificial neural networks. Norse expands PyTorch with primitives for bio-inspired neural
components, bringing you two advantages: a modern and proven infrastructure based on PyTorch and deep
learning-compatible spiking neural network components.

.. seeAlso::
   Read the full installation guide of Norse :doc:`here <norse:pages/installing>`.

The API Server for Norse Simulator is referred to as **Norse Server**.

.. note::
   Before you start :code:`norse-server`, you are able to set these environment variables in bash:

   .. code-block:: bash

      export NEST_SERVER_DISABLE_RESTRICTION=1


Conda
-----

#. Activate the Mamba environment :bdg:`norse`:

   .. code-block:: bash

      mamba create -n norse norse

#. Install Norse Server:

   .. code-block:: bash

      python3 -m pip install norse-server@git+https://github.com/babsey/norse-server

#. Start Norse Server as the backend:

   .. code-block:: bash

      norse-server start

Norse Server is now running at http://localhost:11428.

.. info::

   Disable restriction

   .. code-block:: bash

      mamba activate norse
      mamba env config vars set NORSE_SERVER_DISABLE_RESTRICTION=1
