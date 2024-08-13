from tkinter import *
from tkinter import messagebox

questionList = [
    {"question": "What is the process by which plants make their food called?", "ans": ["Photosynthesis","Respiration","Fermentation","Digesion"], "correctAns":1},
    {"question": "Which part of the plant is primarily responsible for water absorption", "ans": ["Flowers","Leaves","Stem","Roots"], "correctAns":4},
    {"question": "Which organelle is known as the control center of the cell", "ans": ["Ribosome","Nucleus","Lysosome","Vacuole"], "correctAns":2},
    {"question": "What is the pigment that's called that gives plant their green color and is involved in photosynthesis ", "ans": ["Melanin","Carotene","Chlorophyll","Hemoglobin"], "correctAns":3},
    {"question": "Which part of the plant is primarily responsible for water absorption", "ans": ["Flowers","Leaves","Stem","Roots"], "correctAns":4},
    {"question": "What type of oraganism can make it's own food using sunlight", "ans": ["Parasite","Autotroph","decomposer","Heterotroph"], "correctAns":2}
]

def home_page(base):
    main_frame = Frame(base, width=800, height=400)
    content_frame = Frame(main_frame, width=780, height=280)
    content_frame.grid(row=2, column=0, padx=5, pady=5)
    Label(main_frame, text="Welcome to Quiz Quest", font=(14)).grid(row=1, column=0, padx=5, pady=5)
    Label(content_frame, text="""In this game, the game will ask you a series of questions on a topic.
           If your answers are correct you will recieve points,\n after each question the user 
           can wager their points for double the amount\n
           but if you get it wrong you may loose some points.""", width=70, height=12, font=(10)).grid(row=2, column=0, padx=5, pady=5)
    button_frame = Frame(main_frame, width=780, height=100)
    button_frame.grid(row=3, column=0, padx=5, pady=5)
    button_exit = Button(button_frame, text="Exit", command=root.quit)
    button_exit.pack(side="left")
    button_continue = Button(button_frame, text="Continue",command=on_continueFirst)
    button_continue.pack(side="right")
    main_frame.grid(row=0, column=0, padx=5, pady=5)
    return main_frame

def last_page(base):
    main_frame = Frame(base, width=800, height=400)
    content_frame = Frame(main_frame, width=780, height=280)
    content_frame.grid(row=2, column=0, padx=5, pady=5)
    Label(main_frame, text="Thank you for completing the quiz", font=(14)).grid(row=1, column=0, padx=5, pady=5)
    score_lbl = Label(content_frame, text="Congratulations! Your score is " + str(score), width=70, height=12, font=(10)).grid(row=2, column=0, padx=5, pady=5)
    button_frame = Frame(main_frame, width=780, height=100)
    button_frame.grid(row=3, column=0, padx=5, pady=5)
    button_exit = Button(button_frame, text="Exit", command=root.quit)
    button_exit.pack(side="left")
    main_frame.grid(row=0, column=0, padx=5, pady=5)
    return main_frame

class Question:
    def __init__(self,base,q,i):
        self.q = q
        self.index = i
        self.main_frame = Frame(base, width=800, height=400)
        header_frame = Frame(self.main_frame, width=780, height=100)
        header_frame.grid(row=1, column=0, padx=5, pady=5)
        Label(header_frame, text="Question "+str(i+1)+".", width=70, font=("Ariel",12)).grid(row=1, column=0, padx=5, pady=5)
        self.score_lbl = Label(header_frame, text="Score: "+str(score))
        self.score_lbl.grid(row=1, column=1, padx=5, pady=5)
        
        content_frame = Frame(self.main_frame, width=580, height=100)
        content_frame.grid(row=2, column=0, padx=5, pady=5)
        Label(content_frame, text=q["question"], width=70, height=3, font=("Ariel",14),wraplength=800).grid(row=2, column=0, padx=5, pady=5)
        answer_frame = Frame(self.main_frame, width=780, height=100)
        answer_frame.grid(row=3, column=0, padx=5, pady=5)
        self.answer=IntVar(value=0)
        self.ans = [None]*4
        self.ans[0] = Radiobutton(answer_frame, variable=self.answer, text=q["ans"][0], height=2, anchor="w", value=1, font=("Ariel",12), command=self.check_ans)
        self.ans[0].grid(row=1, column=0)
        self.ans[1] = Radiobutton(answer_frame, variable=self.answer, text=q["ans"][1], height=2, anchor="w", value=2, font=("Ariel",12), command=self.check_ans)
        self.ans[1].grid(row=1, column=1)
        self.ans[2] = Radiobutton(answer_frame, variable=self.answer, text=q["ans"][2], height=2, anchor="w", value=3, font=("Ariel",12), command=self.check_ans)
        self.ans[2].grid(row=2, column=0, padx=50)
        self.ans[3] = Radiobutton(answer_frame, variable=self.answer, text=q["ans"][3], height=2, anchor="w", value=4, font=("Ariel",12), command=self.check_ans)
        self.ans[3].grid(row=2, column=1, padx=50)

        result_frame = Frame(self.main_frame, width=580, height=200,)
        result_frame.grid(row=4, column=0, padx=5, pady=5)

        self.result = Label(result_frame, text="", width=60, height=1,font=("Ariel",12))
        self.result.grid(row=1, column=0, padx=5, pady=5)

        multi_frame = Frame(self.main_frame, width=580, height=50,)
        multi_frame.grid(row=5, column=0, padx=5, pady=5)
        self.multiVar=IntVar(value=-1)
        self.multi_lbl = Label(multi_frame, text="Do you wish to multiply point in next question?", width=40, height=2,font=("Ariel",12))
        self.multi_yes = Radiobutton(multi_frame, variable=self.multiVar, text="Yes", height=1, anchor="w", value=1, font=("Ariel",12))
        self.multi_no = Radiobutton(multi_frame, variable=self.multiVar, text="No", height=1, anchor="w", value=0, font=("Ariel",12))
        
        button_frame = Frame(self.main_frame, width=780, height=100)
        button_frame.grid(row=6, column=0, padx=5, pady=5)
        button_exit = Button(button_frame, text="Skip", command=lambda:on_continue(i))
        button_exit.pack(side="left")
        button_continue = Button(button_frame, text="Continue", command=lambda:self.validateQuestion(i))
        button_continue.pack(side="right")

    def check_ans(self):
        if self.q["correctAns"] == self.answer.get() :
            self.result.configure(text="Correct!!")
            global score
            if self.index>0 and pageList[self.index-1].multiVar.get() == 1 :
                score = score + 2
            else: score = score+1
            self.score_lbl.configure(text="Score: "+str(score))
            self.score_lbl.update()        
        else:
            self.result.configure(text="Wrong answer..!!.")
        self.result.update()
        for i in range(0,4):
            self.ans[i].configure(state = DISABLED)
        self.multi_lbl.grid(row=2, column=0, padx=5, pady=5)
        self.multi_yes.grid(row=2, column=1, padx=5)
        self.multi_no.grid(row=2, column=2, padx=5)

    def validateQuestion(self,i):
        if self.answer.get() == 0:
            messagebox.showerror('Quiz Quest', 'Please select an answer!')
        else:
            on_continue(i)


def on_continueFirst():
    first_page.grid_remove()
    pageList[0].main_frame.grid(row=0, column=0, padx=5, pady=5)

def on_continue(i):
    print(i)
    if len(pageList)-1 > i :
        pageList[i].main_frame.grid_remove()
        pageList[i+1].main_frame.grid(row=0, column=0, padx=5, pady=5)
        pageList[i+1].score_lbl.configure(text="Score: "+str(score))
        pageList[i+1].score_lbl.update() 
    else :
        pageList[len(pageList)-1].main_frame.grid_remove()
        last_page(root).tkraise()

root = Tk()

root.minsize(800,400)
first_page = home_page(root)
pageList = []
score = 0
for index, q in enumerate(questionList):
    pageList.append(Question(root,q,index))
first_page.tkraise()
root.mainloop()
