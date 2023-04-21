import qrcode
import customtkinter
from PIL import Image, ImageTk

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
resaltion="700x700"
root=customtkinter.CTk()
root.geometry(resaltion)
root.title("Qr Generator")

def paste():
    text=root.clipboard_get()
    data.delete(0,"end")
    data.insert(1,text)
    
def generat():
    qr.add_data(str(data.get()))
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(name.get()+".png")
    
def preview():
    img = Image.open(name.get()+".png")
    photo = ImageTk.PhotoImage(img)
    label = customtkinter.CTkLabel(root, image=photo)
    label.place(x=200,y=300)
    
title=customtkinter.CTkLabel(master=root,text="Qr Generator",font=("Roborto",24),text_color="#ffffff")
title.place(y=30,x=280)

data_l=customtkinter.CTkLabel(master=root,text="Enter The Data:",font=("Roborto",20),text_color="#ffffff")
data_l.place(y=80,x=150)

data=customtkinter.CTkEntry(master=root,placeholder_text="Data")
data.place(y=80,x=330)

name_l=customtkinter.CTkLabel(master=root,text="Enter The Qr Name:",font=("Roborto",20),text_color="#ffffff")
name_l.place(y=130,x=150)

name=customtkinter.CTkEntry(master=root,placeholder_text="name",width=120)
name.place(y=130,x=350)

paste=customtkinter.CTkButton(master=root,text="Paste",text_color="black",fg_color="#eaebed",width=30,command=paste)
paste.place(x=500,y=80)

generate=customtkinter.CTkButton(master=root,text="Generate",text_color="black",fg_color="#eaebed",command=generat)
generate.place(x=250,y=180)

previeww=customtkinter.CTkButton(master=root,text="Preview",text_color="black",fg_color="#eaebed",command=preview)
previeww.place(x=250,y=220)

root.mainloop()