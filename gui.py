from tkinter import*
from PIL import Image,ImageTk
import speech_to_text
import assist as assist  # Import just the function


root = Tk()
root.title("AI Assistant")
root.geometry("550x700")
root.resizable(False , False)
root.config(bg="#D3D3D3")

#ASK FUN
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = assist.action(user_val)  
    text.insert(END, 'user--->' + str(user_val) + "\n")
    if bot_val != None:
        text.insert(END, "BOT <---"+str(bot_val)+"\n")
    if bot_val == "ok sir":
        root.destroy()

#send  fun
def send():
    send = entry.get()
    bot = assist.action(send)
    text.insert(END , 'user--->'+ send +"\n")
    if bot != None:
        text.insert(END, "BOT <---"+str(bot)+"\n")
    if bot == "ok sir" :  
        root.destroy()


# delete fun
def delete_text():
    text.delete('1.0' , "end")


#frame

frame = LabelFrame(root , padx= 100 ,pady =7, borderwidth= 3 , relief= "raised")
frame.config(bg="#D3D3D3")
frame.grid(row=0 , column =1,padx =20, pady=10)


#text lable

text_label = Label(frame, text="AI Assistant", font=("comic Sans ms",14 , "bold"), bg="#356696")
text_label.grid(row = 0 ,column = 0 , padx =20 , pady=10)

#image
image = ImageTk.PhotoImage(Image.open("C:/Users/Dell/OneDrive/Desktop/college work/project/assistant/image.jpg"))
image_label= Label(frame ,image=image)
image_label.grid(row=1,column =0,pady=20)

#adding the text
text= Text(root,font=('courier 10 bold'),bg ="#356696")
text.grid(row=2,column=0)
text.place(x=100,y=450 ,width=375,height=100)

#entry widget

entry= Entry(root, justify=CENTER)
entry.place(x=100 , y=560, width = 350, height=30)

#button
Button1= Button(root,text="ASK", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
Button1.place(x=70,y=600)

#button2
Button2= Button(root,text="Send", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=send)
Button2.place(x=400,y=600)
#button3
Button3= Button(root,text="Delete", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=delete_text)
Button3.place(x=225,y=600)

root.mainloop()