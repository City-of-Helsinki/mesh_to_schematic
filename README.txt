For OBJToMinecraft to work you have to install the free open source software CloudCompare:http://www.cloudcompare.org/


How it works

Run objToMinecraft.bat
The program takes an input mesh file, like obj/dae/ply/fbx...
It converts it to a point cloud using Cloud Compare (Cloud Compare has to be installed)
It converts the point cloud into a MagicaVoxel .vox file using FileToVox
It uses a VBS script to open the vox file using MagicaVoxel.exe, and sends the keypress F2 to save the file.
(This extra step is necessary, as it somehow fixes some file format issues and makes the file readable for the next application)
The VBS script then closes MagicaVoxel.
The program converts the vox file to a Minecraft .schematic file using McThing's Vox2Schematic.py
The .schematic file can be added to minecraft using a mod, or a world edit tool such as Amulet https://www.amuletmc.com/