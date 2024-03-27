.. _nest-desktop-on-jupyter-jsc:

NEST Desktop on Jupyter JSC
===========================

.. grid:: 2

   .. grid-item::
      :columns: 7

      `Jupyter JSC <https://jupyter-jsc.fz-juelich.de>`__ is designed to provide the rich high performance computing
      (HPC) ecosystem to the world's most popular software: web browsers. JupyterLab is a web-based interactive
      development environment for Jupyter notebooks, code, and data. JupyterLab is flexible to support a wide range of
      workflows in data science, scientific computing, and machine learning.

   .. grid-item::
      :columns: 5

      .. image:: /_static/img/logo/jupyterjsc-logo.png

**Requirements**
   - `JSC account <https://judoor.fz-juelich.de/login>`__

**Steps on Jupyter JSC**
   #. Go to `Jupyter JSC <https://jupyter-jsc.fz-juelich.de/>`__.

   #. Login with your JSC account.

      .. image:: /_static/img/screenshots/online-services/jupyter-jsc-login.png

   #. Create a new JupyterLab.

      .. image:: /_static/img/screenshots/online-services/jupyter-jsc-new-jupyterlab.png

      - Possible systems: JUWELS, JUWELSBooster, JURECA, HDF-Cloud

         .. image:: /_static/img/screenshots/online-services/jupyter-jsc-lab-config.png

      - In :bdg:`Kernel and Extensions`: Check NEST Desktop and then save the config.

         .. image:: /_static/img/screenshots/online-services/jupyter-jsc-lab-kernels-extensions.png

   #. Start lab (with NEST Desktop proxy).

      .. image:: /_static/img/screenshots/online-services/jupyter-jsc-lab-start.png

   #. In JupyterLab launcher, click on NEST Desktop icon.

      .. image:: /_static/img/screenshots/online-services/jupyter-jsc-lab-notebook.png

.. note::
   Please stop lab in landing page when you do not require it.

   .. image:: /_static/img/screenshots/online-services/jupyter-jsc-lab-open-stop.png


Acknowledgements
----------------

Thanks for deploying NEST Desktop on Jupyter JSC:

- Jens Henrik Göbbert (Jülich)
