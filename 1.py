############################################
def func_check (list1,J,Ka,Kc,str1):
    if len(list1)==0:
        list1.append([str1])
        return 0
    k=0
    for i in range(len(list1)):
        l=len(list1[i])-1
 #       print(str1)
#        print (i)
#        print (int(J)-1,int(list1[i][l][0]), \
#            int(Ka),int(list1[i][l][1]), \
#            int(Kc)-1,int(list1[i][l][2]))
        if int(J)-1==int(list1[i][l][0]) and \
            int(Ka)==int(list1[i][l][1]) and \
            int(Kc)-1==int(list1[i][l][2]):
 #           print ('!!! add')
#            print (i)
 #           print (list1[i])
 #           print ('\n')
            list1[i].append(str1)
#            print (list1[i])
            k=1
            break
#    print (k)
#    a=input()
    if k==1:
        return 0
    else:
#        print ('! new\n')
        list1.append([str1])
#    a=input()
    return list1

#########################################################

import os

ini_path = os.path.abspath('ini')
res_path = os.path.abspath('res')

if os.path.exists(ini_path)==False:
    ini_path = os.path.abspath('Serias_for_Origin/ini')
    res_path = os.path.abspath('Serias_for_Origin/res')

f=open(ini_path,'r').readlines()

for i in range(len(f)):
    f[i]=f[i].replace('-',' ')
    f[i]=f[i].replace('_',' ')
    f[i]=f[i].replace('+',' ')
    f[i]=f[i].replace('I',' ')
    f[i]=f[i].replace('?',' ')
    f[i]=f[i].replace('st',' ')
    f[i]=f[i].replace('s',' ')
    f[i]=f[i].replace('p',' ')

with open(ini_path,'w') as F:
    F.writelines(f)

F.close()

file=open(ini_path,'r')
list1=[]

count=0

while(True):
    str1=file.readline()
    if len(str1)==0:
        break

    if str1.find('Sea',0,len(str1))!=-1:
        str1=str1.split()
        _,J0,Ka0,Kc0,*_=str1
        count++
        continue
    str1=str1[1:78]
    str1=str1.split()

    if len(str1)==6:
        J,Ka,Kc,Tr,I,E=str1

        list0=func_check(list1,J,Ka,Kc,str1)
        if list0!=0:
            list1=list0
        else:
            continue
    if len(str1)==12:
        J,Ka,Kc,Tr,I,E,*_=str1
        str2=[J,Ka,Kc,Tr,I,E]
        list0=func_check(list1,J,Ka,Kc,str2)
        if list0!=0:
            list1=list0
        else:
            *_,J,Ka,Kc,Tr,I,E=str1
            str2=[J,Ka,Kc,Tr,I,E]
            list0=func_check(list1,J,Ka,Kc,str2)
            if list0!=0:
                list1=list0
            else:
                continue
        *_,J,Ka,Kc,Tr,I,E=str1
        str2=[J,Ka,Kc,Tr,I,E]
        list0=func_check(list1,J,Ka,Kc,str2)
        if list0!=0:
            list1=list0
        else:
            continue
file2=open(res_path,'w')

max=0
for i in range(len(list1)):
    if len(list1[i])>max:
        max=len(list1[i])
#print(max)
#print (len(list1[0]))
#print (list1)
for i in range(max):
    for j in range(len(list1)):
        #print (i, len(list1[j])-1)
        if i>len(list1[j])-1:
            file2.write ('                             \t')
            continue
        file2.write('%3s %3s %3s %s %3.3f\t'%(list1[j][i][0],list1[j][i][1],list1[j][i][2],\
                                           list1[j][i][3],round((float(list1[j][i][4])/100-0.005),4)))
        #print(list1[j][i][3],list1[j][i][4])

    file2.write('\n')
#print (list1)

file2.close()
file.close()
