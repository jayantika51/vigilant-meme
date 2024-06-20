from tkinter import *
import random
root=Tk
root.geometry("900x500")

dictionary={'colour':['maroon1','lawn green','magenta2','purple1','springgreen2','chocolate1', 'deep pink','cyan']}

def randombg():
    color_list = dictionary['colour']
    random_no = random.randint(0,8)
    random_color=dictionary['colour'][random_no]
    print("random color picked:{random_color}")
    root.configure(background=random_color)
    
    
btn = Button(root, text="Change Background Color", command=randombg)
btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  

root.mainloop()  