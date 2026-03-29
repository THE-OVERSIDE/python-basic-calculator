##########################
# BASIC CALCULATOR v.1.1 #
##########################

from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry

#Color palette configuration
color_palette = {
    "background": "#414141",
    "frame": "#636363",
    "number_buttons": "#525252",
    "operator_buttons": "#414141",
    "text": "#ffffff",
    "display": "#767676",
    "button_hover_color": "#5c5c5c",
    "text_button_color": "#A1A0A0"}

#Font configuration
letter_fonts = {
    "display_font": ("Arial", 50),
    "button_font": ("Arial", 40)}

#Main class
class BasicCalculator():
    """
    This class creates the interface of the calculator and contains all the functions to make it work.
    
    Methods:
    - __init__: Initializes the window and calls the interface method.
    - interface: Creates the interface of the calculator.
    - number_button_click: Function that is called when a number button is clicked. It adds the number to the display.
    - operator_button_click: Function that is called when an operator button is clicked. It adds the operator to the display.
    - equals_button_click: Function that is called when the equals button is clicked. It evaluates the expression in the display and shows the result.
    - clear_entry_button_click: Function that is called when the clear entry button is clicked. It clears the display and enables all the buttons.
    - change_display_text: Function that changes the text in the display.
    - change_state_of_all_buttons_without_CE: Function that changes the state of all the buttons except the clear entry button.
    
    This class doesn't need any parameters to be initialized."""
    
    #Initializes the window and calls the interface method.
    def __init__(self):
        
        #Window configuration
        self.window = CTk(fg_color=color_palette["background"])
        self.window.title("Basic Calculator - V.1.1.2")
        self.window.geometry("600x700")
        self.window.resizable(False, False)
        
        #Creating the interface of the calculator
        self.interface()
        
        #Starting the main loop of the window
        self.window.mainloop()
        
    #Interface method (Front end)
    def interface(self):
        
        #This frame contains all the elements of the calculator (display and buttons)
        self.principal_frame = CTkFrame(self.window,
                                        fg_color=color_palette["frame"],
                                        width=550,
                                        height=650,
                                        corner_radius=30)

        #This is the display of the calculator, it is a disabled entry that shows the numbers and the result of the operations.
        self.display = CTkEntry(self.principal_frame,
                                   fg_color=color_palette["display"],
                                   text_color=color_palette["text"],
                                   width=500,
                                   height=100,
                                   corner_radius=10,
                                   border_width=0,
                                   font=letter_fonts["display_font"],
                                   state="disabled")
        
        self.principal_frame.place(x=25, y=25)
        self.display.place(x=25, y=25)
        
        
        #Creating the buttons for the numbers and the operations
        
        #ROW 1 ------------------------------------------------------------------
        self.btn_number_7 = CTkButton(self.principal_frame,
                                      text="7", fg_color=color_palette["number_buttons"],
                                      text_color=color_palette["text_button_color"],
                                      width=100,
                                      height=100,
                                      corner_radius=10,
                                      font=letter_fonts["button_font"],
                                      hover_color=color_palette["button_hover_color"],
                                      command=lambda:self.number_button_click("7"))
        
        self.btn_number_8 = CTkButton(self.principal_frame,
                                      text="8", fg_color=color_palette["number_buttons"],
                                      text_color=color_palette["text_button_color"],
                                      width=100,
                                      height=100,
                                      corner_radius=10,
                                      font=letter_fonts["button_font"],
                                      hover_color=color_palette["button_hover_color"],
                                      command=lambda:self.number_button_click("8"))
        
        self.btn_number_9 = CTkButton(self.principal_frame,
                                      text="9", fg_color=color_palette["number_buttons"],
                                      text_color=color_palette["text_button_color"],
                                      width=100,
                                      height=100,
                                      corner_radius=10,
                                      font=letter_fonts["button_font"],
                                      hover_color=color_palette["button_hover_color"],
                                      command=lambda:self.number_button_click("9"))
          
        self.btn_addition = CTkButton(self.principal_frame,
                                      text="+", fg_color=color_palette["operator_buttons"],
                                      text_color=color_palette["text_button_color"],
                                      width=100,
                                      height=100,
                                      corner_radius=10,
                                      font=letter_fonts["button_font"],
                                      hover_color=color_palette["button_hover_color"],
                                      command=lambda:self.operator_button_click("addition"))
        
        self.btn_number_7.place(x=25, y=150)
        self.btn_number_8.place(x=150, y=150)
        self.btn_number_9.place(x=275, y=150)
        self.btn_addition.place(x=425, y=150)
        
        #ROW 2 ------------------------------------------------------------------
        self.btn_number_4 = CTkButton(self.principal_frame,
                                      text="4", fg_color=color_palette["number_buttons"],
                                      text_color=color_palette["text_button_color"],
                                      width=100,
                                      height=100,
                                      corner_radius=10,
                                      font=letter_fonts["button_font"],
                                      hover_color=color_palette["button_hover_color"],
                                      command=lambda:self.number_button_click("4"))

        self.btn_number_5 = CTkButton(self.principal_frame,
                                      text="5", fg_color=color_palette["number_buttons"],
                                      text_color=color_palette["text_button_color"],
                                      width=100,
                                      height=100,
                                      corner_radius=10,
                                      font=letter_fonts["button_font"],
                                      hover_color=color_palette["button_hover_color"],
                                      command=lambda:self.number_button_click("5"))
        
        self.btn_number_6 = CTkButton(self.principal_frame,
                                      text="6", fg_color=color_palette["number_buttons"],
                                      text_color=color_palette["text_button_color"],
                                      width=100,
                                      height=100,
                                      corner_radius=10,
                                      font=letter_fonts["button_font"],
                                      hover_color=color_palette["button_hover_color"],
                                      command=lambda:self.number_button_click("6"))

        self.btn_subtraction = CTkButton(self.principal_frame,
                                         text="-", fg_color=color_palette["operator_buttons"],
                                         text_color=color_palette["text_button_color"],
                                         width=100,
                                         height=100,
                                         corner_radius=10,
                                         font=letter_fonts["button_font"],
                                         hover_color=color_palette["button_hover_color"],
                                         command=lambda:self.operator_button_click("subtraction"))
        
        self.btn_number_4.place(x=25, y=275)
        self.btn_number_5.place(x=150, y=275)
        self.btn_number_6.place(x=275, y=275)
        self.btn_subtraction.place(x=425, y=275)
        
        #ROW 3 ------------------------------------------------------------------
        self.btn_number_1 = CTkButton(self.principal_frame,
                                      text="1", fg_color=color_palette["number_buttons"],
                                      text_color=color_palette["text_button_color"],
                                      width=100,
                                      height=100,
                                      corner_radius=10,
                                      font=letter_fonts["button_font"],
                                      hover_color=color_palette["button_hover_color"],
                                      command=lambda:self.number_button_click("1"))

        self.btn_number_2 = CTkButton(self.principal_frame,
                                      text="2", fg_color=color_palette["number_buttons"],
                                      text_color=color_palette["text_button_color"],
                                      width=100,
                                      height=100,
                                      corner_radius=10,
                                      font=letter_fonts["button_font"],
                                      hover_color=color_palette["button_hover_color"],
                                      command=lambda:self.number_button_click("2"))
    
        self.btn_number_3 = CTkButton(self.principal_frame,
                                        text="3", fg_color=color_palette["number_buttons"],
                                        text_color=color_palette["text_button_color"],
                                        width=100,
                                        height=100,
                                        corner_radius=10,
                                        font=letter_fonts["button_font"],
                                        hover_color=color_palette["button_hover_color"],
                                        command=lambda:self.number_button_click("3"))
        
        self.btn_multiplication = CTkButton(self.principal_frame,
                                            text="X", fg_color=color_palette["operator_buttons"],
                                            text_color=color_palette["text_button_color"],
                                            width=100,
                                            height=100,
                                            corner_radius=10,
                                            font=letter_fonts["button_font"],
                                            hover_color=color_palette["button_hover_color"],
                                            command=lambda:self.operator_button_click("multiplication"))
        
        self.btn_number_1.place(x=25, y=400)
        self.btn_number_2.place(x=150, y=400)
        self.btn_number_3.place(x=275, y=400)
        self.btn_multiplication.place(x=425, y=400)
        
        #ROW 4 ------------------------------------------------------------------
        self.btn_clear_entry = CTkButton(self.principal_frame,
                                      text="CE", fg_color=color_palette["operator_buttons"],
                                      text_color=color_palette["text_button_color"],
                                      width=100,
                                      height=100,
                                      corner_radius=10,
                                      font=letter_fonts["button_font"],
                                      hover_color=color_palette["button_hover_color"],
                                      command=self.clear_entry_button_click)

        self.btn_number_0 = CTkButton(self.principal_frame,
                                        text="0", fg_color=color_palette["number_buttons"],
                                        text_color=color_palette["text_button_color"],
                                        width=100,
                                        height=100,
                                        corner_radius=10,
                                        font=letter_fonts["button_font"],
                                        hover_color=color_palette["button_hover_color"],
                                        command=lambda:self.number_button_click("0"))

        self.btn_equals = CTkButton(self.principal_frame,
                                    text="=", fg_color=color_palette["operator_buttons"],
                                    text_color=color_palette["text_button_color"],
                                    width=100,
                                    height=100,
                                    corner_radius=10,
                                    font=letter_fonts["button_font"],
                                    hover_color=color_palette["button_hover_color"],
                                    command=self.equals_button_click)

        self.btn_division = CTkButton(self.principal_frame,
                                        text="/", fg_color=color_palette["operator_buttons"],
                                        text_color=color_palette["text_button_color"],
                                        width=100,
                                        height=100,
                                        corner_radius=10,
                                        font=letter_fonts["button_font"],
                                        hover_color=color_palette["button_hover_color"],
                                        command=lambda: self.operator_button_click("division"))
        
        self.btn_clear_entry.place(x=25, y=525)
        self.btn_number_0.place(x=150, y=525)
        self.btn_equals.place(x=275, y=525)
        self.btn_division.place(x=425, y=525)
        
        #?: Operation Controller
        
        self.allow_operation = False #This variable controls if an operation can be performed
        
        
    def number_button_click(self, number):
        """
        This function is called when a number button is clicked. It adds the number to the display.
        
        Parameters:
            number (str): The number to be added to the display."""
        
        #Getting the actual text in the display and adding the new number to it.
        actual_text_display = self.display.get()
        new_text_display = actual_text_display + number
        self.change_display_text(new_text_display)
        
    def operator_button_click(self, operator):
        """
        This function is called when an operator button is clicked. It adds the operator to the display.
        
        Parameters:
            operator (str): The operator to be added to the display. It can be "addition", "subtraction", "multiplication" or "division"."""
            
        
        #This match determines the symbol of the operator to be added to the display.
        match operator:
            case "addition":
                operator_symbol = "+"
            case "subtraction":
                operator_symbol = "-"
            case "multiplication":
                operator_symbol = "*"
            case "division":
                operator_symbol = "/"
        
        #Gets the actual text in the display.
        actual_text_display = self.display.get()
        
        #Checks if an operation is already in the display.
        if actual_text_display[-1] ==  " ":
            self.allow_operation = False
            
        else:
            self.allow_operation = True
        
        #If allow_operation is True, it adds the opperator to the display. 
        if self.allow_operation:
            new_text_display = actual_text_display + " " + operator_symbol + " "
            self.change_display_text(new_text_display)
        
    def equals_button_click(self):
        """
        This function is called when the equals button is clicked. It evaluates the expression in the display and shows the result.
        It also handles the errors that can occur when evaluating the expression, such as division by zero or invalid syntax.      
        Puts the result in the display if the expression is valid, otherwise shows an error message and disables all the buttons except the clear entry button."""
        
        #Gets the actual text in the display.
        actual_text_display = self.display.get()
        
        #Evaluates the opperation in the display, if there is not any error, it shows the result in the display. If there is an error, it shows an error message and disables all the buttons except the clear entry button.
        try:
            result = eval(actual_text_display)
            self.change_display_text(str(result))
        except ZeroDivisionError:
            self.change_display_text("Zero Division Error")
            self.change_state_of_all_buttons_without_CE("disabled")
        except Exception:
            self.change_display_text("Math ERROR")
            self.change_state_of_all_buttons_without_CE("disabled")

    def clear_entry_button_click(self):
        """
        This function is called when the clear entry (CE)button is clicked. It clears the display and enables all the buttons if previously disabled."""
        
        self.display.configure(state="normal")
        self.display.delete(0, "end")
        self.display.configure(state="disabled")
        self.change_state_of_all_buttons_without_CE("normal")
    
    def change_display_text(self, new_text):
        """
        This function changes the text in the display."""
        
        self.display.configure(state="normal")
        self.display.delete(0, "end")
        self.display.insert(0, new_text)
        self.display.configure(state="disabled")
    
    def change_state_of_all_buttons_without_CE(self, state):
        """
        This function changes the state of all the buttons except the clear entry button.
        Specifically, this function is used to disable all the buttons when an error occurs and enable them again when the clear entry button is clicked.
        
        Parameters:
            state (str): The state to be set for the buttons. It can be "normal" or "disabled". """
        
        all_buttons_without_CE = [self.btn_addition,
                                  self.btn_subtraction,
                                  self.btn_multiplication,
                                  self.btn_division,
                                  self.btn_equals,
                                  self.btn_number_0,
                                  self.btn_number_1,
                                  self.btn_number_2,
                                  self.btn_number_3,
                                  self.btn_number_4,
                                  self.btn_number_5,
                                  self.btn_number_6,
                                  self.btn_number_7,
                                  self.btn_number_8,
                                  self.btn_number_9]
        
        #Puts all the buttons in the state specified in the parameter (enabled or disabled).
        for button in all_buttons_without_CE:
            button.configure(state=state)
            
            
#Running the calculator
app = BasicCalculator()
