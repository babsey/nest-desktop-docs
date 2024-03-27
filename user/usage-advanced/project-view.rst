.. _project-view:

Project view
============

NEST Desktop has a project management helping you to organize your networks and network activity.

.. grid:: 2

   .. grid-item::
      :columns: 4

      .. image:: /_static/img/thumbnails/project-view.png

   .. grid-item::
      :columns: 8

      It contains a :ref:`project-view-projects-menu` in the system bar to manage multiple projects, a
      :ref:`project-view-project-navigation-sidebar`, a :ref:`project-view-project-bar` and content for
      :ref:`project-view-project-subpages`.

      If you want to explore the network activity of the project, you have to start the simulation before (|see|
      :ref:`usage-basic-simulate-networks`).


.. _project-view-projects-menu:

Projects menu
-------------

.. grid:: 2

   .. grid-item::
      :columns: 4

      .. image:: /_static/img/screenshots/project/projects-menu.png


   .. grid-item::
      :columns: 8

      The projects menu will be displayed when the user clicks the :bdg:`PROJECTS` entry in the system bar (top black
      bar). The opened project menu shows the same options which are displayed as buttons in the toolbar.

      In the menu you find options to create a new project (|new|) as well as to reload (|reload|), export (|export|),
      import (|import|), delete (|delete-projects|) or reset (|reset|) multiple projects.


.. _project-view-project-dialog:

Project dialog
--------------

It is possible to import projects from different sources: You can choose between drive (local storage), GitHub and URL
(other one than GitHub URLs). The GitHub category points to a model collection available in the separate `NEST Desktop
model repository <https://github.com/nest-desktop/nest-desktop-projects>`__.

.. image:: /_static/img/screenshots/project/projects-import.png

----

Also you are able to export multiple projects. The selection checkbox appears when the project is loaded (check the
:bdg:`validate` box by clicking it).

.. image:: /_static/img/screenshots/project/projects-export.png

----


.. _project-view-project-navigation-sidebar:

Project navigation sidebar
--------------------------

.. grid:: 2

   .. grid-item::
      :columns: 5

      .. image:: /_static/img/screenshots/project/project-nav.png

   .. grid-item::
      :columns: 7

      In the navigation sidebar you find a :ref:`project-view-project-toolbar` and then a
      :ref:`project-view-project-list`.


.. _project-view-project-toolbar:

Project toolbar
^^^^^^^^^^^^^^^

.. image:: /_static/img/screenshots/project/project-toolbar.png

At the top of the navigation sidebar, you see a toolbar containing buttons to create a new project (|new|) as well as to
reload (|reload|), export (|export|), import (|import|), delete (|delete-projects|) or reset (|reset|) multiple
projects.

Clicking on the buttons to export, import or delete projects opens a dialog showing a list of project (|see|
:ref:`project-view-project-dialog`).

.. warning::
   You should export projects that you want to keep: If you refresh your browser or delete the web page cookie, the project
   will be lost!

Creating a new project lets you construct a network from scratch (|see| :ref:`usage-basic-construct-networks`).


.. _project-view-project-list:

Project list
^^^^^^^^^^^^

.. grid:: 2

   .. grid-item::
      :columns: 6

      .. image:: /_static/img/screenshots/project/project-menu.png

   .. grid-item::
      :columns: 6

      Below the buttons you find the search field and a list of the projects. Select a project to load it for the usage.
      Once a project is loaded, a save icon (|save-ok|) appears on the right side. You can move the mouse on the project
      item, it shows three vertical dots (|vertical-dots|) for a menu with options to rename (|rename|), unload
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
      :columns: 8

      After every network change, NEST Desktop pushes a snapshot of the current network to the edit history list. With
      that history of the network, you can undo or redo the network changes. Loading a snapshot from this history is
      called `checkout network`.

   .. grid-item::
      :columns: 4

      .. image:: /_static/img/gif/network-history.gif


.. _project-view-simulation-button:

Simulation button
^^^^^^^^^^^^^^^^^

.. grid:: 2

   .. grid-item::
      :columns: 7

      You can click on the :bdg:`SIMULATE` button to start the simulation.

   .. grid-item::
      :columns: 5

      .. image:: /_static/img/gif/simulation-button.gif


.. _project-view-project-subpages:

Project subpages
----------------

.. card-carousel:: 1

   .. card:: Network editor

      .. image:: /_static/img/screenshots/network/network-editor.png

   .. card:: Activity explorer

      .. image:: /_static/img/screenshots/activity/activity-explorer.png

   .. card:: Lab book

      .. image:: /_static/img/screenshots/project/project-lab-book.png