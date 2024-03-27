.. _model-view:

Model view
==========

This is the guide for the model view in NEST Desktop.

.. grid:: 2

   .. grid-item::
      :columns: 4

      .. image:: /_static/img/thumbnails/model-view.png

   .. grid-item::
      :columns: 8

      Below the icon for the project view, you can see the one of the :ref:`model view <model-view-model-subpages>`,
      where you can read the model description, explore model activities or edit model configurations.


Models menu
-----------

.. grid:: 2

   .. grid-item::
      :columns: 4

      .. image:: /_static/img/screenshots/model/models-menu.png

   .. grid-item::
      :columns: 8

      By clicking the right mouse button on the model icon, a menu appears where you can select actions for models.


.. _model-view-model-dialog:

Model dialog
------------

You can import models from various sources, e.g. a file you uploaded from you computer, a file from a GitHub repository
or from a specified URL.

.. image:: /_static/img/screenshots/model/models-import.png

.. note::
   Model files should be formatted in JSON.

When you select :bdg:`Import from GitHub`, choose an element type and then a JSON file of your desired model group which
includes all functions of synapse currents.

The table shows a list of models from which you can select which ones you want to import.


.. _model-view-model-navigation-sidebar:

Model navigation sidebar
------------------------

.. grid:: 2

   .. grid-item::
      :columns: 6

      .. image:: /_static/img/screenshots/model/model-nav.png

   .. grid-item::
      :columns: 6

      In the navigation sidebar you find a :ref:`model-view-model-toolbar` and then :ref:`model-view-model-list`.

      You can select a model to read its documentation, its activity or to edit its configuration.


.. _model-view-model-toolbar:

Model toolbar
^^^^^^^^^^^^^

.. image:: /_static/img/screenshots/model/model-toolbar.png

At the top of the navigation sidebar, you see a toolbar containing buttons to reload (|reload|), export (|export|),
import (|import|), delete (|delete-models|) or reset (|reset|) multiple models.


.. _model-view-model-list:

Model List
^^^^^^^^^^

Above the model list you will find a search field and tags which you can use to filter the models in the list. Selected
filter tags appear as chips under the search field. In order to select a tag you need to click on the `filter` icon left
to the search field. Multiple filter tags can be applied. Selected filter tags can be removed (click on |close|).


.. _model-view-import-models:

Import models
*************

Go to the model view and find your desired synapse model. Next, click on the icon |dots-vertical|, then select a menu
item |import| :bdg:`import` to import it from GitHub.


.. _model-view-filter-models:

Filter models
*************

.. grid:: 2

   .. grid-item::
      :columns: 3

      .. image:: /_static/img/screenshots/model/models-filter-tag.png

   .. grid-item::
      :columns: 9

      It is possible to select filter tags to display only models with certain properties. The following filter tags are
      available:

      Installed:
         Show models which are installed in NEST Desktop

      GitHub:
         Show models which are provided in `an own GitHub repository
         <https://github.com/nest-desktop/nest-desktop-models>`__.

      Neuron/stimulator/recorder/synapse:
         Show models of the selected element type


.. _model-view-model-subpages:

Model subpages
--------------

.. card-carousel:: 1

   .. card:: Model documentation

      .. image:: /_static/img/screenshots/model/model-doc.png

      It shows the official user documentation of a selected model which also can be found on
      http://nest-simulator.readthedocs.io/en/latest/models/.

   .. card:: Model explorer

      You can explore the activity dynamics of **neuron** models only.

      .. grid:: 2

         .. grid-item::
            :columns: 8

            .. image:: /_static/img/screenshots/model/model-explorer.png


         .. grid-item::
            :columns: 4

            .. image:: /_static/img/screenshots/model/model-explorer-projects.png

      First, choose a simulation to see the neuronal response to a specific stimulus device. Then start the simulation
      by clicking on the :bdg:`SIMULATE` button. You can use the code editor to see changes in activity.

      .. note::
         It is important to disable the Insite pipeline for the simulation (in the settings).

   .. card:: Model editor

      .. image:: /_static/img/screenshots/model/model-editor.png

      The model editor allows you to make changes in parameter specifications, e.g. default value, unit, label or
      inputs.