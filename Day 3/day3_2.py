def find_encoded(word):
        listing= list(str(word))
        a=len(word)
        for i in range(0,a):
                if listing[i]>='a'and listing[i]<='m':
                        t=ord(listing[i])+13
                        listing[i]=chr(t)
                elif listing[i]>='n'and listing[i]<='z':
                        t=ord(listing[i])-13
                        listing[i]=chr(t)		
        cword="".join(listing)
        print "the word before change  "+word
        print "The word after change  "+cword 
                


word = raw_input("Enter any word:")

find_encoded(word)
