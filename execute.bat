@echo off
set scripts= "D:\daguado\dev\P02_generar_geometrias\scripts"
set venv= "D:\daguado\dev\P02_generar_geometrias\env"
set code= "%1"
set table= "%2"
set name= "%3"
set wkid= "%4"

call %venv%\Scripts\activate.bat
python %scripts%\rungeom.py %code% %table% %name% %wkid%
call %venv%\Scripts\deactivate.bat
@echo on
