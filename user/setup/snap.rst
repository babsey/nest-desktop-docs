.. _setup-snap:

Snap |linux| |macOS|
====================

.. grid:: 2

   .. grid-item::
      :columns: 9

      You can install NEST Desktop (with backends) with single snap command.

   .. grid-item::
      :columns: 3

      .. image:: /_static/img/logo/snapcraft-logo.png
         :target: #
         :width: 120px

.. note::
   In macOS |macOS| you need to install `snapcraft`. See https://snapcraft.io/docs/installing-snapcraft#heading--macos
   for details.

.. code-block:: bash

   snap install nest-desktop

**The installation is now complete!**

.. note::

   If you like to use older version instead and to disable the update to the latest, specify the channel:

   .. code-block:: bash

      sudo install nest-desktop --channel=3.3/stable

   Please consider that older releases are not in the maintenance anymore. Due the limited resources our
   development/maintenance efforts focus only on the current release.

   We are very grateful to have feedback why you prefers the older one.


Start
-----

You can start NEST Desktop in application view or enter the command :code:`nest-desktop` in Terminal.


.. seeAlso::
   For more information, please go to https://snapcraft.io/nest-desktop


Next steps
----------

- :doc:`Now you can start constructing networks for the simulation! </user/usage-basic/index>`
