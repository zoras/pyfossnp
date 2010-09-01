#

def find_magic_number(num):
    list_num = list(str(num))
    #print list_num
    list_num.sort()
    acc = "".join(list_num)
    list_num.reverse()
    dec = "".join(list_num)
    
    result= int(dec)-int(acc)
    print dec , "-" , acc , "=" ,result
    
    if result == 6174:
        return
        
    #if count == 2:
        #return result
    
    find_magic_number(result)
    #while (result!=6174):
        

num = raw_input("Enter any 4 digit number:")

find_magic_number(num)