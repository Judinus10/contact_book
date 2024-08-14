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
        if phoneNumber!=None and phoneNumber not in self.__data :
            listInfo = self.__data[phoneNumber]
            if name!=None :
                listInfo[0] = name
            if address!=None :
                listInfo[1] = address 
            if email!=None :
                listInfo[3] = email 
            self.__data[phoneNumber]=listInfo
            print("Data Updated successfully!")
        else : 
            print("Phone number Does not exits!")

    def view(self):
        pass
    def search(self,query=None,sortField=None):
        pass
    def console(self):
        pass