.. _activity-chart-graph:

Activity chart graph
====================

The chart graph contains graphical panels organized in vertical stacks. Chart panels are introduced specifically to
explore the network activity by mouse interaction. The simulation produces two different types of data sets: Spike
events (recorded by :bdg:`spike recorder`) contain times and sender ids whereas analog signals contain continuous
quantities from the recording devices (:bdg:`voltmeter` or :bdg:`multimeter`).

.. seeAlso::
   :ref:`Use controller for activity graph<controller-sidebar-activity-chart-controller>`

|

.. _activity-chart-graph-analog-signals:

|chart-line| Analog signals
---------------------------

.. grid:: 2

   .. grid-item::
      :columns: 7

      .. image:: /_static/img/screenshots/activity/activity-chart-graph-step-input.png

   .. grid-item::
      :columns: 5

      By default, it displays a line trace of the membrane potential.

.. grid:: 2

   .. grid-item::
      :columns: 7

      .. image:: /_static/img/screenshots/activity/activity-chart-graph-noise.png

   .. grid-item::
      :columns: 5

      With noise input (:bdg:`noise generator`), it shows noise behavior (fluctuation) of the membrane potentials and
      histogram of distributed values.


.. _activity-chart-graph-spike-activity:

|chart-scatter-plot| Spike activity
-----------------------------------

.. grid:: 2

   .. grid-item::
      :columns: 7

      .. image:: /_static/img/screenshots/activity/activity-chart-graph-spike.png

   .. grid-item::
      :columns: 5

      By default, it displays a raster plot of the spike times as well as a time histogram of spikes.

.. grid:: 2

   .. grid-item::
      :columns: 7

      .. image:: /_static/img/screenshots/activity/activity-chart-graph-spike-value-histogram.png

   .. grid-item::
      :columns: 5

      It displays a value histogram of the inter-spike intervals (ISI) as well as of the coefficients of variation of
      the ISI (CV of ISI) for the population.

.. grid:: 2

   .. grid-item::
      :columns: 7

      .. image:: /_static/img/screenshots/activity/activity-chart-graph-spike-sender-histogram.png

   .. grid-item::
      :columns: 5

      It displays spike count, average Inter-spike interval (ISI) and coefficient of variation (CV of ISI) for each
      sender, e.g. neuron.
