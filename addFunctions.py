
def specificSearchProgram(target,searchType,contactsLsit):
    '''
    Given a target (name-surname or countrycode-number)
    and a type of search + the contacts in the contact book
    
    Output
    -> return the target contact
    - > None in case of error

    '''
    tester = None
    if(len(contactsLsit) > 0):
        for contact in contactsLsit:
            if searchType == "name":
                # Strip anything to avoid having anything other than the input characters 
                tester = contact.name.strip() + contact.surname.strip()
            elif searchType == "phone":
                # Test if the contact actually has a phone number
                if contact.phoneNumber != None:
                    tester = contact.phoneNumber.strip()
                else:
                    continue

            # Check with lower case letter, to have a precsesearch, no mausc weird stuff
            if(target == tester.lower()):
                return contact

    else:
        return None

def genericaSearchProgram(target, searchType,contactsLsit):
    '''
    Given a target (name-surname or countrycode-number)
    and a type of search + the contacts in the contact book

    The different if are to search only a specific elements, 
    that's why this may return multiple contacts
    
    Output
    -> return the array with the contacts
    - > None in case of error
    '''
    returnArr = []
    tester = None

    if(len(contactsLsit) > 0):
        for contact in contactsLsit:
            if searchType == "name":
                tester = contact.name
            elif searchType == "surname":
                tester = contact.surname
            elif searchType == "countryCode":
                # Test if the contact actually has a phone number
                if contact.phoneNumber != None:
                    # This part is just because the country code and the phone number are divided by |
                    ind = contact.phoneNumber.strip().find("|")
                    tester = contact.phoneNumber.strip()[0:ind]
                else:
                    continue
            elif searchType == "number":
                # Test if the contact actually has a phone number
                if contact.phoneNumber != None:
                    ind = contact.phoneNumber.strip().find("|") +1
                    tester = contact.phoneNumber.strip()[ind :]
                else:
                    continue
            
            if(target == tester.lower()):
                returnArr.append(contact)
        
        return returnArr if len(returnArr) > 0 else None

    else:
        return None
