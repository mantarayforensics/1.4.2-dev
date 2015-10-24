#DESCRIPTION: This script runs unix2dos against a file
#INPUT: absolute path to a file
#OUTPUT: NONE

#########################COPYRIGHT INFORMATION############################
#Copyright (C) 2011  dougkoster@hotmail.com				                 #
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

import subprocess

def unix2dos(infile):
	unix2dos_command = "sudo unix2dos " + infile
	subprocess.call([unix2dos_command], shell=True)
