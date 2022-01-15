from tkinter import * 
from tkinter import Button
import sys
import webbrowser
 
root = Tk()
 
root.resizable(False, False)
root.geometry('180x1100+1740+0')
root.title('Charms bar')
root.overrideredirect(True)
root.configure(background='#383838')
root.attributes('-topmost', True)

ExitBtnImg = PhotoImage(file = r"ExitBtn.png")
Button(root, image = ExitBtnImg, bd = 0, borderwidth=0, highlightthickness = 0, command = lambda: sys.exit(0)).pack(side = TOP)

SettingsBtnImg = PhotoImage(file = r"SettingsBtn.png")
Button(root, image = SettingsBtnImg, bd = 0, borderwidth=0, highlightthickness = 0, command = lambda: webbrowser.open('ms-settings://') and sys.exit(0)).pack(side = TOP)
 
root.mainloop()