# Packages to be used
import os
import subprocess
import pandas as pd
import numpy as np
from matplotlib import pyplot

## Functions
#############################################################
def get_shear_rate(filename):
    # Extract shear rate from the file name
    shear_rate = filename.split("rate")[1].split("cl.dat")[0]

    # Read the contents of the file into a dataframe

    return shear_rate

#############################################################
def get_shear_rates(directory):
    shear_rate_list = list()

    for filename in os.listdir(directory):
        if filename.startswith("pst_"):
            shear_rate = get_shear_rate(filename)
            shear_rate_list.append(float(shear_rate))

    shear_rate_list.sort()

    return shear_rate_list

#############################################################
def read_pst_file(filename):
    # Allocate Particle Sigma Array
    particle_sigma_array = np.empty((500,2001))

    with open(filename, 'r') as f:
        # Skip initial comments that starts with #
        while True:
            line = f.readline()
            # break while statement if it is not a comment line
            # i.e. does not startwith #
            if not line.startswith('#'):
                break

        # Read until the start of next time block
        time_index = 0 # Initiate time index
        particle_index = 0 # Initiate particle index
        for line in f:
            if line.startswith('#'):
                time_index += 1 # increment time index
                particle_index = 0 # reset particle index
            else:
                particle_sigma_array[particle_index, time_index] = line.split(' ')[2]
                particle_index += 1 # increment particle index

    return particle_sigma_array

#############################################################
def read_int_file(filename):
    # Allocate Particle Z Array
    particle_z_array = np.zeros((500,2001))

    with open(filename, 'r') as f:
        # Skip initial comments that starts with #
        while True:
            line = f.readline()
            # break while statement if it is not a comment line
            # i.e. does not startwith #
            if not line.startswith('#'):
                break
    
        # Read until the start of next time block
        
        for line in f:
            if line.startswith('#'):
                time_index = int(100*float(line.split(' ')[1])) # set time index
            else:
                line_list = line.split(' ')
                first_particle = int(line_list[0])
                second_particle = int(line_list[1])
                contact_flag = int(line_list[2])
                if contact_flag > 1:
                    particle_z_array[first_particle, time_index] += 0.5
                    particle_z_array[second_particle, time_index] += 0.5
                    #print(first_particle, second_particle, contact_flag)
    
    return particle_z_array
#############################################################

def build_histogram(particle_sigma_array, particle_z_array):
    # Allocate Histogram Array
    sigma_histogram_array = np.zeros((25,150),dtype=np.int32)
    z_histogram_array = np.zeros((25,1),dtype=np.int32)

    for time in range(2001):
        for particle in range(500):
            z_index = int(particle_z_array[particle, time])
            z_histogram_array[z_index, 0] += 1
            if particle_sigma_array[particle, time] > 0:
                sigma_index = int(10*(np.log10(particle_sigma_array[particle, time]) + 10))
                sigma_histogram_array[z_index, sigma_index] += 1
            else:
                sigma_histogram_array[z_index, 0] += 1
                


    return sigma_histogram_array, z_histogram_array


# Main routine

def main():
    directory = subprocess.check_output('pwd').strip().decode("utf-8") 
    print(directory)
    shear_rate_list = get_shear_rates(directory)
    print(shear_rate_list)

    np.savetxt("shear_rates_VF56.txt",shear_rate_list, delimiter=" ")

    for shear_rate in shear_rate_list:
        particle_sigma_array = read_pst_file('pst_D3N500VF0.56Bidi1.4_0.5Cubic_1_pardata2_rate'+str(shear_rate)+'cl.dat')
        particle_z_array = read_int_file('int_D3N500VF0.56Bidi1.4_0.5Cubic_1_pardata2_rate'+str(shear_rate)+'cl.dat')
        sigma_histogram, z_histogram = build_histogram(particle_sigma_array, particle_z_array)
        #plot_histogram()

        #print(particle_sigma_array[:, 1000])
        #print(particle_z_array[:, 1000])

        sigma_probability_normalization1 = np.divide(sigma_histogram, z_histogram)
        sigma_probability_normalization2 = np.divide(sigma_histogram, 1000500)
    
        np.savetxt("sigma_histogram_VF56_"+str(shear_rate)+"cl.txt", sigma_histogram, delimiter=" ")
        np.savetxt("z_histogram_VF56_"+str(shear_rate)+"cl.txt", z_histogram, delimiter=" ")
        np.savetxt("sigma_probability1_VF56_"+str(shear_rate)+"cl.txt", sigma_probability_normalization1, delimiter=" ")
        np.savetxt("sigma_probability2_VF56_"+str(shear_rate)+"cl.txt", sigma_probability_normalization2, delimiter=" ")

        print(sigma_histogram[2,:])
        print(sigma_probability_normalization1[2,:])
        
        print(sigma_probability_normalization2[2,:])
        print(z_histogram[:,0])
        print(np.sum(z_histogram[:,0]), np.sum(sigma_probability_normalization1[2,:]))
        
        print(np.unique(particle_z_array))
        print(shear_rate, np.amax(particle_z_array))
        
if __name__ == "__main__":
    main()