

def AddPhoneNumber():
    '''
    This program is the one that takes care of the imput of the phone number

    Output
    '''

    pn = (input("Do you want to add a phone number?  (yes / y / to skip press enter): "))
        
    if ( len(pn) and pn[0].lower() == "y"):
        countryCode = input("Enter the country code of the phone number: ")
        if len(countryCode) < 1 : print("You must enter a valid country code"); return None;
        
        number = input("Enter the actual phone number: ")
        if len(countryCode) < 1 : print("You must enter a valid country code"); return None;
        
        return "+" + countryCode + number
    
    else:
        return None

def AddEmail():
    '''
    This program is the one that takes care of the imput of the phone number

    Output
    '''

    em = (input("Do you want to add a phone number?  (yes / y / to skip press enter): "))
        
    if ( len(em) and em[0].lower() == "y"):
        countryCode = input("Enter the country code of the phone number: ")
        if len(countryCode) < 1 : print("You must enter a valid country code"); return False;
        
        number = input("Enter the actual phone number: ")
        if len(countryCode) < 1 : print("You must enter a valid country code"); return False;
        
        return "+" + countryCode + number
    
    else:
        return None

def specificSearchProgram(target, contactsLsit):

    if(len(contactsLsit) > 0):
        for contact in contactsLsit:
            tester = contact.name.strip() + contact.surname.strip()
            if(target == tester):
                return contact

    else:
        return None

def genericaSearchProgram(target, searchType,contactsLsit):

    returnArr = []

    if(len(contactsLsit) > 0):
        for contact in contactsLsit:
            tester = contact.name.strip() if searchType == "name" else contact.surname.strip()
            
            if(target == tester):
                returnArr.append(contact) 
        
        return returnArr

    else:
        return None

            






    