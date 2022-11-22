import tkinter as tk
from pagesFunctions import *
from contactbook import ContactBook


def main():
    try:
        # Create the contactBook
        contactBook = ContactBook()
        
        # Create the frame where visual elements are created and positioned
        root=tk.Tk()
        # Set the size of the window
        root.geometry("500x600")

        # Create a second frame that will hold different graphical elements
        frame=tk.Frame(root)
        #Psoition of the second frame
        frame.place(relx=0.2,rely=0.3,relheight=0.6,relwidth=0.6)


        def Add_Contact_page():
            '''
            This function and all the nested functions manage 
            the page that enable the user to ad contacts to the book
            '''
            
            # Clear the frame from any widgets
            for widget in frame.winfo_children():
                widget.destroy()
            
            # Entry and label for name
            nameEntry = tk.Entry(frame)
            nameEntry.place(relx=0.3,rely=0.15)
            nameLabel=tk.Label(frame,text='Name')
            nameLabel.place(relx=0.1,rely=0.15)

            # Entry and label for surname   
            surnameEntry = tk.Entry(frame)
            surnameEntry.place(relx=0.3,rely=0.25)
            surnameLabel=tk.Label(frame,text='Surname')
            surnameLabel.place(relx=0.008,rely=0.25)

            # Entry and label for email
            emailEntry = tk.Entry(frame)
            emailEntry.place(relx=0.3,rely=0.35)
            emailLabel=tk.Label(frame,text='Email')
            emailLabel.place(relx=0.1,rely=0.35)

            # This part is the one that hides or shows the phonefields, 
            # We call it in phoneNumberYes, if we want to show the components
            # Else in phoneNumberNo we hide it
            phoneNumberCountryCodeEntry = tk.Entry(frame)
            phoneNumberEntry = tk.Entry(frame)
            phoneNumberLabel=tk.Label(frame,text='Phone\nNumber')
            phoneCountryCondeLabel=tk.Label(frame,text='Country\nCode')

                
            # The two circle buttons that manage the phone entry
            radioSelectorValue = tk.IntVar()
            phoneNumberYes = tk.Radiobutton(frame, text='Yes', value = 1 ,variable=radioSelectorValue, command = lambda : setPhoneField(True ,phoneNumberCountryCodeEntry , phoneCountryCondeLabel, phoneNumberEntry, phoneNumberLabel))
            phoneNumberNo = tk.Radiobutton(frame, text='No',value = 0, variable=radioSelectorValue, command = lambda : setPhoneField(False, phoneNumberCountryCodeEntry , phoneCountryCondeLabel, phoneNumberEntry, phoneNumberLabel) )
            phoneNumberYes.place(relx=0.3,rely=0.45)
            phoneNumberNo.place(relx=0.5,rely=0.45)
            
            #Phone entry label
            phoneLabel=tk.Label(frame,text='Phone\nNumber')
            phoneLabel.place(relx=0.05,rely=0.45)
            
            # Button to add the contact
            confirmButton = tk.Button(frame, text='Add Contact!', width=25, command= lambda:  add_contact_in_book(nameEntry, surnameEntry, emailEntry, phoneNumberCountryCodeEntry, phoneNumberEntry, contactBook, root, radioSelectorValue))
            confirmButton.place(relx=0.2,rely=0.9)

                

        def Remove_Contact_Page():
            '''
            Function that manages the deletion oage of ta contact
            '''

            # Clear the frame from any widgets
            for widget in frame.winfo_children():
                widget.destroy()

            # Warning to avoid accidental deletions
            confirmButtonWarning = False

            nameEntry = tk.Entry(frame)
            nameEntry.place(relx=0.3,rely=0.15)
            nameLabel=tk.Label(frame,text='Name')
            nameLabel.place(relx=0.1,rely=0.15)

            surnameEntry = tk.Entry(frame)
            surnameEntry.place(relx=0.3,rely=0.25)
            surnameLabel=tk.Label(frame,text='Surname')
            surnameLabel.place(relx=0.008,rely=0.25)

            confirmButton = tk.Button(frame, text= "Delete Contact", width=25, command= lambda:  remove_contact_from_book(nameEntry, surnameEntry ))
            confirmButton.place(relx=0.15, rely=0.45)

            
            def remove_contact_from_book(nameEntry, surnameEntry):
                '''
                THis function manages the deletion of the contact, the reason why it's not in the othe file pagesFunction 
                is for the management of the confirmbuttonWarning
                '''
                # THis enables us to use the confirmButton variable
                nonlocal confirmButtonWarning

                # GEt the values from the tries
                nameGet = nameEntry.get()
                surnameGet = surnameEntry.get()

                if (nameGet and surnameGet):

                    # If the entries are valid and the confirmWarning is not confirmed 
                    # and the user to confirm it
                    if not confirmButtonWarning:
                        confirmButtonWarning = True
                        confirmButton.config(text="I want to delete it!")
                    
                    else:
                        remConRes = contactBook.remove_contact(nameGet,surnameGet)
                        # Display the contact removed
                        t = tk.Text(frame, wrap='word')
                        t.insert(tk.END,"Name: " + str(remConRes[1]["name"]) + '\n' +
                                    "Surname: " + str(remConRes[1]["surname"]) + '\n' +
                                    "Phone Number: " + str(remConRes[1]["phoneNumber"]) + '\n' +
                                    "Email: " + str(remConRes[1]["email"]) + '\n'
                                    )
                        t.place(relx=0.01, rely=0.1)
                        t.after(2000, t.destroy)


                        # Reset the delete functionality
                        confirmButton.config(text="Delete Contact")
                        confirmButtonWarning = False   

                else :
                    # if the entries anre not valied tell the user
                    label1 = tk.Label(root, text="Please enter name and surname")
                    label1.place(relx=0.3,rely=0.3)
                    label1.after(2000, label1.destroy)   

        def search_contact_page():
            '''
            Page that manages the search of a contact
            '''

            # Clear the frame from any widgets
            for widget in frame.winfo_children():
                widget.destroy()

            # Text that pops up at the end, declared here cause it's used multiple tiems
            t = tk.Text(frame, wrap='word')

            def search_name_page():
                '''
                Function that manages the search of a contact by anme 
                '''

                # Text box that will display the output of the search
                t = tk.Text(frame, wrap='word')

                # Here add name and surname input field, do the search foe the one he looks for
                # avoid putting genereric and speficic search
                genericLabel=tk.Label(frame,text='You can search by name, surname,\nor both to be more precise ', name='toBeAnnihilated1')
                genericLabel.place(relx=0.1, rely=0.2)

                # Name , surname and search button entries, and labels
                nameEntry = tk.Entry(frame, name='toBeAnnihilated2')
                nameEntry.place(relx=0.3,rely=0.3)
                nameLabel=tk.Label(frame,text='Name', name='toBeAnnihilated3')
                nameLabel.place(relx=0.1,rely=0.3)

                surnameEntry = tk.Entry(frame, name='toBeAnnihilated4')
                surnameEntry.place(relx=0.3,rely=0.4)
                surnameLabel=tk.Label(frame,text='Surname', name='toBeAnnihilated5')
                surnameLabel.place(relx=0.008,rely=0.4)


                SearchButton = tk.Button(frame, text= "Search!", name='toBeAnnihilated6', width=15, command= lambda: search_name_function(nameEntry, surnameEntry,  contactBook, frame, t))
                SearchButton.place(relx=0.3, rely=0.6)    

            def search_phone_page():
                '''
                Function that enables the search contact by phone number
                '''
                
                t = tk.Text(frame, wrap='word')
                # Here add name and surname input field, do the search foe the one he looks for
                # avoid putting genereric and speficic search
                genericLabel=tk.Label(frame,text='You can search by country code, number,\nor both to be more precise ', name='toBeAnnihilated1')
                genericLabel.place(relx=0.1, rely=0.2)
            
                # Below all the entries and labes to get the phone number and country code
                phoneNumberCountryCodeEntry = tk.Entry(frame, name='toBeAnnihilated2')
                phoneNumberCountryCodeEntry.place(relx=0.3,rely=0.3)

                phoneCountryCondeLabel=tk.Label(frame,text='Country\nCode', name='toBeAnnihilated3')
                phoneCountryCondeLabel.place(relx=0.05,rely=0.3)

                phoneNumberEntry = tk.Entry(frame, name='toBeAnnihilated4')
                phoneNumberEntry.place(relx=0.3,rely=0.4)

                phoneNumberLabel=tk.Label(frame,text='Phone\nNumber', name='toBeAnnihilated5')
                phoneNumberLabel.place(relx=0.05,rely=0.4)

                SearchButton = tk.Button(frame, text= "Search!", name='toBeAnnihilated6', width=15, command= lambda: search_phone_function(phoneNumberCountryCodeEntry , phoneNumberEntry , contactBook, frame, t))
                SearchButton.place(relx=0.3, rely=0.6)    


            # Buttons that let you decide what type of search to do either by phone or name
            phoneSearchButton = tk.Button(frame, text= "Search by phone", width=15, command=search_phone_page )
            phoneSearchButton.place(relx=0.01, rely=0.05)

            nameSearchButton = tk.Button(frame, text= "Search by Name", width=15, command=search_name_page)
            nameSearchButton.place(relx=0.55, rely=0.05)     
    


        def See_all_Contats_Page():
            '''
            Function hat will return all the contacts in the book
            '''
            # Clear the frame from any widgets
            for widget in frame.winfo_children():
                widget.destroy()
            
            # Call the book method that returns an array of contacts
            contacts = contactBook.display_contactbook()

            # Text that displays the contacts
            t = tk.Text(frame,  wrap='word')
            t.place(relx=0.35)
            
            if contacts:
                # If there are contacts in the book loop though them to display them
                for c in contacts:
                    # All the extra code is making the display fancy
                    t.insert(tk.END,"Name: " + str(c["name"]) + '\n' +
                                    "Surname: " + str(c["surname"]) + '\n' +
                                    "Phone Number: " + str(c["phoneNumber"]) + '\n' +
                                    "Email: " + str(c["email"]) + '\n' +
                                    "-------------------------------------"
                                    )
                # SHow the text box
                t.pack()

            else:
                t.insert(tk.END, "The contact book is empty" + '\n\n')            
                t.pack()
                

        def import_export_contact_page():
            '''
            Page for importing and exporting the contacts to cvs
            Not required by helpfull for debuggin and testing
            '''    

            # Clear the frame from any widgets
            for widget in frame.winfo_children():
                widget.destroy()        
            
            # Buttons that enables the user to decide what to do
            exportContactsButton = tk.Button(frame, text='Export Contacts to cvs', width=25, command= lambda:  message("export"))
            importContatcsButton = tk.Button(frame, text='Import Contacts from cvs', width=25, command= lambda:  message("import"))

            importContatcsButton.place(relx=0.2,rely=0.1)
            exportContactsButton.place(relx=0.2,rely=0.2)

            def message(type):
                
                if type == "import":
                    label1 = tk.Label(frame, text="Are you sure?\nthis will revrite all current contats")
                    label1.place(relx=0.2,rely=0.4)
                    
                    confirmButton = tk.Button(frame, text='Confirm', width=25, command= lambda:  detroy_widgets_and_call_to_action(contactBook.import_all_contacts, "Contacts Imported!", label1, confirmButton)) 
                    confirmButton.place(relx=0.2,rely=0.55)
                    

                if type == "export":
                    label1 = tk.Label(frame, text="Are you sure?\nthis will revrite all previusly saved contats")
                    label1.place(relx=0.2,rely=0.4)

                    confirmButton = tk.Button(frame, text='Confirm', width=25, command= lambda:  detroy_widgets_and_call_to_action(contactBook.export_all_contacts, "Contacts Exported!", label1, confirmButton))
                    confirmButton.place(relx=0.2,rely=0.55) 

                    

        # Main page buttons (position on the root frame)
        AddContactButton = tk.Button(root, text='Add Contact', width=25, command=Add_Contact_page)
        RemoveContactButton = tk.Button(root, text='Remove Contact', width=25,command=Remove_Contact_Page)
        SearchContactButton = tk.Button(root, text='Search Contact', width=25,command=search_contact_page)

        SeeAllContactButton = tk.Button(root, text='See all Contacts', width=25,command=See_all_Contats_Page)
        importExportContctsButton = tk.Button(root, text='Import / Export Contacts', width=25,command=import_export_contact_page)
        StopButton = tk.Button(root, text='Stop', width=25, command=root.destroy)
        
        AddContactButton.pack()
        RemoveContactButton.pack()
        SearchContactButton.pack()
        SeeAllContactButton.pack()
        importExportContctsButton.pack()
        StopButton.pack()

        # call the root to actually display and make the graphics work
        root.mainloop()
    
    except Exception as error:
        print("Something went wrong!")
        print(error)


# Small function that enables the user to become invincible for 5 minutes
# Nintendo stole the idea when making the star in super mario
# If you read all the comments up to here, hope the last one made you jiggle
if __name__ == "__main__":
    main()

