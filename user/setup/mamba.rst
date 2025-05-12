.. _setup-mamba:

Mamba |linux| |macOS| |windows|
===============================

.. grid:: 2

   .. grid-item::
      :columns: 9

      Anaconda provides packages for `NEST Desktop <https://anaconda.org/conda-forge/nest-desktop>`__. and `NEST
      Simulator <https://anaconda.org/conda-forge/nest-simulator>`__. These packages can be installed with Miniforge
      (from :bdg:`conda-forge`). Since NEST 3, the API server (i.e. :bdg:`NEST Server`) is included which is necessary
      for :bdg:`NEST Desktop`.

   .. grid-item::
      :columns: 3

      .. image:: /_static/img/logo/mamba-logo.png
         :target: #
         :width: 120px

Prequistion for mamba
-------------------------

`Conda-forge` is a collection of packages led by the community and can be used with Mamba. Please install miniforge
first (https://conda-forge.org/download/).



Setup Mamba environment
-----------------------

#. Create a Mamba environment called :bdg:`nest` and install NEST Desktop:

   .. code-block:: bash

      mamba create -n nest nest-desktop

#. Activate the Mamba environment :bdg:`nest`:

   .. code-block:: bash

      mamba activate nest

#. Install backends in Mamba environment. For more infomation, please read the installation guide :doc:`here
   <backends/index>`.

**The installation is now complete!**


Start in Mamba environment
--------------------------

#. Activate the Mamba environment :bdg:`nest`:

   .. code-block:: bash

      mamba activate nest

#. Start backends in Mamba environment. For more information, please follow the start instructions :doc:`here
   <backends/index>`.

#. Start NEST Desktop (in another terminal session):

   .. code-block:: bash

      nest-desktop start

   NEST Desktop is now started and available in the web browser at http://localhost:54286.

.. seeAlso::
   For more information read the full documentation of the command API
   :doc:`here </user/usage-advanced/command-API>`.


Next steps
----------

- :doc:`Now you can start constructing networks for the simulation! </user/usage-basic/index>`


