.. grid:: 2

   .. grid-item::
      :columns: 6

      .. image:: /_static/img/screenshots/activity/activity-explorer.png

   .. grid-item-card:: Step 3: Explore activity
      :columns: 6

      The network activity is composed of neuronal properties (neuron positions and ids) and recorded events from
      recording devices. Events can be subdivided in two groups: spike events and analog signals. Spike events contain
      times and ids of the senders emitting events to the recording devices which can be considered as collectors
      (:bdg:`spike recorder`). Analog signals contain continuous quantities from the recording devices aka samplers
      (:bdg:`voltmeter` or :bdg:`multimeter`) which query their targets at given time intervals. Network activity can be
      explored in :doc:`Activity chart graph </user/usage-advanced/activity-chart-graph>` (|chart-line| or
      |chart-scatter-plot|) :doc:`Activity animation graph </user/usage-advanced/activity-animation-graph>` (|axis-arrow|),
      or :ref:`controller-sidebar-activity-statistics` (|stats|).
