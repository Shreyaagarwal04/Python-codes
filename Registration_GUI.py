#!/usr/bin/env python
# coding: utf-8

# In[11]:


from tkinter import *
from tkinter import messagebox
import re

root = Tk()
root.geometry('500x500')
root.title("Student Accomodation Registration Form")

v_fullname =StringVar()
v_emailId =StringVar()
v_country =StringVar()
v_gender = IntVar()
v_skill =StringVar()
v_skills =StringVar()

#function to validate phone number
#def validate_phoneno(user_phoneno):
 #   if user_phoneno.isdigit():
   #     return True
   # elif user_phoneno is "":
    #    return True
   # else:
    #    messagebox.showinfo('Information', 'Only digits are allowed for phone number')
    #    return False

#function to validate email 
def isValidEmail(user_email):
    if len(user_email) > 7:
        if re.match["^.+@[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$", user_email] != None:
            return True
        else:
            messagebox.showinfo('Information','This is not a valid email id')
            return False
    else:
        messagebox.showinfo('Information','This is not a valid email address')

#function for validation of empty fields
def validateAllFields():
    if v_fullname.get() == "":
        messagebox.showinfo('Information','Please enter fullname to proceed')
    elif v_emailId.get() == "":
        messagebox.showinfo('Information','Please enter Email id to proceed')
    elif v_gender.get() == "":
        messagebox.showinfo('Information','Please enter Gender to proceed')
    elif v_country.get() == "" or v_country.get() =="Select your country":
        messagebox.showinfo('Information','Please enter Country to proceed')
    elif v_skill.get() =="" and v_skills.get() =="":
        messagebox.showinfo('Information','Please enter Skills to proceed')
    elif v_emailId.get() != "":
        status = isValidEmail(v_emailId.get)
        if(status):
            messagebox.showinfo('Information','User Registered Successfully!!')
    else: 
        messagebox.showinfo('Information','User Registered successfully!!')
            
label_0 = Label(root, text="Student Accomodation\n Registration Form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root, textvariable = v_fullname)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root, textvariable = v_emailId)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

Radiobutton(root, text="Male",padx = 5, variable=v_gender, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=v_gender, value=2).place(x=290,y=230)

label_4 = Label(root, text="country",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];
c=StringVar()
droplist=OptionMenu(root,v_country, *list1)
droplist.config(width=15)
c.set('Select your country') 
droplist.place(x=240,y=280)

label_4 = Label(root, text="Skill",width=20,font=("bold", 10))
label_4.place(x=85,y=330)

Checkbutton(root, text="java", variable=v_skill).place(x=235,y=330)

Checkbutton(root, text="python", variable=v_skills).place(x=290,y=330)

Button(root, text='Submit',command = validateAllFields,width=20,bg='brown',fg='white').place(x=180,y=380)

root.mainloop()


# In[ ]:





# In[ ]:




