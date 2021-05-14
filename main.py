from tkinter import *
from PIL import Image, ImageTk


#globals
BLUE = '#91E8E1'
TEXT_COLOR = '#2f5d62'
FONT = 'verdana'

#create window
window = Tk()
window.title("HuurHuisSnel")
window.config(padx=25, pady=12, bg=BLUE)

canvas = Canvas(width=250, height=150, bg=BLUE, highlightthickness=0)


# commands
def submit():
    stad = e1.get()
    prijsmin = e2.get()
    prijsmax = e3.get()
    telnr = e4.get()
    new_lijst = (stad, prijsmin, prijsmax, telnr)
    print(new_lijst[0])
    return new_lijst


def quitting():
    window.quit()


# labels of GUI
label_stad = Label(text="Stad", bg=BLUE, highlightthickness=0, font=(FONT, 15, "bold"), fg=TEXT_COLOR)
label_stad.grid(column=0, row=1)
e1 = Entry(window, show=None, font=('Arial', 14))
e1.grid(column=1, row=1)

label_min = Label(text="Minimale huurprijs", bg=BLUE, highlightthickness=0, font=(FONT, 15, "bold"), fg=TEXT_COLOR)
label_min.grid(column=0, row=2)
e2 = Entry(window, show=None, font=('Arial', 14))
e2.grid(column=1, row=2)

label_max = Label(text="Maximale huurptijs", bg=BLUE, highlightthickness=0, font=(FONT, 15, "bold"), fg=TEXT_COLOR)
label_max.grid(column=0, row=3)
e3 = Entry(window, show=None, font=('Arial', 14))
e3.grid(column=1, row=3, padx=(10))

label_telnr = Label(text="Telefoon nummer", bg=BLUE, highlightthickness=0, font=(FONT, 15, "bold"), fg=TEXT_COLOR)
label_telnr.grid(column=0, row=4)
e4 = Entry(window, show=None, font=('Arial', 14))
e4.grid(column=1, row=4, padx=(10))

# buttons of GUI
button_start = Button(text="Submit", bg=BLUE, font=(FONT, 12, 'bold'), fg=TEXT_COLOR, command=submit, )
button_start.grid(column=0, row=5, columnspan=2, pady=(10))

button_quit = Button(text="Exit", bg=BLUE, font=(FONT, 12, 'bold'), fg=TEXT_COLOR, command=quitting, )
button_quit.grid(column=0, row=6, columnspan=2, pady=(10))

# image
house_img = PhotoImage(file="house.png")
smaller_image = house_img.subsample(4, 4)
canvas.create_image(120, 75, image=smaller_image)
canvas.grid(column=0, row=7, columnspan=2)

window.quit()
window.mainloop()

