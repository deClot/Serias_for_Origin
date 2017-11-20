def comments_separation_index (element):
    for i in range(len(element)):
        if element[i].isdigit() == False:
            if i == len(element)-1:
                return 'none'
            else:
                continue
        else:
            return i

def comments_separation (element, i):
    return element[i:len(element)]
    #return [element[0:i],element[i:len(element)]]
