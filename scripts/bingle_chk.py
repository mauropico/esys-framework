#bingle_chk.py: A simple two-particle collision simulation
# with data output via a CheckPointer
# Author: D. Weatherley
# Date: 15 May 2007
# Organisation: ESSCC, University of Queensland
# (C) All rights reserved, 2007.
#
#
#import the appropriate ESyS-Particle modules:
from esys.lsm import *
from esys.lsm.util import Vec3, BoundingBox
#instantiate a simulation object
#and initialise the neighbour search algorithm:
sim = LsmMpi(numWorkerProcesses=1, mpiDimList=[1,1,1])
sim.initNeighbourSearch(
    particleType="NRotSphere",
    gridSpacing=2.5,
    verletDist=0.5
)
#specify the number of timesteps and timestep increment
sim.setNumTimeSteps(10000)
sim.setTimeStepSize(0.001)
#specify the spatial domain for the simulation:
domain = BoundingBox(Vec3(-20,-20,-20), Vec3(20,20,20))
sim.setSpatialDomain(domain)
#add the first particle to the domain:
particle=NRotSphere(id=0, posn=Vec3(-5,5,-5), radius=1.0, mass=1.0)
particle.setLinearVelocity(Vec3(1.0,-1.0,1.0))
sim.createParticle(particle)
#add the second particle to the domain:
particle=NRotSphere(id=1, posn=Vec3(5,5,5), radius=1.5, mass=2.0)
particle.setLinearVelocity(Vec3(-1.0,-1.0,-1.0))
sim.createParticle(particle)
#specify the type of interactions between colliding particles:
sim.createInteractionGroup(
    NRotElasticPrms(
        name = "elastic_repulsion",
        normalK = 10000.0,
        scaling = True
    )
)
#add a CheckPointer to save simulation data at regular intervals:
sim.createCheckPointer (
    CheckPointPrms (
        fileNamePrefix = "cpt",
        beginTimeStep = 0,
        endTimeStep = 10000,
        timeStepIncr = 100
    )
)
#Execute the simulation
sim.run()
