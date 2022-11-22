import tkinter as tk

#  ADD CONTACT PAGE ----------------------------------------------------------------------------------------------------------------------

def setPhoneField (value,phoneNumberCountryCodeEntry , phoneCountryCondeLabel, phoneNumberEntry, phoneNumberLabel): 
    '''
    Function that maneges the hone field in add a contact page
    '''
    #Function that based on the selection in the circle selector 
    # (yes/no) shows or hides the phone entry fields
    if value:
        phoneNumberCountryCodeEntry.place(relx=0.3,rely=0.65)
        phoneCountryCondeLabel.place(relx=0.05,rely=0.65)

        phoneNumberEntry.place(relx=0.3,rely=0.75)
        phoneNumberLabel.place(relx=0.05,rely=0.75)

    else:
        # Remove the fields if the user selects 
        # that doesn't want to add a phone number
        phoneNumberCountryCodeEntry.place_forget()
        phoneCountryCondeLabel.place_forget()
        phoneNumberEntry.place_forget()
        phoneNumberLabel.place_forget()


def add_contact_in_book(nameEntry, surnameEntry, emailEntry,phoneNumberCountryCodeEntry,  phoneNumberEntry, contactBook, root, radioSelectorValue):  
    '''
    This function is the one that collects the data from the different entries
    and then calls the method in the contactbook to actually add the contact
    '''
    # Get the different data
    radioSelectorGet = radioSelectorValue.get()
    nameGet = nameEntry.get()
    surnameGet = surnameEntry.get()
    emailGet = emailEntry.get()
    phoneNumberGet = phoneNumberCountryCodeEntry.get() + "|" + phoneNumberEntry.get()

    # Check that the phone number is acutally a number
    addContactResult = None
    # First check that the user whants to add a number
    if radioSelectorGet == 1:
        # If yes check that is made by number only, if yes create the contact
        if (phoneNumberCountryCodeEntry.get().isnumeric() and phoneNumberEntry.get().isnumeric()):
            addContactResult = contactBook.add_contact(nameGet, surnameGet, emailGet, phoneNumberGet)
        else : 
            addContactResult = "Both the country code and the phone number\nmust be only numbers"
    elif radioSelectorGet == 0:
        addContactResult = contactBook.add_contact(nameGet, surnameGet, emailGet, phoneNumberGet)


    # Label that 
    label1 = tk.Label(root, text=addContactResult)
    label1.place(relx=0.3,rely=0.3)

    label1.after(2000, label1.destroy)

#  SEARCH CONTACT PAGE ----------------------------------------------------------------------------------------------------------------------

def search_name_function(nameEntry, surnameEntry, contactBook, frame, t):
    '''
    Function that actually search the contact in the book when called
    '''

    # Get the values
    nameGet = nameEntry.get()
    surnameGet = surnameEntry.get()

    # Call the method that does the search
    FoundContacts = contactBook.search_contact_by_name(nameGet, surnameGet)

    # Hide the search elements
    for widget in frame.winfo_children():
        if(str(widget)[0 : 23] == ".!frame.toBeAnnihilated"):
            widget.destroy()
    
    # Show the result fromt he search, if we have a iterate through it, else  show the string
    if type (FoundContacts) == list:
        for c in FoundContacts:
            c = vars(c)
            t.insert(tk.END,"Name: " + str(c["name"]) + '\n' +
                                    "Surname: " + str(c["surname"]) + '\n' +
                                    "Phone Number: " + str(c["phoneNumber"]) + '\n' +
                                    "Email: " + str(c["email"]) + '\n' +
                                    "-------------------------------------"
                                    )
    else : 
        t.insert(tk.END, str(FoundContacts) + "\n\n")
    
    # Show the result
    t.pack()

def search_phone_function(phoneNumberCountryCodeEntry, phoneNumberEntry, contactBook, frame, t):

    '''
    This function calls the search phone method of the contactbook 
    class and gets the resulting value then displays a text box with the information
    '''

    # Get the values
    phoneNumberCountryCodeGet = phoneNumberCountryCodeEntry.get()
    phoneNumberGet = phoneNumberEntry.get()

    # Call the method that does the search
    FoundContacts = contactBook.search_contact_by_phone(countryCode = phoneNumberCountryCodeGet, number= phoneNumberGet)

    # Hide the search elements
    for widget in frame.winfo_children():
        if(str(widget)[0 : 23] == ".!frame.toBeAnnihilated"):
            widget.destroy()
    
    # Show the result fromt he search, if we have a iterate through it, else  show the string
    if type (FoundContacts) == list:
        for c in FoundContacts:
            c = vars(c)
            t.insert(tk.END,"Name: " + str(c["name"]) + '\n' +
                                    "Surname: " + str(c["surname"]) + '\n' +
                                    "Phone Number: " + str(c["phoneNumber"]) + '\n' +
                                    "Email: " + str(c["email"]) + '\n' +
                                    "-------------------------------------"
                                    )
    else : 
        t.insert(tk.END, str(FoundContacts) + "\n\n")
    
    # Show the result
    t.pack()

#  IMPORT/EXPORT CONTACT PAGE ----------------------------------------------------------------------------------------------------------------------

def detroy_widgets_and_call_to_action(function, text, label1, confirmButton):
    '''
    This funtion handles import and exports, 
    It calls the passed as function variable
    If the return is not False then it will show the text variable added when calling it
    else it will display that something went wrong

    '''
    resultImportExport = function()
    if not resultImportExport: 
        text = "Something went wrong\nCheck that the working directory is right\nOr that the file to read from exists"
    label1.config(text=text)
    confirmButton.destroy()
    label1.after(2000, label1.destroy)