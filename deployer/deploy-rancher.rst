.. _deploy-rancher:

Deploy on Rancher
=================

.. grid:: 2

   .. grid-item::
      :columns: 7

      This part of the documentation shows how to deploy NEST Desktop on Rancher resources.

   .. grid-item::
      :columns: 5

      .. image:: /_static/img/logo/rancher-logo.svg
         :alt: Rancher
         :width: 240px


.. _deploy-rancher-deploy-nest-desktop-on-ebrains:

Rancher on EBRAINS
------------------

.. grid:: 2

   .. grid-item::
      :columns: 7

      EBRAINS provides two Rancher infrastructures:

      - https://rancher.tc.humanbrainproject.eu/ for the production and
      - https://rancher.dev-cineca.publicamundi.eu/ for the development.

   .. grid-item::
      :columns: 5

      .. image:: /_static/img/logo/ebrains-logo.svg
         :alt: EBRAINS
         :width: 320px


Rancher on Helmholtz cloud
--------------------------

.. grid:: 2

   .. grid-item::
      :columns: 7

      Helmholtz Cloud provides a Rancher infrastructure:

      - https://rancher.desy.de/

   .. grid-item::
      :columns: 5

      .. image:: /_static/img/logo/helmholtz-cloud-logo.svg
         :alt: Helmholtz cloud
         :width: 320px



.. _deploy-rancher-build-nest-desktop:

Build NEST Desktop on Rancher
-----------------------------

You can find the configurations on https://github.com/nest-desktop/nest-desktop-rancher.

.. note::
   Therein, you have to modify the environment for EBRAINS authentication, i.e. ``OIDC_CLIENT_ID`` and
   ``OIDC_CLIENT_SECRET`` of NEST Desktop (which is printed after setting up the client for NEST Desktop).

   For more information, please read the registration guide :doc:`here <register-client-ebrains>`.

Acknowledgements
----------------

Thanks for the help to integrate NEST Desktop on EBRAINS resources:

- Sofia Karvounari
- Eleni Mathioulaki
- Nikos Pappas
