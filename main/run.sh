#!/bin/sh
export PATH=/usr/local/bin/:$PATH
export LIBRARY_PATH=/usr/local/lib/:$LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/local/lib/:$LD_LIBRARY_PATH
export PYTHONPATH=/usr/local/lib/python3.10/dist-packages:/usr/local/lib/python3/dist-packages:$PYTHONPATH

# Execute script with ESySParticle.
mpirun -np 2 esysparticle scripts/bingle_chk.py

# In progress:
# Dump to VTK for Paraview Visualization
#dump2vtk -i ./cpt -o ./frame -t 0 1000 100

