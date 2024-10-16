.. grid:: 2
   :gutter: 1

   .. grid-item-card:: Step 1: Construct network
      :columns: 7

      If you want to construct a network, you will have to open the network editor. The network editor shows the network
      graph composed of nodes (shapes) and connections (lines).

   .. grid-item::
      :child-align: center
      :columns: 5

      .. image:: /_static/img/screenshots/network/network-graph.png

   .. grid-item::
      :child-align: center
      :columns: 4

      .. image:: /_static/img/gif/create-nodes.gif
         :target: #create-nodes

   .. grid-item-card:: Step 1a: Create nodes
      :columns: 8

      In order to create a new node, you can click with the right mouse button in the network editor and a `pie` panel
      with three letters appears to select an element type. A node is divided into three element types: stimulator
      (:bdg:`S`), recording (:bdg:`R`) device and neuron (:bdg:`N`). Then it creates a node of the selected element
      type.

   .. grid-item::
      :child-align: center
      :columns: 4

      .. image:: /_static/img/gif/connect-nodes.gif
         :target: #connect-nodes
         :width: 240px

   .. grid-item-card:: Step 1b: Connect nodes
      :columns: 8

      Forming a network of nodes is defined by making connections between and within nodes. In order to connect nodes,
      you can click on a connector of a node, then move the mouse towards anther node and finally click on a target
      node. It creates a connection between source and target nodes.

.. hint::
   By pressing the hotkey :keys:`alt` and clicking a node at the same time, you enable the connecting mode or continue
   connecting other nodes.

.. grid:: 2

   .. grid-item-card:: Step 1c: Select model and parameters
      :columns: 7

      You are able to select the model of a node in the network controller. Then it shows a list of parameters which you
      might want to work on. Finally, you are able to change the values of visible parameters.

   .. grid-item::
      :child-align: center
      :columns: 5

      .. image:: /_static/img/gif/edit-node.gif
         :target: #select-model-and-parameters
         :width: 320px

