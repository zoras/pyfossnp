def comp(x,y):
    return len(x)-len(y)

sentance = raw_input("Enter a sentance:")

words = sentance.split(" ")
words.sort(comp)

#print words
print " ".join(words)




