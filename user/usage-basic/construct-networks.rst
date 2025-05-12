.. grid:: 2
   :gutter: 1

   .. grid-item::
      :columns: 7

      .. grid:: 1
         :gutter: 1

         .. grid-item-card:: Step 1: Construct network

            If you want to construct a network, you will have to open the network editor. The network editor shows the
            network graph composed of nodes (shapes) and connections (lines).

   .. grid-item::
      :child-align: center
      :columns: 5

      .. image:: /_static/img/screenshots/network/network-graph.png

   .. grid-item::
      :columns: 4

      .. image:: /_static/img/gif/create-node.gif

   .. _usage-basic-create-nodes:

   .. grid-item::
      :child-align: center
      :columns: 8

      .. grid:: 1
         :gutter: 1

         .. grid-item-card:: Step 1a: Create nodes

            In order to create a new node, you can click with the mouse button in the network editor and a circular 
            panel with three letters appears to select an element type. A node is divided into three element types: 
            stimulator (:bdg:`S`), recording (:bdg:`R`) device and neuron (:bdg:`N`). Click on one element type, a menu
            of models in corresponding element type appears. Then, selecting a model creates a node of the selected 
            model.

   .. _usage-basic-connect-nodes:

   .. grid-item::
      :columns: 4

      .. image:: /_static/img/gif/connect-nodes.gif

   .. grid-item::
      :child-align: center
      :columns: 8

      .. grid:: 1
         :gutter: 1

         .. grid-item-card:: Step 1b: Connect nodes

            Forming a network of nodes is defined by making connections between and within nodes. In order to connect
            nodes, you can click on a connector of a node, then move the mouse towards anther node and finally click on
            a target node. It creates a connection between source and target nodes.

.. hint::
   By pressing the hotkey :keys:`alt` and clicking a node at the same time, you enable the connecting mode or continue
   connecting other nodes.

.. grid:: 2
   :gutter: 1

   .. _usage-basic-select-model-and-parameters:

   .. grid-item::
      :child-align: center
      :columns: 7

      .. grid:: 1
         :gutter: 1

         .. grid-item-card:: Step 1c: Select model and parameters

            You are able to select the model of a node in the network controller. Then it shows a list of parameters which
            you might want to work on. Finally, you are able to change the values of visible parameters.

   .. grid-item::
      :columns: 5

      .. image:: /_static/img/gif/edit-node.gif

