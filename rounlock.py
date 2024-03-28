# # Roblox FPS Unlocker | https://github.com/coolpancakes
# Unlocks FPS framerate

import time
import os
from pathlib import Path


def banner():
    print(r'''

			made by coolpancakes | RoUnlock | https://github.com/coolpancakes


    ____        __  __      __           __  
   / __ \____  / / / /___  / /___  _____/ /__
  / /_/ / __ \/ / / / __ \/ / __ \/ ___/ //_/
 / _, _/ /_/ / /_/ / / / / / /_/ / /__/ ,<   
/_/ |_|\____/\____/_/ /_/_/\____/\___/_/|_|  



		''')

    print('[:] Adding files...')
    print('[:] Writing...')
    time.sleep(2)
    print('[:] SUCCESS!')
    time.sleep(2)


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
                create_file = os.system('mkdir ClientSettings')
                if create_file == 1:
                    os.chdir('ClientSettings')
                    with open('ClientAppSettings.json', 'w') as fps:
                        fps.write('{"DFIntTaskSchedulerTargetFps": 101010}')
                        os.system('cls')
                        banner()
                else:
                    os.chdir('ClientSettings')
                    with open('ClientAppSettings.json', 'w') as fps:
                        fps.write('{"DFIntTaskSchedulerTargetFps": 101010}')
                        banner()


add_json()
