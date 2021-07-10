# KeyboardPal
# Type out user input automatically after 5 seconds

from tkinter import *
from tkinter import scrolledtext
import pyautogui
import time

### Configuration Options
TYPING_SPEED  = 0.02 # 0.02 feels like a natural typing speed. hence default
NEWLINE_DELAY = 1.2  # additional delay for any newlines, to stop screwups

### EDIT PRESETS HERE
PRESET_1 = """Mary had a little lamb,
It's fleece was white as snow."""
PRESET_1_BTNTXT = "MaryTest"
PRESET_2 = "This button (preset 2) is undefined"
PRESET_2_BTNTXT = "Preset 2"
PRESET_3 = "This button (preset 3) is undefined"
PRESET_3_BTNTXT = "Preset 3"
PRESET_4 = "This button (preset 4) is undefined"
PRESET_4_BTNTXT = "Preset 4"
PRESET_5 = "This button (preset 5) is undefined"
PRESET_5_BTNTXT = "Preset 5"
PRESET_6 = "This button (preset 6) is undefined"
PRESET_6_BTNTXT = "Preset 6"
PRESET_7 = "This button (preset 7) is undefined"
PRESET_7_BTNTXT = "Preset 7"
PRESET_8 = "This button (preset 8) is undefined"
PRESET_8_BTNTXT = "Preset 8"
PRESET_9 = "This button (preset 9) is undefined"
PRESET_9_BTNTXT = "Preset 9"
PRESET_10 = "This button (preset 10) is undefined"
PRESET_10_BTNTXT = "Preset 10"
PRESET_11 = "This button (preset 11) is undefined"
PRESET_11_BTNTXT = "Preset 11"
PRESET_12 = "This button (preset 12) is undefined"
PRESET_12_BTNTXT = "Preset 12"
PRESET_13 = "This button (preset 13) is undefined"
PRESET_13_BTNTXT = "Preset 13"
PRESET_14 = "This button (preset 14) is undefined"
PRESET_14_BTNTXT = "Preset 14"
PRESET_15 = "This button (preset 15) is undefined"
PRESET_15_BTNTXT = "Preset 15"
PRESET_16 = "This button (preset 16) is undefined"
PRESET_16_BTNTXT = "Preset 16"
PRESET_17 = "This button (preset 17) is undefined"
PRESET_17_BTNTXT = "Preset 17"
PRESET_18 = "This button (preset 18) is undefined"
PRESET_18_BTNTXT = "Preset 18"
PRESET_19 = "This button (preset 19) is undefined"
PRESET_19_BTNTXT = "Preset 19"
PRESET_20 = "This button (preset 20) is undefined"
PRESET_20_BTNTXT = "Preset 20"


class Application(Frame):
    """ GUI application that types out user input like a keyboard emulator. """
    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)  
        #self.grid()
        self.grid(row=0, column=0, sticky = "nsew")
        self.create_widgets()

    def create_widgets(self):
        """ Create widgets to get story information and to display story. """
        # create instruction label
        Label(self,
              text = "text to type out:"
              ).grid(row = 1, column = 0, columnspan = 1, sticky = "nsew")


        self.main_txt = scrolledtext.ScrolledText(self, height = 10, wrap = WORD)
        self.main_txt.grid(row = 2, column = 0, columnspan = 3, rowspan = 4, sticky = "nsew")

        
        Button(self,
               text = "Type in 5 Seconds",
               command = self.tiepit
               ).grid(row = 6, column = 0, sticky = "sw")

        Button(self,
               text = "CLEAR",
               command = self.reset
               ).grid(row = 6, column = 2, sticky = "se")


        self.main_txt2 = scrolledtext.ScrolledText(self, height = 10, wrap = WORD)
        self.main_txt2.grid(row = 7, column = 0, columnspan = 3, rowspan = 4, sticky = "nsew")

        
        Button(self,
               text = "Type in 5 Seconds",
               command = self.tiepit2
               ).grid(row = 11, column = 0, sticky = "sw")

        Button(self,
               text = "CLEAR",
               command = self.reset2
               ).grid(row = 11, column = 2, sticky = "se")


        buttons_frame = Frame(self)
        buttons_frame.grid(row=1, column=3, columnspan = 3, rowspan = 10, sticky=N+S+E+W)
        Label(buttons_frame,
              text = "Presets:"
              ).grid(row = 0, column = 0, sticky = "nsew")

        # First Column of 10 Buttons
        Button(buttons_frame,
               text = PRESET_1_BTNTXT,
               command = self.preset1
               ).grid(row = 1, column = 0,  sticky = "nsew")
        Button(buttons_frame,
               text = PRESET_2_BTNTXT,
               command = self.preset2
               ).grid(row = 2, column = 0,  sticky = "nsew")
        Button(buttons_frame,
               text = PRESET_3_BTNTXT,
               command = self.preset3
               ).grid(row = 3, column = 0, sticky = "nsew")
        Button(buttons_frame,
               text = PRESET_4_BTNTXT,
               command = self.preset4
               ).grid(row = 4, column = 0, sticky = "nsew")
        Button(buttons_frame,
               text = PRESET_5_BTNTXT,
               command = self.preset5
               ).grid(row = 5, column = 0, sticky = "nsew")

        Button(buttons_frame,
               text = PRESET_6_BTNTXT,
               command = self.preset6
               ).grid(row = 6, column = 0, sticky = "nsew")

        Button(buttons_frame,
               text = PRESET_7_BTNTXT,
               command = self.preset7
               ).grid(row = 7, column = 0, sticky = "nsew")

        Button(buttons_frame,
               text = PRESET_8_BTNTXT,
               command = self.preset8
               ).grid(row = 8, column = 0, sticky = "nsew")

        Button(buttons_frame,
               text = PRESET_9_BTNTXT,
               command = self.preset9
               ).grid(row = 9, column = 0, sticky = "nsew")

        Button(buttons_frame,
               text = PRESET_10_BTNTXT,
               command = self.preset10
               ).grid(row = 10, column = 0, sticky = "nsew")

        # Second Column of 10 Buttons
        Button(buttons_frame,
               text = PRESET_11_BTNTXT,
               command = self.preset11
               ).grid(row = 1, column = 2,  sticky = "nsew")
        Button(buttons_frame,
               text = PRESET_12_BTNTXT,
               command = self.preset12
               ).grid(row = 2, column = 2,  sticky = "nsew")
        Button(buttons_frame,
               text = PRESET_13_BTNTXT,
               command = self.preset13
               ).grid(row = 3, column = 2, sticky = "nsew")
        Button(buttons_frame,
               text = PRESET_14_BTNTXT,
               command = self.preset14
               ).grid(row = 4, column = 2, sticky = "nsew")
        Button(buttons_frame,
               text = PRESET_15_BTNTXT,
               command = self.preset15
               ).grid(row = 5, column = 2, sticky = "nsew")

        Button(buttons_frame,
               text = PRESET_16_BTNTXT,
               command = self.preset16
               ).grid(row = 6, column = 2, sticky = "nsew")

        Button(buttons_frame,
               text = PRESET_17_BTNTXT,
               command = self.preset17
               ).grid(row = 7, column = 2, sticky = "nsew")

        Button(buttons_frame,
               text = PRESET_18_BTNTXT,
               command = self.preset18
               ).grid(row = 8, column = 2, sticky = "nsew")

        Button(buttons_frame,
               text = PRESET_19_BTNTXT,
               command = self.preset9
               ).grid(row = 9, column = 2, sticky = "nsew")

        Button(buttons_frame,
               text = PRESET_20_BTNTXT,
               command = self.preset20
               ).grid(row = 10, column = 2, sticky = "nsew")

        ## required for flexible window resizing
        self.columnconfigure(0,weight=0)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)
        self.columnconfigure(3,weight=1)
        self.columnconfigure(4,weight=1)
        self.columnconfigure(5,weight=1)
        self.rowconfigure(0,weight=0)
        self.rowconfigure(1,weight=0)
        self.rowconfigure(2,weight=1)
        self.rowconfigure(3,weight=1)
        self.rowconfigure(4,weight=1)
        self.rowconfigure(5,weight=1)
        self.rowconfigure(6,weight=0)
        self.rowconfigure(7,weight=0)
        self.rowconfigure(8,weight=1)
        self.rowconfigure(9,weight=1)
        self.rowconfigure(10,weight=1)
        self.rowconfigure(11,weight=0)
        buttons_frame.columnconfigure(0,weight=1)
        buttons_frame.rowconfigure(0,weight=1)
        buttons_frame.rowconfigure(1,weight=1)
        buttons_frame.rowconfigure(2,weight=1)
        buttons_frame.rowconfigure(3,weight=1)
        buttons_frame.rowconfigure(4,weight=1)
        buttons_frame.rowconfigure(5,weight=1)
        buttons_frame.rowconfigure(6,weight=1)
        buttons_frame.rowconfigure(7,weight=1)
        buttons_frame.rowconfigure(8,weight=1)
        buttons_frame.rowconfigure(9,weight=1)
        buttons_frame.rowconfigure(10,weight=1)



    def tiepit(self):
        """ Types the text in the box. """
        # get values from the GUI
        myText = self.main_txt.get(0.0, END)
        lines = myText.splitlines()
        time.sleep(5) 
        self.typout(lines)
        # https://github.com/asweigart/pyautogui/issues/46#issuecomment-132640299

    def tiepit2(self):
        """ Types the text in the box. """
        # get values from the GUI
        myText = self.main_txt2.get(0.0, END)
        lines = myText.splitlines()

        time.sleep(5) 
        self.typout(lines)
        # https://github.com/asweigart/pyautogui/issues/46#issuecomment-132640299
        
    def typout(self, lines):
        for line in lines:
            ## skip last newline
            ## Only provide newlines "between" lines
            if (line == lines[-1]):
                pyautogui.typewrite(line, TYPING_SPEED)
            else:
                pyautogui.typewrite(line, TYPING_SPEED)
                pyautogui.typewrite("\n")
                time.sleep(NEWLINE_DELAY)

    def reset(self):
        self.main_txt.delete(0.0, END)

    def reset2(self):
        self.main_txt2.delete(0.0, END)

    def preset1(self):
        self.main_txt.delete(0.0, END)
        self.main_txt.insert(0.0, PRESET_1)

    def preset2(self):
        self.main_txt.delete(0.0, END)
        self.main_txt.insert(0.0, PRESET_2)

    def preset3(self):
        self.main_txt.delete(0.0, END)
        self.main_txt.insert(0.0, PRESET_3)

    def preset4(self):
        self.main_txt.delete(0.0, END)
        self.main_txt.insert(0.0, PRESET_4)

    def preset5(self):
        self.main_txt.delete(0.0, END)
        self.main_txt.insert(0.0, PRESET_5)

    def preset6(self):
        self.main_txt.delete(0.0, END)
        self.main_txt.insert(0.0, PRESET_6)

    def preset7(self):
        self.main_txt.delete(0.0, END)
        self.main_txt.insert(0.0, PRESET_7)

    def preset8(self):
        self.main_txt.delete(0.0, END)
        self.main_txt.insert(0.0, PRESET_8)

    def preset9(self):
        self.main_txt.delete(0.0, END)
        self.main_txt.insert(0.0, PRESET_9)

    def preset10(self):
        self.main_txt.delete(0.0, END)
        self.main_txt.insert(0.0, PRESET_10)

    def preset11(self):
        self.main_txt.delete(0.0, END)
        self.main_txt.insert(0.0, PRESET_11)

    def preset12(self):
        self.main_txt.delete(0.0, END)
        self.main_txt.insert(0.0, PRESET_12)

    def preset13(self):
        self.main_txt.delete(0.0, END)
        self.main_txt.insert(0.0, PRESET_13)

    def preset14(self):
        self.main_txt.delete(0.0, END)
        self.main_txt.insert(0.0, PRESET_14)

    def preset15(self):
        self.main_txt.delete(0.0, END)
        self.main_txt.insert(0.0, PRESET_15)

    def preset16(self):
        self.main_txt.delete(0.0, END)
        self.main_txt.insert(0.0, PRESET_16)

    def preset17(self):
        self.main_txt.delete(0.0, END)
        self.main_txt.insert(0.0, PRESET_17)

    def preset18(self):
        self.main_txt.delete(0.0, END)
        self.main_txt.insert(0.0, PRESET_18)

    def preset19(self):
        self.main_txt.delete(0.0, END)
        self.main_txt.insert(0.0, PRESET_19)

    def preset20(self):
        self.main_txt.delete(0.0, END)
        self.main_txt.insert(0.0, PRESET_20)

# main
root = Tk()
root.title("KeyboardPal v0.0.0.1")
app = Application(root)
root.geometry("800x400")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()
