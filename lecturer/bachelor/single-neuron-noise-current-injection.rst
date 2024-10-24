Noise current injection into single neurons
============================================

To account for additional effects seen in recordings from real nerve cells, we add some `noise` current to the input
mimicking spontaneous channel openings, or `synaptic bombardment` originating from a large pool of presynaptic neurons.
If the fluctuations of a physical variable are due to the combined influence of a large number of small contributions,
the concept of White Noise can provide an adequate descriptive model. In this idealized type of signal, all frequencies
are present in equal proportions, but with random phases (`wind`). A well-known example is `white` light, which
comprises all colors from the visible spectrum. In our simulations, we use a sequence of independent identically
distributed Gaussian random variables to approximate a particular type of white noise, Gaussian White Noise (GWN).

----

.. question::

   1. First look at the effect of noise in the subthreshold case. While you explore the membrane potential response for
      (weak) noise current input, note that GWN, like any Gaussian random variable, has two parameters: mean and
      variance.

      Perform systematic simulations with different combinations of mean and variance (or standard deviation) and find a
      way to document the results.

.. example::
   :collapsible:

   .. md-tab-set::

      .. md-tab-item:: Lab book

         |

         .. image:: /_static/img/screenshots/lecture/single-neuron-noise-current-injection-1-1.png

      .. md-tab-item:: Code

         .. code-block:: Python

            nest.ResetKernel()

            # Set simulation kernel
            nest.SetKernelStatus({
               "resolution": 0.1,
            })

            # Create nodes
            n1 = nest.Create("iaf_psc_alpha")
            n2 = nest.Create("iaf_psc_alpha")
            ng1 = nest.Create("noise_generator", params={
               "mean": 10,
               "std": 0,
               "start": 100,
               "stop": 600,
            })
            ng2 = nest.Create("noise_generator", params={
               "mean": 10,
               "std": 2,
               "start": 300,
               "stop": 800,
            })
            vm1 = nest.Create("voltmeter")
            vm2 = nest.Create("voltmeter")

            # Connect nodes
            nest.Connect(ng1, n1)
            nest.Connect(ng2, n2)
            nest.Connect(vm1, n1)
            nest.Connect(vm2, n2)

            # Run simulation
            nest.Simulate(1000)

      .. md-tab-item:: Activity

         .. image:: /_static/img/screenshots/lecture/single-neuron-noise-current-injection-1-2.png


|

.. question::

   2. Now, consider a spiking neuron with “strong” noise current as input. If the strength of the input (mean), or the
      amplitude fluctuations of the input (variance), are large enough, the firing threshold is crossed and action
      potentials are generated. In contrast to the case of DC input, the fluctuations of the membrane potential will now
      affect the timing of the action potentials to some extent.

      Document this phenomenon with a suitable set of experiments, where you run the simulations with different seeds of
      the random number generator.

.. example::
   :collapsible:

   .. md-tab-set::

      .. md-tab-item:: Lab book

         |

         .. image:: /_static/img/screenshots/lecture/single-neuron-noise-current-injection-2-1.png


      .. md-tab-item:: Code

         .. code-block:: Python

            nest.ResetKernel()

            # Set simulation kernel
            nest.SetKernelStatus({
               "resolution": 0.1,
            })

            # Create nodes
            n1 = nest.Create("iaf_psc_alpha", 10)
            n2 = nest.Create("iaf_psc_alpha", 100)
            ng1 = nest.Create("noise_generator", params={
               "mean": 376,
               "std": 0,
               "start": 100,
               "stop": 900,
            })
            ng2 = nest.Create("noise_generator", params={
               "mean": 370,
               "std": 10,
               "start": 100,
               "stop": 900,
            })
            vm1 = nest.Create("voltmeter")
            vm2 = nest.Create("voltmeter")
            sr1 = nest.Create("spike_recorder")
            sr2 = nest.Create("spike_recorder")

            # Connect nodes
            nest.Connect(ng1, n1)
            nest.Connect(ng2, n2)
            nest.Connect(vm1, n1, conn_spec={
               "rule": "fixed_outdegree",
               "outdegree": 1,
            })
            nest.Connect(vm2, n2, conn_spec={
               "rule": "fixed_outdegree",
               "outdegree": 1,
            })
            nest.Connect(n1, sr1)
            nest.Connect(n2, sr2)

            # Run simulation
            nest.Simulate(1000)

      .. md-tab-item:: Activity

         .. image:: /_static/img/screenshots/lecture/single-neuron-noise-current-injection-2-2.png


|

.. question::

   3. Play with the parameters of the noise current over a certain range of values when there is

      (a) no action potential generated, and
      (b) several spikes generated.

      What exactly is the “threshold” now? To judge the effect of random fluctuations, it is important to look at
      multiple
      repetitions of the same experiment.

      What happens to the frequency of spikes and the irregularity of spike trains as mean and/or variance of the noise
      is increased? The irregularity of neuronal spiking can be assessed, for example,  by the coefficient of variation
      (CV) of the inter-spike intervals.

.. example::
   :collapsible:

   .. md-tab-set::

      .. md-tab-item:: Spike threshold

         .. md-tab-set::

            .. md-tab-item:: Lab book

               |

               .. image:: /_static/img/screenshots/lecture/single-neuron-noise-current-injection-3a-1.png

            .. md-tab-item:: Code

               .. code-block:: Python

                  nest.ResetKernel()

                  # Set simulation kernel
                  nest.SetKernelStatus({
                     "resolution": 0.1,
                  })

                  # Create nodes
                  n1 = nest.Create("iaf_psc_alpha")
                  n2 = nest.Create("iaf_psc_alpha")
                  ng1 = nest.Create("noise_generator", params={
                     "mean": 360,
                     "std": 25,
                     "start": 100,
                     "stop": 900,
                  })
                  vm1 = nest.Create("voltmeter")
                  vm2 = nest.Create("voltmeter")

                  # Connect nodes
                  nest.Connect(ng1, n1)
                  nest.Connect(ng1, n2)
                  nest.Connect(vm1, n1)
                  nest.Connect(vm2, n2)

                  # Run simulation
                  nest.Simulate(1000)

            .. md-tab-item:: Activity

               .. image:: /_static/img/screenshots/lecture/single-neuron-noise-current-injection-3a-2.png

      .. md-tab-item:: Irregularity of neuronal spiking

         .. md-tab-set::

            .. md-tab-item:: Lab book

               |

               .. image:: /_static/img/screenshots/lecture/single-neuron-noise-current-injection-3b-1.png


            .. md-tab-item:: Code

               .. code-block:: Python

                  nest.ResetKernel()

                  # Set simulation kernel
                  nest.SetKernelStatus({
                     "resolution": 0.1,
                  })

                  # Create nodes
                  n1 = nest.Create("iaf_psc_alpha")
                  n2 = nest.Create("iaf_psc_alpha")
                  n2 = nest.Create("iaf_psc_alpha")
                  ng1 = nest.Create("noise_generator", params={
                     "mean": 376,
                     "std": 50,
                  })
                  ng2 = nest.Create("noise_generator", params={
                     "mean": 376,
                     "std": 5,
                  })
                  ng3 = nest.Create("noise_generator", params={
                     "mean": 376,
                  })
                  vm1 = nest.Create("voltmeter")
                  vm2 = nest.Create("voltmeter")
                  vm3 = nest.Create("voltmeter")

                  # Connect nodes
                  nest.Connect(ng1, n1)
                  nest.Connect(ng2, n2)
                  nest.Connect(ng3, n3)
                  nest.Connect(vm1, n1)
                  nest.Connect(vm2, n2)
                  nest.Connect(vm3, n3)

                  # Run simulation
                  nest.Simulate(1000)

            .. md-tab-item:: Activity

               .. image:: /_static/img/screenshots/lecture/single-neuron-noise-current-injection-3b-2.png


|

.. question::

   4. Now you should systematically measure two types of input-output curves of the neuron:

      (a) Keep the variance of the noise at a fixed level and systematically change the mean of the noise. What is the
          difference to the curve you obtained with pure DC input?
      (b) Now keep the mean of the noise at a fixed level and systematically change the variance of the noise. What is
          the minimal variance (“threshold”) that leads to a non-zero response rate?

.. example::
   :collapsible:

   .. md-tab-set::

      .. md-tab-item:: Lab book

         |

         .. image:: /_static/img/screenshots/lecture/single-neuron-noise-current-injection-4-1.png

      .. md-tab-item:: Code

         .. code-block:: Python

            nest.ResetKernel()

            # Set simulation kernel
            nest.SetKernelStatus({
               "resolution": 0.1,
            })

            # Create nodes
            n1 = nest.Create("iaf_psc_alpha", 100)
            n2 = nest.Create("iaf_psc_alpha", 100)
            ng1 = nest.Create("noise_generator", 100, params={
               "mean": np.linspace(350, 450, 100),
               "std": 50,
            })
            ng2 = nest.Create("noise_generator", 100, params={
               "mean": np.linspace(350, 450, 100),
            })
            sr1 = nest.Create("spike_recorder")
            sr2 = nest.Create("spike_recorder")

            # Connect nodes
            nest.Connect(ng1, n1, "one_to_one")
            nest.Connect(ng2, n2, "one_to_one")
            nest.Connect(n1, sr1)
            nest.Connect(n2, sr2)

            # Run simulation
            nest.Simulate(1000)

      .. md-tab-item:: Activity

         .. image:: /_static/img/screenshots/lecture/single-neuron-noise-current-injection-4-2.png


