import tkinter as tk #for gui
from tkinter import filedialog,Text #for text and all
import os #for runnig apps

root = tk.Tk()# it is where all the screen is place 

#adding all the files into an array
apps=[]

if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = tempApps

def addApp():#the function to open up the files

    for widget in frame.winfo_children():#when selecting a new app this will clear the screen so that no duplicates are added
        widget.destroy()

    filename=filedialog.askopenfilename(initialdir="/",title="Select File",filetypes=(("executables",".exe"),("all files","*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:#this will add all the apps selected to the frame
        label =tk.Label(frame,text=app,bg="gray")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)

canvas  = tk.Canvas(root,height=700,width=700,bg="#263D42") #what will be inside the screen
canvas.pack()

frame = tk.Frame(root,bg="white")#when you need to add something in the project
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

openFile = tk.Button(root,text="Open File",padx=10,pady=5,fg="white",bg="#263D42",command=addApp)#adding the button name of the button is openFile
openFile.pack()#adding the button to the canvas

runApps= tk.Button(root,text="Run the Apps",padx=10,pady=5,fg="white",bg="#263D42",command=runApps)#adding the button name of the button is runapps
runApps.pack()#adding the button to the canvas


for app in apps:
    label = tk.Label(frame,text=app)
    label.pack()

root.mainloop()


#all the apps we have selected will be saved here so when the app is closed the apps are saved
with open('save.txt','w') as f:
    for app in apps:
        f.write(app + ',' )