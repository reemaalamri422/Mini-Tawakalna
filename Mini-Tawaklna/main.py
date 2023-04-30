import tkinter
from tkinter import *
import datetime
from tkinter import ttk, messagebox
import sqlite3
import re
from dataBaseClass import dataBaseClass




class myPROJECT:
    def __init__(self):
        self.window = Tk()
        self.window.title("Mini Tawakkalna")
        self.window.geometry('500x450')
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack()
        self.tab1 = Frame(self.notebook)
        self.tab2 = Frame(self.notebook)
        self.tab3 = Frame(self.notebook)
        self.tab1.pack(fill="both", expand=1)
        self.tab2.pack(fill="both", expand=1)
        self.tab3.pack()
        self.notebook.add(self.tab1, text="Check-in")
        self.notebook.add(self.tab2, text="(Immunity Check")
        self.notebook.add(self.tab3, text="(Import & Export)")
        ttk.Label(self.tab1, text="Enter your First Name, Last Name : ").pack()
        self.name = tkinter.Entry(self.tab1 )
        self.name.pack()
        ttk.Label(self.tab1, text="Select your gender : ").pack()
        self.radio_var = tkinter.IntVar()
        self.sex1= tkinter.Radiobutton(self.tab1 , text='Male' , value=1).pack()
        self.sex2 = tkinter.Radiobutton(self.tab1, text='Female' , value=2).pack()
        self.radio_var.set(1)
        ttk.Label(self.tab1, text="Enter your ID number : ").pack()
        self.Id = tkinter.Entry(self.tab1)
        self.Id.pack()
        ttk.Label(self.tab1, text="Enter Year of your Birth : ").pack()
        self.birth = tkinter.Entry(self.tab1)
        self.birth.pack()
        ttk.Label(self.tab1, text="Select the Type of Vaccine you had taken : ").pack()
        self.types = ('Pfizer', 'AstraZeneca', 'Moderna', 'J&J')
        self.selectt = tkinter.StringVar()
        self.typeOfVac = ttk.Combobox(self.tab1, textvariable=self.selectt)
        self.typeOfVac['values'] = self.types
        self.typeOfVac.current(1)
        self.typeOfVac.pack()
        ttk.Label(self.tab1, text="Enter Date & Time of it(in this format 12/10/2021 10:30 AM) : ").pack()
        self.date_time = tkinter.Entry(self.tab1)
        self.date_time.pack()
        ttk.Label(self.tab1, text="Enter your Phone number : ").pack()
        self.phoneN = tkinter.Entry(self.tab1)
        self.phoneN.pack()

        self.info_button = ttk.Button(self.tab1 ,text='submit', command=self.addInfo).pack()


        #TAB 2 code
        self.id_lable = tkinter.Label(self.tab2,text = "Enter your ID: ")
        self.id_lable.pack()
        self.id_feild = tkinter.Entry(self.tab2)
        self.id_feild.pack()

        self.yv = "yellowVacc.png"
        self.rv = "redvacc.png"
        self.gv = "greenVacc.png"
        self.img =''
        self.imgfile = tkinter.PhotoImage(file=self.img)

        self.check_button = tkinter.Button(self.tab2, text="check", command=self.checkID)
        self.check_button.pack()

        self.canvas = tkinter.Canvas(self.tab2, width=550, heigh=500, bg="white")
        self.canvas.create_image(100, 100, image=self.imgfile)
        self.canvas.pack(fill="both", expand="yes", pady="30", padx="30")

        self.window.mainloop()

    def addInfo(self):

        try:
            if self.checkValidaite():
                namE = self.name.get()
                ID = self.Id.get()
                birtH = self.birth.get()
                date_timE = self.date_time.get()
                phonEN = self.phoneN.get()
                global selection
                selection = self.radio_var.get()
                if selection == 1:
                    seX = 'Male'
                elif selection == 2:
                    seX = 'Female'
                typeOfVaC = self.selectt.get()
                dataBaseClass.construct(self,namE,seX,ID,birtH,typeOfVaC,date_timE,phonEN)
                print("Added successfully! ")

            else:
                messagebox.showinfo("Wornning","Please Enter Valid information .. ")

        except ValueError:
            print("can not added to database ")

        except:
            print("something went Wrong ")



    def checkValidaite(self):
        try:

            reg = "^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)"  # name
            pat = re.compile(reg)
            n1 = re.search(pat, self.name.get())
            xname = True
            if (n1):
                xname = True
            else :
                xname = False

            xbirth = True
            day, month, year = self.birth.get().split('/')
            if (int(year) < 1900 and int(year) > 2003):
                xbirth = True
            try:
               datetime.datetime(int(year), int(month), int(day))
            except ValueError:
               xbirth = False

            xdae_time = True
            day, month, year = self.date_time.get().split('/')
            if (int(year) > 2019):
                xdae_time = True
            #try:
                #datetime.datetime(int(year), int(month), int(day))
            #except ValueError:
                #xdae_time = False



            reg3 = '^(05)[0-9]{8}$'  # phone number
            pat3 = re.compile(reg3)
            p3 = re.search(pat3, self.phoneN.get())
            xphoneN = True
            if (p3) :
                xphoneN = True
            else:
                xphoneN = False

            reg4 = '^[0-9]{10}'
            pat4 = re.compile(reg4)
            i4 = re.search(pat4 , self.Id.get())
            xId = True
            if (i4):
                xId = True
            else:
                xId = False

            if xname and xId and xdae_time and xphoneN and xbirth :
                if xname != None and xId != None and xdae_time != None and xphoneN != None and xbirth!= None :
                   return True

            else:
                print("second else")
                return False

        except:
              return False


    #Tab 2 check id function:
    def checkID(self):
        cursor = dataBaseClass.cur()
        counter=0
        if (len(str(self.id_feild.get())) == 10):
            for row in cursor:
                if row[0] == self.id_feild.get():
                    counter += 1
            if counter >= 2:
                self.img = self.gv
            if counter == 1:
                self.img = self.yv
            if counter == 0:
                self.img = self.rv
            self.imgfile = tkinter.PhotoImage(file=self.img)
            self.canvas.create_image(190, 100, image=self.imgfile)
        else:
            messagebox.showinfo("Warning", "Please Enter valid ID")



p = myPROJECT()
dataBaseClass.closeCursor()
