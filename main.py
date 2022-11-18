from contactbook import ContactBook
import tkinter as tk


def main():
    contactBook = ContactBook()

    #tkinterPages.startPage()
    
    '''
    root = tk.Tk()
    main = MainView(root, contactBook)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()
    '''

    root=tk.Tk()
    root.geometry("500x500")

    frame=tk.Frame(root)
    frame.place(relx=0.2,rely=0.3,relheight=0.6,relwidth=0.6)



    def Add_Collection_page():
        # Clear the frame from any widgets
        for widget in frame.winfo_children():
            widget.destroy()
        
        
        nameEntry = tk.Entry(frame)
        nameEntry.place(relx=0.3,rely=0.15)
        nameLabel=tk.Label(frame,text='Name')
        nameLabel.place(relx=0.1,rely=0.15)

        surnameEntry = tk.Entry(frame)
        surnameEntry.place(relx=0.3,rely=0.25)
        surnameLabel=tk.Label(frame,text='Surname')
        surnameLabel.place(relx=0.008,rely=0.25)

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

        def setPhoneField (value): 
            if value:
                phoneNumberCountryCodeEntry.place(relx=0.3,rely=0.65)
                phoneCountryCondeLabel.place(relx=0.05,rely=0.65)

                phoneNumberEntry.place(relx=0.3,rely=0.75)
                phoneNumberLabel.place(relx=0.05,rely=0.75)

            else:
                phoneNumberCountryCodeEntry.place_forget()
                phoneCountryCondeLabel.place_forget()
                phoneNumberEntry.place_forget()
                phoneNumberLabel.place_forget()
            

        phoneNumberYes = tk.Radiobutton(frame, text='Yes', value=0, command = lambda : setPhoneField(True))
        phoneNumberNo = tk.Radiobutton(frame, text='No',value=1, command = lambda : setPhoneField(False) )
        phoneNumberYes.place(relx=0.3,rely=0.45)
        phoneNumberNo.place(relx=0.5,rely=0.45)
        

        phoneLabel=tk.Label(frame,text='Phone\nNumber')
        phoneLabel.place(relx=0.05,rely=0.45)
        
        confirmButton = tk.Button(frame, text='Add Contact!', width=25, command= lambda:  add_contact_in_book(nameEntry, surnameEntry, emailEntry, phoneNumberCountryCodeEntry, phoneNumberEntry))
        confirmButton.place(relx=0.2,rely=0.9)

        def add_contact_in_book(nameEntry, surnameEntry, emailEntry,phoneNumberCountryCodeEntry,  phoneNumberEntry):  
            nameGet = nameEntry.get()
            surnameGet = surnameEntry.get()
            emailGet = emailEntry.get()
            phoneNumberGet = phoneNumberCountryCodeEntry.get() + "|" + phoneNumberEntry.get()

            addContactResult = contactBook.add_contact(nameGet, surnameGet, emailGet, phoneNumberGet)
            
            label1 = tk.Label(root, text=addContactResult)
            label1.place(relx=0.3,rely=0.3)

            label1.after(2000, label1.destroy)


    def Remove_Contact_Page():
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

        confirmButton = tk.Button(frame, text= "Delete Contact", width=25, command= lambda:  remove_contact_from_book(nameEntry, surnameEntry))
        confirmButton.place(relx=0.15, rely=0.45)

        def remove_contact_from_book(nameEntry, surnameEntry):
            # THis enables us to use the confirmButton variable
            nonlocal confirmButtonWarning

            nameGet = nameEntry.get()
            surnameGet = surnameEntry.get()

            if (nameGet and surnameGet):

                if not confirmButtonWarning:
                    confirmButtonWarning = True
                    confirmButton.config(text="I want to delete it!")
                
                else:
                    removeContactResult = contactBook.remove_contact(nameGet,surnameGet)
                    
                    # Display the contact removed
                    t = tk.Text(frame)
                    t.insert(tk.END, str(removeContactResult))
                    t.place(relx=0.01, rely=0.1)
                    t.after(2000, t.destroy)


                    # Reset the delete functionality
                    confirmButton.config(text="Delete Contact")
                    confirmButtonWarning = False   

            else :
                label1 = tk.Label(root, text="Please enter name and surname")
                label1.place(relx=0.3,rely=0.3)
                label1.after(2000, label1.destroy)         



    def See_all_Contats_Page():
        # Clear the frame from any widgets
        for widget in frame.winfo_children():
            widget.destroy()
        
        contacts = contactBook.display_contactbook()

        t = tk.Text(frame)
        t.place(relx=0.35)
        
        if contacts:
            
            for c in contacts:
                t.insert(tk.END, str(c) + '\n\n')            
            t.pack()

        else:
            t.insert(tk.END, "The contact book is empty" + '\n\n')            
            t.pack()
            

    def import_export_contact_page():
        # Clear the frame from any widgets
        for widget in frame.winfo_children():
            widget.destroy()

        # Check that the user is cd into the right folder:
        
             
        exportContactsButton = tk.Button(frame, text='Export Contacts to cvs', width=25, command= lambda:  message("export"))
        importContatcsButton = tk.Button(frame, text='Import Contacts from cvs', width=25, command= lambda:  message("import"))

        importContatcsButton.place(relx=0.15,rely=0.1)
        exportContactsButton.place(relx=0.15,rely=0.2)

        def message(type):
            
            if type == "import":
                label1 = tk.Label(frame, text="Are you sure?\nthis will revrite all current contats")
                label1.place(relx=0.15,rely=0.4)
                
                confirmButton = tk.Button(frame, text='Confirm', width=25, command= lambda:  detroy_widgets_and_call_to_action(contactBook.import_all_contacts, "Contacts Imported!")) 
                confirmButton.place(relx=0.15,rely=0.55)
                

            if type == "export":
                label1 = tk.Label(frame, text="Are you sure?\nthis will revrite all previusly saved contats")
                label1.place(relx=0.15,rely=0.4)

                confirmButton = tk.Button(frame, text='Confirm', width=25, command= lambda:  detroy_widgets_and_call_to_action(contactBook.export_all_contacts, "Contacts Exported!"))
                confirmButton.place(relx=0.15,rely=0.55) 


            def detroy_widgets_and_call_to_action(function, text):
                resultImportExport = function()
                if not resultImportExport: 
                    text = "Something went wrong\nCheck that the working directory is right\nOr that the file to read from exists"
                label1.config(text=text)
                confirmButton.destroy()
                label1.after(2000, label1.destroy)
                


    AddContactButton = tk.Button(root, text='Add Contact', width=25, command=Add_Collection_page)
    RemoveContactButton = tk.Button(root, text='Remove Contact', width=25,command=Remove_Contact_Page)
    SeeAllContactButton = tk.Button(root, text='See all Contacts', width=25,command=See_all_Contats_Page)
    importExportContctsButton = tk.Button(root, text='Import / Export Contacts', width=25,command=import_export_contact_page)
    StopButton = tk.Button(root, text='Stop', width=25, command=root.destroy)
    
    AddContactButton.pack()
    RemoveContactButton.pack()
    SeeAllContactButton.pack()
    importExportContctsButton.pack()
    StopButton.pack()

    root.mainloop()


    # Adding a contact

    #contactBook.add_contact()
    #contactBook.add_contact()
    #contactBook.add_contact()
    #contactBook.search_contact_by_name()
    
    #contactBook.add_contact()

    #contactBook.remove_contact()

    #contactBook.display_contactbook()

if __name__ == "__main__":
    main()

