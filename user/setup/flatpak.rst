.. _setup-flatpak:

Flatpak |linux|
===============

.. grid:: 2

   .. grid-item::
      :columns: 9

      You can install the Flatpak of NEST Desktop (with backends) from Flathub.

   .. grid-item::
      :columns: 3

      .. image:: /_static/img/logo/Flatpak-logo.svg
         :target: #
         :width: 120px

Requirements
------------

Install flatpak in Ubuntu:

.. code-block:: bash

   sudo apt install flatpak

.. seeAlso::

   To get more information about flatpak setup, please go to: https://flatpak.org/setup/


Install
-------

To install the flatpak NEST Desktop from flathub, use the following (without :code:`sudo`):

.. code-block:: bash

   flatpak install --user flathub io.github.nest-desktop


**The installation is now complete!**


Start
-----

You can start NEST Desktop in application view or enter the command in Terminal:

.. seeAlso::
   For more information, please go to https://flathub.org/apps/io.github.nest-desktop


.. code-block:: bash

   flatpak run io.github.nest-desktop


Next steps
----------

- :doc:`Now you can start constructing networks for the simulation! </user/usage-basic/index>`
