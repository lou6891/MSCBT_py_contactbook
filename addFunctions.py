

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

def specificSearchProgram(target,searchType,contactsLsit):
    tester = None

    if(len(contactsLsit) > 0):
        for contact in contactsLsit:
            if searchType == "name":
                tester = contact.name.strip() + contact.surname.strip()
            elif searchType == "phone":
                tester = contact.phoneNumber.strip()

            if(target == tester.lower()):
                return contact

    else:
        return None

def genericaSearchProgram(target, searchType,contactsLsit):

    returnArr = []
    tester = None

    if(len(contactsLsit) > 0):
        for contact in contactsLsit:
            if searchType == "name":
                tester = contact.name.strip()
            elif searchType == "surname":
                tester = contact.surname.strip()
            elif searchType == "countryCode":
                ind = contact.phoneNumber.strip().find("|")
                tester = contact.phoneNumber.strip()[0:ind]
            elif searchType == "number":
                ind = contact.phoneNumber.strip().find("|") +1
                tester = contact.phoneNumber.strip()[ind :]
            
            print(tester)
            if(target == tester.lower()):
                returnArr.append(contact) 
        
        return returnArr if len(returnArr) > 0 else None

    else:
        return None

            






    