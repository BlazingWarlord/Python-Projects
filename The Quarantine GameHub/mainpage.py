from datetime import datetime

from tkinter import *
from tkinter import messagebox


from os import system, name
with open('count.txt','w') as f:
    f.write('0,0,0,0')
    f.close()

def playcount(n):
    with open('count.txt','r') as f:
        global playl
        a = f.read()
        playl = a.split(',')
        playl[n]= int(playl[n])+1
        f.close()
    with open('count.txt','w') as f:
        for x in playl:
            f.write(str(x))
            f.write(',')
        f.close()
  
  
def about():
    main = Toplevel()
    main.title('About The Quarantine GameHub')
    main.config(bg='#04c211')
    main.geometry('1200x600')
    label = Label(main,text='FEELING BORED DURING THE LOCKDOWN ?',font=('Showcard Gothic','30'),justify='center',bg='#b8b804',relief='groove')
    label.pack()
    labelgp = Label(main,text='',font=('Goudy Stout','25'),fg='#ff5005',bg='#04c211')
    labelgp.pack()
    label1 = Label(main,text='Not to worry cause The Quarantine GameHub is up and running',font=('Showcard Gothic','25'),justify='center',bg='#04c211',fg='#034a16')
    label1.pack()
    labeltext = Label(main,text='This Quarantine Lockdown has left everyone feeling bored and upset with nothing to do.\n\n But don\'t worry anymore. The Quarantine GameHub is now ready to use\n\nIt comes along with 4 simple and fun to play games to \n\nknock your boredom OUT OF THE PARK !!!\n\nIt also has its own Time Played Remainder System \n\nto help you keep track of how long you\'ve spent.\n\nJust fire up your laptops and...\n\n',font=('Bodoni MT Black','15'),justify='center',bg='#04c211')
    labeltext.pack()
    labelgp = Label(main,text='GET PLAYING',font=('Goudy Stout','25'),fg='#ff5005',bg='#04c211')
    labelgp.pack()


def battleship():
    a = datetime.now()
    import subprocess
    subprocess.call('python BattleshipFn.py', creationflags=subprocess.CREATE_NEW_CONSOLE)
    b = datetime.now()
    s = str(b-a)[:7]
    l = s.split(':')
    playcount(0)
    messagebox.showinfo('Time Played',f'You played Battleship for {l[0]} Hours, {l[1]} Minutes and {l[2]} Seconds ')


def tictactoe():
    a = datetime.now()
    import subprocess
    subprocess.call('python TTTFn.py', creationflags=subprocess.CREATE_NEW_CONSOLE)
    b = datetime.now()
    s = str(b-a)[:7]
    l = s.split(':')
    playcount(1)
    messagebox.showinfo('Time Played',f'You played Tic-Tac-Toe for {l[0]} Hours, {l[1]} Minutes and {l[2]} Seconds ')


def wordle():
    a = datetime.now()
    import subprocess
    subprocess.call('python WordleFn.py', creationflags=subprocess.CREATE_NEW_CONSOLE)
    b = datetime.now()
    s = str(b-a)[:7]
    l = s.split(':')
    playcount(2)
    messagebox.showinfo('Time Played',f'You played Wordle for {l[0]} Hours, {l[1]} Minutes and {l[2]} Seconds ')

def rps():
    a = datetime.now()
    import subprocess
    subprocess.call('python RPSFn.py', creationflags=subprocess.CREATE_NEW_CONSOLE)
    b = datetime.now()
    s = str(b-a)[:7]
    l = s.split(':')
    playcount(3)
    messagebox.showinfo('Time Played',f'You played Rock-Paper-Scissors for {l[0]} Hours, {l[1]} Minutes and {l[2]} Seconds ')


    
def playcountpage():
    with open('count.txt','r') as f:
        global playl
        a = f.read()
        playl = a.split(',')
        f.close()
    main = Toplevel()
    main.title('About The Quarantine GameHub')
    main.config(bg='#04c211')
    main.geometry('1200x600')
    label = Label(main,text='NUMBER OF TIMES PLAYED THIS SESSION:',font=('Showcard Gothic','30'),justify='center',bg='#b8b804',relief='groove')
    label.pack()
    labelgp = Label(main,text='',font=('Goudy Stout','25'),fg='#ff5005',bg='#04c211')
    labelgp.pack()
    label1 = Label(main,text=f'Tic-Tac-Toe: {playl[1]} times',font=('Showcard Gothic','25'),justify='center',bg='#04c211',fg='#fffb00')
    label1.pack()
    label1 = Label(main,text=f'Battleship: {playl[0]} times',font=('Showcard Gothic','25'),justify='center',bg='#04c211',fg='#fffb00')
    label1.pack()
    label1 = Label(main,text=f'Wordle: {playl[2]} times',font=('Showcard Gothic','25'),justify='center',bg='#04c211',fg='#fffb00')
    label1.pack()
    label1 = Label(main,text=f'Rock-Paper-Scissors: {playl[3]} times',font=('Showcard Gothic','25'),justify='center',bg='#04c211',fg='#fffb00')
    label1.pack()
    
    
    

def quitwin():
    global root
    root.destroy()


def gh():
    global root
    root.destroy()
    
    root = Tk()
    root.geometry('860x450')


    menubar = Menu(root)
    menu = Menu(menubar, tearoff=0)
    menu.add_command(label='New GameHub',command=gh)
    menu.add_command(label='About',command=about)
    menu.add_command(label='Quit',command=quitwin)
    menubar.add_cascade(label='GameHub Menu',menu=menu)

    gmenu = Menu(menubar, tearoff=0)
    gmenu.add_command(label='Tic-Tac-Toe',command=tictactoe)
    gmenu.add_command(label='Tambola-Ticket-Gen',command=wordle)
    gmenu.add_command(label='Rock-Paper-Scissors',command=rps)
    gmenu.add_command(label='Battleships',command=battleship)
    menubar.add_cascade(label='Games Menu',menu=gmenu)

    root.config(bg='#1aab3c',menu=menubar)


    mainlabel = Label(root,text='The Quarantine GameHub',justify='center',relief='groove',font=('Copperplate Gothic Bold','44'),bg='#00c72f')
    mainlabel.grid(row=0,column=1)
    label = Label(root,text='\t\t\t\t\tOne-Stop Boredom Beater\t\t\t\t\t',justify='center',relief='groove',font=('Fixedsys','10'),bg='#d6c102')
    label.grid(row=1,column=1)
    enter = Label(root,text='',justify='center',relief='flat',font=('Fixedsys','10'),bg='#1aab3c')
    enter.grid(row=2,column=1)
    enter1 = Label(root,text='',justify='center',relief='flat',font=('Fixedsys','10'),bg='#1aab3c')
    enter1.grid(row=3,column=1)
    gamelabel = Label(root,text='GAMES',justify='center',relief='raised',font=('Fixedsys','20'),bg='#05f3ff')
    gamelabel.grid(row=4,column=1)
    enter2 = Label(root,text='',justify='center',relief='flat',font=('Fixedsys','10'),bg='#1aab3c')
    enter2.grid(row=5,column=1)

    buttonframe = Frame(root)

    button1 = Button(buttonframe,text='TIC-TAC-TOE',justify='center',relief='raised',font=('Fixedsys','10'),bg='#d6c102',activebackground='#05f3ff',height=7,width=25,activeforeground='#1aab3c',command=tictactoe)
    button1.grid(row=0,column=0)
    button1 = Button(buttonframe,text='ROCK-PAPER-SCISSORS',justify='center',relief='raised',font=('Fixedsys','8'),bg='#d6c102',activebackground='#05f3ff',height=7,width=25,activeforeground='#1aab3c',command=rps)
    button1.grid(row=0,column=1)
    button1 = Button(buttonframe,text='WORDLE',justify='center',relief='raised',font=('Fixedsys','7'),bg='#d6c102',activebackground='#05f3ff',height=7,width=25,activeforeground='#1aab3c',command=wordle)
    button1.grid(row=1,column=0)
    button1 = Button(buttonframe,text='BATTLESHIPS',justify='center',relief='raised',font=('Fixedsys','10'),bg='#d6c102',activebackground='#05f3ff',height=7,width=25,activeforeground='#1aab3c',command=battleship)
    button1.grid(row=1,column=1)

    buttonframe.grid(row=6,column=1)
    
    button1 = Button(root,text='NUMBER OF TIMES PLAYED',justify='center',relief='raised',font=('Fixedsys','10'),bg='#d6c102',activebackground='#05f3ff',height=2,width=52,activeforeground='#1aab3c',command=playcountpage)
    button1.grid(row=7,column=1)



    root.mainloop()





root = Tk()
root.geometry('860x480')


menubar = Menu(root)
menu = Menu(menubar, tearoff=0)
menu.add_command(label='New GameHub',command=gh)
menu.add_command(label='About',command=about)
menu.add_command(label='Quit',command=quitwin)
menubar.add_cascade(label='GameHub Menu',menu=menu)

gmenu = Menu(menubar, tearoff=0)
gmenu.add_command(label='Tic-Tac-Toe',command=tictactoe)
gmenu.add_command(label='Wordle',command=wordle)
gmenu.add_command(label='Rock-Paper-Scissors',command=rps)
gmenu.add_command(label='Battleships',command=battleship)
menubar.add_cascade(label='Games Menu',menu=gmenu)

root.config(bg='#1aab3c',menu=menubar)

root.title('The Quarantine GameHub')


mainlabel = Label(root,text='The Quarantine GameHub',justify='center',relief='groove',font=('Copperplate Gothic Bold','44'),bg='#00c72f')
mainlabel.grid(row=0,column=1)
label = Label(root,text='\t\t\t\t\tOne-Stop Boredom Beater\t\t\t\t\t',justify='center',relief='groove',font=('Fixedsys','10'),bg='#d6c102')
label.grid(row=1,column=1)
enter = Label(root,text='',justify='center',relief='flat',font=('Fixedsys','10'),bg='#1aab3c')
enter.grid(row=2,column=1)
enter1 = Label(root,text='',justify='center',relief='flat',font=('Fixedsys','10'),bg='#1aab3c')
enter1.grid(row=3,column=1)
gamelabel = Label(root,text='GAMES',justify='center',relief='raised',font=('Fixedsys','20'),bg='#05f3ff')
gamelabel.grid(row=4,column=1)
enter2 = Label(root,text='',justify='center',relief='flat',font=('Fixedsys','10'),bg='#1aab3c')
enter2.grid(row=5,column=1)

buttonframe = Frame(root)

button1 = Button(buttonframe,text='TIC-TAC-TOE',justify='center',relief='raised',font=('Fixedsys','10'),bg='#d6c102',activebackground='#05f3ff',height=7,width=25,activeforeground='#1aab3c',command=tictactoe)
button1.grid(row=0,column=0)
button1 = Button(buttonframe,text='ROCK-PAPER-SCISSORS',justify='center',relief='raised',font=('Fixedsys','8'),bg='#d6c102',activebackground='#05f3ff',height=7,width=25,activeforeground='#1aab3c',command=rps)
button1.grid(row=0,column=1)
button1 = Button(buttonframe,text='WORDLE',justify='center',relief='raised',font=('Fixedsys','7'),bg='#d6c102',activebackground='#05f3ff',height=7,width=25,activeforeground='#1aab3c',command=wordle)
button1.grid(row=1,column=0)
button1 = Button(buttonframe,text='BATTLESHIPS',justify='center',relief='raised',font=('Fixedsys','10'),bg='#d6c102',activebackground='#05f3ff',height=7,width=25,activeforeground='#1aab3c',command=battleship)
button1.grid(row=1,column=1)

buttonframe.grid(row=6,column=1)

button1 = Button(root,text='NUMBER OF TIMES PLAYED',justify='center',relief='raised',font=('Fixedsys','10'),bg='#d6c102',activebackground='#05f3ff',height=2,width=52,activeforeground='#1aab3c',command=playcountpage)
button1.grid(row=7,column=1)




root.mainloop()




