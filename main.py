# BASIC CALCULATOR 

from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry

color_palette = {
    "background": "#414141",
    "frame": "#636363",
    "number_buttons": "#525252",
    "opperator_buttons": "#414141",
    "text": "#ffffff",
    "display": "#767676",
    "button_hover_color": "#5c5c5c",
    "text_button_color": "#A1A0A0"}


letter_fonts = {
    "display_font": ("Arial", 30),
    "button_font": ("Arial", 40)}


#Creating the main class for the calculator
class BasicCalculator():
    def __init__(self):
        
        #Window configuration
        self.window = CTk(fg_color=color_palette["background"])
        self.window.title("Basic Calculator")
        self.window.geometry("600x700")
        self.window.resizable(False, False)
        
        self.interface()
        
        #Starting the main loop of the window
        self.window.mainloop()
        

    def interface(self):
        self.principal_frame = CTkFrame(self.window,
                                        fg_color=color_palette["frame"],
                                        width=550,
                                        height=650,
                                        corner_radius=30)
  
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
                                      text="+", fg_color=color_palette["opperator_buttons"],
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
                                         text="-", fg_color=color_palette["opperator_buttons"],
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
                                            text="X", fg_color=color_palette["opperator_buttons"],
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
                                      text="CE", fg_color=color_palette["opperator_buttons"],
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
                                    text="=", fg_color=color_palette["opperator_buttons"],
                                    text_color=color_palette["text_button_color"],
                                    width=100,
                                    height=100,
                                    corner_radius=10,
                                    font=letter_fonts["button_font"],
                                    hover_color=color_palette["button_hover_color"],
                                    command=self.equals_button_click)

        self.btn_division = CTkButton(self.principal_frame,
                                        text="/", fg_color=color_palette["opperator_buttons"],
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
        
        #Input regulator of opperations
        self.allow_operation = False
        
    def number_button_click(self, number):
        actual_text_display = self.display.get()
        new_text_display = actual_text_display + number
        self.change_display_text(new_text_display)
        
    def operator_button_click(self, operator):
        match operator:
            case "addition":
                operator_symbol = "+"
            case "subtraction":
                operator_symbol = "-"
            case "multiplication":
                operator_symbol = "*"
            case "division":
                operator_symbol = "/"
        
        actual_text_display = self.display.get()
        
        if actual_text_display[-1] in ["+", "-", "*", "/"]:
            self.allow_operation = False
            
        else:
            self.allow_operation = True
        
        if self.allow_operation:
            new_text_display = actual_text_display + operator_symbol
            self.change_display_text(new_text_display)
        
    def equals_button_click(self):
        actual_text_display = self.display.get()
        try:
            result = eval(actual_text_display)
            self.change_display_text(str(result))
        except ZeroDivisionError:
            self.change_display_text("Zero Division Error")
            self.change_state_of_all_buttons_without_CE("disabled")
        except Exception:
            self.change_display_text("Error")
            self.change_state_of_all_buttons_without_CE("disabled")

    def clear_entry_button_click(self):
        self.display.configure(state="normal")
        self.display.delete(0, "end")
        self.display.configure(state="disabled")
        self.change_state_of_all_buttons_without_CE("normal")
    
    def change_display_text(self, new_text):
        self.display.configure(state="normal")
        self.display.delete(0, "end")
        self.display.insert(0, new_text)
        self.display.configure(state="disabled")
    
    def change_state_of_all_buttons_without_CE(self, state):
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
        
        for button in all_buttons_without_CE:
            button.configure(state=state)
            
            
#Running the calculator
app = BasicCalculator()