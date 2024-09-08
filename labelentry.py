from tkinter import*
tk = Tk()
tk.geometry("400x300")
tk.title("Login Page")

tk.config(background="grey")

user_name = Label(tk,text="Username").place(x=40,y=50)
user_entry=Entry(tk,width=30).place(x=100,y=50)

password = Label(tk,text="Password").place(x=40,y=80)
password_entry=Entry(tk,show="*",width=30).place(x=100,y=80)
tk.mainloop()