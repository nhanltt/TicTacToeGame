import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import os

playerName = ['Player 1', 'Player 2']


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}
      
        for F in (StartPage, Three_Three, Again_Exit):

            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
    
    def __del__(self):
      class_name = self.__class__.__name__       
      print(class_name, "destroyed")
   
# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # print("you're in start page")

        self.player = ["Player 1", "Player 2"]
        self.playersign = ['X', 'O']
        self.turn = 1
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

        # label of frame Layout 2
        label = tk.Label(self, text="Welcome to Tic Tac Toe")
        label.grid(row=0, column=2, padx=10, pady=10)

        button1 = tk.Button(self, text="Start",
                            command=lambda: [controller.show_frame(Three_Three), self.closed()])
        button1.grid(row=4, column=4, padx=10, pady=10)

    def closed(self):
        self.destroy()


# second window frame page1
class Three_Three(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        # print("you're in second page")

        self.t = StartPage(self, self.controller)

        self.getname1 = tk.Label(self, text="Player 1's Name")
        self.getname1.grid(row=2, column=2)
        self.name1 = tk.Entry(self)
        self.name1.grid(row=2, column=3, padx=10)

        self.getname2 = tk.Label(self, text="Player 2's Name")
        self.getname2.grid(row=3, column=2)
        self.name2 = tk.Entry(self)
        self.name2.grid(row=3, column=3, padx=10, pady=10)

        self.reg_btn = tk.Button(
            self, text="Register", command=lambda: self.regName())
        self.reg_btn.grid(row=4, column=3)

        self.count = self.t.turn

    def regName(self):

        playerName[0] = self.name1.get()
        playerName[1] = self.name2.get()
        label = tk.Label(
            self, text=playerName[0] + " is " + self.t.playersign[0])
        label.grid(row=0, column=4, padx=10, pady=10)
        label = tk.Label(
            self, text=playerName[1] + " is " + self.t.playersign[1])
        label.grid(row=1, column=4, padx=10, pady=10)

        self.name1.after(100, self.name1.destroy())
        self.name2.after(100, self.name2.destroy())
        self.getname1.after(100, self.getname1.destroy())
        self.getname2.after(100, self.getname2.destroy())
        self.reg_btn.after(100, self.reg_btn.destroy())

        self.button2 = tk.Button(self, text="Play!!!",
                                 command=self.createGameURLs)
        self.button2.grid(row=2, column=1, padx=10, pady=0)

    def createGameURLs(self):
        self.button2.after(100, self.button2.destroy())

        if self.t.turn == 0:
            label = tk.Label(self, text=playerName[0] + "'s turn")
            label.grid(row=0, column=5, padx=10, pady=10)
        elif self.t.turn == 1:
            label = tk.Label(self, text=playerName[1] + "'s turn")
            label.grid(row=0, column=5, padx=10, pady=10)

        self.button = []
        for i in range(0, 9):
            # print(i)
            self.button.append(tk.Button(self, text=str(i+1),
                                         command=lambda i=i: self.open_this(i), width=15))
            col = 4 + (i // 3)
            Row = (i % 3) + 2
            self.button[i].grid(column=col, row=Row, sticky=W)

    def space_check(self, board, position):
        
        return board[position] == ' '

    def win_check(self, board, mark):

        if board[0] == board[1] == board[2] == mark or board[3] == board[4] == board[5] == mark or board[6] == board[7] == board[8] == mark:
            return True
        if board[0] == board[3] == board[6] == mark or board[1] == board[4] == board[7] == mark or board[2] == board[5] == board[8] == mark:
            return True
        if board[0] == board[4] == board[8] == mark or board[2] == board[4] == board[6] == mark:
            return True
        return False

    def full_board_check(self, board):

        for i in range(9):
            if self.space_check(board, i):
                return False
        return True

    def open_this(self, myNum):
        # print(myNum)
        # print(self.t.turn)

        if self.space_check(self.t.board, myNum):

            self.t.board[myNum] = self.t.playersign[self.t.turn]
            self.button[myNum]["text"] = self.t.playersign[self.t.turn]

            if self.win_check(self.t.board, self.t.playersign[self.t.turn]) == True:
                print(f'The winner is {self.t.player[self.t.turn]}')
                winner = tk.Label(self, text='The winner: ' + playerName[self.t.turn])
                winner.grid(row=7, column=4, pady=10, padx=10)
                next_btn = tk.Button(self, text="Next", 
                command=lambda: self.controller.show_frame(Again_Exit))
                next_btn.grid(row=8, column=4, padx=10, pady=10)
                # Link to final page -> Inform the winner
            elif self.full_board_check(self.t.board):
                print('TIE GAME!')
                tie = tk.Label(self, text='TIE GAME!')
                tie.grid(row=7, column=4, padx=10, pady=10)
                next_btn = tk.Button(self, text="Next", 
                command=lambda: [self.controller.show_frame(Again_Exit), self.closed()])
                next_btn.grid(row=8, column=4, padx=10, pady=10)
            else:
                self.count += 1
                self.t.turn = self.count % 2

                if self.t.turn == 0:
                    label = tk.Label(self, text=playerName[0] + "'s turn", width= 10)
                    label.grid(row=0, column=5, padx=10, pady=10)
                elif self.t.turn == 1:
                    label = tk.Label(self, text=playerName[1] + "'s turn", width= 10)
                    label.grid(row=0, column=5, padx=10, pady=10)
                print(self.t.board)

    def closed(self):
        self.destroy()

class Again_Exit(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        inform = tk.Label(self, text = "Do you want to continue or exit? \n Click button below \n or \n Enter R: Play again \n Enter X: Exit")
        inform.grid(row=0, column=1, padx=10, pady=10)

        controller.bind("<Key>", self.key_handle)

        again_btn = tk.Button(self, text="Fightinggg", command= lambda: [self.controller.show_frame(Again_Exit), self.closed()])
        again_btn.grid(row=1, column=1, padx=10, pady=10)

        exit_btn = tk.Button(self, text="Bye Bye", command=lambda: self.Exit_but())
        exit_btn.grid(row=2, column=1, padx=10, pady=10)
    
    def key_handle(self, key):
        # print(key.char)
        if key.char == 'r':
            self.closed()
        elif key.char == 'x':
            self.Exit_but()
        else:
            pass
    
    def closed(self):

        self.destroy()
        self.controller.destroy()
        self.new = tkinterApp()
        self.new.title("T.T.T")
        # self.mainloop()

    def Exit_but(self):
        
        self.destroy()
        self.controller.destroy()


app = tkinterApp()
app.title("T.T.T")
app.mainloop()

