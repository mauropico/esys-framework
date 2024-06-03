#!/bin/sh

# Execute script with ESySParticle.
mpirun -np 2 esysparticle scripts/bingle_chk.py

# In progress:
# Dump to VTK for Paraview Visualization
#dump2vtk -i ./cpt -o ./frame -t 0 1000 100

