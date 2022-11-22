class Contact:
    
    def __init__ (self, name , surname,   phoneNumber = None , email = None):

        self.name = name
        self.surname = surname
        self.phoneNumber = phoneNumber
        self.email = email

    def display_contact(self):
        # Returns the contact information
        return [self.name, self.surname, self.phoneNumber, self.email]
    
        