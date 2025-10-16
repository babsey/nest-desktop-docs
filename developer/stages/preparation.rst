Prepare the environment
=======================

NEST Desktop is written in `Vue.js` (a web framework written in TypeScript), and also in TypeScript. The Vue code is
transpiled to HTML5 and JavaScript Code. There are multiple ways to develop Vue applications, but my preferred way to 
develop NEST Desktop is to use `Node.js` (and optionally `Yarn`).

Requirements
  - Node.js LTS (v24 or higher), Yarn
  - NEST Simulator 3.8 or higher

You can install these requirements in the host system. First install nvm which is a cross-platform Node.js version 
manager. See detailed steps on https://nodejs.org/en/download.

For Linux/macOS developer execute these command lines in terminal:

.. code-block:: bash

   # Download and install nvm:
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash

   # in lieu of restarting the shell
   \. "$HOME/.nvm/nvm.sh"

   # Download and install Node.js:
   nvm install 24

   # Verify the Node.js version:
   node -v # Should print "v24.7.0".

   # Download and install Yarn:
   corepack enable yarn

   # Verify Yarn version:
   yarn -v


.. _preparation-commands:

Commands
--------

Install node modules for NEST Desktop:

.. code-block:: bash

   yarn install

Start a development server:

.. code-block:: bash

   yarn dev

.. note::

   The command ``yarn serve`` uses the configuration file ``vue.config.js``.  This file controls the threads used for
   the linting (the statical-syntactical code checks). With the default configuration, all available threads are used to
   minimize the build time.  This might slow down other programs. There are cases where you cannot afford that and
   prefer a slightly longer execution time. In that cases, you can either adjust the number of threads in that file.This
   reduces the CPU load, but some CPU resources might stay unused. Alternatively you can execute the console in which
   you want to spawn the ``yarn`` command with a lower priority. On Linux (even on MacOS or Windows using WSL2 and an
   available shell command) this can be done using

   .. code-block:: bash

      nice -n 20 bash

   This will spawn a new console inside your current console, but with the lowest processing priority possible, i.e.
   this console and its tasks do not block other tasks (like video conferences, etc.) significantly. Do not be confused
   that there will be no new window and no major visual cues that you are now in another process. In that console you
   can now execute the commands mentioned above.

|

.. _preparation-useful-commands:

Useful commands
---------------

Check if any node modules are outdated:

.. code-block:: bash

   yarn outdated

Upgrade outdated node modules:

.. code-block:: bash

   yarn upgrade
