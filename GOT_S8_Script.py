from tkinter import *
from tkinter import simpledialog

class GUI:
    def create_options(self, n, r, c):
        # Make options menu
        options = ["       Alive        ", "       Dead       ", "White Walker"]
        self.lab = Label(self.master, text=n).grid(row=r, column=c)
        lab_choice = StringVar()
        lab_choice.set("       Alive        ")
        self.character_choices.append(lab_choice)
        if c == 0:
            self.lab_menu = OptionMenu(*(self.master, self.character_choices[r-1*(c+1)]) +
                                   tuple(options)).grid(row=r, column=c+1)
        else:
            self.lab_menu = OptionMenu(*(self.master, self.character_choices[r+13]) +
                                   tuple(options)).grid(row=r, column=c+1)


    def make_questions(self, q, r):
        self.labelq = Label(self.master, text=q).grid(row=r, column=0, columnspan=3)
        ans = StringVar()
        self.bq_answers.append(ans)
        self.formquestions = Entry(self.master, textvariable=self.bq_answers[r-16]).grid(
                                                    row=r, columnspan=2, column = 3, sticky=W)
        

    def __init__(self, master):
        self.master = master

        #Headers
        self.col0 = Label(master, text="Character").grid(row=0, column=0)
        self.col1 = Label(master, text="Status at the end").grid(row=0, column=1, columnspan=2)
        i = 0
        while i < 15:
            self.coli = Label(master, text="| |").grid(row=i, column=3)
            i = i + 1
            
        self.col2 = Label(master, text="Character").grid(row=0, column=4)
        self.col3 = Label(master, text="Status at the end").grid(row=0, column=5, columnspan=2)

        #Characters and Check boxes
        self.character_choices = []
        options = ["       Alive        ", "       Dead       ", "White Walker"]
        
        #Jon Snow
        self.snow = Label(master, text="Jon Snow").grid(row=1, column=0)
        js_choice = StringVar()
        js_choice.set("       Alive        ")
        self.character_choices.append(js_choice)
        self.js_menu = OptionMenu(*(master, js_choice) + tuple(options)).grid(row=1, column=1)

        # Sansa
        self.sansa = Label(master, text="Sansa Stark").grid(row=2, column=0)
        sansa_choice = StringVar()
        sansa_choice.set("       Alive        ")
        self.character_choices.append(sansa_choice)
        self.sansa_menu = OptionMenu(*(master, sansa_choice) + tuple(options)).grid(row=2, column=1)

        # Arya Stark
        self.arya = Label(master, text="Arya Stark").grid(row=3, column=0)
        as_choice = StringVar()
        as_choice.set("       Alive        ")
        self.character_choices.append(as_choice)
        self.as_menu = OptionMenu(*(master, as_choice) + tuple(options)).grid(row=3, column=1)

        # Bran Stark
        self.bran = Label(master, text="Bran Stark").grid(row=4, column=0)
        bs_choice = StringVar()
        bs_choice.set("       Alive        ")
        self.character_choices.append(bs_choice)
        self.bs_menu = OptionMenu(*(master, bs_choice) + tuple(options)).grid(row=4, column=1)

        # Cersei Lannister
        self.cersei = Label(master, text="Cersei Lannister").grid(row=5, column=0)
        cl_choice = StringVar()
        cl_choice.set("       Alive        ")
        self.character_choices.append(cl_choice)
        self.cl_menu = OptionMenu(*(master, cl_choice) + tuple(options)).grid(row=5, column=1)

        # Jaime Lannister
        self.jaime = Label(master, text="Jaime Lannister").grid(row=6, column=0)
        jl_choice = StringVar()
        jl_choice.set("       Alive        ")
        self.character_choices.append(jl_choice)
        self.jl_menu = OptionMenu(*(master, jl_choice) + tuple(options)).grid(row=6, column=1)

        # Tyrion Lannister
        self.tyrion = Label(master, text="Tyrion Lannister").grid(row=7, column=0)
        tl_choice = StringVar()
        tl_choice.set("       Alive        ")
        self.character_choices.append(tl_choice)
        self.tl_menu = OptionMenu(*(master, tl_choice) + tuple(options)).grid(row=7, column=1)

        # Daenerys Targaryen
        self.danny = Label(master, text="Daenerys Targaryen").grid(row=8, column=0)
        dt_choice = StringVar()
        dt_choice.set("       Alive        ")
        self.character_choices.append(dt_choice)
        self.dt_menu = OptionMenu(*(master, dt_choice) + tuple(options)).grid(row=8, column=1)

        # Yara Greyjoy
        self.yg = Label(master, text="Yara Greyjoy").grid(row=9, column=0)
        yg_choice = StringVar()
        yg_choice.set("       Alive        ")
        self.character_choices.append(yg_choice)
        self.yg_menu = OptionMenu(*(master, yg_choice) + tuple(options)).grid(row=9, column=1) 

        # Theon using function
        self.create_options("Theon Greyjoy", 10, 0)

        # Melisandre using function
        self.create_options("Lady Melisandre", 11, 0)

        # Jorah Mormont using function
        self.create_options("Jorah Mormont", 12, 0)

        # Hound using function
        self.create_options("The Hound", 13, 0)

        # Mountain using function
        self.create_options("The Mountain", 14, 0)

        # looping to create widgets with functions
        names = ["Samwell Tarley", "Gilly", "Sam(child)", "Lord Varys", "Brienne of Tarth",
                 "Davos Seaworth", "Bronn", "Podrick Payne", "Tormund Giantsbane", "Grey Worm",
                 "Gendry", "Beric Dondarrion", "Euron Greyjoy"]
        j = 1
        for n in names:
            self.create_options(n, j, 4)
            j = j + 1

        # Tie Breakers
        self.bq_answers = []
        self.bq = Label(master, text="Bonus Questions!!!").grid(row=15, column=0,
                                                                pady = 6, columnspan=6, sticky="S")

        questions = ["Who will end up on the throne? (3 points)",
                     "Who kills the Night King? (2 points)",
                     "Do Jon and Daenerys end up together? (1 point)"]
        m = 16
        for q in questions:
            self.make_questions(q, m)
            m = m + 1
            
        
        # Enter Button
        button = Button(root, text="Click Here to Submit", command=self.onclick).grid(
                            row=20, columnspan=6, padx=5, pady=10)


    def onclick(self):
        una = simpledialog.askstring("Name", "Enter you name")
        un = str(una)
        users_name = un.replace(' ', '')
        fn = users_name + "_GameOfThrones.txt"
        f = open(fn, "w+")
        printed_answers = []
        i = 0
        printed_answers.append(users_name)
        for cc in self.character_choices:
            c = str(cc.get())
            c = c.strip()
            c = c[0]
            printed_answers.append(c)
            i = i + 1
            k = str(i)
            # print(k + ": " + c)

        #print()
        #print("Bonus Questions")
        for bqq in self.bq_answers:
            bqa = bqq.get()
            printed_answers.append(bqa)
            #print(bqa)

        for pa in printed_answers:
            f.write(pa+ "\n")

        f.close()
        root.destroy()
        #print()
        

        


root = Tk()
mygui = GUI(root)
mygui.master.title("GOT S8 BRACKET")
root.mainloop()
