from tkinter import * 
from functions import *

home = Tk()
 
home.title("DCC Analysis Interface Home")

home.geometry('610x750')
 
greeter = Label(home, text="Welcome to DCC Analysis Interface",
                font = ("Arial Bold", 27),
                fg = "navy")

greeter.grid(column=0, row=0)

logo = Label(home, text="detroit",
                font = ("Arial Bold", 50),
                fg = "white")
logo.place(x = 100, y = 630)

slogan = Label(home, text="crime",
                font = ("Arial Bold", 50),
                fg = "royal blue")
slogan.place(x = 311, y = 630)

under = Label(home, text="C O M M I S S I O N",
                font = ("Arial", 23),
                fg = "lavender") 
under.place(x = 205, y = 701)



# FUNCTIONALITY FOR BUTTON 1

def clicked1(): 
    func_window = Tk()
    func_window.geometry('600x400')
    func_window.title('Single field search')
    header = Label(func_window,
                    text = 'Searchable fields include: investigators, date, reference, report type, summary, complainant',
                    font = ("Arial Bold", 10),
                    fg = "navy")                
    header.grid(column=0, row=0)
    field_label = Label(func_window,
                    text = "Enter field",
                    font = ("Arial Bold", 8)).place(x = 0, y = 40, anchor = W)
    condition_label = Label(func_window,
                    text = "Enter keyword",
                    font = ("Arial Bold", 8)).place(x = 0, y = 65, anchor = W)
    

    variable = StringVar(func_window)
    variable.set("set field")
    field = OptionMenu(func_window, variable, "investigators", "date", "reference", "report type", "summary", "complainant")
    
    condition = Entry(func_window, width = 15)

    field.place(x = 140, y = 40, anchor = CENTER)
    condition.place(x = 140, y = 65, anchor = CENTER)

    logo = Label(func_window, text="detroit",
                font = ("Arial Bold", 50),
                fg = "white")
    logo.place(x = 10, y = 270)

    slogan = Label(func_window, text="crime",
                font = ("Arial Bold", 50),
                fg = "royal blue")
    slogan.place(x = 221, y = 270)

    under = Label(func_window, text="C O M M I S S I O N",
                font = ("Arial", 23),
                fg = "lavender") 
    under.place(x = 115, y = 341)

    def searcherExc():
            root = Tk()
            root.title('Single search output')

            scrollbar = Scrollbar(root)
            scrollbar.pack( side = RIGHT, fill=Y )
            xscrollbar = Scrollbar(root, orient = HORIZONTAL)
            xscrollbar.pack(side=BOTTOM, fill=X)

            df = searcher(variable.get(), condition.get())
 
            mylist = Listbox(root, width = 500, yscrollcommand = scrollbar.set)
            for x in range(len(df)):
                vals = df.iloc[x]
                table = '  --  '.join(str(v) for v in vals[:5])
                ref = vals[5]
                summary = vals[6]
                names = vals[7]
                mylist.insert(END, "")
                mylist.insert(END, ".........................." + str(x + 1) + "...........................")
                mylist.insert(END, "........................................................")
                mylist.insert(END, "")
                mylist.insert(END, table.upper())
                mylist.insert(END, "")
                mylist.insert(END, ref)
                mylist.insert(END, "")
                mylist.insert(END, summary)
                mylist.insert(END, "")
                mylist.insert(END, names) 

                
            mylist.pack( side = LEFT, fill = BOTH )
            scrollbar.config( command = mylist.yview )
            xscrollbar.config( command = mylist.xview )          
                        
    execute = Button(func_window, text = "search", command = searcherExc, bg = 'PaleGreen1').place(x = 0, y = 95, anchor = W)

# FUNCTIONALITY FOR BUTTON 2

def clicked2(): 
    func_window = Tk()
    func_window.geometry('600x400')
    func_window.title('Double Inclusive field search')
    header = Label(func_window,
                    text = 'Searchable fields include: investigators, date, reference, report type, summary, complainant',
                    font = ("Arial Bold", 10),
                    fg = "navy")                    
    header.grid(column=0, row=0)
    field_label = Label(func_window,
                    text = "Enter field1",
                    font = ("Arial Bold", 8)).place(x = 0, y = 40, anchor = W)
    condition_label = Label(func_window,
                    text = "Enter keyword1",
                    font = ("Arial Bold", 8)).place(x = 0, y = 65, anchor = W)
    field_label2 = Label(func_window,
                    text = "Enter field2",
                    font = ("Arial Bold", 8)).place(x = 0, y = 90, anchor = W)
    condition_label2 = Label(func_window,
                    text = "Enter keyword2",
                    font = ("Arial Bold", 8)).place(x = 0, y = 115, anchor = W)
    
    variable = StringVar(func_window)
    variable.set("set field")
    field = OptionMenu(func_window, variable, "investigators", "date", "reference", "report type", "summary", "complainant")
    
    condition = Entry(func_window, width = 15)
    
    variable2 = StringVar(func_window)
    variable2.set("set field")
    field2 = OptionMenu(func_window, variable2, "investigators", "date", "reference", "report type", "summary", "complainant")
    
    condition2 = Entry(func_window, width = 15)
    
    field.place(x = 155, y = 40, anchor = CENTER)
    condition.place(x = 155, y = 65, anchor = CENTER)
    field2.place(x = 155, y = 90, anchor = CENTER)
    condition2.place(x = 155, y = 115, anchor = CENTER)

    logo = Label(func_window, text="detroit",
                font = ("Arial Bold", 50),
                fg = "white")
    logo.place(x = 10, y = 270)

    slogan = Label(func_window, text="crime",
                font = ("Arial Bold", 50),
                fg = "royal blue")
    slogan.place(x = 221, y = 270)

    under = Label(func_window, text="C O M M I S S I O N",
                font = ("Arial", 23),
                fg = "lavender") 
    under.place(x = 115, y = 341)


    def dubSearcherIncExc():
            root = Tk()
            root.title('Double search inclusive output')

            scrollbar = Scrollbar(root)
            scrollbar.pack( side = RIGHT, fill=Y )
            xscrollbar = Scrollbar(root, orient = HORIZONTAL)
            xscrollbar.pack(side=BOTTOM, fill=X)

            df = dubSearcherInc(variable.get(), condition.get(), variable2.get(), condition2.get())
 
            mylist = Listbox(root, width = 500, yscrollcommand = scrollbar.set)
            for x in range(len(df)):
                vals = df.iloc[x]
                table = '  --  '.join(str(v) for v in vals[:5])
                ref = vals[5]
                summary = vals[6]
                names = vals[7]
                mylist.insert(END, "")
                mylist.insert(END, ".........................." + str(x + 1) + "...........................")
                mylist.insert(END, "........................................................")
                mylist.insert(END, "")
                mylist.insert(END, table.upper())
                mylist.insert(END, "")
                mylist.insert(END, ref)
                mylist.insert(END, "")
                mylist.insert(END, summary)
                mylist.insert(END, "")
                mylist.insert(END, names)

                
            mylist.pack( side = LEFT, fill = BOTH )
            scrollbar.config( command = mylist.yview )
            xscrollbar.config( command = mylist.xview )          
                        
    execute = Button(func_window, text = "search", command = dubSearcherIncExc, bg = 'pale green').place(x = 0, y = 140, anchor = W)

# FUNCTIONALITY FOR BUTTON 3

def clicked3(): 
    func_window = Tk()
    func_window.geometry('600x400')
    func_window.title('Double Exclusive field search')
    header = Label(func_window,
                    text = 'Searchable fields include: investigators, date, reference, report type, summary, complainant',
                    font = ("Arial Bold", 10),
                    fg = "navy")                    
    header.grid(column=0, row=0)
    field_label = Label(func_window,
                    text = "Enter field1",
                    font = ("Arial Bold", 8)).place(x = 0, y = 40, anchor = W)
    condition_label = Label(func_window,
                    text = "Enter keyword1",
                    font = ("Arial Bold", 8)).place(x = 0, y = 65, anchor = W)
    field_label2 = Label(func_window,
                    text = "Enter field2",
                    font = ("Arial Bold", 8)).place(x = 0, y = 90, anchor = W)
    condition_label2 = Label(func_window,
                    text = "Enter keyword2",
                    font = ("Arial Bold", 8)).place(x = 0, y = 115, anchor = W)
    
    variable = StringVar(func_window)
    variable.set("set field")
    field = OptionMenu(func_window, variable, "investigators", "date", "reference", "report type", "summary", "complainant")
    
    condition = Entry(func_window, width = 15)
    
    variable2 = StringVar(func_window)
    variable2.set("set field")
    field2 = OptionMenu(func_window, variable2, "investigators", "date", "reference", "report type", "summary", "complainant")
    
    condition2 = Entry(func_window, width = 15)
    
    field.place(x = 155, y = 40, anchor = CENTER)
    condition.place(x = 155, y = 65, anchor = CENTER)
    field2.place(x = 155, y = 90, anchor = CENTER)
    condition2.place(x = 155, y = 115, anchor = CENTER)

    logo = Label(func_window, text="detroit",
                font = ("Arial Bold", 50),
                fg = "white")
    logo.place(x = 10, y = 270)

    slogan = Label(func_window, text="crime",
                font = ("Arial Bold", 50),
                fg = "royal blue")
    slogan.place(x = 221, y = 270)

    under = Label(func_window, text="C O M M I S S I O N",
                font = ("Arial", 23),
                fg = "lavender") 
    under.place(x = 115, y = 341)


    def dubSearcherExcExc():
            root = Tk()
            root.title('Double search exclusive output')

            scrollbar = Scrollbar(root)
            scrollbar.pack( side = RIGHT, fill=Y )
            xscrollbar = Scrollbar(root, orient = HORIZONTAL)
            xscrollbar.pack(side=BOTTOM, fill=X)

            df = dubSearcherExc(variable.get(), condition.get(), variable2.get(), condition2.get())
 
            mylist = Listbox(root, width = 500, yscrollcommand = scrollbar.set)
            for x in range(len(df)):
                vals = df.iloc[x]
                table = '  --  '.join(str(v) for v in vals[:5])
                ref = vals[5]
                summary = vals[6]
                names = vals[7]
                mylist.insert(END, "")
                mylist.insert(END, ".........................." + str(x + 1) + "...........................")
                mylist.insert(END, "........................................................")
                mylist.insert(END, "")
                mylist.insert(END, table.upper())
                mylist.insert(END, "")
                mylist.insert(END, ref)
                mylist.insert(END, "")
                mylist.insert(END, summary)
                mylist.insert(END, "")
                mylist.insert(END, names)
                
            mylist.pack( side = LEFT, fill = BOTH )
            scrollbar.config( command = mylist.yview )
            xscrollbar.config( command = mylist.xview )          
                        
    execute = Button(func_window, text = "search", command = dubSearcherExcExc, bg = 'pale green').place(x = 0, y = 140, anchor = W)

# FUNCTIONALITY FOR BUTTON 4

def clicked4(): 
    func_window = Tk()
    func_window.geometry('600x400')
    func_window.title('Names Search')
    header = Label(func_window,
                    text = 'Thoroughly search DCC reports by a single name',
                    font = ("Arial Bold", 10),
                    fg = "navy")                    
    header.grid(column=0, row=0)
    field_label = Label(func_window,
                    text = "Enter Name",
                    font = ("Arial Bold", 8)).grid(row = 2, sticky = 'w')
    field = Entry(func_window, width = 15)
    field.place(x = 140, y = 30, anchor = CENTER)

    logo = Label(func_window, text="detroit",
                font = ("Arial Bold", 50),
                fg = "white")
    logo.place(x = 10, y = 270)

    slogan = Label(func_window, text="crime",
                font = ("Arial Bold", 50),
                fg = "royal blue")
    slogan.place(x = 221, y = 270)

    under = Label(func_window, text="C O M M I S S I O N",
                font = ("Arial", 23),
                fg = "lavender") 
    under.place(x = 115, y = 341)

    
    def namesExc():
            root = Tk()
            root.title('Names search output')

            scrollbar = Scrollbar(root)
            scrollbar.pack( side = RIGHT, fill=Y )
            xscrollbar = Scrollbar(root, orient = HORIZONTAL)
            xscrollbar.pack(side=BOTTOM, fill=X)

            df = names(field.get())
 
            mylist = Listbox(root, width = 500, yscrollcommand = scrollbar.set)
            for x in range(len(df)):
                vals = df.iloc[x]
                table = '  --  '.join(str(v) for v in vals[:5])
                ref = vals[5]
                summary = vals[6]
                namesy = vals[7]
                mylist.insert(END, "")
                mylist.insert(END, ".........................." + str(x + 1) + "...........................")
                mylist.insert(END, "........................................................")
                mylist.insert(END, "")
                mylist.insert(END, table.upper())
                mylist.insert(END, "")
                mylist.insert(END, ref)
                mylist.insert(END, "")
                mylist.insert(END, summary)
                mylist.insert(END, "")
                mylist.insert(END, namesy)

                
            mylist.pack( side = LEFT, fill = BOTH )
            scrollbar.config( command = mylist.yview )
            xscrollbar.config( command = mylist.xview )          
                        
    execute = Button(func_window, text = "search", command = namesExc, bg = 'pale green').grid(row = 4, sticky = 'w')

# FUNCTIONALITY FOR BUTTON 5

def clicked5(): 
    func_window = Tk()
    func_window.geometry('550x400')
    func_window.title('Clemis Search')
    header = Label(func_window,
                    text = 'Search available CLEMIS data for a single name',
                    font = ("Arial Bold", 10),
                    fg = "navy")                    
    header.grid(column=0, row=0)
    field_label = Label(func_window,
                    text = "Enter Name",
                    font = ("Arial Bold", 8)).grid(row = 2, sticky = 'w')
    field = Entry(func_window, width = 15)
    field.place(x = 140, y = 30, anchor = CENTER)

    logo = Label(func_window, text="detroit",
                font = ("Arial Bold", 50),
                fg = "white")
    logo.place(x = 10, y = 270)

    slogan = Label(func_window, text="crime",
                font = ("Arial Bold", 50),
                fg = "royal blue")
    slogan.place(x = 221, y = 270)

    under = Label(func_window, text="C O M M I S S I O N",
                font = ("Arial", 23),
                fg = "lavender") 
    under.place(x = 115, y = 341)

    
    def clemisExc():
            root = Tk()
            root.title('Clemis search output')

            scrollbar = Scrollbar(root)
            scrollbar.pack( side = RIGHT, fill=Y )
            xscrollbar = Scrollbar(root, orient = HORIZONTAL)
            xscrollbar.pack(side=BOTTOM, fill=X)

            df = inClemis(field.get())
 
            mylist = Listbox(root, width = 500, yscrollcommand = scrollbar.set)
            for x in range(len(df)):
                vals = df.iloc[x]
                table = '  --  '.join(str(v) for v in vals[:2])
                DandR = '  --  '.join(str(v) for v in vals[3:5])
                ofense = vals[2]
                citation = vals[5]
                mylist.insert(END, "")
                mylist.insert(END, ".........................." + str(x + 1) + "...........................")
                mylist.insert(END, "........................................................")
                mylist.insert(END, "")
                mylist.insert(END, table.upper() + ' -- ' + DandR.upper())
                mylist.insert(END, "")
                mylist.insert(END, ofense)
                mylist.insert(END, "")
                mylist.insert(END, citation)

                
            mylist.pack( side = LEFT, fill = BOTH )
            scrollbar.config( command = mylist.yview )
            xscrollbar.config( command = mylist.xview )          
                        
    execute = Button(func_window, text = "search", command = clemisExc, bg = 'pale green').grid(row = 4, sticky = 'w')


# HOME BUTTON PLACEMENTS

func1 = Button(home, text="Search by single field", font = ("Arial Bold", 9), command = clicked1, bg = "white")
func1.place(x= 200, y= 80)
func1.config(height = 5, width = 28)

func2 = Button(home, text="Search by two fields (inclusive)", font = ("Arial Bold", 9), command = clicked2, bg = "azure")
func2.place(x=200, y = 180)
func2.config(height = 5, width = 28)

func3 = Button(home, text="Search by two fields (exclusive)", font = ("Arial Bold", 9), command = clicked3, bg = "white")
func3.place(x=200, y =280)
func3.config(height = 5, width = 28)

func4 = Button(home, text="Search reports by POI", font = ("Arial Bold", 9), command = clicked4, bg = "azure")
func4.place(x=200, y = 380)
func4.config(height = 5, width = 28)

func5 = Button(home, text="Search CLEMIS by POI", font = ("Arial Bold", 9), command = clicked5, bg = "white")
func5.place(x=200, y = 480)
func5.config(height = 5, width = 28)


home.mainloop()

