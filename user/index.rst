
.. _user-guide:

=================
|user| User guide
=================

The user guide provides detailed documentation of the GUI of NEST Desktop.

.. note::
   If you want to see a quick start guide for in NEST Desktop, we have prepared a
   :ref:`usage-basic-video-tutorial` showing the :ref:`usage-basic-first-steps`.


How to use NEST Desktop
=======================

.. toctree::
   :hidden:

   Setup <setup/index>
   Basic usage <usage-basic/index>

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: Setup guide
      :link: setup-guide
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 3
            :class: card-img

            |setup|

         .. grid-item::
            :columns: 9

            Learn how to install NEST Desktop and backends

   .. grid-item-card:: Basic usage
      :link: basic-usage-guide
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 3
            :class: card-img

            |usage|

         .. grid-item::
            :columns: 9

            Learn the basic steps how to use NEST Desktop


Advanced guide
==============

Views
-----

.. toctree::
   :hidden:

   usage-advanced/project-view
   usage-advanced/model-view

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: Project view
      :link: project-view
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 4

            .. image:: /_static/img/thumbnails/project-view.png

         .. grid-item::
            :columns: 8

            Allows users to construct networks and analyze activity

   .. grid-item-card:: Model view
      :link: model-view
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 4

            .. image:: /_static/img/thumbnails/model-view.png

         .. grid-item::
            :columns: 8

            Contains different components to explore models

Graphs
------

.. toctree::
   :hidden:

   Network graph <usage-advanced/network-graph>
   Activity chart graph <usage-advanced/activity-chart-graph>
   Activity animation graph <usage-advanced/activity-animation-graph>

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: Network graph
      :link: network-graph
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 4

            .. image:: /_static/img/thumbnails/network-graph.png

         .. grid-item::
            :columns: 8

            Shows nodes and connections in the network editor

   .. grid-item-card:: Activity chart graph
      :link: activity-chart-graph
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 4

            .. image:: /_static/img/thumbnails/activity-chart-graph.png

         .. grid-item::
            :columns: 8

            Activity can be displayed in a chart graph for spikes and analog signals

   .. grid-item-card:: Activity animation graph
      :link: activity-animation-graph
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 4

            .. image:: /_static/img/gif/activity-anim-graph.gif

         .. grid-item::
            :columns: 8

            Animated activity graph for the spatial network of neurons with geographical positions

NEST features
-------------

.. toctree::
   :hidden:

   usage-advanced/nest/copy-model
   .. usage-advanced/nest/compartmental-neuron
   .. usage-advanced/nest/synapse-model
   usage-advanced/nest/nestml-models

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: Copy model
      :link: copy-model
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 4

            .. image:: /_static/img/thumbnails/copy-model.png

         .. grid-item::
            :columns: 8

            The user learns how to copy a model

   .. .. grid-item-card:: Compartmental neuron
   ..    :link: compartmental-neuron
   ..    :link-type: ref

   ..    .. grid:: 2

   ..       .. grid-item::
   ..          :columns: 4

   ..          .. image:: /_static/img/thumbnails/compartmental-neuron.png

   ..       .. grid-item::
   ..          :columns: 8

   ..          The user learns how to create a compartmental neuron

   .. .. grid-item-card:: Synapse model
   ..    :link: synapse-model
   ..    :link-type: ref

   ..    .. grid:: 2

   ..       .. grid-item::
   ..          :columns: 4

   ..          .. image:: /_static/img/thumbnails/synapse-model.png

   ..       .. grid-item::
   ..          :columns: 8

   ..          The user learns the implementation of a synapse model in a simulation

   .. grid-item-card:: NESTML models
      :link: nestml-models
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 4

            .. image:: /_static/img/thumbnails/nestml-model.png

         .. grid-item::
            :columns: 8

            The user learns how to create own models with NESTML


External software
=================

.. toctree::
   :hidden:

   .. usage-external/simulate-with-insite
   .. usage-external/usage-with-nrp
   .. usage-external/usage-with-visimpl
   usage-external/libre-office-extension


.. note::

   Insite, NRP and ViSimpl has been removed in this version because it is not working with these external softwares
   anymore. We are working on reimplement these software in next release.

   If you like to see the documentation about these external softwares, please go to the older version of docs:
   - https://nest-desktop.readthedocs.io/en/3.3/user/index.html#external-software


.. grid:: 2
   :gutter: 2

   .. .. grid-item-card:: Simulate with Insite
   ..    :link: simulate-with-insite
   ..    :link-type: ref

   ..    .. grid:: 2

   ..       .. grid-item::
   ..          :columns: 4

   ..          .. image:: /_static/img/gif/external-insite.gif

   ..       .. grid-item::
   ..          :columns: 8

   ..          Learn how to use NEST Desktop with Insite

   .. .. grid-item-card:: NeuroRobotics Platform
   ..    :link: use-nest-desktop-with-nrp
   ..    :link-type: ref

   ..    .. grid:: 2

   ..       .. grid-item::
   ..          :columns: 4

   ..          .. image:: /_static/img/gif/external-nrp.gif

   ..       .. grid-item::
   ..          :columns: 8

   ..          Learn how to use NEST Desktop with NRP

   .. .. grid-item-card:: ViSimpl
   ..    :link: use-nest-desktop-with-visimpl
   ..    :link-type: ref

   ..    .. grid:: 2

   ..       .. grid-item::
   ..          :columns: 4

   ..          .. image:: /_static/img/gif/external-visimpl.gif

   ..       .. grid-item::
   ..          :columns: 8

   ..          Learn how to use NEST Desktop with ViSimpl

   .. grid-item-card:: LibreOffice extension
      :link: libreoffice_extension
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 4

            .. image:: /_static/img/screenshots/network/annotation/example.png

         .. grid-item::
            :columns: 8

            Create publication-ready network graphs
