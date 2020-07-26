"""from tkinter import *
import random
Root = Tk()

cnvs = Canvas(Root,width=500,height=500)
cnvs.pack()


wheel = PhotoImage("C:\\Users\\rushil\\Desktop\\python\\spin_the_wheel.png")
lbl = Label(image=wheel).pack

cnvs.create_image(100,100,anchor = NW,image=wheel)
print("YYYY")


Root.mainloop()"""

import random
import time

kr = [
    "Blue",
    "Purple",
    "Green",
    "yellow",
    "Red",
    "Black",
    "Bronze",
    "!Silver!",
    "!!GOLD!!"
]

print("Blue = 50\nPurple = 70\nGreen = 125\nYellow = 225\nRed = 500\nBlack = 1500\nBronze = 3000\n!Silver! = 5000\n!!GOLD!! = 10000")

tygryt = input("Press enter to spin the wheel")

print("■")
time.sleep(0.1)
print("■■")
time.sleep(0.1)
print("■■■")
time.sleep(0.1)
print("■■■■")
time.sleep(0.1)
print("■■■■■")
time.sleep(0.1)
print("■■■■■■")
tkr = random.choice(kr)
print("your roll =",tkr)
time.sleep(0.1)
print("waiting for lucky roll ...")
time.sleep(0.1)
print("■■■■■■■■")
time.sleep(0.1)
print("■■■■■■■■■")
time.sleep(0.1)
print("■■■■■■■■■■")
time.sleep(0.1)
print("■■■■■■■■■■■")
time.sleep(0.1)
print("■■■■■■■■■■■■")
comtkr = random.choice(kr)
print("The lucky rool = ",comtkr)

if tkr == comtkr:
    print("Wow you have unboxed 100000 Kr \nThis is because you rolled the lucky colour")
    k_r = 50000


elif tkr != comtkr:
    print("Aww your colour is different from the lucky colour ")    
    k_r = 0 

#________________________________________________________________________________________________________#

if tkr == 'Blue':
    k__r = 50 
    k___r = k_r+k__r
    print("Kr unboxed in lucky rool =",k_r,"\nKr unboxed by colour =",k__r,"\nTotal Kr unboxed =",k___r)
elif tkr == 'Purple':
    k__r = 70
    k___r = k_r+k__r
    print("Kr unboxed in lucky rool =",k_r,"\nKr unboxed by colour =",k__r,"\nTotal Kr unboxed =",k___r)
elif tkr == ['Green']:
    k__r = 125
    k___r = k_r+k__r
    print("Kr unboxed in lucky rool =",k_r,"\nKr unboxed by colour =",k__r,"\nTotal Kr unboxed =",k___r)
elif tkr == 'yellow':
    k__r = 225
    k___r = k_r+k__r
    print("Kr unboxed in lucky rool =",k_r,"\nKr unboxed by colour =",k__r,"\nTotal Kr unboxed =",k___r)
elif tkr == 'Red':
    k__r = 500
    k___r = k_r+k__r
    print("Kr unboxed in lucky rool =",k_r,"\nKr unboxed by colour =",k__r,"\nTotal Kr unboxed =")
elif tkr == 'Black':
    k__r = 1500
    k___r = k_r+k__r
    print("Kr unboxed in lucky rool =",k_r,"\nKr unboxed by colour =",k__r,"\nTotal Kr unboxed =",k___r)
elif tkr == 'Bronze':
    k__r = 3000
    k___r = k_r+k__r
    print("Kr unboxed in lucky rool =",k_r,"\nKr unboxed by colour =",k__r,"\nTotal Kr unboxed =",k___r,"\nYou have also reached a very high colour")
elif tkr == '!Silver!':
    k__r = 5000
    k___r = k_r+k__r
    print("Kr unboxed in lucky rool =",k_r,"\nKr unboxed by colour =",k__r,"\nTotal Kr unboxed =",k___r,"\nYou have also reached a very high colour")
elif tkr == '!!GOLD!!':
    k__r = 10000
    k___r = k_r+k__r
    print("Kr unboxed in lucky rool =",k_r,"\nKr unboxed by colour =",k__r,"\nTotal Kr unboxed =",k___r,"\nYou have also reached the highest colour")