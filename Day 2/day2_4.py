#=== On read mode ========
#file= open("test", 'r')

#=== On append mode ========
file= open("test", 'a')

#==========For read entire file=======
#print file.read()

#========For reading single line=======
#print file.readline()


#========For writing on file ========
file.write("\nanother line")

print file.read()

file.close()