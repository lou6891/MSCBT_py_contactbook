
from contact import Contact
import addFunctions
import csv


class ContactBook:

    def __init__ (self):
        self.contacts = []
        self.nameCSVfile = "contactBook_backup.csv"
        self.contactField =[ "name" , "surname", "phoneNumber" , "email" ]
        pass
    
    def add_contact(self, name, surname, email=None, phoneNumber= None):
        
        # Check that name and surname are valid options
        if len(name) == 0 or len(surname) == 0 : 
            return("Name and surname must be valid")

        # Check that iether the email is valid or the phone number is valid 
        # phonenumber must be bigger than 1 since we insert a caracter
        if (len(email) == 0 and len(phoneNumber) < 2):
            return ("To be considered a contact the entry must\nhave at least 1 valid argument (either phoneNumber, email)")
        
        # CHeck that both the number and the country code are valid
        elif(len(phoneNumber) > 2):
            tester = phoneNumber.split("|")
            
            if(len(tester[0]) < 1):
                return "Please enter a valid country code"
            if (len(tester[1]) < 1):
                return "please enter a valid phone number"
        

        # Check if the contact already exsits, if it does tell the user
        isExistant = addFunctions.specificSearchProgram(name.strip().lower() + surname.strip().lower(), "name" ,self.contacts)
        # If it exists return
        if(isExistant != None): 
            return ("The contact already exists")
        
        else :
            new_contact = Contact(name = name, surname=surname, email=email if len(email) > 0 else None, phoneNumber= phoneNumber if len(phoneNumber) > 1 else None)
            self.contacts.append(new_contact)

            return "Contat added"

    def display_contactbook(self):

        returnArr = []

        if(len(self.contacts) > 0):
            for contact in self.contacts:
                returnArr.append(vars(contact))
        else:
            # IF the contactbook is empty return false
            # else return an array with all the contacts
            return False
        
        return returnArr

    def remove_contact(self, name, surname):
                        
        if len(name) == 0 or len(surname) == 0 : print("Name and surname must be valid"); return False;

        for contact in self.contacts:
            if (contact.name.lower() == name.lower() and contact.surname.lower() == surname.lower()):
                self.contacts.remove(contact)
                return "Contact Removed", contact
        else:
            return("No such contact found")

    def import_all_contacts(self):
        try:
            # Clear any existing contact
            self.contacts = []

            # Open the csv file containing the data
            with open(self.nameCSVfile, "r") as file:
                # Loop though the row to get the single contats
                for index, row in enumerate(file):

                    # Skip the first row since it's a header
                    if (index == 0):
                        continue
                    else:   
                        # Remove any \n around the row and make it into a list
                        row = row.strip().split(",")
                        # Create a new contact and add it to the contactbook
                        new_contact = Contact(name = row[0], 
                                                surname=row[1], 
                                                phoneNumber=row[2] if len(row[2]) > 0 else None,
                                                email=row[3] if len(row[3]) > 0 else None,
                                                )
                        self.contacts.append(new_contact)

            # If all went right return true
            return True

        # Else tell the GUI that something went wrong
        except Exception as error:
            print(error)
            return False
    
    def export_all_contacts(self):
        try:

            header = self.contactField
            
            with open(self.nameCSVfile, "w", newline='') as file:
                writer = csv.writer(file)

                # write the header
                writer.writerow(header)

                for contact in self.contacts:
                    writer.writerow(contact.display_contact())

            # If all went right return true
            return True

        except Exception as error:
            print(error)
            return False

    def search_contact_by_name(self, nameSearched, surnameSearched):
        
        # Data cleaning and transormation for capitl letter tht might interfer
        nameSearched = nameSearched.strip().lower()
        surnameSearched = surnameSearched.strip().lower()

        if len(nameSearched) > 0 and len(surnameSearched) > 0:
            
            isExistant = addFunctions.specificSearchProgram(nameSearched + surnameSearched, "name" ,self.contacts)
            return vars(isExistant) if isExistant != None else "No contact Found"

        elif len(nameSearched) > 0 and len(surnameSearched) == 0:
            
            isExistant = addFunctions.genericaSearchProgram(nameSearched, "name" , self.contacts)
            return isExistant if isExistant != None else "No contact Found"

        elif len(nameSearched) == 0 and len(surnameSearched) > 0:
            
            isExistant = addFunctions.genericaSearchProgram(surnameSearched, "surname" , self.contacts)
            return isExistant if isExistant != None else "No contact Found"

        else:
            return "Something went wrong!\nCheck that the entries are valid"

    def search_contact_by_phone(self, countryCode, number):
            
        # Data cleaning and transormation for capitl letter tht might interfer
        countryCode = countryCode.strip().lower()
        number = number.strip().lower()

        if len(countryCode) > 0 and len(number) > 0:
            
            isExistant = addFunctions.specificSearchProgram(countryCode + "|" + number, "phone", self.contacts)
            return vars(isExistant) if isExistant != None else "No contact Found"

        elif len(countryCode) > 0 and len(number) == 0:
            
            isExistant = addFunctions.genericaSearchProgram(countryCode, "countryCode" , self.contacts)
            return isExistant if isExistant != None else "No contact Found"

        elif len(countryCode) == 0 and len(number) > 0:
            
            isExistant = addFunctions.genericaSearchProgram(number, "number" , self.contacts)
            return isExistant if isExistant != None else "No contact Found"

        else:
            return "Something went wrong!\nCheck that the entries are valid"

         
                 
            

            

        
        




'''
    def add_contact(self):
        print("\n")
        print("Define the new contact")
        name = input("Add the name of the contact (mandatory): ")
        surname = input("Add the surname of the contact (mandatory): ")

        # check that the input exists and is valid, else end the program
        if len(name) == 0 or len(surname) == 0 : print("Name and surname must be valid"); return False;
        
        # Check if the contact already exsits
        isExistant = addFunctions.specificSearchProgram(name.strip() + surname.strip(), self.contacts)
        
        if(isExistant != None): 
            print("The contact already exists")
            print(vars(isExistant))
            
            # if it exists ask if you want to modify it
            modifyIt = input("Do you want to modify the existing contact (Yes = Yes, No = any other input): ")
            if len(modifyIt) > 0 and modifyIt[0].upper() == "Y":
                # To be finished
                pass

            return False;
            


        nickName = input("Add the nickname of the contact (to skip press enter): ")
        phoneNumber = addFunctions.AddPhoneNumber()

        email = input("Do you want to add an email address?  (to skip press enter): ")

        print("\n")

        new_contact = Contact(name, surname, nickName, phoneNumber, email)
        self.contacts.append(new_contact)
        
        print(vars(self.contacts[0]))


    def remove_contact(self):
        print("\n")
        
        warning = input("This program deletes a contact, do you want to procede? (Yes = Yes, No = any other input): ")
        
        if len(warning) > 0 and warning[0].upper() == "Y":
                
            name = input("Add the name of the contact (mandatory): ")
            surname = input("Add the surname of the contact (mandatory): ")
            if len(name) == 0 or len(surname) == 0 : print("Name and surname must be valid"); return False;

            for contact in self.contacts:
                if (contact.name.lower() == name.lower() and contact.surname.lower() == surname.lower()):
                    self.contacts.remove(contact)
                    print("contact removed: \n", vars(contact))
                    print("\n")
                    return True
            else:
                print("No such contact found")
                print("\n")
                return False
        
        else:
            return False

    
    def search_contact_by_name(self):

        while True:
            print("\n")
            searchType = input("Do whant to a generic search or specific one? \n" +
            "(G = generic, S = specific  or Q to exit): ")

            if len(searchType) > 0 :
                if( searchType[0].upper() == "Q"):
                    return False;
                elif(searchType[0].upper() == "G" ):
                    a = "l"
                    b = "name"
                    test = addFunctions.genericaSearchProgram(a, b, self.contacts)
                    test2 = list(vars(i) for i in test)
                    print(test2)
                    return
                elif(searchType[0].upper() == "S" ):
                    # specific search
                    pass
                else:
                    print("Something went wrong, let's retry")
            
        pass

    def search_contact_by_phone_number(self, phone_number):
        pass


    def display_contactbook(self):
        print("\n")
        print("Printing all contacts in the contact book: ")

        if(len(self.contacts) > 0):
            for contact in self.contacts:
                print(vars(contact))
        else:
            print("The contact book is empty")
        print("\n")
        '''