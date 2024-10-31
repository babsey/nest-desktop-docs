.. _setup-python:

Python |linux| |macOS| |windows|
================================

.. grid:: 2

   .. grid-item::
      :columns: 9

      PyPI contains packages of NEST Desktop. We recommend to install both packages.

   .. grid-item::
      :columns: 3

      .. image:: /_static/img/logo/python-logo.png
         :target: #
         :width: 120px


Install with pip
----------------

#. Install NEST Desktop

   NEST Desktop is available on PyPI and can be installed with the ``pip`` command:

   .. code-block:: bash

      pip3 install nest-desktop [--user] [--upgrade]

   .. seeAlso::
      For more information, please read the complete installing guide :doc:`here </user/setup/index>`.

#. Install backends. For more information, please read the installing guide :doc:`here <backends/index>`.

**The installation is now complete!**

Start
-----

#. Start backends. For more information, please read the start guide :doc:`here <backends/index>`.

#. Start NEST Desktop (in another terminal session):

   .. code-block:: bash

      nest-desktop start

Now NEST Desktop is started. You can use NEST Desktop in the web browser at http://localhost:54286.

.. seeAlso::
   For more information read the full documentation of the command API
   :doc:`here </user/usage-advanced/command-API>`.

Next steps
----------

- :doc:`Now you can start constructing networks for the simulation! </user/usage-basic/index>`