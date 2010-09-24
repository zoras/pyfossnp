#num = input(Enter any number: )
def palindrom(word):
    rev = word[::-1]
    #result = cmp(rev,word)
    if rev == word:
        return True
    return False

string = "malayalam"
list = list(string)
print list

#rev_list = "".join(list)
#rev_list.reverse()

#en = len(list)

for st in range(0,len(list)):
    for en in range(st+2,len(list)):
        word = list[st:en]
        ans = palindrom(word)
        if(ans == 1):
            print word
            
