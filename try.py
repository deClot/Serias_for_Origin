import os
import sys

sys.path.append('Serias_for_Origin/')
sys.path.append('Serias_for_Origin/modules')

###########################################################
class Path_file:
    def __init__ (self, name, path):
        self.name = name
        self.path = path
###########################################################

ini_path = Path_file ('ini', '')
res_path = Path_file ('res', '')

paths =[ini_path,\
        res_path]

dir_path = ''

for i in range(len(paths)):
    paths[i].path=os.path.abspath(dir_path+paths[i].name)
    if os.path.exists(paths[i].path)==False:
       dir_path = 'Serias_for_Origin/'
       paths[i].path=os.path.abspath(dir_path+paths[i].name)

#print (ini_path.path, id(ini_path.path), paths[0].path, id( paths[0].path))
############################################################

import find_separation

J_separate = find_separation.Find_Separation(ini_path.path) # fint out J in separation

