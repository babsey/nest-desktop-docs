Direct current injection into single neurons
============================================

.. abstract::

   Intracellular recordings give access to the membrane potential of single neurons. If cells are studied `in vitro` in
   an acute slice preparation, the synaptic input, which a neuron normally receives under `in vivo` conditions, is then
   missing. It must be replaced by artificial input applied to the neuron through the electrode. One can use direct
   current (DC) of various amplitudes to systematically explore the response properties of a neuron. This represents, in
   fact, a simple and efficient method to characterize biological neurons in electrophysiological experiments. We will
   here apply it to model neurons as well.

You will use a simple linear integrate-and-fire (LIF) point neuron model to devise a single-neuron current injection
experiment. In the LIF neuron model, spikes are generated each time the membrane potential reaches a predefined
threshold. Spike waveforms are not modeled explicitly, and you recognize a spike only by the reset (strong downward
deflection) of the membrane potential that follows a threshold crossing.

----

.. question::

   1. What is the membrane potential response for both negative and positive values of the applied current? You can
      measure the membrane potential by performing an intracellular recording, using a voltmeter.

.. example::
   :collapsible:

   .. md-tab-set::

      .. md-tab-item:: Lab book

         |

         .. image:: /_static/img/screenshots/lecture/single-neuron-direct-current-injection-1-1.png

      .. md-tab-item:: Code

         .. code-block:: Python

            nest.ResetKernel()

            # Set simulation kernel
            nest.SetKernelStatus({
               "resolution": 0.1,
            })

            # Create nodes
            n1 = nest.Create("iaf_psc_alpha")
            dc1 = nest.Create("dc_generator", params={
               "amplitude": 1,
               "start": 100,
               "stop": 400,
            })
            dc2 = nest.Create("dc_generator", params={
               "amplitude": -1,
               "start": 600,
               "stop": 900,
            })
            vm1 = nest.Create("voltmeter")

            # Connect nodes
            nest.Connect(dc1, n1)
            nest.Connect(dc2, n1)
            nest.Connect(vm1, n1)

            # Run simulation
            nest.Simulate(1000)

      .. md-tab-item:: Activity

         .. image:: /_static/img/screenshots/lecture/single-neuron-direct-current-injection-1-2.png

.. hint::
   Try different amplitudes of the applied current and describe the phenomena you observe.

|

.. question::

   2. Explore how the membrane potential response depends on the biophysical neuron parameters. In particular, describe
      the influence of the time constant of the membrane, the spike threshold and the absolute refractory time on the
      membrane potential trajectories.

.. example::
   :collapsible:

   .. md-tab-set::

      .. md-tab-item:: Lab book

         |

         .. image:: /_static/img/screenshots/lecture/single-neuron-direct-current-injection-2-1.png


      .. md-tab-item:: Code

         .. code-block:: Python

            nest.ResetKernel()

            # Set simulation kernel
            nest.SetKernelStatus({
               "resolution": 0.1,
            })

            # Create nodes
            n1 = nest.Create("iaf_psc_alpha", params={
               "tau_m": 10
            })
            n2 = nest.Create("iaf_psc_alpha", params={
               "tau_m": 20
            })
            dc1 = nest.Create("dc_generator", params={
               "mean": 1,
               "start": 100,
               "stop": 600,
            })
            vm1 = nest.Create("voltmeter")
            vm2 = nest.Create("voltmeter")

            # Connect nodes
            nest.Connect(dc1, n1)
            nest.Connect(dc1, n2)
            nest.Connect(vm1, n1)
            nest.Connect(vm2, n2)

            # Run simulation
            nest.Simulate(1000)

      .. md-tab-item:: Activity

         .. image:: /_static/img/screenshots/lecture/single-neuron-direct-current-injection-2-2.png


