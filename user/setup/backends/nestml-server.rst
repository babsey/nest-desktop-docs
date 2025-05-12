.. _setup-nestml-server:

NESTML Server
=============

|nestml|

NESTML is a domain-specific language for neuron and synapse models. These dynamical models can be used in simulations of
brain activity on several platforms, in particular the NEST Simulator.

NESTML combines:
- Concise yet expressive syntax inspired by Python. Easy to write and understand. Precise and unambiguous.
- Direct language support for (spike) events, differential equations, convolutions, stochasticity, and arbitrary
algorithms using imperative programming concepts.
- Generated code approaches runtime and memory efficiency of hand-coded models.

.. info::

   We tested nestml and nestml-server with Python 3.11.

.. seeAlso::
   Read the full installation guide of NESTML :doc:`here <nestml:installation>`.

The API Server for NESTML is referred to as **NESTML Server**.

.. note::
   NEST has to find custom, NESTML-compiled models. Before you start :code:`nest-server`, you have to set module path
   for environment variable in bash:

   .. code-block:: bash

      export NESTML_MODULE_PATH=/tmp/nestmlmodules
      nest-server start


Mamba (Conda)
-------------

#. Activate the Mamba environment :bdg:`nest`:

   .. code-block:: bash

      mamba activate nest

#. Install NESTML:

   .. code-block:: bash

      mamba install nestml

#. Install NESTML Server:

   .. code-block:: bash

      python3 -m pip install nestml-server@git+https://github.com/babsey/nestml-server@v1.0

#. Start NESTML Server as backend:

   .. code-block:: bash

      nestml-server start

NESTML Server is now running at http://localhost:52426.

.. note::
   NEST has to find custom, NESTML-compiled models. Before you start :code:`nest-server`, you have to set module path
   for environment variable in bash:

   .. code-block:: bash

      mamba activate nest
      mamba env config vars set NESTML_MODULE_PATH=/tmp/nestmlmodules

Python
------


#. Install NESTML and dependencies for the NESTML Server:

   .. code-block:: bash

      python3 -m pip install nestml flask flask-cors gunicorn

#. Install NESTML Server:

   .. code-block:: bash

      python3 -m pip install nestml-server@git+https://github.com/babsey/nestml-server@v1.0

#. Start NESTML Server as the back end:

   .. code-block:: bash

      nestml-server start

NEST Server is now running at http://localhost:52426.
