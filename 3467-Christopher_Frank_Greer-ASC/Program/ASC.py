from tkinter import *
import smtplib
import sqlite3
class ASC(Frame):
    def createWidgets(self):

        def mainMenu():
            def removeAccountMenu():
                Back.grid_forget()
                Title.grid_forget()
                account.grid_forget()
                priveleges.grid_forget()
                pword.grid_forget()
                RemoveRemoveButton()

            def accountToMenu():
                account.grid_forget()
                priveleges.grid_forget()
                pword.grid_forget()
                RemoveRemoveButton()
                showMenu()
                
            def removeAccount():
                Back.grid_forget()
                ID.grid_forget()
                idLabel.grid_forget()
                account.grid_forget()
                accountLabel.grid_forget()
                privileges.grid_forget()
                privilegesLabel.grid_forget()
                pword.grid_forget()
                pwordLabel.grid_forget()
                Edit.grid_forget()
                Remove.grid_forget()
                Inst.grid_forget()
                showMenu()
                
            def removeMenu():
                ExitASC.grid_forget()
                List.grid_forget()
                Add.grid_forget()
                Account.grid_forget()
                title1.grid_forget()
                title2.grid_forget()
                Menu.grid_forget()
                
            def showMenu():
                mainMenu()
#make Add Item                
            def makeAdd():
                List.grid_forget()
                Add.grid_forget()
                Account.grid_forget()
                title1.grid_forget()
                title2.grid_forget()
                Menu.grid_forget()
                def removeAdd():
                    BackAdd.grid_forget()
                    item.grid_forget()
                    itemLabel.grid_forget()
                    itemNo.grid_forget()
                    itemNoLabel.grid_forget()
                    price.grid_forget()
                    priceLabel.grid_forget()
                    description.grid_forget()
                    descriptionLabel.grid_forget()
                    Addbtn.grid_forget()
                    AddTitle.grid_forget()
                    showMenu()
                    
                def getName():
                    Name=NameInput.get()
                    if Name==(""):
                        print ("Blank Field")
                        return
                    else:
                        global AddName
                        AddName=NameInput.get()
                        getNo()                        
                        return AddName

                def getNo():
                    No=NoInput.get()
                    if No==(""):
                        print ("Blank Field")
                        return
                    else:
                        global AddNo
                        AddNo=NoInput.get()
                        getPrice()
                        return AddNo


                def getPrice():
                    Price=PriceInput.get()
                    if Price==(""):
                        print ("Blank Field")
                        return
                    else:
                        global AddPrice
                        AddPrice=PriceInput.get()
                        getDesc()
                        return AddPrice

                def getDesc():
                    Desc=DescInput.get()
                    if Desc==(""):
                        print ("Blank Field")
                        return
                    else:
                        global AddDesc
                        AddDesc=DescInput.get()
                        return AddDesc

                def addItem():
                    getName()
                    print(AddName)
                    print(AddNo)
                    print(AddPrice)
                    print(AddDesc)
                    conn = sqlite3.connect('ASC.db')
                    cur=conn.cursor()
                    cur.execute ("INSERT INTO Stock VALUES (?,?,?,?)", ([AddName],[AddNo],[AddPrice],[AddDesc]))
                    conn.commit()

                NameInput=StringVar()
                NoInput=StringVar()
                PriceInput=StringVar()
                DescInput=StringVar()
                        
                BackAdd= Button(self, width=5, fg="red", text="Back", command=removeAdd)
                BackAdd.grid (sticky=W,row=10, column=1)

                AddTitle= Label(self, text="Add Item", font="calibri, 16", pady="20")
                AddTitle.grid (row=1,column=2)

                item= Entry(self, width=27,textvariable=NameInput)
                item.grid (sticky=W,column=2,row=2)

                itemLabel= Label(self, text="Item Name:")
                itemLabel.grid (sticky=E,column=1, row=2)

                itemNo= Entry(self, width=27,textvariable=NoInput)
                itemNo.grid (sticky=W,column=2,row=3)

                itemNoLabel= Label(self, text="Item Code:")
                itemNoLabel.grid (sticky=E,column=1, row=3)

                price= Entry(self, width=27,textvariable=PriceInput)
                price.grid (sticky=W,column=2,row=4)

                priceLabel= Label(self, text="Price:")
                priceLabel.grid (sticky=E,column=1, row=4)

                description= Entry(self, width=27,textvariable=DescInput)
                description.grid (sticky=W,column=2,row=5)

                descriptionLabel= Label(self, text="Description:")
                descriptionLabel.grid (sticky=E,column=1, row=5)

                Addbtn= Button(self, width=20, bg="light blue", text="Add Item", font="calibri", command=addItem)
                Addbtn.grid (sticky=E,column=2,row=6)

#Make Add End

#Make Account
            def makeAccountMenu():
                List.grid_forget()
                Add.grid_forget()
                Account.grid_forget()
                title1.grid_forget()
                title2.grid_forget()
                Menu.grid_forget()
                ExitASC.grid_forget()

                def showAccountMenu():
                    ToAMenu.grid_forget()
                    TitleA.grid_forget()
                    accountAMenu.grid_forget()
                    pwordAMenu.grid_forget()
                    conn = sqlite3.connect('signin.db')
                    cursor= conn.cursor()
                    cursor.execute("SELECT PRIVELLAGES from SignIn WHERE Name='%s'" %disUN)
                    row = cursor.fetchone()
                    for cursor in row:
                        Priv=row[0]
                    if Priv=="Admin":
                        RemoveAMenu.grid_forget()
                        privilegesAMenu.grid_forget()
                    else:
                        return
                    
                    
                    

#make remove
                def RemoveAccount():                                           
                    def RemoveRemove():
                        ToAMenu.grid_forget()
                        ID.grid_forget()
                        idLabel.grid_forget()
                        accountMenu.grid_forget()
                        accountLabel.grid_forget()
                        privileges.grid_forget()
                        privilegesLabel.grid_forget()
                        pword.grid_forget()
                        pwordLabel.grid_forget()
                        Remove.grid_forget()
                        Inst1.grid_forget()
                        Inst2.grid_forget()
                        RemTitle.grid_forget()
                        showAccountMenu()
                        makeAccountMenu()                   

                    def remove():
                        pop = Toplevel()
                        pop.title("REMOVED")

                        msg = Label(pop, text="THIS ACCOUNT HAS BEEN REMOVED")
                        msg.pack()
                        
                        ok = Button(pop, text="Dismiss", command=pop.destroy)
                        ok.pack()

                        ID=idInput.get()
                        conn = sqlite3.connect('signin.db')
                        conn.execute("DELETE from SignIn WHERE ID='%s'" %ID)
                        conn.commit()
                        conn.close()
                        print("REMOVED USER")
                    
                    def warning():
                        pop = Toplevel()
                        pop.title("WARNING")

                        msg = Label(pop, text="THIS WILL REMOVE ALL ACCOUNT DETAILS, ARE YOU SURE?")
                        msg.pack()

                        yes = Button(pop, text="I Am Sure",command=remove, bg="light blue")
                        yes.pack()
                        
                        no = Button(pop, text="Dismiss", command=pop.destroy)
                        no.pack()
                        
                    showAccountMenu()
                        
                    idInput=StringVar()
                    
                    pwordInput=StringVar()

                    nameInput=StringVar()
                    
                    privInput=StringVar()
                    
                    ToAMenu = Button(self, width=5, fg="red", text="Back",command=RemoveRemove)
                    ToAMenu.grid (sticky=W,row=10, column=1)

                    RemTitle= Label(self, pady=20, font="calibri, 20", width=27, text="Remove an Account")
                    RemTitle.grid (sticky=W,column=2,row=1)

                    ID= Entry(self, width=27,textvariable=idInput)
                    ID.grid (sticky=W,column=2,row=2)

                    idLabel= Label(self, text="ID No.:")
                    idLabel.grid (sticky=E,column=1, row=2)
                    
                    accountMenu= Entry(self, width=27, textvariable=nameInput)
                    accountMenu.grid (sticky=W,column=2,row=3)

                    accountLabel= Label(self, text="User Name:")
                    accountLabel.grid (sticky=E,column=1, row=3)

                    privileges= Entry(self, width=27, textvariable=privInput)
                    privileges.grid (sticky=W,column=2,row=4)

                    privilegesLabel= Label(self, text="Privileges:")
                    privilegesLabel.grid (sticky=E,column=1, row=4)

                    pword= Entry(self, width=27,textvariable=pwordInput)
                    pword.grid (sticky=W,column=2,row=5)

                    pwordLabel= Label(self, text="Password:")
                    pwordLabel.grid (sticky=E,column=1, row=5)

                    Remove= Button(self, width=20, bg="light blue", text="Remove Account", font="calibri", command=warning)
                    Remove.grid (sticky=W,column=2,row=6)

                    Inst1= Label(self, width=40, text="ID Number is needed", font="calibri")
                    Inst1.grid (row=2, column=3)

                    Inst2= Label(self, width=40, text="Removal can be done with just an ID Number", font="calibri")
                    Inst2.grid (row=3, column=3)
            #Remove Account End

            #Priv Edit Start
                def PrivEdit():
                    
                    def RemovePrivEdit():
                        ToAMenu.grid_forget()
                        ID.grid_forget()
                        idLabel.grid_forget()
                        privileges.grid_forget()
                        privilegesLabel.grid_forget()
                        Edit.grid_forget()
                        Inst1.grid_forget()
                        Inst2.grid_forget()
                        PrivTitle.grid_forget()
                        showAccountMenu()
                        makeAccountMenu()
                        
                    def getPriv():
                        ID=idInput.get()
                        print (ID)
                        conn = sqlite3.connect('signin.db')
                        output = conn.execute("UPDATE signin SET Privileges WHERE ID='?'", ([ID]))

                    def edit():
                        getPriv()
                        
                    showAccountMenu()
                        
                    idInput=StringVar()
                   
                    privInput=StringVar()
                    
                    ToAMenu = Button(self, width=5, fg="red", text="Back", command=RemovePrivEdit)
                    ToAMenu.grid (sticky=W,row=10, column=1)

                    PrivTitle= Label(self, pady=20, font="calibri, 20", width=27, text="Change Privellages")
                    PrivTitle.grid (sticky=W,column=2,row=1)

                    ID= Entry(self, width=27,textvariable=idInput)
                    ID.grid (sticky=W,column=2,row=2)

                    idLabel= Label(self, text="ID No.:")
                    idLabel.grid (sticky=E,column=1, row=2)
                    
                    privileges= Entry(self, width=27, textvariable=privInput)
                    privileges.grid (sticky=W,column=2,row=3)

                    privilegesLabel= Label(self, text="Privileges:")
                    privilegesLabel.grid (sticky=E,column=1, row=3)


                    Edit= Button(self, width=20, bg="light blue", text="Edit Account", font="calibri", command=edit)
                    Edit.grid (sticky=W,column=2,row=4)

                    Inst1= Label(self, width=40, text="ID Number is needed", font="calibri")
                    Inst1.grid (sticky=W,row=2, column=3)

                    Inst2= Label(self, width=40, text="Editing needs all details entered correctly", font="calibri")
                    Inst2.grid (sticky=W,row=3, column=3)
            # Priv Edit End
                def PassEdit():
                    def RemovePassEdit():
                        ToAMenu.grid_forget()
                        ID.grid_forget()
                        idLabel.grid_forget()
                        pword.grid_forget()
                        pwordLabel.grid_forget()
                        Edit.grid_forget()
                        Inst1.grid_forget()
                        Inst2.grid_forget()
                        PassTitle.grid_forget()
                        showAccountMenu()
                        makeAccountMenu()
                        
                    def getPass():
                        ID=idInput.get()
                        PW=pwordInput.get()
                        print (PW)
                        conn = sqlite3.connect('signin.db')
                        output = conn.execute("UPDATE Password from SignIn WHERE ID='%s'" %ID)
       
                    def edit():
                        getPass()

                    
                    showAccountMenu()    
                        
                    idInput=StringVar()
                    
                    pwordInput=StringVar()
                    
                    ToAMenu = Button(self, width=5, fg="red", text="Back", command=RemovePassEdit)
                    ToAMenu.grid (sticky=W,row=10, column=1)

                    PassTitle= Label(self, pady=20, font="calibri, 20", width=27, text="Change Password")
                    PassTitle.grid (sticky=W,column=2,row=1)

                    ID= Entry(self, width=27,textvariable=idInput)
                    ID.grid (sticky=W,column=2,row=2)

                    idLabel= Label(self, text="ID No.:")
                    idLabel.grid (sticky=E,column=1, row=2)

                    pword= Entry(self, width=27,textvariable=pwordInput)
                    pword.grid (sticky=W,column=2,row=3)

                    pwordLabel= Label(self, text="Password:")
                    pwordLabel.grid (sticky=E,column=1, row=3)

                    Edit= Button(self, width=20, bg="light blue", text="Edit Account", font="calibri", command=edit)
                    Edit.grid (sticky=W,column=2,row=4)

                    Inst1= Label(self, width=40, text="ID Number is needed", font="calibri")
                    Inst1.grid (sticky=W,row=2, column=3)

                    Inst2= Label(self, width=40, text="Editing needs all details entered correctly", font="calibri")
                    Inst2.grid (sticky=W,row=3, column=3)
            #Pass Edit End

            #Name Edit Start        
                def NameEdit():
                    
                    def RemoveNameEdit():
                        ToAMenu.grid_forget()
                        ID.grid_forget()
                        idLabel.grid_forget()
                        account.grid_forget()
                        accountLabel.grid_forget()
                        Edit.grid_forget()
                        Inst1.grid_forget()
                        Inst2.grid_forget()
                        NameTitle.grid_forget()
                        showAccountMenu()
                        makeAccountMenu()
                                                
                    def getName():
                        ID=idInput.get()
                        NM=nameInput.get()
                        print (NM)
                        conn = sqlite3.connect('signin.db')
                        output = conn.execute("UPDATE Privileges from SignIn WHERE ID='%s'" %ID)

                    
                    def edit():
                        getName()

                    showAccountMenu()
                        
                    idInput=StringVar()
                    
                    nameInput=StringVar()
                        
                    ToAMenu = Button(self, width=5, fg="red", text="Back", command=RemoveNameEdit)
                    ToAMenu.grid (sticky=W,row=10, column=1)

                    NameTitle= Label(self, pady=20, font="calibri, 20", width=27, text="Change Name")
                    NameTitle.grid (sticky=W,column=2,row=1)

                    ID= Entry(self, width=27,textvariable=idInput)
                    ID.grid (sticky=W,column=2,row=2)

                    idLabel= Label(self, text="ID No.:")
                    idLabel.grid (sticky=E,column=1, row=2)
                    
                    account= Entry(self, width=27, textvariable=nameInput)
                    account.grid (sticky=W,column=2,row=3)

                    accountLabel= Label(self, text="Account Name:")
                    accountLabel.grid (sticky=E,column=1, row=3)

                    Edit= Button(self, width=20, bg="light blue", text="Edit Account", font="calibri", command=edit)
                    Edit.grid (sticky=W,column=2,row=4)

                    Inst1= Label(self, width=40, text="ID Number is needed", font="calibri")
                    Inst1.grid (sticky=W,row=2, column=3)

                    Inst2= Label(self, width=40, text="Editing needs all details entered correctly", font="calibri")
                    Inst2.grid (sticky=W,row=3, column=3)
        #Name Edit End

                def toMainMenu():
                    showAccountMenu()
                    mainMenu()

                def getRemove():
                    conn = sqlite3.connect('signin.db')
                    cursor= conn.cursor()
                    cursor.execute("SELECT PRIVELLAGES from SignIn WHERE Name='%s'" %disUN)
                    row = cursor.fetchone()
                    for cursor in row:
                        Priv=row[0]
                    if Priv=="Admin":
                        ButtonRemove()
                    else:
                        return
                def ButtonRemove():
                    global RemoveAMenu
                    RemoveAMenu= Button(self, font="calibri", width=20, bg="light blue", text="Remove Account",command=RemoveAccount)
                    RemoveAMenu.grid (column=2,row=6)
                    global privilegesAMenu
                    privilegesAMenu= Button(self, font="calibri", width=20, bg="light blue", text="Edit Privileges",command=PrivEdit)
                    privilegesAMenu.grid (column=2,row=4)

                def RemoveRemoveButton():
                    RemoveAMenu.grid_forget()
                    privilegesAMenu.grid_forget()

                getRemove()              
                
                ToAMenu= Button(self, width=5, fg="red", text="Back",command=toMainMenu)
                ToAMenu.grid (sticky=W,row=10, column=1)

                TitleA= Label(self, pady=20, font="calibri, 20", width=27, text="Account Editing Menu")
                TitleA.grid (column=2,row=1)

                accountAMenu= Button(self, font="calibri", width=20, bg="light blue", text="Edit User Name", command=NameEdit)
                accountAMenu.grid (column=2,row=2)

                pwordAMenu= Button(self, font="calibri", width=20, bg="light blue", text="Edit Password",command=PassEdit)
                pwordAMenu.grid (column=2,row=5)

#Account Menu End
            

#make Edit
            def makeEdit():
                List.grid_forget()
                Add.grid_forget()
                Account.grid_forget()
                title1.grid_forget()
                title2.grid_forget()
                Menu.grid_forget()
                def removeAdd():
                    BackAdd.grid_forget()
                    item.grid_forget()
                    itemLabel.grid_forget()
                    itemNo.grid_forget()
                    itemNoLabel.grid_forget()
                    price.grid_forget()
                    priceLabel.grid_forget()
                    description.grid_forget()
                    descriptionLabel.grid_forget()
                    Restock.grid_forget()
                    Addbtn.grid_forget()
                    Remove.grid_forget()
                    showMenu()
                    
                def notify():
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login("AutomaticStockChecker@gmail.com", "ASC12345678")
                    entry=NameInput.get()
                    conn = sqlite3.connect('ASC.db')
                    cursor= conn.cursor()
                    cursor = conn.execute("SELECT*from Stock WHERE ItemName='%s'"%entry)
                    if cursor==None:
                        print("Search is empty")
                        return
                    else:
                        for row in cursor:
                            Item = row[0]
                            return Item
                    msg = "Notification From A.S.C Needs to be restocked as it is running low or is out of stock"
                    server.sendmail("AutomaticStockChecker@gmail.com", "AutomaticStockChecker@gmail.com", msg)
                    server.quit()
                    print ("Email sent")

                def addItem():
                    Name=NameInput.get()
                    No=NoInput.get()
                    Price=PriceInput.get()
                    Desc=DescInput.get()
                    print (Name)
                    print (No)
                    print (Price)
                    print (Desc)
                    conn = sqlite3.connect('ASC.db')
                    conn.execute("SELECT*from Stock")
                    conn.execute ("INSERT INTO Stock VALUES ('%s','%s','%s','%s') ", (Name,No,Price,Desc))
                    row = conn.fetchall()
                    
                def getName():
                    item=NameInput.get()
                    print (NameInput.get())
                    return item

                NameInput=StringVar()
                NoInput=StringVar()
                PriceInput=StringVar()
                DescInput=StringVar()
                        
                BackAdd= Button(self, width=5, fg="red", text="Back", command=removeAdd)
                BackAdd.grid (sticky=W,row=10, column=1)

                item= Entry(self, width=27,textvariable=NameInput)
                item.grid (sticky=W,column=2,row=1)

                itemLabel= Label(self, text="Item Name:")
                itemLabel.grid (sticky=E,column=1, row=1)

                itemNo= Entry(self, width=27,textvariable=NoInput)
                itemNo.grid (sticky=W,column=2,row=2)

                itemNoLabel= Label(self, text="Item No:")
                itemNoLabel.grid (sticky=E,column=1, row=2)

                price= Entry(self, width=27,textvariable=PriceInput)
                price.grid (sticky=W,column=2,row=3)

                priceLabel= Label(self, text="Price code:")
                priceLabel.grid (sticky=E,column=1, row=3)

                description= Entry(self, width=27,textvariable=DescInput)
                description.grid (sticky=W,column=2,row=4)

                descriptionLabel= Label(self, text="Description:")
                descriptionLabel.grid (sticky=E,column=1, row=4)

                Restock= Button(self, width=20, bg="light blue", text="Restock", font="calibri", command=notify)
                Restock.grid (sticky=E,column=2,row=6)

                Addbtn= Button(self, width=20, bg="light blue", text="Add Item", font="calibri", command=addItem)
                Addbtn.grid (sticky=E,column=2,row=7)

                Remove= Button(self, width=20, bg="light blue", text="Remove Item", font="calibri")
                Remove.grid (sticky=E,column=2,row=8)
#Make Edit End
                
#Make List
            def makeList():
                List.grid_forget()
                Add.grid_forget()
                Account.grid_forget()
                title1.grid_forget()
                title2.grid_forget()
                ExitMenu.grid_forget()
                Menu.grid_forget()

            #make sub Edit
                def makeSubEdit():
                    print("Welcome to Sub Edit")
                    def removeEdit():
                        BackEdit.grid_forget()
                        SubTitle.grid_forget()
                        item.grid_forget()
                        itemLabel.grid_forget()
                        itemNo.grid_forget()
                        itemNoLabel.grid_forget()
                        price.grid_forget()
                        priceLabel.grid_forget()
                        description.grid_forget()
                        descriptionLabel.grid_forget()
                        Restock.grid_forget()
                        Addbtn.grid_forget()
                        Remove.grid_forget()
                        makeList()
                        
                    def notify():
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login("AutomaticStockChecker@gmail.com", "ASC12345678")
                        getName() 
                        msg = "Notification From A.S.C", item, "Needs to be restocked as it is running low or is out fo stock"
                        server.sendmail("AutomaticStockChecker@gmail.com", "AutomaticStockChecker@gmail.com", msg)
                        server.quit()
                        print ("Email sent")

                    def addItem():
                        getName()
                        getNo()
                        getDesc()
                        getPrice()
                        conn = sqlite3.connect('ASC.db')
                        conn.execute("INSERT INTO Stock (ItemName,ItemNo,Price,Description) \
                        VALUES ('%s','%s','%s','%s')",(Name,No,Price,Desc));
                        conn.commit()

                    def Remove():
                        getName()
                        getNo()
                        getDesc()
                        getPrice()
                        conn = sqlite3.connect('ASC.db')
                        conn.execute("REMOVE FROM Stock WHERE ID='%s'" %ID)
                        conn.commit()
                        
                    def getName():
                        entry=NameInput.get()
                        if entry==None:
                            Name="No Such Item"
                            return Name
                        else:
                            Name=entry
                            print (Name)
                            return Name
                        
                    
                    def getNo():
                        entry=NoInput.get()
                        if entry==None:
                            No="No Such Item"
                            return No
                        else:                            
                            No=entry
                            print (No)
                            return No
                        
                        

                    def getPrice():
                        entry=PriceInput.get()
                        if entry==None:
                            Price="No Such Item"
                            return Price
                        else:
                            Price=entry
                            print (Price)
                            return Price
                    
                    def getDesc():
                        entry=DescInput.get()
                        if entry==None:
                            Desc="No Such Item"
                            return Desc
                        else:
                            Desc=entry
                            print (Desc)
                            return Desc
                            
                    NameInput=StringVar()
                    NoInput=StringVar()
                    PriceInput=StringVar()
                    DescInput=StringVar()
                            
                    BackEdit= Button(self, width=5, fg="red", text="Back", command=removeEdit)
                    BackEdit.grid (sticky=W,row=10, column=1)

                    SubTitle=Label (self, text="Edit An Item", font="calibri, 16")
                    SubTitle.grid (column=2,row=1)

                    item= Entry(self, width=27,textvariable=NameInput)
                    item.grid (sticky=W,column=2,row=2)

                    itemLabel= Label(self, text="Item Name:")
                    itemLabel.grid (sticky=E,column=1, row=2)

                    itemNo= Entry(self, width=27,textvariable=NoInput)
                    itemNo.grid (sticky=W,column=2,row=3)

                    itemNoLabel= Label(self, text="Item No:")
                    itemNoLabel.grid (sticky=E,column=1, row=3)

                    price= Entry(self, width=27,textvariable=PriceInput)
                    price.grid (sticky=W,column=2,row=4)

                    priceLabel= Label(self, text="Price code:")
                    priceLabel.grid (sticky=E,column=1, row=4)

                    description= Entry(self, width=27,textvariable=DescInput)
                    description.grid (sticky=W,column=2,row=5)

                    descriptionLabel= Label(self, text="Description:")
                    descriptionLabel.grid (sticky=E,column=1, row=5)

                    Restock= Button(self, width=20, bg="light blue", text="Restock", font="calibri", command=notify)
                    Restock.grid (sticky=E,column=2,row=6)

                    Addbtn= Button(self, width=20, bg="light blue", text="Save Changes", font="calibri", command=addItem)
                    Addbtn.grid (sticky=E,column=2,row=7)

                    Remove= Button(self, width=20, bg="light blue", text="Remove Item", font="calibri", command=Remove)
                    Remove.grid (sticky=E,column=2,row=8)
                #make Sub Edit End
                    
                def removeList():
                    Back.grid_forget()
                    search.grid_forget()
                    searchLabel.grid_forget()
                    Name.grid_forget()
                    NO.grid_forget()
                    Price.grid_forget()
                    Desc.grid_forget()
                    RestockL.grid_forget()
                    Edit.grid_forget()
                    searchTitle.grid_forget()
                    Clear.grid_forget()
                    showMenu()

                def notify():
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login("AutomaticStockChecker@gmail.com", "ASC12345678")
                    entry=searchInput.get()
                    conn = sqlite3.connect('ASC.db')
                    cursor= conn.cursor()
                    cursor = conn.execute("SELECT*from Stock WHERE ItemName='%s'"%entry)
                    if cursor==None:
                        print("Search is empty")
                        return
                    else:
                        for row in cursor:
                            Item = row[0]
                            return Item
                    msg = "Notification From A.S.C Needs to be restocked as it is running low or is out of stock"
                    server.sendmail("AutomaticStockChecker@gmail.com", "AutomaticStockChecker@gmail.com", msg)
                    server.quit()
                    print ("Email sent")
                
                def getSearch():
                    def clear():
                        aRestock.grid_forget()
                        aEdit.grid_forget()                  
                        aName.grid_forget()
                        aNO.grid_forget()                    
                        aPrice.grid_forget()
                        aDesc.grid_forget()
                        aClear.grid_forget()

                    def toSubEdit():
                        Back.grid_forget()
                        searchTitle.grid_forget()
                        search.grid_forget()
                        searchLabel.grid_forget()
                        Name.grid_forget()
                        NO.grid_forget()
                        Price.grid_forget()
                        Desc.grid_forget()
                        Clear.grid_forget()
                        RestockL.grid_forget()
                        Edit.grid_forget()
                        clear()
                        searchTitle.grid_forget()
                        makeSubEdit()

                    def getName():
                        entry=searchInput.get()
                        conn = sqlite3.connect('ASC.db')
                        cursor= conn.cursor()
                        cursor = conn.execute("SELECT ItemName from Stock WHERE ItemName LIKE '%s'"%entry)
                        if cursor==None:
                            Name="No Such Item"
                            return Name
                        else:
                            for row in cursor:
                                Name=row[0]
                                return Name
                        
                    
                    def getNo():
                        entry=searchInput.get()
                        conn = sqlite3.connect('ASC.db')
                        cursor= conn.cursor()
                        cursor = conn.execute("SELECT ItemNo from Stock WHERE ItemName LIKE '%s'"%entry)
                        if cursor==None:
                            No="No Such Item"
                            return No
                        else:
                            for row in cursor:
                                No=row[0]
                                return No
                        
                        

                    def getPrice():
                        entry=searchInput.get()
                        conn = sqlite3.connect('ASC.db')
                        cursor= conn.cursor()
                        cursor = conn.execute("SELECT Price from Stock WHERE ItemName LIKE '%s'"%entry)
                        if cursor==None:
                            Price="No Such Item"
                            return Price
                        else:
                            for row in cursor:
                                Price=row[0]
                                return Price
                    
                    def getDesc():
                        entry=searchInput.get()
                        conn = sqlite3.connect('ASC.db')
                        cursor= conn.cursor()
                        cursor = conn.execute("SELECT Description from Stock WHERE ItemName LIKE'%s'"%entry)
                        if cursor==None:
                            Desc="No Such Item"
                            return Desc
                        else:
                            for row in cursor:
                                Desc=row[0]
                                return Desc

                    getNo()
                    getName()
                    getPrice()
                    getDesc()
                        
                    aName= Label(self,width=15,text=getName())
                    aName.grid(sticky=W,column=2,row=3)

                    aNO=Label(self,width=15,text=getNo())
                    aNO.grid(sticky=W,column=3,row=3)

                    aPrice=Label(self,width=15,text=getPrice())
                    aPrice.grid(sticky=W,column=4,row=3)

                    aDesc=Label(self,width=30,text=getDesc())
                    aDesc.grid(sticky=W,column=5,row=3)

                    aRestock=Button(self,width=14,text="Restock", command=notify)
                    aRestock.grid(sticky=W,column=6,row=3)

                    aEdit=Button(self,width=14,text="Edit", command=toSubEdit)
                    aEdit.grid(sticky=W,column=7,row=3)

                    aClear=Button(self,width=14,text="Clear Search", command=clear)
                    aClear.grid(sticky=W,column=8,row=3)
  
                    
                Back = Button(self, width=5, fg="red", text="Back", command=removeList)
                Back.grid (sticky=W,row=100, column=0)

                searchInput=StringVar()

                searchTitle=Label (self, text="Item Search", font="calibri, 16")
                searchTitle.grid (column=1,row=1)

                search=Entry(self,textvariable=searchInput)
                search.grid (sticky=W,column=1,row=2)

                searchLabel=Button(self, text="Search:",command=getSearch)
                searchLabel.grid (sticky=W,column=0, row=2)

                Name= Label(self,width=15,text="ItemName",bg="grey")
                Name.grid(sticky=W,column=2,row=2)

                NO=Label(self,width=15,text="ItemNo.",bg="grey")
                NO.grid(sticky=W,column=3,row=2)

                Price=Label(self,width=15,text="ItemPrice",bg="grey")
                Price.grid(sticky=W,column=4,row=2)

                Desc=Label(self,width=30,text="Description",bg="grey")
                Desc.grid(sticky=W,column=5,row=2)

                RestockL=Label(self,width=15,text="Restock",bg="grey")
                RestockL.grid(sticky=W,column=6,row=2)

                Edit=Label(self,width=15,text="Edit",bg="grey")
                Edit.grid(sticky=W,column=7,row=2)

                Clear=Label(self,width=15,text="Clear",bg="grey")
                Clear.grid(sticky=W,column=8,row=2)
#list end

            def getID():
                conn = sqlite3.connect('signin.db')
                output = conn.execute("SELECT ID from SignIn WHERE Name='%s'" %disUN)
                for row in output:
                    ID=row[0]
                return ID
            
            ExitASC.grid_forget()
            ExitMenu = Button(self, width=5, fg="red", text="Exit")
            ExitMenu["command"] =  self.quit
            ExitMenu.grid (sticky=W,row=10, column=1)

            Menu = Label(self,text="Menu", pady=20, font="calibri, 20")
            Menu.grid (row=1, column=2)

            List = Button(self, width=20, bg="light blue", text="Search Item", font="calibri", command=makeList)
            List.grid (row=2, column=2)

            Add = Button(self, width=20, bg="light blue", text="Add Item", font="calibri", command=makeAdd)
            Add.grid (row=3, column=2)
            
            Account = Button(self, width=20, bg="light blue", text="Account Settings", font="calibri", command=makeAccountMenu)
            Account.grid (row=4, column=2)

            ID1=Label (self, text="Your ID number is:")
            ID1.grid (row=11, column=3, sticky=E)
            
            ID2=Label (self, text=getID())
            ID2.grid (row=11, column=4, sticky=W)

            UN1=Label (self, text="Your UserName is:")
            UN1.grid (row=11, column=1, sticky=E)

            UN2=Label (self, text=disUN)
            UN2.grid (row=11, column=2, sticky=W)
         
            title1=Label(self, text="Bentley and Skinner", font="calibri, 30")
            title1.grid (row=6, column=2)

            title2=Label(self, text="A.S.C", font="calibri, 30")
            title2.grid (row=7, column=2)
#Menu End

#Sign In Start            
        def removeSign():
            SignLabel.grid_forget()
            SignIn.grid_forget()
            UserLabel.grid_forget()
            PwordLabel.grid_forget()
            User.grid_forget()
            Pword.grid_forget()
            title1.grid_forget()
            title2.grid_forget()
            mainMenu()
            
        def findUN():
            conn = sqlite3.connect('signin.db')
            UN=userInput.get()
            output = conn.execute("SELECT*from SignIn WHERE Name='%s'" %UN)
            for row in output:
                Name=row[1]
                if UN==Name:
                    global disUN
                    disUN=Name
                    findPW()
                    conn.close()
                    return disUN
                else:
                    conn.close()
                    return
            conn.close()    
        
        def findPW():
            conn = sqlite3.connect('signin.db')
            PW=pwordInput.get()
            output = conn.execute("SELECT*from SignIn WHERE Password='%s'" %PW)
            for row in output:
                Pass=row[2]
                if PW==Pass:
                    removeSign()
                    conn.close()
                    return PW
                else:
                    conn.close()
                    return   
            conn.close()                
        global ExitASC
        ExitASC = Button(self, width=5, fg="red", text="Exit")
        ExitASC["command"] =  self.quit
        ExitASC.grid (sticky=W,row=10, column=1)

        SignLabel= Label(self, text="Sign In", font="calibri, 16", pady="20")
        SignLabel.grid (row=1, column=2)
        
        UserLabel = Label(self, text="Account Name:", font="calibri")
        UserLabel.grid (sticky=W,row=2,column=2)

        PwordLabel = Label(self, text="Password:", font="calibri")
        PwordLabel.grid (sticky=W,row=3,column=2)
                        
        userInput=StringVar()
        
        pwordInput=StringVar()
        
        User = Entry(self,textvariable=userInput)
        User.grid (row=2, column=2)

        Pword= Entry(self,textvariable=pwordInput)
        Pword.grid (row=3, column=2)

        SignIn=Button(self, text="Sign In",  bg="light blue", font="calibri", command=findUN)
        SignIn.grid (row=4, column=2)
        
        title1=Label(self, text="Bentley and Skinner", font="calibri, 30")
        title1.grid (row=6, column=2)

        title2=Label(self, text="A.S.C", font="calibri, 30")
        title2.grid (row=7, column=2)

        space=Label(self,width=3)
        space.grid (row=6, column=3)

#Sign In Menu end
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()       

   

root = Tk()
root.iconbitmap(r'Icon\favicon.ico')
app = ASC(master=root)
root.title("A.S.C")
root.attributes("-fullscreen",True)
app.mainloop()
root.destroy()

