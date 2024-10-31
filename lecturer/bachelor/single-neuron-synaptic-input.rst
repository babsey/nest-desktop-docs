Excitatory and inhibitory synaptic input into single neurons
============================================================

In a biological neuronal network, communication between neurons typically relies on synaptic input. Whenever the
presynaptic neuron generates a spike, a chemical neurotransmitter (e.g. glutamate or GABA) is released and bound to
postsynaptic receptors. This leads to a transient activation of the synapse, and a transient inward or outward
postsynaptic current (PSC). As a consequence, the membrane potential of the postsynaptic neuron experiences a small
deflection, the postsynaptic potential (PSP). Typically, for an excitatory synapse using glutamate as a transmitter,
this deflection is depolarizing (towards threshold). In contrast, for an inhibitory synapse using GABA as a transmitter,
it is hyperpolarizing (away from threshold). The superposition of many PSCs of either polarity represents the effective
input to a neuron, which may, or may not, lead to an output spike to be sent to other neurons in the same circuit. You
should now explore all these aspects by performing the following numerical experiments:

----

.. question::

   1. Devise a simulation method to study single postsynaptic potentials. Which simulation parameter reflects the
      “strength” of a synapse? Systematically explore the effect of activating single excitatory and inhibitory
      synapses.

      Under which conditions can activating a single synapse elicit an output spike?

.. example::
   :collapsible:

   .. md-tab-set::

      .. md-tab-item:: Lab book

         |

         .. image:: /_static/img/screenshots/lecture/single-neuron-spike-input-1-1.png


      .. md-tab-item:: Code

         .. code-block:: Python

            nest.ResetKernel()

            # Set simulation kernel
            nest.SetKernelStatus({
               "resolution": 0.1,
            })

            # Create nodes
            n1 = nest.Create("iaf_psc_alpha")
            sg1 = nest.Create("spike_generator", params={
               "spike_times": [200],
            })
            vm1 = nest.Create("voltmeter")

            # Connect nodes
            nest.Connect(sg1, n1, syn_spec={
               "weight": 1154
            })
            nest.Connect(vm1, n1)

            # Run simulation
            nest.Simulate(1000)

      .. md-tab-item:: Activity

         .. image:: /_static/img/screenshots/lecture/single-neuron-spike-input-1-2.png

|

.. question::

   2. Multiple PSPs elicited in rapid succession at one and the same synapse add up to a compound signal if they
      sufficiently overlap in time. This phenomenon is called “temporal integration”.

      Multiple PSPs elicited at different synapses are also superimposed, all contributing to the membrane potential of
      the postsynaptic neuron. This is called “spatial integration”.

      Design a set of experiments to illustrate the phenomena of temporal and spatial synaptic integration in the
      subthreshold regime. Which parameters of the neuron are mainly responsible for the temporal overlap between
      individual PSPs?

.. example::
   :collapsible:

   .. md-tab-set::

      .. md-tab-item:: Temporal integration

         .. md-tab-set::

            .. md-tab-item:: Lab book

               |

               .. image:: /_static/img/screenshots/lecture/single-neuron-spike-input-2a-1.png

            .. md-tab-item:: Code

               .. code-block:: Python

                  nest.ResetKernel()

                  # Set simulation kernel
                  nest.SetKernelStatus({
                     "resolution": 0.1,
                  })

                  # Create nodes
                  n1 = nest.Create("iaf_psc_alpha")
                  sg1 = nest.Create("spike_generator", params={
                     "spike_times": [200,210,220,230],
                  })
                  vm1 = nest.Create("voltmeter", params={
                     "interval": 0.1,
                  })

                  # Connect nodes
                  nest.Connect(sg1, n1)
                  nest.Connect(vm1, n1)

                  # Run simulation
                  nest.Simulate(1000)

            .. md-tab-item:: Activity

               .. image:: /_static/img/screenshots/lecture/single-neuron-spike-input-2a-2.png

      .. md-tab-item:: Spatial integration

         .. md-tab-set::

            .. md-tab-item:: Lab book

               |

               .. image:: /_static/img/screenshots/lecture/single-neuron-spike-input-2b-1.png

            .. md-tab-item:: Code

               .. code-block:: Python

                  nest.ResetKernel()

                  # Set simulation kernel
                  nest.SetKernelStatus({
                     "resolution": 0.1,
                  })

                  # Create nodes
                  n1 = nest.Create("iaf_psc_alpha")
                  sg1 = nest.Create("spike_generator", params={
                     "spike_times": [200],
                  })
                  sg2 = nest.Create("spike_generator", params={
                     "spike_times": [210],
                  })
                  sg3 = nest.Create("spike_generator", params={
                     "spike_times": [220],
                  })
                  sg4 = nest.Create("spike_generator", params={
                     "spike_times": [230],
                  })
                  vm1 = nest.Create("voltmeter", params={
                     "interval": 0.1,
                  })

                  # Connect nodes
                  nest.Connect(sg1, n1)
                  nest.Connect(sg2, n1)
                  nest.Connect(sg3, n1)
                  nest.Connect(sg4, n1)
                  nest.Connect(vm1, n1)

                  # Run simulation
                  nest.Simulate(1000)

            .. md-tab-item:: Activity

               .. image:: /_static/img/screenshots/lecture/single-neuron-spike-input-2b-2.png

|

.. question::

   3. A hallmark of the LIF model, which is shared by many biological neurons, is the linearity of temporal and spatial
      integration. The membrane potential response to a combined input is just the sum of the individual responses to
      the individual inputs, as long as all of them remain subthreshold. Design an experiment that demonstrates the
      linearity of synaptic integration for the LIF neuron model. Does linearity also hold for superthreshold inputs
      that lead to action potential firing?


----

NEST Desktop allows you to study how neurons are activated by synaptic input. You can use the so-called
:code:`spike_generator` for experiments with maximal control. In essence, you specify the time point of each spike
explicitly. Don't forget to specify the amplitude of the post-synaptic potential. This way, you can explore the effect
of “spatio-temporal integration”. You can also study, under which conditions synaptic input can trigger an output spike.
