.. _deployer-guide:

=========================
|deployer| Deployer guide
=========================

This guide provides detailed documentation on how to deploy NEST Desktop. You can read the deployment instructions by
clicking one of these images below.


Deploy NEST Desktop
===================

.. toctree::
   :hidden:
   :maxdepth: 1

   deploy-docker-compose
   deploy-openshift
   deploy-openstack
   deploy-rancher

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: Docker Compose
      :link: deploy-docker-compose
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 9

            Start multiple Docker services at once via Docker Compose

         .. grid-item::
            :columns: 3

            |docker-compose|

   .. grid-item-card:: OpenShift
      :link: deploy-openshift
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 9

            Build and deploy Docker images via web service or CLI commands

         .. grid-item::
            :columns: 3

            .. image:: /_static/img/logo/openshift-logo.png
               :alt: Openshift

   .. grid-item-card:: OpenStack
      :link: deploy-openstack
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 9

            Build app with Ansible and deploy on a cloud computing platform via web service

         .. grid-item::
            :columns: 3

            .. image:: /_static/img/logo/openstack-logo.svg
               :alt: Openstack

   .. grid-item-card:: Rancher
      :link: deploy-rancher
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 9

            Build and deploy Docker images via web service

         .. grid-item::
            :columns: 3

            .. image:: /_static/img/logo/rancher-logo.svg
               :alt: Rancher

Register clients for user authentication
========================================

.. toctree::
   :hidden:
   :maxdepth: 1

   register-client-ebrains

.. grid:: 2

   .. grid-item-card:: Register client on EBRAINS
      :link: register-client-ebrains
      :link-type: ref

      .. grid:: 2

         .. grid-item::
            :columns: 8

            Register OIDC client on EBRAINS

         .. grid-item::
            :columns: 4

            .. image:: /_static/img/logo/ebrains-logo.svg
               :alt: EBRAINS


.. Deploy with external software
.. =============================

.. .. toctree::
..    :hidden:
..    :maxdepth: 1

..    deploy-docker-compose-insite
..    deploy-docker-compose-nrp


.. .. grid:: 2
..    :gutter: 2

..    .. grid-item-card:: NEST Desktop with Insite
..       :link: deploy-insite
..       :link-type: ref

..       .. grid:: 2

..          .. grid-item::
..             :columns: 9

..             Deploy Docker Compose with Insite

..          .. grid-item::
..             :columns: 3

..             |docker-compose|

..    .. grid-item-card:: NEST Desktop with NRP
..       :link: deploy-nrp
..       :link-type: ref

..       .. grid:: 2

..          .. grid-item::
..             :columns: 9

..             Deploy Docker Compose with NRP

..          .. grid-item::
..             :columns: 3

..             |docker-compose|
