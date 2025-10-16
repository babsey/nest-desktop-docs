.. _project-view:

Project view
============

NEST Desktop has a project management helping you to organize your networks and network activity.
contains a :ref:`project-view-project-navigation-sidebar`, a :ref:`project-view-project-bar` and content for
:ref:`project-view-project-subpages`.

.. grid:: 2

   .. grid-item::
      :columns: 4

      :ref:`project-view-project-navigation-sidebar`

      .. image:: /_static/img/screenshots/project/project-nav.png
         :target: #project-view-project-navigation-sidebar

   .. grid-item::
      :columns: 8

      :ref:`project-view-project-bar`

      .. image:: /_static/img/screenshots/project/project-bar.png
         :target: #project-view-project-bar

      :ref:`project-view-project-subpages`

      .. image:: /_static/img/screenshots/network/network-editor.png
         :target: #project-view-project-subpages



If you want to explore the network activity of the project, you have to start the simulation before (|see|
:ref:`Simulate networks <usage-basic-simulate-networks>`).


.. _project-view-project-navigation-sidebar:

Project navigation sidebar
--------------------------

.. grid:: 2

   .. grid-item::
      :columns: 4

      .. image:: /_static/img/screenshots/project/project-nav.png

   .. grid-item::
      :columns: 8

      In the navigation sidebar you find a search field, a :ref:`project-view-projects-menu` and then a
      :ref:`project-view-project-list`.


.. _project-view-projects-menu:

Projects menu
^^^^^^^^^^^^^

.. grid:: 2

   .. grid-item::
      :columns: 4

      .. image:: /_static/img/screenshots/project/projects-menu.png


   .. grid-item::
      :columns: 8

      The projects menu will be displayed when the user clicks the |dots-vertical| button right to search field. In menu you find
      items to |import| import, |export| export , |delete-projects| delete multiple projects or |reload| reload project
      list. Clicking on the items to export, import or delete projects opens a dialog showing a list of project (|see|
      :ref:`project-view-project-dialog`).

.. warning::
   You should export projects that you want to keep: If you reset your browser or delete the site data, the project
   will be lost!

.. _project-view-project-dialog:

Project dialog
^^^^^^^^^^^^^^

It is possible to import projects from different sources: You can choose between drive (local storage), GitHub and URL
(other one than GitHub URLs). The GitHub category points to a model collection available in the separate `NEST Desktop
model repository <https://github.com/nest-desktop/nest-desktop-projects>`__.

.. image:: /_static/img/screenshots/project/project-import-dialog.png

.. note::

   |

   .. grid:: 2

      .. grid-item::
         :columns: 3

         .. image:: /_static/img/screenshots/project/project-from-old-database.png

      .. grid-item::
         :columns: 9

         You are able to fetch projects/models from old database. Click the button at the bottom-left corner.

----

In export dialog you are able to export multiple projects and models together to a single file.

.. image:: /_static/img/screenshots/project/project-export-dialog.png

----

.. _project-view-project-list:

Project list
^^^^^^^^^^^^

.. grid:: 2

   .. grid-item::
      :columns: 6

      .. image:: /_static/img/screenshots/project/project-menu.png

   .. grid-item::
      :columns: 6

      You find the search field and a list of the projects. Select a project to load it for the usage.
      Once a project is loaded, a save icon (|save-ok|) appears on the right side. You can move the mouse on the project
      item, it shows three vertical dots (|dots-vertical|) for a menu with options to rename (|rename|), unload
      (|unload|), reload (|reload|), duplicate (|duplicate|), export (|export|) or delete (|delete|) this project.

.. warning::
   Unless you click on the save button, the project is not stored in the database of the web page cookie and is lost
   when you reload the page!

   Another important remark is that NEST Desktop stores only projects with neuronal networks in the cookie database, but
   all activity (i.e. simulation results) will be lost after page reload!


.. _project-view-project-bar:

Project bar
-----------

.. image:: /_static/img/screenshots/project/project-bar.png

The project bar contains tabs for :ref:`project-view-project-subpages`, the project name, the
:ref:`project-view-network-history` and the :ref:`project-view-simulation-button`.

.. tip:: It is useful to give project a proper name so that you can recognize your projects quickly.


.. _project-view-network-history:

Network history
^^^^^^^^^^^^^^^

.. grid:: 2

   .. grid-item::
      :columns: 10

      After every network change, NEST Desktop pushes a snapshot of the current network to the edit history list. With
      that history of the network, you can undo or redo the network changes. Loading a snapshot from this history is
      called `checkout network`.

   .. grid-item::
      :columns: 2

      .. image:: /_static/img/gif/network-history.gif


.. _project-view-simulation-button:

Simulation button
^^^^^^^^^^^^^^^^^

.. grid:: 2

   .. grid-item::
      :columns: 8

      You can click on the :bdg:`SIMULATE` button to start the simulation.

   .. grid-item::
      :columns: 4

      .. image:: /_static/img/gif/simulation-button.gif


.. _project-view-project-subpages:

Project subpages
----------------

Network editor
^^^^^^^^^^^^^^

.. grid:: 2

   .. grid-item::
      :columns: 4

      Network editor is designed to edit nodes and connections on network graph.

   .. grid-item::
      :columns: 8

      .. image:: /_static/img/screenshots/network/network-editor.png

Activity explorer
^^^^^^^^^^^^^^^^^

.. grid:: 2

   .. grid-item::
      :columns: 4

      Activity explorer allows user to explore activity of the simulated network model.

   .. grid-item::
      :columns: 8

      .. image:: /_static/img/screenshots/activity/activity-explorer.png

Lab book
^^^^^^^^

.. grid:: 2

   .. grid-item::
      :columns: 4

      Lab book gives a fancy overview on network setup.

   .. grid-item::
      :columns: 8

      .. image:: /_static/img/screenshots/project/project-lab-book.png



.. include:: controller-sidebar.rst
