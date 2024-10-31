.. grid:: 2
   :gutter: 1

   .. grid-item::
      :child-align: center
      :columns: 6

      .. image:: /_static/img/screenshots/activity/activity-explorer.png

   .. grid-item::
      :columns: 6

      .. grid:: 1
         :gutter: 1

         .. grid-item-card:: Step 3: Explore activity

            The network activity is composed of neuronal properties (neuron positions and ids) and recorded events from
            recording devices. Events can be subdivided in two groups: spike events and analog signals. Spike events
            contain times and ids of the senders emitting events to the recording devices which can be considered as
            collectors (:bdg:`spike recorder`). Analog signals contain continuous quantities from the recording devices
            aka samplers (:bdg:`voltmeter` or :bdg:`multimeter`) which query their targets at given time intervals.
            Network activity can be explored in :ref:`Activity chart graph <activity-chart-graph>`
            (|chart-line| or |chart-scatter-plot|) :ref:`Activity animation graph
            <activity-animation-graph>` (|axis-arrow|), or
            :ref:`controller-sidebar-activity-statistics` (|stats|).
