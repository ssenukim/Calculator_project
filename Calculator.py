import tkinter as t

window = None
display_label = None
expression =''

def replace_str(str, prev, next):
    str_ = str
    cnt = 0
    for i in str_:
        if i==prev:
            print(cnt)
            str_ = str_[:cnt] + next + str_[cnt+1:]
        cnt += 1 
    return str_
                    
def press(num):
    global expression
    expression = expression + str(num)
    display_label['text'] = expression

def press_operator(operator):
    global expression 
    if operator == '+':
        expression = expression + '+'
        display_label['text'] = expression
    elif operator == '-':
        expression = expression + '-'
        display_label['text'] = expression
    elif operator == '*':
        expression = expression + 'x'
        display_label['text'] = expression 
    elif operator == '/':
        expression = expression + '÷'
        display_label['text'] = expression
    elif operator == '.':
        expression = expression + '.'
        display_label['text'] = expression
    elif operator == '**':
        expression = expression + '²'
        display_label['text'] = expression
    elif operator == '%':
        expression = expression + '%'
        display_label['text'] = expression
    elif operator == '<':
        expression = expression[:-1]
        display_label['text'] = expression

def press_clear():
    global expression
    expression = ''
    display_label['text'] = expression

def press_result():
    global expression
    try:
        if 'x' or '÷' or'²' in expression:
            expression = replace_str(expression, 'x', '*')
            expression = replace_str(expression, '÷', '/')
            expression = replace_str(expression, '²', '**2')
    
        result = eval(expression)
        if result % 1 == 0 :
            total = str(int(result))
        else : total = "{:.4f}".format(result)
        display_label['text'] = total
        expression = total
    except:
        expression = 'Error'
        display_label['text'] = expression

def setup_GUI():
    global window
    global display_label
    window = t.Tk()
    window.title('뉴 계산기')
    display_label = t.Label(window, textvariable='', anchor='c', relief=t.GROOVE, width=15, font='Arial 20')
    display_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    btn1 = t.Button(window, text='1', width=5, height=2, font='Arial 15', command=lambda: press(1))
    btn2 = t.Button(window, text='2', width=5, height=2, font='Arial 15', command=lambda: press(2))
    btn3 = t.Button(window, text='3', width=5, height=2, font='Arial 15', command=lambda: press(3))
    btn4 = t.Button(window, text='4', width=5, height=2, font='Arial 15', command=lambda: press(4))
    btn5 = t.Button(window, text='5', width=5, height=2, font='Arial 15', command=lambda: press(5))
    btn6 = t.Button(window, text='6', width=5, height=2, font='Arial 15', command=lambda: press(6))
    btn7 = t.Button(window, text='7', width=5, height=2, font='Arial 15', command=lambda: press(7))
    btn8 = t.Button(window, text='8', width=5, height=2, font='Arial 15', command=lambda: press(8))
    btn9 = t.Button(window, text='9', width=5, height=2, font='Arial 15', command=lambda: press(9))
    btn0 = t.Button(window, text='0', width=5, height=2, font='Arial 15', command=lambda: press(0))
    addBtn = t.Button(window, text='+', fg='red', width=5, height=2, font='Arial 15', command=lambda: press_operator('+'))
    subBtn = t.Button(window, text='-', fg='red', width=5, height=2, font='Arial 15', command=lambda: press_operator('-'))
    mulBtn = t.Button(window, text='*', fg='red', width=5, height=2, font='Arial 15', command=lambda: press_operator('*'))
    divBtn = t.Button(window, text='÷', fg='red', width=5, height=2, font='Arial 15', command=lambda: press_operator('/'))
    float_Btn = t.Button(window, text='.', width=5, height=2, font='Arial 15', command=lambda: press_operator('.'))
    square_Btn = t.Button(window, text='X²', fg='red', width=5, height=2, font='Arial 15', command=lambda: press_operator('**'))
    quotient_Btn = t.Button(window, text='%', fg='red', width=5, height=2, font='Arial 15', command=lambda: press_operator('%')) 
    left_Btn = t.Button(window, text='<', fg='red', width=5, height=2, font='Arial 15', command=lambda: press_operator('<')) 

    btn1.grid(row=2, column=0)
    btn2.grid(row=2, column=1)
    btn3.grid(row=2, column=2)
    btn4.grid(row=3, column=0)
    btn5.grid(row=3, column=1)
    btn6.grid(row=3, column=2)
    btn7.grid(row=4, column=0)
    btn8.grid(row=4, column=1)
    btn9.grid(row=4, column=2)
    btn0.grid(row=5, column=1)
    
    clearBtn = t.Button(window, text='C',fg='red', width=5, height=2, font='Arial 15', command=lambda: press_clear())
    resultBtn = t.Button(window, text='=', width=5, height=2, font='Arial 15', command=lambda: press_result())
    clearBtn.grid(row=1, column=0)
    resultBtn.grid(row=5, column=2)
    addBtn.grid(row=2, column=3)
    subBtn.grid(row=3, column=3)
    mulBtn.grid(row=4, column=3)
    divBtn.grid(row=5, column=3)
    float_Btn.grid(row=5, column=0)
    square_Btn.grid(row=1, column=3)
    quotient_Btn.grid(row=1, column=2)
    left_Btn.grid(row=1, column=1)

setup_GUI()
expression = ''
window.mainloop()