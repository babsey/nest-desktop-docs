.. _lecturer-guide:

=========================
|lecturer| Lecturer guide
=========================

This section gives directions for lecturers who want to teach computational neuroscience with NEST Desktop. Using
computer simulations, students are able to explore models ranging from single neurons to large neuronal networks.
Numerical experiments of increasing complexity help to understand how brain networks function and what the features of
their dynamic behavior are.

.. note::
   This section assumes that you have prior knowledge of how to use NEST Desktop. If you have not used NEST Desktop
   before, please read the User Documentation first (:doc:`/user/index`).


Course organisation
===================

To support the organization of a course, we provide some hints for course instructors:

- :doc:`/lecturer/course-design`
- :doc:`/lecturer/didactic-concept`

Additionally, we provide course materials to be handed out to participants:

- :doc:`/lecturer/first-steps`
- :doc:`/lecturer/course-protocol`

.. toctree::
   :hidden:

   course-design
   didactic-concept
   first-steps
   course-protocol


Course topics
=============

This guide shows how you can teach the biophysics of neurons, synapses and large networks of the brain to students using
NEST Desktop. Video tutorials illustrate important aspects of the course work. The provided material could be used to
prepare handouts for students.


Neuron response
---------------

This section provides sample assignments for students with little prior knowledge. The focus lies on the activity
dynamics of single neurons. In all assignments we use :code:`iaf_psc_alpha` as our neuron model. It is studied how a
neuron responds to different types of input.

- :doc:`/lecturer/neuron-response/single-neuron-direct-current-injection`
- :doc:`/lecturer/neuron-response/single-neuron-noise-current-injection`
- :doc:`/lecturer/neuron-response/single-neuron-synaptic-input`
- :doc:`/lecturer/neuron-response/single-neuron-poisson-input`

.. toctree::
   :hidden:
   :maxdepth: 0

   neuron-response/single-neuron-direct-current-injection
   neuron-response/single-neuron-noise-current-injection
   neuron-response/single-neuron-synaptic-input
   neuron-response/single-neuron-poisson-input


Neuron activity
---------------

This section covers advanced topics for students with previous knowledge in neurobiology. Here, we cover the activity
dynamics of single neurons and of neuronal networks.

- :doc:`/lecturer/neuron-activity/hodgkin-huxley-action-potential`
- :doc:`/lecturer/neuron-activity/point-neuron-conductance`

.. toctree::
   :hidden:
   :maxdepth: 0

   neuron-activity/hodgkin-huxley-action-potential
   neuron-activity/point-neuron-conductance


Network activity
----------------

This section illustrates how NEST Desktop might be used for research in computational neuroscience. A typical example
covers the activity dynamics of neuronal networks with multiple interacting populations.

- :doc:`/lecturer/network-activity/network-dynamics`
- :doc:`/lecturer/network-activity/networks-decision-making`

.. toctree::
   :hidden:
   :maxdepth: 0

   network-activity/network-dynamics
   network-activity/networks-decision-making
