This has been created mainly to generate colored Minecraft models from 3D city mesh models

For OBJToMinecraft to work you have to install the free open source software CloudCompare:http://www.cloudcompare.org/

How to run it:

Download this repository. If you downloaded it as a .zip, unpack it.
Run mesh_to_schematic.bat
When prompted, enter the path to the 3D mesh you wish to convert to a minecraft schematic.
Example: " Enter input 3D mesh model path: C:\Users\Helsinki3D\Desktop\673497a2\Tile_+1988_+2693.obj "
If everything goes succesfully, the program will save the output .schematic file in the result folder.

Advanced settings:
Currently the program uses the transformation_matrix text file in the settings folder to rotate the model -90 degrees in the X-axis.
If you wish to perform other transformations, you can edit the file. You can generate transform matrixes for example by following this stackoverflow answer: https://blender.stackexchange.com/questions/39228/export-model-transformation-matrix

How it works:

Run objToMinecraft.bat
The program takes an input mesh file, like obj/dae/ply/fbx...
It converts it to a point cloud using Cloud Compare (Cloud Compare has to be installed)
It converts the point cloud into a MagicaVoxel .vox file using FileToVox
It uses a VBS script to open the vox file using MagicaVoxel.exe, and sends the keypress F2 to save the file.
(This extra step is necessary, as it somehow fixes some file format issues and makes the file readable for the next application)
The VBS script then closes MagicaVoxel.
The program converts the vox file to a Minecraft .schematic file using McThing's Vox2Schematic.py
The .schematic file can be added to minecraft using a mod, or a world edit tool such as Amulet https://www.amuletmc.com/
