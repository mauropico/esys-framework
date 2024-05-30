import h5py
import numpy as np
import sys
import os

# Specifications of the ESyS-output
# • fields 1, 2 & 3: the X, Y and Z-coordinates of the current particle position
# • field 4: the particle radius
# • field 5: the particle ID
# • field 6: the particle tag (more on tags later)
# • field 7: the particle mass (recall that we set the mass of the second particle to be
# 2.0)
# • fields 8, 9 & 10: the X, Y and Z-coordinates of the initial particle position
# • fields 11, 12 & 13: the X, Y and Z-coordinates of the previous particle position
# • fields 14, 15 & 16: the X, Y and Z-components of the particle velocity
# • fields 17, 18 & 19: the X, Y and Z-components of the net force acting on the particle
# • fields 20, 21 & 22: (used with circular or periodic boundaries) specifies the circular
# shift to be added in the X, Y and Z-directions

# Specify the directory you want to search in
directory = sys.argv[1]
density = float(sys.argv[2])
smoothing_length = 6.9e-2

# Get a list of all .txt files in the directory
information_files = [f for f in os.listdir(directory) if f.endswith('_0.txt')]

for information_file in information_files:
    file_start = information_file.replace("_0.txt","")
    if not os.path.isfile(file_start + '.h5'):
        information_f = open(information_file,'r')
        information = information_f.readlines()
        information_f.close()

        step = float(information[3])
        size = float(information[2])
        simulation_files = information[8]
        simulation_files = simulation_files.split(" ")
        #simulation_files = list(map(str.split('/'), simulation_files))
        time = size * step
        print("Time:", time)
        #print("Simulation Files:", simulation_files)
        #print("Total Particles: ", total_particles)
        total_particles = 0

        for file in simulation_files:
            file = file.split("/")
            file = file[-1]
            if (file != information_file) and (".h5" not in file):
                # Read the simulation output
                with open(file, 'r') as f:
                    data = f.readlines()
                print(file)
                total_particles += int(data[0])
        
        positions = np.zeros((total_particles, 3))
        velocities = np.zeros((total_particles, 3))
        a = np.zeros((total_particles, 3))
        a_grav = np.zeros((total_particles, 3))
        ddeviatoric_stress_dt = np.zeros((total_particles, 9))
        dedt = np.zeros(total_particles)
        deviatoric_stress = np.zeros((total_particles, 9))
        drhodt = np.zeros(total_particles)
        e = np.zeros(total_particles)
        local_strain = np.zeros(total_particles)
        m = np.zeros(total_particles)
        material_type = np.zeros(total_particles)
        number_of_interactions = np.zeros(total_particles)
        p = np.zeros(total_particles)
        rho = np.zeros(total_particles)
        sml = np.zeros(total_particles)
        soundspeed = np.zeros(total_particles)
        total_plastic_strain = np.zeros(total_particles)
        tree_depth = np.zeros(total_particles)
        v_accreted = np.zeros((total_particles, 3))
        particles_done = 0
        
        for file in simulation_files:
            file = file.split("/")
            file = file[-1]
            if (file != information_file) and (".h5" not in file):
                # Read the simulation output
                with open(file, 'r') as f:
                    data = f.readlines()
                
                particle_qty = int(data[0]) 
                
                # Parse the particle position data
                for i in range(1, len(data)-2):
                    split_line = data[i].split()
                    positions[particles_done+i-1:, :] = list(map(float, split_line[:3]))
                    velocities[particles_done+i-1, :] = list(map(float, split_line[13:16]))
                    m[particles_done+i-1] = float(split_line[6])
                    rho[particles_done+i-1] = density
                    sml[particles_done+i-1] = smoothing_length
                particles_done += particle_qty
    

        # Create an HDF5 file and store the particle positions
        with h5py.File(file_start + '.h5', 'w') as hf:
            hf.create_dataset("x",  data=positions)
            hf.create_dataset("v",  data=velocities)
            hf.create_dataset("a",  data=a)
            hf.create_dataset("a_grav",  data=a_grav)
            hf.create_dataset("ddeviatoric_stress_dt",  data=ddeviatoric_stress_dt)
            hf.create_dataset("dedt",  data=dedt)
            hf.create_dataset("deviatoric_stress",  data=deviatoric_stress)
            hf.create_dataset("drhodt",  data=drhodt)
            hf.create_dataset("e",  data=e)
            hf.create_dataset("local_strain",  data=local_strain)
            hf.create_dataset("m",  data=m)
            hf.create_dataset("material_type",  data=material_type)
            hf.create_dataset("number_of_interactions",  data=number_of_interactions)
            hf.create_dataset("p",  data=p)
            hf.create_dataset("rho",  data=rho)
            hf.create_dataset("sml",  data=sml)
            hf.create_dataset("soundspeed",  data=soundspeed)
            hf.create_dataset("total_plastic_strain",  data=total_plastic_strain)
            hf.create_dataset("tree_depth",  data=tree_depth)
            hf.create_dataset("v_accreted",  data=v_accreted)
            hf.create_dataset("time", data=[time])