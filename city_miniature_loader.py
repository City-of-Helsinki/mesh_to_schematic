import math
import requests
import zipfile
from remotezip import RemoteZip as RemoteZip
import sys
from generate_city_model import generate_city_tile
import os
import shutil

def loadtile(leftx,lefty,distx,disty,tmppath,destpath,destpathobj):
    originx = 25490000
    originy = 6668000
    origincode = 668490 #THIS NEEDS TO BE FIXED SO IT USES THE PARAM FROM 2kmx2km

    originxid = math.floor(originx/2000)
    originyid = math.floor(originy/2000)

    rightx = leftx+distx
    righty = lefty+disty

    leftxid = math.floor(leftx/2000)
    leftyid = math.floor(lefty/2000)

    rightxid = math.floor(rightx/2000)
    rightyid = math.floor(righty/2000)

    leftdeltax = leftxid-originxid
    leftdeltay = leftyid-originyid

    rightdeltax = rightxid-originxid
    rightdeltay = rightyid-originyid
    lod = "L20"

    #250m
    #668490a1 = 7 1
    xoffset = 7
    yoffset = 1
    originxid250 = math.floor(originx/250)
    originyid250 = math.floor(originy/250)

    leftxid250 = math.floor(leftx/250)
    leftyid250 = math.floor(lefty/250)

    rightxid250 = math.floor(rightx/250)
    rightyid250 = math.floor(righty/250)

    leftdeltax250 = leftxid250-originxid250
    leftdeltay250 = leftyid250-originyid250

    rightdeltax250 = rightxid250-originxid250
    rightdeltay250 = rightyid250-originyid250
    folderpath = ""
    for x in range(leftdeltax,rightdeltax+1):
        for y in range(leftdeltay,rightdeltay+1):
            tilecode = str(origincode + x*2 + y*2000)+"x2"
            url = "http://3d.hel.ninja/data/mesh/Helsinki3D-MESH_2017_OBJ_2km-250m_ZIP/Helsinki3D_2017_OBJ_"+tilecode+".zip"
            downloadabletiles = []
            for x2 in range(0,8):
                for y2 in range(0,8):
                    coordx = x*2000+x2*250+250
                    coordy = y*2000+y2*250+250
                    isinbounds = (coordx <= (rightdeltax250)*250 and coordx > (leftdeltax250)*250 and coordy <= (rightdeltay250)*250 and coordy > (leftdeltay250)*250)
                    if (isinbounds):
                        downloadabletiles.append("Tile_+"+str(x*8+x2+xoffset).zfill(3)+"_+"+str(y*8+y2+yoffset).zfill(3))
            print("downloadable " + str(downloadabletiles) + ", " + tilecode)
            try:
                with RemoteZip(url) as zip:
                    for zip_info in zip.infolist():
                        for downloadabletile in downloadabletiles:
                            if lod in zip_info.filename and downloadabletile in zip_info.filename:# and ".obj" in zip_info.filename:
                                zip.extract(zip_info.filename,tmppath)
                                folderpath=os.path.dirname(zip_info.filename)
            except:
                print('url ' + url + ' probably not exist')
    #generate_city_tile(tmppath,destpath)
    print("folderpath: " + folderpath)
    if len(folderpath) > 1:
        generate_city_tile(leftx,lefty,rightx,righty,tmppath+"/"+folderpath,destpathobj)
    #os.system("C: &\"C:/Program Files/Blender Foundation/Blender 2.93/Blender.exe\" --background --python "+os.path.realpath(__file__) + "/../generate_city_model.py "+ str(leftx)+" "+ str(lefty)+" "+ str(rightx) +" "+str(righty)+" "+tmppath+"/"+folderpath +" "+destpathobj)
                
                