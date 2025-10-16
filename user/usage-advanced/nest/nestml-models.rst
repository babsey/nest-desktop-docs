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

   For more information about NESTML server, please follow these instructions :ref:`here <setup-nestml-server>`


Workflow
--------

.. grid:: 2
   :gutter: 1

   .. grid-item::
      :columns: 2

      .. image:: /_static/img/screenshots/model/nestml/create-model-button.png

   .. grid-item::
      :columns: 10

      .. grid:: 1
         :gutter: 1

         .. grid-item::
            :child-align: center

            In model navigation sidebar, you find a :bdg:`+` button to create a new model. Clicking it opens a dialog.

.. grid:: 2
   :gutter: 1

   .. grid-item::
      :columns: 8

      .. image:: /_static/img/screenshots/model/nestml/create-model-dialog.png
   .. grid-item::
      :columns: 4

      .. grid:: 1
         :gutter: 1

         .. grid-item::
            :child-align: center

            In dialog you enter name for new model and select a template of NESTML models which can also be fetched from
            GitHub.

Next, you are able to enter text editor in Model editor view and then save it. It gets parameter and state
specifications from NESTML Server which are fetched from NESTML code.

.. image:: /_static/img/screenshots/model/nestml/model-editor.png

----

.. grid:: 2
   :gutter: 1

   .. grid-item::
      :columns: 9

      After the NESTML model has been defined, the code for the NESTML backend can be generated. Clicking the module
      button in model bar opens a dialog.

   .. grid-item::
      :columns: 3

      .. image:: /_static/img/screenshots/model/nestml/module-button.png

.. grid:: 2
   :gutter: 1

   .. grid-item::
      :columns: 8

      In dialog user can select a module to generate its models on NESTML backend.

   .. grid-item::
      :columns: 4

      .. image:: /_static/img/screenshots/model/nestml/module-dialog.png

.. grid:: 2
   :gutter: 1

   .. grid-item::
      :columns: 7

      Now, the module is then available for loading in the simulation kernel on the NEST backend.

   .. grid-item::
      :columns: 5

      .. image:: /_static/img/screenshots/model/nestml/simulation-kernel-module.png

      |

      .. grid:: 1
         :gutter: 1

         .. grid-item::

            .. image:: /_static/img/screenshots/model/nestml/code-install-module.png
               :width: 60%


The neuron model is now available to be instantiated in a network. As a first validation step, we create one single
neuron and stimulate it with a constant current, while measuring the membrane potential and recovery variable. The
recordings can be viewed interactively within the NEST Desktop environment.
