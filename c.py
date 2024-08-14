class conductBook :
    def __init__(self):
        self.__data={} #declare data as private variable

    def add(self,name=None,address=None,phoneNumber=None,email=None):
        if name!=None and address!=None and phoneNumber!=None and email!=None :
            if phoneNumber not in self.__data :
                self.__data(phoneNumber)={name,address,phoneNumber,email}
                print("Contact added Successfully!")
            else :
                print("Number already exists!")
        else :
            print ("Please enter all the values!")

    def delete(self,phoneNumber=None):
        if phoneNumber!=None :
            if phoneNumber not in self.__data :
                print("No matches found")
            else :
                del self.__data(phoneNumber)
                print("Contact deleted Successfully!")
        else :
            print("Please enter Phone number!")

    def edit(self,name=None,address=None,phoneNumber=None,email=None):
        pass
    def view(self):
        pass
    def search(self,query=None,sortField=None):
        pass
    def console(self):
        pass