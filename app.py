import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("eyesaver")
app.geometry("400x200")

label = ctk.CTkLabel(app, text="eyesaver~", font=("Times New Roman", 20))
#position of label
label.pack(pady=20)

button = ctk.CTkButton(app, text="start", command=lambda: print("Button clicked!"), fg_color='pink')
button.pack(pady=10)

app.mainloop()

#pallette F8FCDA E3E9C2 F9FBB2 7C6354 A5ABAF