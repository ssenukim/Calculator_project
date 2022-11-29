#%%
import tkinter as t
#%%
window = None 
display_label = None 
expression = ''


def press(num):
    global expression
    expression = expression + str(num)
    display_label['text'] = expression

def setup_GUI():
    global window 
    global display_label
    
    window = t.Tk()
    window.title('뉴 계산기')
    
    display_label = t.Label(window, textvariable='', anchor='c', relief=t.GROOVE, width=15, font='Arial 20')
    display_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    btn1 = t.Button(window, text='1', width=5, height=2, font='Arial 15')
    btn2 = t.Button(window, text='2', width=5, height=2, font='Arial 15')
    btn3 = t.Button(window, text='3', width=5, height=2, font='Arial 15')
    btn4 = t.Button(window, text='4', width=5, height=2, font='Arial 15')
    btn5 = t.Button(window, text='5', width=5, height=2, font='Arial 15')
    btn6 = t.Button(window, text='6', width=5, height=2, font='Arial 15')
    btn7 = t.Button(window, text='7', width=5, height=2, font='Arial 15')
    btn8 = t.Button(window, text='8', width=5, height=2, font='Arial 15')
    btn9 = t.Button(window, text='9', width=5, height=2, font='Arial 15')
    btn0 = t.Button(window, text='0', width=5, height=2, font='Arial 15')
    btn1.grid(row=1, column=0)
    btn2.grid(row=1, column=1)
    btn3.grid(row=1, column=2)
    btn4.grid(row=2, column=0)
    btn5.grid(row=2, column=1)
    btn6.grid(row=2, column=2)
    btn7.grid(row=3, column=0)
    btn8.grid(row=3, column=1)
    btn9.grid(row=3, column=2)
    btn0.grid(row=4, column=1)
    
    clearBtn = t.Button(window, text='C', width=5, height=2, font='Arial 15' )
    resultBtn = t.Button(window, text='=', width=5, height=2, font='Arial 15')
    addBtn = t.Button(window, text='+', width=5, height=2, font='Arial 15')
    subBtn = t.Button(window, text='-', width=5, height=2, font='Arial 15')
    mulBtn = t.Button(window, text='*', width=5, height=2, font='Arial 15')
    divBtn = t.Button(window, text='/', width=5, height=2, font='Arial 15')
    clearBtn.grid(row=4, column=0)
    resultBtn.grid(row=4, column=2)
    addBtn.grid(row=1, column=3)
    subBtn.grid(row=2, column=3)
    mulBtn.grid(row=3, column=3)
    divBtn.grid(row=4, column=3)

    
setup_GUI()
window.mainloop()