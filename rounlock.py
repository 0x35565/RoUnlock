# # Roblox FPS Unlocker | https://github.com/coolpancakes
# Unlocks FPS framerate 

import os
from pathlib import Path

def add_json():
	user = os.getlogin()

	# path to start iteration from, uses user variable. 

	rblx_dir = Path(f'C:/Users/{user}/AppData/Local/Roblox/Versions')

	# iterates through the directories and stores all paths in potential_targets list

	potential_targets = []
	for rblx in rblx_dir.iterdir():
		potential_targets.append(rblx)
	
	# iterates through potential_targets list

	for potential_target in potential_targets:

		# for each Path inside of potential_targets, iterate through each one.  

		for potential_target_inside_dir in potential_target.iterdir():

			# IF RobloxPlayerBeta.exe is IN one of those paths, change to the path with RobloxPlayerBeta.exe . 

			if 'RobloxPlayerBeta.exe' in str(potential_target_inside_dir):
				os.chdir(str(potential_target_inside_dir).strip(r'\RobloxPlayerBeta.exe'))

				# creates directory to store JSON.

				os.system('mkdir ClientSettings')

				# hops into the directory creates ClientAppSettings.json and sets the max FPS to 101010. 

				os.chdir('ClientSettings')
				with open('ClientAppSettings.json', 'w') as fps:
					fps.write('{"DFIntTaskSchedulerTargetFps": 101010}')
					

add_json()