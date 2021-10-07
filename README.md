This has been created mainly to generate colored Minecraft models from 3D city mesh models (By default the default settings and scripts make it easiest to generate minecraft worlds from Helsinki's 3D mesh datasets), importing them to a minecraft world. It can also create singular minecraft .schematic files.

Installing:
1. Download mesh_to_schematic from github and unpack the .zip file. You can also use a git client to clone it.
2. Install Microsoft Visual Studio Build Tools for C++ (first install the visual studio installer, then build tools for c++ from the installer) (This step might be skippable if you download and run the Amulet minecraft world editor installer: https://www.amuletmc.com/)
3. Run the setup.bat script

How to run it:

Run start.bat and follow the instructions.

If you wish to generate an entire city and import it into a minecraft world, you need the URL of the dataset.
Helsinki's 3D city mesh data sets can be found from http://3d.hel.ninja/data/mesh/. More info: https://www.hel.fi/helsinki/en/administration/information/general/3d/utilise/

Also, if you choose to generate an entire city, you will have to copy a minecraft world into the mesh_to_schematic folder, and rename it "city_map". To do this, you can download a minecraft map online, or, for example, generate a superfalt map in Minecraft, and copy it from %appData%/.minecraft/saves and paste it in the mesh_to_schematic folder.

To make sure everything goes succesfully, you shouldn't use your computer while the program is running. If the program crashes, or you wish to stop it, you can just close it.
When you decide to start it again, it will continue from where it last left off. If you wish to, for example, begin generating the city from the start, delete current_generation_coords.txt from the settings folder. 

If you chose to generate a single minecraft .schematic, the .schematic file will be saved in the the "result" folder.
If you chose to generate an entire city, the world will be visible in the city_map minecraft world once the program has ran.


Technical details:
The Vendor folder contains 3rd party scripts and programs that are necessary for the program to operate. 
These programs are:
MagicaVoxel: https://ephtracy.github.io/, a Voxel file editor
CloudCompare: http://www.cloudcompare.org/, an open source point cloud and mesh processing software
FileToVox: https://github.com/Zarbuz/FileToVox, an open source program used to convert point clouds and 3D meshes into voxel files. The FileToVox folder contains a NOTICE.txt file that describes the changes that have been made to that program.
McThings(vox2schematic) and it's dependencies: https://github.com/Voxelers/mcthings A python programming framework for building a 3D World of Scenes in Minecraft. A NOTICE.txt file in the python_scripts details the changes that have been made to the scripts

The pipeline: