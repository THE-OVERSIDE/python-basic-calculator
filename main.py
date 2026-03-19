# BASIC CALCULATOR 

#Importing customtkinter module
from customtkinter import CTk

#Creating the main class for the calculator
class BasicCalculator():
    
    #Defining the constructor for the class
    def __init__(self):
        
        #Window configuration
        self.window = CTk()
        self.window.title("Basic Calculator")
        self.window.geometry("400x500")
        self.window.resizable(False, False)
        
        #Starting the main loop of the window
        self.window.mainloop()


#Running the calculator
app = BasicCalculator()