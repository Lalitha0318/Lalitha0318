import tkinter as tk
calculation=""

def add_to_calculation(symbol):
    global calculation
    calculation +=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def backspace():
    global calculation
    calculation = calculation[:-1]
    evaluate_calculation()

def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_feild()
        text_result.insert(1.0,"Error")

def clear_feild():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")


root=tk.Tk()
root.geometry("300x275")
root.title("Jagan's calculator")
text_result=tk.Text(root,height=2,width=16,font=("Helvetica",24),bg="white", fg="black")
text_result.grid(columnspan=5)

btn_9=tk.Button(root,text="9",command=lambda:add_to_calculation(9),width=5,font=("Arial",14),bg="lightgray")
btn_9.grid(row=2,column=1)
btn_8=tk.Button(root,text="8",command=lambda:add_to_calculation(8),width=5,font=("Arial",14),bg="lightgray")
btn_8.grid(row=2,column=2)
btn_7=tk.Button(root,text="7",command=lambda:add_to_calculation(7),width=5,font=("Arial",14),bg="lightgray")
btn_7.grid(row=2,column=3)
btn_6=tk.Button(root,text="6",command=lambda:add_to_calculation(6),width=5,font=("Arial",14),bg="lightgray")
btn_6.grid(row=3,column=1)
btn_5=tk.Button(root,text="5",command=lambda:add_to_calculation(5),width=5,font=("Arial",14),bg="lightgray")
btn_5.grid(row=3,column=2)
btn_4=tk.Button(root,text="4",command=lambda:add_to_calculation(4),width=5,font=("Arial",14),bg="lightgray")
btn_4.grid(row=3,column=3)
btn_3=tk.Button(root,text="3",command=lambda:add_to_calculation(3),width=5,font=("Arial",14),bg="lightgray")
btn_3.grid(row=4,column=1)
btn_2=tk.Button(root,text="2",command=lambda:add_to_calculation(2),width=5,font=("Arial",14),bg="lightgray")
btn_2.grid(row=4,column=2)
btn_1=tk.Button(root,text="1",command=lambda:add_to_calculation(1),width=5,font=("Arial",14),bg="lightgray")
btn_1.grid(row=4,column=3)

btn_0=tk.Button(root,text="0",command=lambda:add_to_calculation(0),width=5,font=("Arial",14),bg="lightgray")
btn_0.grid(row=5,column=1)

btn_plus=tk.Button(root,text="+",command=lambda:add_to_calculation("+"),width=5,font=("Arial",14),bg="lightgray")
btn_plus.grid(row=2,column=4)

btn_sub=tk.Button(root,text="-",command=lambda:add_to_calculation("-"),width=5,font=("Arial",14),bg="lightgray")
btn_sub.grid(row=3,column=4)

btn_mul=tk.Button(root,text="*",command=lambda:add_to_calculation("*"),width=5,font=("Arial",14),bg="lightgray")
btn_mul.grid(row=4,column=4)

btn_div=tk.Button(root,text="/",command=lambda:add_to_calculation("/"),width=5,font=("Arial",14),bg="lightgray")
btn_div.grid(row=5,column=4)

btn_open=tk.Button(root,text="(",command=lambda:add_to_calculation("("),width=5,font=("Arial",14),bg="lightgray")
btn_open.grid(row=5,column=2)

btn_close=tk.Button(root,text=")",command=lambda:add_to_calculation(")"),width=5,font=("Arial",14),bg="lightgray")
btn_close.grid(row=5,column=3)

btn_00=tk.Button(root,text="00",command=lambda:add_to_calculation("00"),width=5,font=("Arial",14),bg="lightgray")
btn_00.grid(row=6,column=1)

btn_clear=tk.Button(root,text="DEL",command=backspace,width=5,font=("Helvetica",14),bg="lightgray")
btn_clear.grid(row=6,column=2)

btn_clear=tk.Button(root,text="AC",command=clear_feild,width=5,font=("Helvetica",14),bg="lightgray")
btn_clear.grid(row=6,column=3)

btn_equals=tk.Button(root,text="=",command=evaluate_calculation,width=5,font=("Arial",14),bg="lightgray")
btn_equals.grid(row=6,column=4)

root.mainloop()