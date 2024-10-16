.. _setup-appimage:

AppImage |linux|
================

.. grid:: 2

   .. grid-item::
      :columns: 9

      AppImage are applications for Linux without installation.

   .. grid-item::
      :columns: 3

      .. image:: /_static/img/logo/AppImage-logo.svg
         :target: #
         :width: 120px

AppImages do not need to be installed. All you have to do is download them, make them executable and run them. This can
either be done using the GUI or via the command line.


Download and change mode
------------------------

Download the NEST Desktop AppImage from the `releases page <https://appimage.github.io/NEST_Desktop/>`__
and make it executable using your file manager or by entering the following commands in a terminal:

.. code-block:: bash

   chmod +x ./nest-desktop-*.AppImage


Start
-----

Click the :code:`nest-desktop-x.y.z.AppImage` file to run NEST Desktop.

.. note::
   The AppImage contains only frontend interface and doesn't include the backends. Thus, you have to start the API
   server of backends manually. For more information please read the instructions :doc:`here <backends/index>`.


Next steps
----------

- :doc:`Now you can start constructing networks for the simulation! </user/usage-basic/index>`
