#!/bin/sh

export PATH=/usr/local/bin/:$PATH
export LIBRARY_PATH=/usr/local/lib/:$LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/local/lib/:$LD_LIBRARY_PATH
export PYTHONPATH=/usr/local/lib/python3.10/dist-packages:/usr/local/lib/python3/dist-packages:/usr/local/lib/python3/dist-packages:$PYTHONPATH
export PYTHONPATH="/usr/local/lib/python3/dist-packages/gengeo:${PYTHONPATH}"

# Execute simulation script with ESyS-Particle.
mpirun -np 2 esysparticle scripts/bingle_chk.py

# Dump to VTK results for Visualization with Paraview
#dump2vtk -i ./cpt -o ./frame -t 0 1000 100

# Generate geometry using GenGeo library. 
# python scripts/generate_geometry.py

# To navigate in the container (similar to ssh into the machine)
#bash