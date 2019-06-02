
from tkinter import *
window = Tk()
window.title('LOGIN')
window.geometry('316x393')



header_label = Label(window, text='TIC-TAC-TOE', font=('Impact',20,'bold'),width=17)
header_label.grid(row=0,columnspan=3)


counter = 0
def game(button):
    global counter
    counter += 1
    if button['text'] == '':
        
        if counter%2 == 0:
            button['text'] = '0'
        else:
            button['text'] = 'x'
            
    # condition 1
    if button_1['text']=='0' and button_2['text']=='0' and button_3['text']=='0':
        winner_label.configure(text='PLAYER WITH 0 IS WINNER', fg='GREEN')
     # condition 2
    elif button_1['text']=='x' and button_2['text']=='x' and button_3['text']=='x':
        winner_label.configure(text='PLAYER WITH X IS WINNER', fg='GREEN')
  # condition 3
    elif button_4['text']=='0' and button_5['text']=='0' and button_6['text']=='0':
        winner_label.configure(text='PLAYER WITH 0 IS WINNER', fg='GREEN')
 # condition 4
    elif button_4['text']=='x' and button_5['text']=='x' and button_6['text']=='x':
        winner_label.configure(text='PLAYER WITH X IS WINNER', fg='GREEN')
 # condition 5
    elif button_7['text']=='0' and button_8['text']=='0' and button_9['text']=='0':
        winner_label.configure(text='PLAYER WITH 0 IS WINNER', fg='GREEN')
 # condition 6
    elif button_7['text']=='x' and button_8['text']=='x' and button_9['text']=='x':
        winner_label.configure(text='PLAYER WITH X IS WINNER', fg='GREEN')
 # condition 7
    elif button_1['text']=='0' and button_4['text']=='0' and button_7['text']=='0':
        winner_label.configure(text='PLAYER WITH 0 IS WINNER', fg='GREEN')
 # condition 8
    elif button_1['text']=='x' and button_4['text']=='x' and button_7['text']=='x':
        winner_label.configure(text='PLAYER WITH x IS WINNER', fg='GREEN')
 # condition 9
    elif button_2['text']=='0' and button_5['text']=='0' and button_8['text']=='0':
        winner_label.configure(text='PLAYER WITH 0 IS WINNER', fg='GREEN')
 # condition 10
    elif button_2['text']=='x' and button_5['text']=='x' and button_8['text']=='x':
        winner_label.configure(text='PLAYER WITH X IS WINNER', fg='GREEN')
 # condition 11
    elif button_3['text']=='0' and button_6['text']=='0' and button_9['text']=='0':
        winner_label.configure(text='PLAYER WITH 0 IS WINNER', fg='GREEN')
 # condition 12
    elif button_3['text']=='x' and button_6['text']=='x' and button_9['text']=='x':
        winner_label.configure(text='PLAYER WITH X IS WINNER', fg='GREEN')
 # condition 13
    elif button_1['text']=='0' and button_5['text']=='0' and button_9['text']=='0':
        winner_label.configure(text='PLAYER WITH 0 IS WINNER', fg='GREEN')
 # condition 14
    elif button_1['text']=='x' and button_5['text']=='x' and button_9['text']=='x':
        winner_label.configure(text='PLAYER WITH X IS WINNER', fg='GREEN')
 # condition 15
    elif button_7['text']=='0' and button_5['text']=='0' and button_3['text']=='0':
        winner_label.configure(text='PLAYER WITH 0 IS WINNER', fg='GREEN')
 # condition 16
    elif button_7['text']=='x' and button_5['text']=='x' and button_3['text']=='x':
        winner_label.configure(text='PLAYER WITH X IS WINNER', fg='GREEN')
 # condition 17
    elif button_1['text'] != '' and button_2['text'] != '' and button_3['text'] != '' and button_4['text'] != '' and button_5['text'] != '' and button_6['text'] != '' and button_7['text'] != '' and button_8['text'] != '' and button_9['text'] != ''  :
        winner_label.configure(text='GAME IS DRAW', fg='GREEN')
        

        
        

    
        


button_1 = Button(window,text='', width=10,height=4, command=lambda: game(button_1),font=('arial black',10,'bold'),bd=5,bg='grey')
button_1.grid(row=1,column=0)

button_2 = Button(window,text='', width=10,height=4, command=lambda: game(button_2),bd=5,font=('arial black',10,'bold'))
button_2.grid(row=1,column=1)

button_3 = Button(window,text='', width=10,height=4, command=lambda: game(button_3),bd=5,bg='grey',font=('arial black',10,'bold'))
button_3.grid(row=1,column=2)

button_4 = Button(window,text='', width=10,height=4, command=lambda: game(button_4),bd=5,font=('arial black',10,'bold'))
button_4.grid(row=2,column=0)

button_5 = Button(window,text='', width=10,height=4, command=lambda: game(button_5),bd=5,bg='grey',font=('arial black',10,'bold'))
button_5.grid(row=2,column=1)

button_6 = Button(window,text='', width=10,height=4, command=lambda: game(button_6),bd=5,font=('arial black',10,'bold'))
button_6.grid(row=2,column=2)

button_7 = Button(window,text='', width=10,height=4, command=lambda: game(button_7),bd=5,bg='grey',font=('arial black',10,'bold'))
button_7.grid(row=3,column=0)

button_8 = Button(window,text='', width=10,height=4, command=lambda: game(button_8),bd=5,font=('arial black',10,'bold'))
button_8.grid(row=3,column=1)

button_9 = Button(window,text='', width=10,height=4, command=lambda: game(button_9),bd=5,bg='grey',font=('arial black',10,'bold'))
button_9.grid(row=3,column=2)

winner_label = Label(window, text='',font=('Franklin Gothic Medium',18))
winner_label.grid(row=4,columnspan=3)

def reset():
    button_1.configure(text='')
    button_2.configure(text='')
    button_3.configure(text='')
    button_4.configure(text='')
    button_5.configure(text='')
    button_6.configure(text='')
    button_7.configure(text='')
    button_8.configure(text='')
    button_9.configure(text='')
    winner_label.configure(text='')

reset_button = Button(window, text='RESET',font=('Franklin Gothic Medium',11), command = reset,bd=5,bg='grey')
reset_button.grid(row=5,columnspan=3)
                                        
window.mainloop()
