from tkinter import *  
from PIL import ImageTk,Image  
root = Tk()  
canvas = Canvas(root, width = 1600, height = 600)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open(r'D:\Nextcloud\Work\CODING\BCG\Files\BC_TEMPLATES\001.jpg'))  
canvas.create_image(20, 20, anchor=NW, image=img) 

# Create a Button 
btn = Button(root, text = 'close BCG', bd = '5', 
                          command = root.destroy)  
  
# Set the position of button on the top of window.    
btn.pack(side = 'top')  

root.mainloop()