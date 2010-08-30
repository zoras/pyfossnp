def setinfo ():
    ''' This is the function to set information '''
    file = open("info.txt",'a')
    info = name +","+ address +","+ city
    file.write(info)
    #value = [name, address, city]
    #return value
    file.close()

def getinfo ():
    '''This is the function to get information '''
    file = open("info.txt",'r')
    for line in file
    print line
    
    file.close()

global name
global address
global city

name = raw_input ("Enter name : ")
address = raw_input ("Enter address : ")
city = raw_input ("Enter city : ")

#print info()