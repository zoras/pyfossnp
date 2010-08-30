def info ():
    ''' This is the function to get information '''
    value = [name, address, city]
    return value
    
global name
global address
global city

name = raw_input ("Enter name : ")
address = raw_input ("Enter address : ")
city = raw_input ("Enter city : ")

print info()

help(info)