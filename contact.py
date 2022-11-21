class Contact:
    
    def __init__ (self, name , surname,   phoneNumber = None , email = None):
        
        #if (phoneNumber == None and email == None and address == None):
        #    return Exception ("To be considered a contact  the entry must have at least 1 valid argument (either hone, email, address)")

        self.name = name
        self.surname = surname
        self.phoneNumber = phoneNumber
        self.email = email

    def display_contact(self):
        return [self.name, self.surname, self.phoneNumber, self.email]
    
        