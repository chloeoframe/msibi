import os

import numpy as np

from msibi.pair import Pair
from msibi.state import State

rdf_relative_tol = 0.01
rdf_absolute_tol = 0.01

# Load states
state0 = State(k=5, T=1.0, traj_path='query.dcd', top_path='query.pdb')
states = [state0, state1]

# Creating pairs
indices = [a.index for a in state0.traj.top._atoms]
target = np.loadtxt('rdf.txt')
pair0 = Pair('HC-CH', target)

pairs = [pair0, pair3]

# Add pairs to relevant states.
pair0.add_state(state0, target_rdf0, alpha0, pair_indices0)


for n in range(10):
    for state in states:
        gather_potentials(pairs)
        os.system('hoomd {0}'.format(input_script))

    for pair in pairs:
        for state in pair.states:
            pair.compute_current_rdf(state)

        update_all

