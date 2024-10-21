.. _backends:

Backends
--------

NEST Desktop requires backends for the full functionality. Each backend provides an API Server which can forward
requests to the simulation engine.


.. toctree::
   :hidden:

   NEST Simulator <nest-server>
   NESTML <nestml-server>
   Norse Simulator <norse-server>


.. grid:: 3
   :gutter: 2

   .. grid-item-card:: NEST Simulator
      :columns: 4
      :link: setup-nest-server
      :link-type: ref

      |nest|

      Simulator for spiking neural network models

   .. grid-item-card:: NESTML
      :columns: 4
      :link: setup-nestml-server
      :link-type: ref

      |nestml|

      Domain-specific language for neuron and synapse models

   .. grid-item-card:: Norse Simulator
      :columns: 4
      :link: setup-norse-server
      :link-type: ref

      |norse|

      Deep learning with spiking neural networks in PyTorch

