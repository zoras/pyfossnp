#=== On read mode ========
file= open("urls.txt", 'r')

#=== On append mode ========
#file= open("test", 'a')

#==========For read entire file=======
#print file.read()

#========For reading single line=======
print file.readline()

for line in file:
        print line,


file.close()