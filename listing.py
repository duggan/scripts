import os, json

''' Produce an ordered list of the top level files/directories in the current directory '''
dirlist = {}
for entry in os.listdir('.'):
    if (entry != os.path.basename(__file__)):
        dirlist[entry] = 0

print json.dumps(dirlist, sort_keys=True, indent=4)
