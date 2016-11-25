#!/usr/bin/python

# Allow to transcode a SROS config file collected by admin display-config in a flat config file
# The only limitation is do not have 4 space characters in your description as indentation is 
# made of 4 space characters
#
#  
import sys

# INIT file path
file_cfg = "./" + str(sys.argv[1])

try:
	#Load config file
	cfg_desc = open(file_cfg, 'r')
except IOError:
	print "\nError: file not found"
	sys.exit()
	
#target file 
file_target = "./flat-" + str(sys.argv[1])
flat_desc = open(file_target, 'w')

tab_LINE = [] 
index =0 
last_indentation =0
indentation = 0
exit_found = False

for read in cfg_desc :
	# Read an config line
	line = read
	# Extract Comment lines
	isComment = line[0]
	isEcho = line[0:4]
	# Exclude comment, echo and empty line 
	if isComment != '#':
		if isEcho != 'echo':
			if line.strip()!='' and line.strip() != 'exit all':
				#SROS indentation is made of 4 space characters
				indentation = line.count('    ')
				
				#Manage line that are not made of an exit 
				if line.strip() != 'exit':	
					#If current line is more specific that previous one add word to the list
					if ((indentation > last_indentation ) or indentation == 0 ):
						tab_LINE.append(line.strip())
						index+=1
						exit_found = False
					#If current line is less specific that previous one remove word to the list
					if (indentation < last_indentation ):
						del tab_LINE[index-1]
						tab_LINE.append(line.strip())		
					#If current line is same specific that previous and depending on last exit found write config line in file
					if ((last_indentation == indentation ) and indentation!=0 ):
						if exit_found:							
							del tab_LINE[index-1]
							tab_LINE.append(line.strip())
							flat_desc.write(' '.join(tab_LINE) + '\n')
						else:
							flat_desc.write(' '.join(tab_LINE) + '\n')
							del tab_LINE[index-1]
							tab_LINE.append(line.strip())
					last_indentation = indentation
				#Manage line with an exit statement
				else:
					if exit_found != True:
						if last_indentation != indentation:
							flat_desc.write(' '.join(tab_LINE) + '\n')
							del tab_LINE[index-1]
							index-=1
							del tab_LINE[index-1]
							index-=1
							last_indentation = indentation - 1
							exit_found = True					
						else:
							exit_found = False
					else:
						del tab_LINE[index-1]
						index-=1	
						last_indentation = indentation - 1
				
cfg_desc.close ()
flat_desc.close()
mystr = "\nFlat config has been pushed in file: " + file_target
print mystr
