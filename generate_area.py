import sys
import os
import math
import subprocess
from load_city_schematics import schematics_to_world

def setup():
    path_2km_input = input("Enter the path of your file: ")
    gen2km(path_2km_input)

def gen2km(path_2km, offsetx = 0, offsety = 0):
    assert os.path.exists(path_2km), "I did not find the file at, "+str(path_2km)
    #folder_name = os.path.basename(path_2km)
    # remove the x2 from the name
    # up ycoord 000000a0-000000a2-000000b0-000000b2-001000a0
    # up xcoord 000000a0-000000a3-000000c0-000000c3-000001a0
    #tile_base_name = folder_name[:-2]
    print("GEN2KM PATH FOUND")
    #Goes through every 250m x 250m tile in the 2km x 2km tile and creates a schematic of them
    for y in range(0,8):
        for x in range(0,8):
            print("GEN2KM "+str(x)+", "+str(y))
            #Figure out what is the name of the 250m x 250m tile that is in the local coordinates x,y (local to the 2km x 2km tile)
            xcoord = x+offsetx
            ycoord = y+offsety
            path_to_250m_tile = path_2km+"tileX"+str(x)+"Y"+str(y)+".obj"
            print(path_to_250m_tile)
            #In case there are many .obj files in the folder, pick the largest one
            if os.path.exists(path_to_250m_tile):

                #Create a .schematic from the chosen .obj file
                subprocess.run([os.path.realpath(__file__) + "\..\mesh_to_schematic.bat", path_to_250m_tile, str(xcoord)+"_"+str(ycoord)+"_"+"ORIGINY"])
                #Add the schematic to the city_map minecraft world using load_city_schematics.py script's schematics_to_world function
                schematics_to_world()