from tkinter import *
from tkinter import filedialog
import qrcode
import os


def generate(window, entry, save_button):
    # Get text from the entry box
    text = entry.get()
    # Enable the save button
    save_button.config(state=ACTIVE)

    # Generate and save the QRcode in current directory for now
    qr = qrcode.QRCode(version=2, box_size=10, border=2)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image()
    img.save("./temp.png")
 
    # Show the QRcode to the user
    photo = PhotoImage(file="./temp.png")
    qr_label = Label(window, image=photo, compound="bottom")
    qr_label.grid(row=2, column=0, columnspan=2, pady=20)
    # When the program exits the function the image will be lost,
    # that's why we have to keep it in a variable that won't get lost
    qr_label.image = photo  # needed to add this line, else the image doesn't show


def save(save_buton):
    # Returns file object, we only want the path
    img_path = filedialog.asksaveasfile(filetypes=[("PNG Image", "*.png")])

    # Check the case user presses cancel, aka img_path = None
    if img_path:
        os.rename("./temp.png", img_path.name)
        save_button.config(state=DISABLED)
 

# Main window dimensions
WIDTH = 500
HEIGHT = 500
BG_COLOR = "pink"

# Set up our main window
window = Tk()
window.geometry(str(WIDTH) + "x" + str(HEIGHT))
window.title("QR code generator")
window.config(background=BG_COLOR)

prompt = Label(window, text="Enter text: ", pady=20, bg=BG_COLOR)
prompt.grid(row=0, column=0)

entry = Entry(window, width=50)
entry.grid(row=0, column=1)

frame = Frame(window, bg=BG_COLOR)
frame.grid(row=1, column=0, columnspan=2)

save_label = Label(frame, text="When saving the QR code, add '.png' at the end of the file name.", bg=BG_COLOR)
save_label.grid(row=0, column=0, columnspan=2)

save_button = Button(frame, text="Save", command=lambda: save(save_button), state=DISABLED, cursor="hand2")
save_button.grid(row=1, column=1)

generate_button = Button(frame, text="Generate", command=lambda: generate(window, entry, save_button), cursor="hand2")
generate_button.grid(row=1, column=0)


window.mainloop()

# If the user doesn't save the QRcode, we need to delete the one
# we saved in the current directory
if os.path.exists("./temp.png"):
    os.remove("./temp.png")
