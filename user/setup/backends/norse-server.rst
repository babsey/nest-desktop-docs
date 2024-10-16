.. _norse-server:

Norse Server
============

|norse|

Norse aims to exploit the advantages of bio-inspired neural components, which are sparse and event-driven - a
fundamental difference from artificial neural networks. Norse expands PyTorch with primitives for bio-inspired neural
components, bringing you two advantages: a modern and proven infrastructure based on PyTorch and deep
learning-compatible spiking neural network components.


Conda |linux| |macOS| |windows|
-------------------------------

#. Activate the Conda environment :bdg:`nest`:

   .. code-block:: bash

      conda create -n norse norse

#. Install Norse Server:

   .. code-block:: bash

      python3 -m pip install norse-server@git+https://github.com/babsey/nestml-server

#. Start NEST Server as the back end:

   The API Server for NEST Simulator is referred to as **NEST Server**.

   .. code-block:: bash

      nest-server start

NEST Server is now running at http://localhost:52425.