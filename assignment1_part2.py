
class Book:
    #only class (static) variables get defined here
    #these are shared by all instance variables
    def __init__(self, author="",title=""):
        #instance variables get defined here
        self.author = author
        self.title = title
    def display(self):
        print("'"+self.title+"' by "+self.author)

obj1 = Book("John Steinbeck","Of Mice and Men")
obj2 = Book("Harper Lee","To kill a Mockingbird")
obj1.display()
obj2.display()
