#import file

class fileopener:
    def openfile(self,filename):
        try:
            f = open(filename)
            print f
        except FineNotFoundException:
            print "Error has occured while opening file"
        
        finally:
            f.close()
            
myfileopener = fileopener()
myfileopener.openfile("text.txt")