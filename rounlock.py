# # Roblox FPS Unlocker | https://github.com/coolpancakes
# Unlocks FPS framerate 

import os
from pathlib import Path

def banner():
    pass


def add_json():
    user = os.getlogin()
    rblx_dir = Path(f'C:/Users/{user}/AppData/Local/Roblox/Versions')
    potential_targets = []
    for rblx in rblx_dir.iterdir():
	potential_targets.append(rblx)
    	for potential_target in potential_targets:
	    for potential_target_inside_dir in potential_target.iterdir():
	        if 'RobloxPlayerBeta.exe' in str(potential_target_inside_dir):
	        os.chdir(str(potential_target_inside_dir).strip(r'\RobloxPlayerBeta.exe'))
	        os.system('mkdir ClientSettings') 
                os.chdir('ClientSettings')
	        with open('ClientAppSettings.json', 'w') as fps:
		    fps.write('{"DFIntTaskSchedulerTargetFps": 101010}')
					

add_json()
