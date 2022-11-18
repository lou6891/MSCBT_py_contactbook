class Contact:
    
    def __init__ (self, name , surname, nickname = None , phoneNumber = None , email = None):
        
        #if (phoneNumber == None and email == None and address == None):
        #    return Exception ("To be considered a contact  the entry must have at least 1 valid argument (either hone, email, address)")

        self.name = name
        self.surname = surname
        self.nickname = nickname
        self.phoneNumber = phoneNumber
        self.email = email

    def display_contact(self):
        return [self.name, self.surname, self.nickname, self.phoneNumber, self.email]
    
        