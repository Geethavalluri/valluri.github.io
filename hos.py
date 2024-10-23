from tkinter import*
from tkinter import ttk
import random 
import tkinter.messagebox
import mysql.connector


class HospitalManagementSystem:
     def _init_(self,root):
          self.root=root
          self.root.title("Hospital Management System")
          self.root.geometry("1550x800+0+0")

         
          
          

root=Tk()
obj=HospitalManagementSystem(root)
root.mainloop()