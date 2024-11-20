Plotly.js
=========

Plotly.js is a javascript-based charting library. However the full library is huge (>10mb) and we don't need all trace 
modules. We found the solution to build custom bundle with only required trace modules.

Build custom bundle library
---------------------------

Clone from the repo:

.. code-block:: bash

   git clone --depth 1 --branch v2.35.2 https://github.com/plotly/plotly.js.git
   cd plotly.js/

Then build bundle with Nodejs 18.

.. code-block:: bash

   nvm install 18
   nvm use 18
   npm i
   npm run custom-bundle -- --traces scatter,scattergl,bar,histogram


Then copy/move the file `dist/plotly-custom.min.js` to NEST Desktop folder `public/assets/js/vendors/`.

.. seeAlso::
   For more information, please read the detailed guide `here <https://github.com/plotly/plotly.js/blob/master/CUSTOM_BUNDLE.md>`.


Optional: Add hash to the filename:

.. code-block:: bash

   sha256sum public/assets/js/vendors/plotly-custom.min.js | cut -c1-8

Then change the script source of plotly in `index.html`.