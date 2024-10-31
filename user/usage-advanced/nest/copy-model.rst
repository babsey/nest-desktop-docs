.. _copy-model:

Copy models
===========


NEST Simulator provides a function to copy a model together with its set of parameters. The ``nest.CopyModel()``
function is useful when multiple populations or synapses should be created with the same set of parameters. This
simplifies the work a lot, as you can see in the example below:

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Code without CopyModel

     - Code with CopyModel

   * - .. code-block:: Python

          # Set parameter values
          params = {
            "C_m": 250,
            "E_L": 0,
            "I_e": 0,
            "V_m": 0,
            "V_reset": 0,
            "V_th": 20,
            "t_ref": 2,
            "tau_m": 20,
            "tau_syn_ex": 0.5,
            "tau_syn_in": 0.5,
          }
          n1_params = params.copy()
          n1_params["V_th"] = 15

          # Create nodes
          n1 = nest.Create("iaf_psc_alpha", 100, n1_params)
          n2 = nest.Create("iaf_psc_alpha", 25, params)

     - .. code-block:: Python

          # Copy node model with default parameters
          nest.CopyModel("iaf_psc_alpha", "brunel", params={
            "C_m": 250,
            "E_L": 0,
            "I_e": 0,
            "V_m": 0,
            "V_reset": 0,
            "V_th": 20,
            "t_ref": 2,
            "tau_m": 20,
            "tau_syn_ex": 0.5,
            "tau_syn_in": 0.5,
          })

           # Create nodes
           n1 = nest.Create("brunel", 100, params={"V_th": 15})
           n2 = nest.Create("brunel", 25)


.. _copy-model-steps-how-to-copy-model:

How to copy models - step by step
---------------------------------

.. grid:: 2

   .. grid-item::
      :columns: 4

      Click on the :bdg:`MODEL` tab in the network controller and then select a model to copy. Then confirm with a click
      on :bdg:`COPY`.

   .. grid-item::
      :columns: 8

      .. image:: /_static/img/screenshots/controller/nest/copy-model-step1.png
        :target: #

.. grid:: 2

   .. grid-item::
      :columns: 5

      Enter the name of the new model. If you like to have other model parameters than the default one, just click on
      the model title and select the parameters you want to change. This shows sliders and fields to edit their
      values.

   .. grid-item::
      :columns: 7

      .. image:: /_static/img/screenshots/controller/nest/copy-model-step2.png
        :target: #


.. grid:: 2

   .. grid-item::
      :columns: 5

      Choose the copied node model for your node and you are able to customize parameters as well.

      .. note::
         Copied synapse models can also be applied for synapses (analogously as above).


   .. grid-item::
      :columns: 7

      .. image:: /_static/img/screenshots/controller/nest/copy-model-step3.png
        :target: #
