# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import GUImain

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Button, PhotoImage


def run(calc):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame1")

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
        541.0,
        50.0,
        anchor="nw",
        text="Bar Settings",
        fill="#000000",
        font=("Inter", 34 * -1),
    )

    canvas.create_text(
        444.0,
        146.0,
        anchor="nw",
        text="Material =",
        fill="#000000",
        font=("Inter", 20 * -1),
    )

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(719.0, 158.5, image=entry_image_1)
    entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_1.place(x=644.0, y=143.0, width=150.0, height=29.0)

    canvas.create_text(
        444.0,
        192.0,
        anchor="nw",
        text="Experiment Type =",
        fill="#000000",
        font=("Inter", 20 * -1),
    )

    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(719.0, 205.5, image=entry_image_2)
    entry_2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_2.place(x=644.0, y=190.0, width=150.0, height=29.0)

    canvas.create_text(
        444.0,
        239.0,
        anchor="nw",
        text="Length =",
        fill="#000000",
        font=("Inter", 20 * -1),
    )

    entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(719.0, 252.5, image=entry_image_3)
    entry_3 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_3.place(x=644.0, y=237.0, width=150.0, height=29.0)

    canvas.create_text(
        800.0, 239.0, anchor="nw", text="mm", fill="#000000", font=("Inter", 20 * -1)
    )

    canvas.create_text(
        444.0,
        286.0,
        anchor="nw",
        text="Diameter =",
        fill="#000000",
        font=("Inter", 20 * -1),
    )

    entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(719.0, 299.0, image=entry_image_4)
    entry_4 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_4.place(x=644.0, y=283.0, width=150.0, height=30.0)

    canvas.create_text(
        800.0, 286.0, anchor="nw", text="mm", fill="#000000", font=("Inter", 20 * -1)
    )

    canvas.create_text(
        444.0,
        333.0,
        anchor="nw",
        text="Volume =",
        fill="#000000",
        font=("Inter", 20 * -1),
    )

    entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(719.0, 345.5, image=entry_image_5)
    entry_5 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_5.place(x=644.0, y=330.0, width=150.0, height=29.0)

    canvas.create_text(
        800.0, 333.0, anchor="nw", text="mm^3", fill="#000000", font=("Inter", 20 * -1)
    )

    canvas.create_text(
        444.0,
        380.0,
        anchor="nw",
        text="Mass =",
        fill="#000000",
        font=("Inter", 20 * -1),
    )

    entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(719.0, 392.5, image=entry_image_6)
    entry_6 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_6.place(x=644.0, y=377.0, width=150.0, height=29.0)

    canvas.create_text(
        800.0, 380.0, anchor="nw", text="g", fill="#000000", font=("Inter", 20 * -1)
    )

    canvas.create_text(
        444.0,
        427.0,
        anchor="nw",
        text="Density =",
        fill="#000000",
        font=("Inter", 20 * -1),
    )

    entry_image_7 = PhotoImage(file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(719.0, 439.5, image=entry_image_7)
    entry_7 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_7.place(x=644.0, y=424.0, width=150.0, height=29.0)

    canvas.create_text(
        800.0,
        427.0,
        anchor="nw",
        text="kg/m^3",
        fill="#000000",
        font=("Inter", 20 * -1),
    )

    canvas.create_text(
        444.0,
        473.0,
        anchor="nw",
        text="Celerity =",
        fill="#000000",
        font=("Inter", 20 * -1),
    )

    entry_image_8 = PhotoImage(file=relative_to_assets("entry_8.png"))
    entry_bg_8 = canvas.create_image(719.0, 486.5, image=entry_image_8)
    entry_8 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_8.place(x=644.0, y=471.0, width=150.0, height=29.0)

    canvas.create_text(
        800.0, 473.0, anchor="nw", text="m/s", fill="#000000", font=("Inter", 20 * -1)
    )

    canvas.create_text(
        444.0,
        520.0,
        anchor="nw",
        text="Young Modulus =",
        fill="#000000",
        font=("Inter", 20 * -1),
    )

    entry_image_9 = PhotoImage(file=relative_to_assets("entry_9.png"))
    entry_bg_9 = canvas.create_image(719.0, 533.5, image=entry_image_9)
    entry_9 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_9.place(x=644.0, y=518.0, width=150.0, height=29.0)

    canvas.create_text(
        800.0, 520.0, anchor="nw", text="MPa", fill="#000000", font=("Inter", 20 * -1)
    )

    canvas.create_text(
        444.0,
        567.0,
        anchor="nw",
        text="J1 - Sample =",
        fill="#000000",
        font=("Inter", 20 * -1),
    )

    entry_image_10 = PhotoImage(file=relative_to_assets("entry_10.png"))
    entry_bg_10 = canvas.create_image(719.0, 580.0, image=entry_image_10)
    entry_10 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_10.place(x=644.0, y=564.0, width=150.0, height=30.0)

    canvas.create_text(
        800.0, 567.0, anchor="nw", text="mm", fill="#000000", font=("Inter", 20 * -1)
    )

    canvas.create_text(
        444.0,
        614.0,
        anchor="nw",
        text="Sample - J2 =",
        fill="#000000",
        font=("Inter", 20 * -1),
    )

    entry_image_11 = PhotoImage(file=relative_to_assets("entry_11.png"))
    entry_bg_11 = canvas.create_image(719.0, 626.5, image=entry_image_11)
    entry_11 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_11.place(x=644.0, y=611.0, width=150.0, height=29.0)

    canvas.create_text(
        800.0, 614.0, anchor="nw", text="mm", fill="#000000", font=("Inter", 20 * -1)
    )

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
        command=lambda: calc.import_bar_settings(),
        relief="flat",
    )
    button_2.place(x=50.0, y=283.0, width=200.0, height=50.0)

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: calc.export_bar_settings(),
        relief="flat",
    )
    button_3.place(x=50.0, y=381.0, width=200.0, height=50.0)
    window.resizable(False, False)
    window.mainloop()
