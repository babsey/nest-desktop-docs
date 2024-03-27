.. _compartmental-neuron:

Compartmental neuron
====================

NEST Simulator is actually a simulation tool of point-neurons but it also provides a model :bdg:`cm_default` which is a
neurons with compartments. Here, the guide shows the steps to create a simple neuron with compartments.


.. _compartmental-model-steps-how-to:

Step by step guide
------------------

.. grid:: 2

   .. grid-item::
      :columns: 6

      First import :bdg:`cm_default` from GitHub and create a node with :bdg:`cm_default`. Then open node selection
      popup, add compartments (|new|) and select compartment parameters to modify. Add receptors (|new|) in each
      compartment and select receptor parameters to modify.

      Click on the chips (:bdg:`soma 1`, :bdg:`dendrite 1`, ...) of a compartment to see its content.

   .. grid-item::
      :columns: 6

      .. image:: /_static/img/screenshots/controller/compartmental-neuron-step1.png
         :target: #

.. grid:: 2

   .. grid-item::
      :columns: 6

      You can modify the values in each compartment and and its receptors.

   .. grid-item::
      :columns: 6

      .. image:: /_static/img/screenshots/controller/compartmental-neuron-step2.png
         :target: #

.. note::
   Use :bdg:`multimeter` to record events from various compartments.
