#!/bin/sh

# Execute script with ESySParticle.
mpirun -np 2 esysparticle scripts/bingle_chk.py

# Dump to VTK for Paraview Visualization
#dump2vtk -i cpt -o frame -t 0 1001 1

