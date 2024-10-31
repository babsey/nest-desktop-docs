.. _register-client-ebrains:

Register client on EBRAINS
--------------------------

To access to NEST Desktop on EBRAINS infrastructure, an authentication is requested. You find the codes on
https://github.com/nest-desktop/apache2-oidc.

Here are the steps how to setup the authentication for NEST Desktop properly.

.. code-block:: bash

   bash get-dev-token.sh

Change the configuration file and then create a client for your application.

.. code-block:: bash

   bash create-client.sh

Keep ``client_id`` and ``client_secret`` for the cloud infrastructure.