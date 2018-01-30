import os


namebat = 'execute.bat'

dirmain = os.path.dirname(__file__)

venv = os.path.join(dirmain, 'env')
pathbat = os.path.join(dirmain, namebat)

scripts = os.path.join(dirmain, 'scripts')

if os.path.exists(pathbat):
	os.remove(pathbat)

bat = open(namebat, 'w')

bat.write('@echo off\n')
bat.write('set scripts= "{}"\n'.format(scripts))
bat.write('set venv= "{}"\n'.format(venv))
bat.write('set code= "%1"\n')
bat.write('set table= "%2"\n')
bat.write('set name= "%3"\n')
bat.write('set wkid= "%4"\n')
bat.write('set row= "%5"\n')
bat.write('\n')
bat.write('call %venv%\\Scripts\\activate.bat\n')
bat.write('%venv%\Scripts\python.exe %scripts%\\rungeom.py %code% %table% %name% %wkid% %row%\n')
bat.write('call %venv%\\Scripts\deactivate.bat\n')
bat.write('@echo on\n')

bat.close()