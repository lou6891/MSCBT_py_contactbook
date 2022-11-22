
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
        '''
        Method that add a contact, 
        
        Output:
        -> String of text to be displayed
        '''
        
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
            # If everything is good add create a contact and add it to the book
            new_contact = Contact(name = name, surname=surname, email=email if len(email) > 0 else None, phoneNumber= phoneNumber if len(phoneNumber) > 1 else None)
            self.contacts.append(new_contact)

            return "Contat added"

    def display_contactbook(self):
        '''
        Method that returns all the contacts in the book, 
        
        Output:
        -> The array with the contact
        -> False
        '''
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
        '''
        Method that removes a contact from the book book, 
        
        Output:
        -> String of text to be displayed
        -> String of text to be displayed and the contact
        -> False
        '''
                        
        if len(name) == 0 or len(surname) == 0 : print("Name and surname must be valid"); return False;

        for contact in self.contacts:
            if (contact.name.lower() == name.lower() and contact.surname.lower() == surname.lower()):
                self.contacts.remove(contact)
                return "Contact Removed", vars(contact)
        else:
            return("No such contact found")

    def import_all_contacts(self):
        '''
        Method that imports the contacts to csv
        Possible imporvement chose if to add the contacts to the book 
        or delete what is present (current version)
        
        Output:
        -> True
        -> False
        '''

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
        '''
        Method that exports the contacts to csv
        Possible imporvement chose if to add the contacts to the cvs 
        or delete what is present (current version)
        
        Output:
        -> True
        -> False
        '''

        try:
            # Create an header with the fiels of the contact class 
            # (for easy of coding I just wrote them)
            header = self.contactField
            
            with open(self.nameCSVfile, "w", newline='') as file:
                writer = csv.writer(file)

                # write the header
                writer.writerow(header)
                # For each contact in the book write a row
                for contact in self.contacts:
                    writer.writerow(contact.display_contact())

            # If all went right return true
            return True

        except Exception as error:
            print(error)
            return False

    def search_contact_by_name(self, nameSearched, surnameSearched):
        '''
        Works the same as search by phone
        This method takes 2 inputs.
        Depending on the inputs it will filter and call the relative fucntion with the right parameters
        this will retrieve the contact/s
        
        Output:
        -> Either 1 specific contact
        - > Multiple contacts
        '''
        
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
        '''
        Works the same as search by name

        This method takes 2 inputs.
        Depending on the inputs it will filter and call the relative fucntion with the right parameters
        this will retrieve the contact/s

        Output:
        -> Either 1 specific contact
        - > Multiple contacts
        '''
            
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
