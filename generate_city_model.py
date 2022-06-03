import os
import glob
import math
import sys

def generate_city_tile(leftx,lefty,rightx,righty,tmppath, destpath):
    lod = 1

    originx = 25490000
    originy = 6668000
    leftx-=originx
    rightx-=originx
    righty-=originy
    lefty-=originy

    model_dir = tmppath
    obj_list = []
    for dirpath, dirnames, filenames in os.walk(model_dir):
        for filename in [f for f in filenames if f.endswith(".obj")]:
            if (os.path.getsize(os.path.join(dirpath, filename))>0):
                obj_list.append(os.path.join(dirpath, filename))
    cloudcompare_arguments = "-SILENT -AUTO_SAVE OFF"
    # loop through the strings in obj_list and add the files to the scene
    for path_to_file in obj_list:
        cloudcompare_arguments += " -o "+path_to_file
    cloudcompare_arguments += " -MERGE_MESHES -M_EXPORT_FMT OBJ -SAVE_MESHES FILE " + destpath

    #with open(tmppath+"/cloudcompare_arguments.txt", "w") as file:
        #file.write(cloudcompare_arguments)
    #print(cloudcompare_arguments)
    if len("\"C:\\Program Files\\CloudCompare\\CloudCompare.exe\" "+cloudcompare_arguments) > 8192:
        print(cloudcompare_arguments)
    os.system("\"C:\\Program Files\\CloudCompare\\CloudCompare.exe\" "+cloudcompare_arguments)#crop might be unnecessary
#-CROP "+str(leftx)+":"+str(lefty)+":-100:"+str(rightx)+":"+str(righty)+":1500
#-CROP "+str(leftx)+":-100:"+str(lefty)+":"+str(rightx)+":1500:"+str(righty)
#generate_city_tile(int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6]),int(sys.argv[7]),sys.argv[8],sys.argv[9])