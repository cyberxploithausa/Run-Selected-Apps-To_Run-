############################################################
#####                   CYBERXPLOIT                    #####
##### PROJECT NAME: RUN SELECTED APPS(TO_RUN)          #####
##### PROJECT ID: CYBX007                              #####
#####                                                  #####
############################################################


#Importing the modules 
import tkinter as tk
from tkinter import filedialog, Text
import os

#main
root = tk.Tk()
apps = []


#This will save the previous apps that are selected and the save in a text file called "save.txt"
#It will read the apps in the text file.
if os.path.isfile('save.txt'):
    with open('save.txt', "r") as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        #print(tempApps)
        apps = [x for x in tempApps if x.strip()]

#Adding app in frame
def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                    filetypes=(("executables", "*.exe"), ("all files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="grey")
        label.pack()
        
#Running app
def runApp():
    for app in apps:
        os.startfile(app)

#Title of the tkinter app
Title = root.title("To Do App")

canvas = tk.Canvas(root, height=500, width=500, bg="#263042")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.7, relx=0.08, rely=0.08)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, 
                    fg="white", bg="#263042", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5,
                    fg="white", bg="#263042", command=runApp)
runApps.pack()

for app in apps:
    label1 = tk.Label(frame, text=app)
    label1.pack()


root.mainloop()

#creating a txt file to save added apps.
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')




############################################################
#####                   CYBERXPLOIT                    #####
##### PROJECT NAME: RUN SELECTED APPS(TO_RUN)          #####
##### PROJECT ID: CYBX007                              #####
#####                                                  #####
############################################################






