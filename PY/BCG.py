from tkinter import * 
from tkinter import Canvas, filedialog  
from PIL import ImageTk,Image,ImageDraw,ImageFont
import tkinter as tk

#loads base image
im = Image.open(r"X:\BCG\Files\BC_TEMPLATES\001.jpg")

#draw command
draw = ImageDraw.Draw(im)

#load fonts
fontNAME = ImageFont.truetype(r'X:\BCG\Files\fonts\HelveticaNeueIt.ttf', 70)
fontPOS = ImageFont.truetype(r'X:\BCG\Files\fonts\HelveticaNeueLt.ttf', 35)
fontINFO = ImageFont.truetype(r'X:\BCG\Files\fonts\HelveticaNeueLt.ttf', 25)

#Creat windows for showing the BC
root = Tk()  

#defines windows size
canvas = Canvas(root, width = 1600, height = 800)  
canvas.pack()  

#creates user input field
#StringVar = useroutput #???? evtl???

#FNAME = StringVar()
#LNAME = StringVar()
#POS = StringVar() 
#TEL  = StringVar()
#MAIL = StringVar() 
#LOC = StringVar()

#L1 = Label(root, text="FNAME")
#L1.place(x = 1200, y = 150)
#E1 = Entry(root, textvariable = FNAME, bd=5)
#E1.place(x = 1270, y = 150)
#FNAME = FNAME.get()

#L2 = Label(root, text="LNAME")
#L2.place(x = 1200, y = 200)
#E2 = Entry(root, bd=5)
#E2.place(x = 1270, y = 200)

#L3 = Label(root, text="POS")
#L3.place(x = 1200, y = 250)
#E3 = Entry(root, textvariable = POS , bd=5)
#E3.place(x = 1270, y = 250)
#POS = POS.get()

#L4 = Label(root, text="TEL")
#L4.place(x = 1200, y = 300)
#E4 = Entry(root, bd=5)
#E4.place(x = 1270, y = 300)

#Mail textbox

L5 = Label(root, text="MAIL").place(x = 1200, y = 350) # labe position displayed in gui
E5 = Entry(root, bd=5).place(x = 1270, y = 350) #textbox postion on gui

L6 = Label(root, text="LOC")
L6.place(x = 1200, y = 400)
E6 = Entry(root, bd=5)
E6.place(x = 1270, y = 400)
#LOC = LOC.get()

#btn3 = Button(root, text = 'apply', bd = '5',  command = (print())


##-------------------------------------##
mystring = StringVar()
def getvalue(self, userinput):
    userinput = self
    self = getvalue 
    print(mystring.get(self))
#*************************************

    L4 = Label(root, text="Text to get")
    L4 = Label.place(x = 1200, y = 250)  #label
    E4 = Entry(root, textvariable = mystring, bd=5)
    E4 = Entry.place(x = 1200, y = 250 ) #entry textboxk

WSignUp = Button(root, text="print text", command=getvalue)
WSignUp.place(x = 1200, y = 100) #button
WSignUp = Entry(root, bd=5)
WSignUp = WSignUp.get()

##-------------------------------------###


#######################################################################
# the text needs to be replaced bei user input and then be written on top of the image
#this has to be move down unter the user input that will be genrated with tkinter
#write text on image
FNAME = 'FNAME'
draw.text((240, 100), FNAME, font = fontNAME)
LNAME = 'LNAME'
draw.text((240, 170), LNAME, font = fontNAME)
POS = 'POS'
draw.text((240, 246), POS, font = fontPOS)
TEL = 'TEL'
draw.text((595, 465), TEL, font = fontINFO)
MAIL = 'MAIL'
draw.text((595, 510), MAIL, font = fontINFO)
LOC = 'LOC'
draw.text((595, 560), LOC, font = fontINFO)  


#save image as 001_mod.jpg
im.save(r"X:\BCG\Files\temp\001_mod.jpg")
#####################################################################

#loads modifyed BC
img = ImageTk.PhotoImage(Image.open(r'X:\BCG\Files\temp\001_mod.jpg'))  
canvas.create_image(20, 20, anchor=NW, image=img) 


# Create a Button 
btn1 = Button(root, text = 'close BCG', bd = '5', 
                          command = root.destroy)                        
# Set the position of button on the top of window.    
btn1.pack()
btn1.place(x = 1350, y = 700, bordermode=OUTSIDE, height=30, width=80)  



##############save with button#####################

def savefile():
    hsl = Image.open(edged)
    hsl = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if hsl is None:
        return

######################
# Create a second Button 
btn2 = Button(root, text = 'SAVE AS', bd = '5', 
                          command = savefile)                        
# Set the position of button on the top of window.    
btn2.pack()
btn2.place(x = 1200, y = 700, bordermode=OUTSIDE, height=30, width=80)  










root.mainloop()