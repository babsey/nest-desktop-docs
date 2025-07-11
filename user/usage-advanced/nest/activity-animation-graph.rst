.. _activity-animation-graph:

|axis-arrow| Activity animation graph
=====================================

It displays an animated 3D graph for the spatial network forming layers in topology whose neurons have geographical
positions.

.. seeAlso::
   - :ref:`Use controller for activity graph<controller-sidebar-activity-animation-controller>`

.. _activity-animation-graph-analog-signals:

Analog signals
--------------

.. grid:: 2

   .. grid-item::
      :columns: 5

      .. image:: /_static/img/gif/anim-analog-signals.gif

   .. grid-item::
      :columns: 7

      Analog signals contain continuous quantities from the recording devices (:bdg:`voltmeter` or :bdg:`multimeter`).

      It is possible to display an animated 3D graph for the spatial network forming layers in topology whose neurons
      have geographical positions.

      Each box represents a neuron in its geographical position. Values of the analog signals can be visualized using
      the colors of recorded event (here, it shows the color map :bdg:`spectral`).


.. _activity-animation-graph-spike-activity:

Spike activity
--------------

.. grid:: 2

   .. grid-item::
      :columns: 5

      .. image:: /_static/img/gif/anim-spike-activity.gif

   .. grid-item::
      :columns: 7

      Spike events contain times and ids of the senders collected by the :bdg:`spike recorder`.

      Spikes can be visualized as transient blobs appearing in the animated 3D graph. To follow the spike activity
      better, the trail length can be increased.

      Optionally, trails can be faded after the spike time, and a growing or shrinking mode can also be applied.
