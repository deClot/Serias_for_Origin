def Find_Separation (ini_path):
    f=open(ini_path,'r').readlines()

    separate=0
    count=0
    for i in range(len(f)):
        f[i]=f[i].replace('-',' ')
        f[i]=f[i].replace('_',' ')
        f[i]=f[i].replace('+',' ')
        f[i]=f[i].replace('I',' ')
        f[i]=f[i].replace('?',' ')
        f[i]=f[i].replace('st',' ')
        f[i]=f[i].replace('s',' ')
        f[i]=f[i].replace('p',' ')


        if separate==0:   #if did not find minimal J for separate
            if f[i].find('Sea',0,len(f[i]))!=-1:   # if include SEARCHING

                count+=1     #counter for even or odd Searching

                str1=f[i].split()
                _,J,Ka,Kc,*_=str1
                J=int(J)
                Ka=int(Ka)
                Kc=int(Kc)
                #print (count)

                if count % 2!=0:    #if odd - first searching from couple
                    J0=J
                    Ka0=Ka
                    Kc0=Kc
                    continue
                else:                #if second from couple
                    if J==J0 and Ka==Ka0:    #if there is repeating
                        continue
                    else:    #if there is no couple - separation
                        separate=J0    # find and save J for separation
                        # print ('!', separate)
        else:
            continue
    with open(ini_path,'w') as F:
        F.writelines(f)

    F.close()

    if separate == 0 :
        separate = 1000
    return separate
