import comments_clear

def isint(s):    #check int number or not
    try:
        int(s)
        return True
    except ValueError:
        return False

def make (ini_path):
    f=open(ini_path,'r').readlines()

    for i in range(len(f)):
        if f[i].find('Sea',0,len(f[i]))!=-1:   # skip all searching line
            continue

        str1=f[i].split()
        if len(str1)==0:   # if line is empty - skip
            continue

        if len(str1)==12 or len(str1)==6:
            # make clear comment for 1st element
            # return index position for J number or 'none' 
            index = comments_clear.comments_separation_index(str1[0])

            # return part of string from index to end
            add = comments_clear.comments_separation(str1[0],index)
            _=str1.pop(0)
            str1.insert (0,add)
            f[i]=str1
#            print (str1)
            continue

        else:    # if len of line not standart

            # make clear comment for 1st element
            # return index position for J number or 'none' 
            index = comments_clear.comments_separation_index(str1[0])
            if isinstance(index, str) ==True:    # if index is string
                 _=str1.pop(0)
                 f[i]=str1
#                 print (str1)
                 continue
            else:
                # return part of string from index to end
                add = comments_clear.comments_separation(str1[0],index)
                if isint(add) == True:
                    _=str1.pop(0)
                    str1.insert (0,add)
                    f[i]=str1
                else:
                    _=str1.pop(0)
                    f[i]=str1
            print (f[i])
    return f


#ini_path = 'Serias_for_Origin/ini'
#make(ini_path)

