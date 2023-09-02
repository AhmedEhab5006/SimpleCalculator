from tkinter import *
## creating the variable where the mathmatical expression will be stored
expression = ''
## Creating the app
root = Tk()
root.geometry("529x691")
root.title("Simple Calculator")
## making app"s window unresizable
root.resizable(False,False)
## Creating App's icon
root.iconbitmap('E:\\FCAIH\\Calculator Project\\Images\\favicon.ico')
bg=PhotoImage(file="E:\\FCAIH\\Calculator Project\\Images\\WhatsApp Image 2023-09-01 at 5.14.31 AM (1).png")
## creating the background
back_label=Label(root, image=bg)
## Creating a label for screen
screen_label=Label(borderwidth=0,font="LiquidCrystal 50",fg="black",bg="#9CAD7D",text="")
screen_label.place(x=30,y=91)
## Creating button's pressing function :
def press (num) :
    global expression
    expression = expression + str(num)
    equation.set(expression)
    screen_label["text"]=expression
## Creating equal button's function to calculate evaluate the mathmatical expression that's entered by user
def equal ():
    global expression
    try:
     expression=str(eval(expression))
     equation.set(expression)
     screen_label["text"]=expression
     expression = ""
    except:
     equation.set("Error")
     screen_label["text"]="Error"
## Creating the function which clears the expression
def clear ():
    global expression
    expression = ""
    screen_label["text"]=expression
## creating the variable where the equation will be stored and calculated
equation = StringVar()
## Creating number's buttons
zero_img=PhotoImage(file="E:\\FCAIH\\Calculator Project\\Buttons\\0.png")
zero_button=Button(image=zero_img,command=lambda : press(0),borderwidth=0)
zero_button.place(x=22,y=590)
one_img=PhotoImage(file="E:\\FCAIH\\Calculator Project\\Buttons\\1.png")
one_button=Button(image=one_img,command=lambda : press(1),borderwidth=0)
one_button.place(x=26,y=499)
two_img=PhotoImage(file="E:\\FCAIH\\Calculator Project\\Buttons\\2.png")
two_button=Button(image=two_img,command=lambda : press(2),borderwidth=0)
two_button.place(x=146,y=499)
three_img=PhotoImage(file="E:\\FCAIH\\Calculator Project\\Buttons\\3.png")
three_button=Button(image=three_img,command=lambda : press(3),borderwidth=-0)
three_button.place(x=270,y=499)
four_img=PhotoImage(file="E:\\FCAIH\\Calculator Project\\Buttons\\4.png")
four_button=Button(image=four_img,command=lambda : press(4),borderwidth=0)
four_button.place(x=23,y=402)
five_img=PhotoImage(file="E:\\FCAIH\\Calculator Project\\Buttons\\5.png")
five_button=Button(image=five_img,command=lambda : press(5),borderwidth=0)
five_button.place(x=145,y=402)
six_img=PhotoImage(file="E:\\FCAIH\\Calculator Project\\Buttons\\6.png")
six_button=Button(image=six_img,command=lambda : press(6),borderwidth=0)
six_button.place(x=268,y=402)
seven_img=PhotoImage(file="E:\\FCAIH\\Calculator Project\\Buttons\\7.png")
seven_button=Button(image=seven_img,command=lambda : press(7),borderwidth=0)
seven_button.place(x=25,y=313)
eight_img=PhotoImage(file="E:\\FCAIH\\Calculator Project\\Buttons\\8.png")
eight_button=Button(image=eight_img,command=lambda : press(8),borderwidth=0)
eight_button.place(x=146,y=313)
nine_img=PhotoImage(file="E:\\FCAIH\\Calculator Project\\Buttons\\9.png")
nine_button=Button(image=nine_img,command=lambda : press(9),borderwidth=0)
nine_button.place(x=270,y=313)
dot_img=PhotoImage(file="E:\\FCAIH\\Calculator Project\\Buttons\\..png")
dot_button=Button(image=dot_img,command=lambda : press("."),borderwidth=0)
dot_button.place(x=270,y=590)
## Creating opreator's buttons
equal_img=PhotoImage(file="E:\\FCAIH\\Calculator Project\\Buttons\\=.png")
equal_button=Button(image=equal_img,command=equal,borderwidth=0)
equal_button.place(x=389,y=495)
plus_img=PhotoImage(file="E:\\FCAIH\\Calculator Project\\Buttons\\+.png")
plus_button=Button(image=plus_img,command=lambda : press("+"),borderwidth=0)
plus_button.place(x=389,y=404)
minus_img=PhotoImage(file="E:\\FCAIH\\Calculator Project\\Buttons\\-.png")
minus_button=Button(image=minus_img,command=lambda : press("-"),borderwidth=0)
minus_button.place(x=390,y=313)
times_img=PhotoImage(file="E:\\FCAIH\\Calculator Project\\Buttons\\x.png")
times_button=Button(image=times_img,command=lambda : press("*"),borderwidth=0)
times_button.place(x=389,y=220)
divison_img=PhotoImage(file="E:\\FCAIH\\Calculator Project\\Buttons\\D.png")
divison_button=Button(image=divison_img,command=lambda : press("/"),borderwidth=0)
divison_button.place(x=269,y=220)
## Other buttons
M_plus_img=PhotoImage(file="E:\\FCAIH\\Calculator Project\\Buttons\\M+.png")
M_plus_button=Button(image=M_plus_img,command=lambda : press("M+"),borderwidth=0)
M_plus_button.place(x=144,y=220)
MC_img=PhotoImage(file="E:\\FCAIH\\Calculator Project\\Buttons\\MC.png")
MC_button=Button(image=MC_img,command= clear ,borderwidth=0)
MC_button.place(x=25,y=220)
back_label.pack()
root.mainloop()