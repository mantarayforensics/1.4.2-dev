#This program will recursively remove the duplicates from a folder and all subfolders using fdupes
#INPUT: Absolute path to the folder you want to process
#OUTPUT: None
#NOTE: FDUPES must be installed for this program to function properly

#########################COPYRIGHT INFORMATION############################
#Copyright (C) 2011 	dougkoster@hotmail.com			                 #
#This program is free software: you can redistribute it and/or modify    #
#it under the terms of the GNU General Public License as published by    #
#the Free Software Foundation, either version 3 of the License, or       #
#(at your option) any later version.                                     #
                                                                         #
#This program is distributed in the hope that it will be useful,         #
#but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
#GNU General Public License for more details.                            #
                                                                         #
#You should have received a copy of the GNU General Public License       #
#along with this program.  If not, see http://www.gnu.org/licenses/.     #
#########################COPYRIGHT INFORMATION############################

#import modules
from easygui import *
from get_output_location import *
from done import *
from unix2dos import *
import os
from os.path import join
import re
import shutil
import io
import sys
import string
import subprocess

def remove_dupes_module(folder, outfile):

	#add quotes to image path in case of spaces
	quoted_path = "'" +folder +"'"

	#ask if user wants to backup their files before removing dupes
	answer = boolbox(msg='Do you want to make a backup copy of your folder before removing the dupes?', title=' ', choices=('Yes', 'No'), image=None)

	if(answer == 1):
		copy_command = "sudo cp -r " + quoted_path + " /tmp"
		print("Copying folder to /tmp\n")
		subprocess.call([copy_command], shell=True)
	
		msgbox(msg='(Your folder has been copied to /tmp)', title='Copy Complete ', ok_button='OK', image=None, root=None)

	no_quotes = quoted_path.replace("'","")
	log_file_path = "/tmp/duplicates_log.txt"

	remove_dupes_command = "sudo fdupes -r -d -N " + quoted_path + " >> /tmp/fdupes_duplicates_log.txt"
	print ("The remove dupes command is: " + remove_dupes_command + "\n\n")
	print ("Removing duplicate files recursively from folder: " + quoted_path + "\n\n")


	#run the remove dupes command
	subprocess.call([remove_dupes_command], shell=True)

	#get filesize of mmls_output.txt
	file_size = os.path.getsize("/tmp/fdupes_duplicates_log.txt") 

	#if filesize of mmls output is 0 then run parted
	if(file_size == 0):
		print("No duplicates found\n")
		outfile = open(log_file_path, 'wt+')
		outfile.write("No duplicate files found!")
		os.remove("/tmp/fdupes_duplicates_log.txt")
		#close outfile
		outfile.close()
	else:
		#if log file exists then run unix2dos against the logfile
		unix2dos("/tmp/fdupes_duplicates_log.txt")

		
		

	#remove empty directories	
	for root,dirs,files in os.walk(no_quotes):
		for directories in dirs:
			dir_name = os.path.join(root,directories)
			#if directory is empty then delete it
			if not os.listdir(dir_name):
				os.rmdir(dir_name)

	#move log file to folder
	move_command = "mv /tmp/*duplicates_log.txt " + quoted_path
	subprocess.call([move_command], shell=True)

	

	

