@echo off

:a
set /p i_obj="Enter input 3D mesh model path: "

if not exist %i_obj% (
	echo %i_obj% does not exist
	goto a
)

set i_cloudCompare=%ProgramFiles%\CloudCompare\CloudCompare.exe
echo %i_cloudCompare%
:c
if exist %i_cloudCompare% (
	echo CloudCompare located in %i_cloudCompare%
	goto b
)

echo CloudCompare not found in %i_cloudCompare%
set /p i_cloudCompare ="Enter path to CloudCompare.exe: "
goto c

:b
set i_fileToVox="%~dp0FileToVox\FileToVox.exe"
:e
if exist %i_fileToVox% (
	echo FileToVox located in %i_fileToVox%
	goto d
)

echo FileToVox not found in %i_fileToVox%
set /p i_fileToVox ="Enter path to FileToVox.exe: "
goto e

:d

set i_vox2schematic="%~dp0python_scripts\bin\vox2schematic.py"

if exist %i_vox2schematic% (
	echo vox2schematic located in %i_fileToVox%
	
) else (
	echo vox2schematic not found in %i_vox2schematic% !
	goto fail
)
echo please wait, converting mesh to point cloud
start cmd /k ""%i_cloudCompare%"  -AUTO_SAVE OFF -o -GLOBAL_SHIFT AUTO "%i_obj%" -SAMPLE_MESH DENSITY 100 -APPLY_TRANS "%~dp0settings\transformation_matrix.txt" -C_EXPORT_FMT PLY -NO_TIMESTAMP -SAVE_CLOUDS FILE TMP_outputfiles/point_cloud_output.ply"

:wait
if not exist "%~dp0TMP_outputfiles/point_cloud_output.ply" (
	timeout 1 > NUL
	echo "waiting1"
	goto wait
)
echo point cloud located!
wscript "%~dp0ExitCloudCompare.vbs"
echo please wait, converting point cloud to vox file
"%i_FileToVox%" -i "%~dp0TMP_outputfiles/point_cloud_output.ply" -o "%~dp0TMP_outputfiles/vox_output.vox" -p "%~dp0settings\minecraft_palette.png" --chunk-size=256

:wait2
if not exist "%~dp0TMP_outputfiles/vox_output.vox" (
	timeout 1 > NUL
	echo "waiting2"
	goto wait2
)

echo vox file located!
echo please wait, converting vox file to schematic

wscript "%~dp0SaveVoxFile.vbs"
echo SAVED
cd "%i_vox2schematic%"\..
python vox2schematic.py "%~dp0TMP_outputfiles/vox_output.vox" -o "%~dp0result/schematic_output.schematic"

:wait3
if not exist "%~dp0result/schematic_output.schematic" (
	timeout 1 > NUL
	echo "waiting3"
	goto wait3
)
del "%~dp0TMP_outputfiles\vox_output.vox"
del "%~dp0TMP_outputfiles\point_cloud_output.ply"
echo minecraft schematic created at %~dp0result/schematic_output.schematic , import it into minecraft using for example the amulet world editing tool!

:fail
pause
