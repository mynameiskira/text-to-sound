from tkinter import *
from gtta import gtts
from playsound import playsound






root = Tk()
geometry root.("720x350")
root.configure(bg='ghost white')
root.title("Project - VoiceIA - by BSK / ZCA")






Label(root, text = "TEXTE EN VOIX", font = 'Monaco', bg = 'green').pack()
Label(text = "Data flair", font = "arial", bg = "white smoke", width = '20').pack(side = "bottom")




//a//

Msg = StringVar()
Label(root, text = "Veuillez entrer un texte à traiter", font = "arial", bg = "white smoke").place(x=20, y=60)





entry_field = Entry(root, textvariable = Msg, width = '50')
entry_feld.place(x=20, y=100)




def Exit():
  root.destroy()

def Texte_En_Voix():
  Message = entry_field.get()
  speech = gTTS(text = Message)
  speech.save('Output.mp3')
  playsound('Output.mp3')
  
def Reset():
  Msg.set("")

Button(root, text = "PLAY", font = 'Monaco', command = Texte_En_Voix, width = '4').place(x=25, y=140)
Button(root, text = "EXIT", font = 'Monaco', command = EXIT, bg = "Orange", width = "4").place(x=100, y=140)
Button(root, text = "RESET", font = 'Monaco', command = Reset, bg = "Red", width = "6").place(x=175, y=140)

root.mainloop()
