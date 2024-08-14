from beautifultable import BeautifulTable


class conductBook :
    def __init__(self):
        self.__data={} #declare data as private variable

    def add(self,name=None,address=None,phoneNumber=None,email=None):
        if name!=None and address!=None and phoneNumber!=None and email!=None :
            if phoneNumber not in self.__data :
                self.__data[phoneNumber]={name,address,phoneNumber,email}
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
                del self.__data[phoneNumber]
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
        table = BeautifulTable()
        for child_data in data:
            table.rows.append(child_data)

        table.rows.header = [str(i) for i in range(1, len(data) + 1)]
        table.columns.header = ["name", "address", "phone_number", "email"]
        print(table)

    def search(self,query=None,sortField=None):
        if query != None:
            search_arr = []
            for key, val in self.__data.items():
                search_arr.append(val + [" ".join(val)])
                        
            result = set()
            for word in query.lower().split():
                for i in range(len(search_arr)):
                    if word in search_arr[i][-1].lower():
                        result.add(i)
            
            ans = []
            for i in result:
                ans.append(search_arr[i][:-1])
            
            indx = 0
            if sort_field == "name":
                indx = 0
            if sort_field == "address":
                indx = 1
            if sort_field == "phone_number":
                indx = 2
            if sort_field == "email":
                indx = 3
            ans.sort(key= lambda x : x[indx])

            self.viewContact(ans)
        else:
            return []

    def console(self):
        while True:
            try:
                print("\n1. Add Contact\n2. Delete Contact\n3. Edit Contact\n4. Search Contact\n5. View Contacts\n6. Stop")
                n = int(input("Enter your options: "))
            
                if n == 1:
                    name = input("Name: ")
                    address = input("Address: ")
                    phone_number = input("Phone Number: ")
                    email = input("Email: ")
                    if len(name) == 0:
                        name = None
                    if len(address) == 0:
                        address = None
                    if len(phone_number) == 0:
                        phone_number = None
                    if len(email) == 0:
                        email = None
                    self.addContact(name, address, phone_number, email)

                

            except Exception as e:
                pass

# conductBook = conductBook()
# conductBook.add("Rahul", "colombo", "0775648753", "jj@gmail.com")