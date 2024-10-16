.. _nestml-models:

NESTML models
=============

The NEST Simulator kernel contains a number of built-in neuron models and synaptic plasticity rules. With NESTML, the
user no longer needs to write C++ code (used by NEST for performance reasons), eliminating the challenge for researchers
without a programming background to customize and extend the NEST built-in neuron and synapse models. However,
previously, NEST Desktop could only access the built-in models of NEST.

Here, the integration of NEST Desktop and NESTML allows researchers and students to customize existing models or develop
new ones using NESTML. Then NEST Desktop have them instantly available to create networks using the graphical interface
of NEST Desktop, before simulating them scalably and efficiently using NEST thanks to code generation. The combined
strength of these components creates a low-barrier environment for rapid prototyping and exploration of neuron, synapse
and network models.


.. note::
   You have to start NESTML server that you are able to create your custom models.

   For more information about NESTML server, please follow these instructions :doc:`here <nestml>`


Workflow
--------



Creating a new model (1) opens a text editor in which the NESTML model code can be entered (2). NESTML models can also
be fetched from GitHub (3). Eachodel is assigned to a specific module (4) for dynamical loading into the NEST kernel.


After the NESTML model has been defined, the code for the NESTML backend can be generated. Clicking the module button
opens a dialog (5) in which user can select a module to generate its models on NESTML backend (6). The module is then
available for loading in the simulation kernel on the NEST backend (7).

The neuron model is now available to be instantiated in a network. As a first validation step, we create one single
neuron and stimulate it with a constant current, while measuring the membrane potential and recovery variable (8). The
recordings can be viewed interactively within the NEST Desktop environment (9).