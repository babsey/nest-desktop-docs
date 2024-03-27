.. _deploy-openstack

Deploy on OpenStack
===================

.. grid:: 2

   .. grid-item::
      :columns: 7

      The guide provides a step-by-step documentation on how to deploy NEST Desktop on OpenStack resources. For more
      information on OpenStack, please follow this link: https://www.redhat.com/en/topics/openstack.

      Deployers can build an OpenStack image via Packer and Ansible.

   .. grid-item::
      :columns: 5

      .. image:: /_static/img/logo/openstack-logo.svg
         :alt: OpenStack
         :width: 240px

Requirements:
  - `Packer <https://www.packer.io/downloads.html>`__
  - `Ansible (2.3.2.0 or newer) <https://releases.ansible.com/ansible/>`__


Deploy NEST Desktop on bwCloud
------------------------------

.. grid:: 2

   .. grid-item::
      :columns: 7

      We show the deployment on bwCloud, which is assigned to the
      universities in Baden-Württemberg, Germany. For more information bwCloud, follow the link:
      https://www.bw-cloud.org/.

      You can find the source code on https://github.com/nest-desktop/nest-desktop-bwCloud.

   .. grid-item::
      :columns: 5

      .. image:: /_static/img/logo/bwcloud-logo.svg
         :alt: OpenStack
         :width: 240px

**Steps**

#. Download the OpenStack RC File from
   `bwCloud dashboard <https://portal.bw-cloud.org/project/api_access/>`__:

   :bdg:`Project` -> :bdg:`API Access` -> :bdg:`Download OpenStack RC File`

#. Source the RC file to login:

   .. code-block:: bash

      source Project_<userID>-openrc.sh

#. Modify the Ansible configurations in ``infrastructure/bwCloud/nest-desktop.json``.

   Set ``image_name``. Values for ``source_image`` and ``networks`` are taken from bwCloud dashboard.

#. Build an image on bwCloud:

   .. code-block:: bash

      packer build nest-desktop.json

#. Start an instance on the bwCloud dashboard and it will have a public IP of the virtual machine.

.. _deploy-openstack-acknowledgements:

Acknowledgements
----------------

Thanks for the help to integrate NEST Desktop on *bwCloud*:

- Bernd Wiebelt
- Jonathan Bauer
- Michael Janczyk
- Manuel Messner
- Christopher Ill
