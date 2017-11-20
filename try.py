import os
import sys

sys.path.append('Serias_for_Origin/')
sys.path.append('Serias_for_Origin/modules')

###########################################################
class Path_file:
    def __init__ (self, name, path):
        self.name = name
        self.path = path

class Transition:
    def __init__(self, J, Ka, Kc):
        self.J = J
        self.Ka= Ka
        self.Kc = Kc
        self.R_Tr = []
        self.Q_Tr = []
        self.P_Tr = []
        self.R_Tr_f1 = []
        self.Q_Tr_f1 = []
        self.P_Tr_f1 = []
        self.R_Tr_f2 = []
        self.Q_Tr_f2 = []
        self.P_Tr_f2 = []

class Info_Transitions:
    def __init__ (self, J,Ka,Kc,Trans=0.0,I=0.0,E=0.0):
        self.J = J
        self.Ka= Ka
        self.Kc = Kc
        self.Trans = Trans
        self.I = I
        self.E = E
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

import clear_file
import comments_clear
import find_separation
import separate_transitions
import check_branch

#J_separate = find_separation.Find_Separation(ini_path.path) # fint out J in separation

file = open(ini_path.path, 'r')
count = 0

#Inf_Transition = Info_Transitions(0,0,0)
#Quan_number_UpSt = Info_Transitions (0,0,0)

while (True):
    str1=file.readline()

    if len(str1) == 0:
        beak

    if str1.find('Sea',0,len(str1))!=-1:
        str1=str1.split()
        _,J0,Ka0,Kc0,*_=str1 
        J0=int(J0)
        Ka0=int(Ka0)
        Kc0=int(Kc0)

        Up_State1 = Transition(J0, Ka0, Kc0)
        count+=1
        ref = Up_State1
        file.seek(0) 
 
        break
print (count)
while (True):
    str1=file.readline()
    if len(str1)==0:
        break

    if str1.find('Sea',0,len(str1))!=-1:
        str1=str1.split()
        _,J0,Ka0,Kc0,*_=str1
        J0=int(J0)
        Ka0=int(Ka0)
        Kc0=int(Kc0)

        print (str1)
        print (abs(ref.J-J0),abs (ref.Kc-Kc0),ref.Ka,Ka0)
        if abs(ref.J-J0) == abs (ref.Kc-Kc0) and ref.Ka == Ka0:
            continue
        else:
            print ('@')
            if count == 1:
                Up_State2 = Transition(J0, Ka0, Kc0)
                count+=1
                ref = Up_State2
                continue
            else:
                if ref == Up_State1:
                    ref = Up_State2
                elif ref == Up_State2:
                    ref = Up_State1

    else:
        print (str1)
        separate_transitions.Separate_transitions(J0,Ka0,Kc0,str1,ref)


print (Up_State2.R_Tr)

file2 = open(res_path.path, 'w')

if count > 1:
    name_list = [Up_State1, Up_State2]
else: name_list = [Up_State1]

for name in name_list:
    file2.write('\n\n!!!!!!!!!!!!!\n')
    file2.write('!!!--R Branch--!!!\n')
    for i in range(len(name.R_Tr)):
        if i == 0:
            file2.write('%f %f\n' % (name.R_Tr[i][0], name.R_Tr[i][1]))
        else:
            file2.write('%f %f %f\n' % (name.R_Tr[i][0], name.R_Tr[i][1],\
                                     name.R_Tr[i][0]-name.R_Tr[i-1][0] ))

    file2.write('\n!!!--Q Branch--!!!\n')
    for i in range(len(name.Q_Tr)):
        file2.write('%f %f\n' % (name.Q_Tr[i][0],name.Q_Tr[i][1]))

    file2.write('\n!!!--P Branch--!!!\n')
    for i in range(len(name.P_Tr)):
        file2.write('%f %f\n' % (name.P_Tr[i][0], name.P_Tr[i][1]))

    for attribute in [name.P_Tr_f1,name.P_Tr_f2,name.R_Tr_f1,name.R_Tr_f2,\
                      name.Q_Tr_f1,name.Q_Tr_f2]:
        if len(attribute)!=0:
            file2.write('\n!!!--Forbidden Branch--!!!\n')
            for i in range(len(attribute)):
                if i == 0:
                    file2.write('%f %f\n' % (attribute[i][0], attribute[i][1]))
                else:
                    file2.write('%f %f %f\n' % (attribute[i][0], attribute[i][1],\
                    attribute[i][0]-attribute[i-1][0]))
'''
elif count == 1:

    file2.write('!!!--R Branch--!!!\n')
    for i in range(len(Up_State1.R_Tr)):
        file2.write('%f %f\n' % (Up_State1.R_Tr[i][0], Up_State1.R_Tr[i][1]))

    file2.write('\n!!!--Q Branch--!!!\n')
    for i in range(len(Up_State1.Q_Tr)):
        file2.write('%f %f\n' % (Up_State1.Q_Tr[i][0], Up_State1.Q_Tr[i][1]))

    file2.write('\n!!!--P Branch--!!!\n')
    for i in range(len(Up_State1.P_Tr)):
        file2.write('%f %f\n' % (Up_State1.P_Tr[i][0], Up_State1.P_Tr[i][1]))



file2 = open(res_path.path, 'w')
file2.write('!!!--R Branch--!!!\n')
for i in range(len(Tr.R_Tr)):
    file2.write('%f %f\n' % (Tr.R_Tr[i], Tr.R_I[i]))

file2.write('\n!!!--Q Branch--!!!\n')
for i in range(len(Tr.Q_Tr)):
    file2.write('%f %f\n' % (Tr.Q_Tr[i], Tr.Q_I[i]))

file2.write('\n!!!--P Branch--!!!\n')
for i in range(len(Tr.P_Tr)):
    file2.write('%f %f\n' % (Tr.P_Tr[i], Tr.P_I[i]))

 '''


