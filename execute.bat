@echo off
set scripts= "D:\daguado\dev\P02_generar_geometrias\scripts"
set venv= "D:\daguado\dev\P02_generar_geometrias\env"
set code= "%1"
set table= "%2"
set name= "%3"
set wkid= "%4"
set row= "%5"

call %venv%\Scripts\activate.bat
%venv%\Scripts\python.exe %scripts%\rungeom.py %code% %table% %name% %wkid% %row%
call %venv%\Scripts\deactivate.bat
@echo on