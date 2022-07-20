#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import networkx as nx
import numpy as np

def main():
    INPUT_PATH = '/Users/omersedes/Documents/Personal/PostPhD/suspensions-research/KCoreExtraction/data/input'
    OUTPUT_PATH = '/Users/omersedes/Documents/Personal/PostPhD/suspensions-research/KCoreExtraction/data/output'

    Cycles = 4001
    NumberofParticles = 2000

    AverageDegree = np.zeros(Cycles)
    AverageDegree_Net = np.zeros(Cycles)
    Nodes = np.zeros(Cycles)
    Edges = np.zeros(Cycles)
    OneShell = np.zeros(Cycles)
    TwoShell = np.zeros(Cycles)
    ThreeShell = np.zeros(Cycles)
    Coreness = np.zeros((Cycles, NumberofParticles), dtype=int)

    # Open interaction file - Input
    int_file_name = os.path.join(INPUT_PATH, 'int_D2N2000VF0.77Bidi1.4_0.5Square_1_pardata_phi0.77_stress2cl.dat')
    int_file = open(int_file_name, 'r')

    # Open coreness file - Output
    core_file_name = os.path.join(OUTPUT_PATH, 'coreness_D2N2000VF0.77Bidi1.4_0.5Square_1_pardata_phi0.77_stress2cl.csv')
    core_file = open(core_file_name, 'w')

    # Read until the end of the header lines
    line = int_file.readline()

    while line != '\n': #Searching for the blank line
        line = int_file.readline()
    int_file.readline()

    #initialize cycle number and the edge list
    cy = -1
    EdgeList = list()

    # Read the interactions
    for line in int_file:
        Entry = line.split(' ')
        if Entry[0] == '#': # New Cycle, new frictional network 
            #Store Graph And Calculate the Metrics
            cy = cy + 1
            Frictional_Network = nx.Graph(EdgeList)
            coreness = nx.core_number(Frictional_Network)
            
            print("writing graph")

            K3Core = nx.k_core(Frictional_Network, 3)
            K2Core = nx.k_core(Frictional_Network, 2)
            K1Core = nx.k_core(Frictional_Network, 1)

            K3Shell = nx.k_shell(Frictional_Network, 3)
            K2Shell = nx.k_shell(Frictional_Network, 2)
            K1Shell = nx.k_shell(Frictional_Network, 1)

            #nx.write_graphml(Frictional_Network,"FrictionalNetwork.graphml")
            #nx.write_graphml(K3Core,"K3Core.graphml")
            #nx.write_graphml(K2Core,"K2Core.graphml")
            #nx.write_graphml(K1Core,"K1Core.graphml")

            #nx.write_edgelist(Frictional_Network, "FrictionalNetwork.csv", delimiter=',', data=False)
            #nx.write_edgelist(K3Core, "K3Core.csv", delimiter=',', data=False)
            #nx.write_edgelist(K2Core, "K2Core.csv", delimiter=',', data=False)
            #nx.write_edgelist(K1Core, "K1Core.csv", delimiter=',', data=False)

            #nx.write_edgelist(K3Shell, "K3Shell.csv", delimiter=',', data=False)
            #nx.write_edgelist(K2Shell, "K2Shell.csv", delimiter=',', data=False)
            #nx.write_edgelist(K1Shell, "K1Shell.csv", delimiter=',', data=False)

            for keys in coreness:
                Coreness[cy][keys] = coreness[keys]
            
            print(Coreness[cy])
            print(cy)

            #Reset Graph
            EdgeList = list()
            Frictional_Network = nx.Graph()
        else:
            if int(Entry[2]) > 1: #Check the contact state flag, here we require > 1 for frictional contacts
                #print(Entry[2])
                EdgeList.append((int(Entry[0]), int(Entry[1])))

    for i in range(Cycles):
        for j in range(NumberofParticles):
            core_file.write(str(Coreness[i][j]) + ',')
        core_file.write('\n')

    int_file.close()
    core_file.close()



if __name__ == '__main__':
    main()

