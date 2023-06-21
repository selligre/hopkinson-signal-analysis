# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import GUImain
import GUIspecimen
import GUIanalyze

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os


def run(calc):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame2")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window = Tk()

    window.geometry("1280x720")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(1179.0, 45.0, image=image_image_1)

    canvas.create_text(
        483.0,
        50.0,
        anchor="nw",
        text="Specimen and Data",
        fill="#000000",
        font=("Inter", 34 * -1),
    )

    canvas.create_rectangle(431.0, 141.0, 1179.0, 524.0, fill="#D9D9D9", outline="")

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (window.destroy(), GUImain.run(calc)),
        relief="flat",
    )
    button_1.place(x=50.0, y=50.0, width=200.0, height=50.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (window.destroy(), GUIspecimen.run(calc)),
        relief="flat",
    )
    button_2.place(x=50.0, y=285.0, width=250.0, height=75.0)

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: calc.import_data_file(),
        relief="flat",
    )
    button_3.place(x=50.0, y=449.0, width=250.0, height=75.0)

    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (window.destroy(), GUIanalyze.run(calc)),
        relief="flat",
    )
    button_4.place(x=639.0, y=555.0, width=300.0, height=100.0)
    window.resizable(False, False)
    window.mainloop()
