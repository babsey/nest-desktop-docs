.. _model-view:

Model view
==========

This is the guide for the model view in NEST Desktop.

.. grid:: 2

   .. grid-item::
      :columns: 4

      .. image:: /_static/img/screenshots/model/model-nav.png

   .. grid-item::
      :columns: 8

      Below the icon for the project view, you can see the one of the :ref:`model view <model-view-model-subpages>`,
      where you can read the model description, explore model activities or edit model configurations.

.. _model-view-model-navigation-sidebar:

Model navigation sidebar
------------------------

.. grid:: 2

   .. grid-item::
      :columns: 4

      .. image:: /_static/img/screenshots/model/model-nav.png

   .. grid-item::
      :columns: 8

      In the navigation sidebar you find a search field and then :ref:`model-view-model-list` of filtered models.
      You can select a model to read its documentation, its activity or to edit its configuration.


.. _model-view-models-menu:

Models menu
^^^^^^^^^^^

.. grid:: 2

   .. grid-item::
      :columns: 4

      .. image:: /_static/img/screenshots/model/models-menu.png

   .. grid-item::
      :columns: 8

      Click on the menu icon right to search field, a menu appears where you can select actions for models.


.. _model-view-model-dialog:

Model dialog
^^^^^^^^^^^^

You can export models to file or import models from various sources, e.g. a file you uploaded from you computer, a file
from a GitHub repository or from a specified URL.

.. image:: /_static/img/screenshots/model/models-import.png

.. note::
   Model files are stored in JSON or YAML format.

When you select the button with github icon, then click models icon, select an element type and a JSON file of your
desired model group. Click on :bdg:`fetch` button shows a list of models from which you can select which ones you want
to import.

.. .. _model-view-import-models:

.. Import models
.. *************

.. Go to the model view and find your desired synapse model. Next, click on the |dots-vertical| icon, then select a menu
.. item |import| :bdg:`import` to import it from GitHub.



.. _model-view-model-list:

Model List
^^^^^^^^^^

Above the model list you will find a search field and tags which you can use to filter the models in the list. Selected
filter tags appear under the search field. In order to select a tag you need to click it.


.. _model-view-filter-models:

Filter models
*************

It is possible to select filter tags to display only models with certain properties. The following filter tags are
available:

- **installed** - show models which are installed in NEST Desktop

- **custom** - show custom models (e.g. for NESTML)

- **nest** - show all built-in models of NEST Simulator

- **neuron/stimulator/recorder/synapse** - show models of the selected element type

.. - **GitHub** Show models which are provided in `an own GitHub repository
..    <https://github.com/nest-desktop/nest-desktop-models>`__.


.. .. _model-view-model-bar:

.. Model bar
.. ---------



.. _model-view-model-subpages:

Model subpages
--------------

Model documentation
^^^^^^^^^^^^^^^^^^^

.. grid:: 2

   .. grid-item::
      :columns: 4

      It shows the official user documentation of a selected model which also can be found on
      http://nest-simulator.readthedocs.io/en/latest/models/.

   .. grid-item::
      :columns: 8

      .. image:: /_static/img/screenshots/model/model-doc.png


Model explorer
^^^^^^^^^^^^^^

.. grid:: 2

   .. grid-item::
      :columns: 4

      You can explore the activity dynamics of **neuron** models only.

   .. grid-item::
      :columns: 8

      .. image:: /_static/img/screenshots/model/model-explorer.png


   .. grid-item::
      :columns: 4

      .. image:: /_static/img/screenshots/model/model-explorer-projects.png

   .. grid-item::
      :columns: 8

      First, choose a simulation to see the neuronal response to a specific stimulus device. Then start the simulation
      by clicking on the :bdg:`SIMULATE` button. You can use the code editor to see changes in activity.

      .. note::
         It is important to disable the Insite pipeline for the simulation (in the settings).

Model editor
^^^^^^^^^^^^

.. grid:: 2

   .. grid-item::
      :columns: 8

      .. image:: /_static/img/screenshots/model/model-editor.png

   .. grid-item::
      :columns: 4

      The model editor allows you to make changes in parameter specifications, e.g. default value, unit, label or
      inputs.