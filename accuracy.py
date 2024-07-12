# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import CMatrix
def show(accuracy_svc,accuracy_xgb,accuracy_gnb,textb,precision_svc, precision_xgb, precision_gnb, recall_svc, recall_xgb, recall_gnb, f1_svc, f1_xgb, f1_gnb, data, labels, Gvalue, Cvalue):
 from pathlib import Path
 # from tkinter import *
 # Explicit imports to satisfy Flake8
 from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
 import LCurve
 import PLOT
 import CMatrix
 OUTPUT_PATH = Path(__file__).parent
 ASSETS_PATH = OUTPUT_PATH / Path(r"E:\Tkinter designer\New Accuracy\build\assets\frame0")
 def relative_to_assets(path: str) -> Path:
   return ASSETS_PATH / Path(path)
 def plot():
   PLOT.show(accuracy_svc, accuracy_xgb, accuracy_gnb, precision_svc, 
precision_xgb, precision_gnb, recall_svc, recall_xgb, recall_gnb,
 f1_svc, f1_xgb, f1_gnb)
 def CM():
   CMatrix.show()
 def curve():
    LCurve.show(data, labels, Gvalue, Cvalue)
    window = Tk()
    window.geometry("1300x762")
    window.configure(bg="#181818")
    canvas = Canvas(
    window,
    bg="#181818",
    height=762,
    width=1300,
    bd=0,
    highlightthickness=0,
    relief="ridge"
    )
    canvas.place(x=0, y=0)
    canvas.create_rectangle(
    0.0,
    625.0,
    1300.0,
    762.0,

    fill="#75D6FE",
    outline="")
    button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
    button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=CM,
    relief="flat"
    )
    button_1.place(
    x=640.0,
    y=647.0,
    width=187.0,
    height=74.0
    )
    canvas.create_rectangle(
    0.0,
    80.0,
    1300.0,
    155.0,
    fill="#005162",
    outline="")
    canvas.create_rectangle(
    1188.0,
    80.0,
    1300.0,
    625.0,
    fill="#005162",
    outline="")
    canvas.create_rectangle(
    0.0,
    155.0,
    242.0,
    625.0,
    fill="#005162",
    outline="")
    button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
    button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=plot,
    relief="flat"
    )
    button_2.place(
    x=868.0,
    y=647.0,
    width=187.0,
    height=74.0
    )
    button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))

    button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=window.destroy,
    relief="flat"
    )
    button_3.place(
    x=1086.0,
    y=647.0,
    width=187.0,
    height=74.0
    )
    button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
    button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=curve,
    relief="flat"
    )
    button_4.place(
    x=415.0,
    y=647.0,
    width=187.0,
    height=74.0
    )
    image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
    650.0,
    40.0,
    image=image_image_1
    )
    canvas.create_text(
    308.0,
    199.0,
    anchor="nw",
    text=accuracy_svc,
    fill="#FFFFFF",
    font=("Yu Gothic UI Light", 32 * -1)
    )
    canvas.create_text(
    37.0,
    345.0,
    anchor="nw",
    text="XGBOOST",
    fill="#FFFFFF",
    font=("Yu Gothic UI Light", 32 * -1)
    )
    canvas.create_text(
    37.0,
    208.0,
    anchor="nw",
    text="SVC",

    fill="#FFFFFF",
    font=("Yu Gothic UI Light", 32 * -1)
    )
    canvas.create_text(
    225.0,
    103.0,
    anchor="nw",
    text=" ACCURACY",
    fill="#FFFFFF",
    font=("Yu Gothic UI Light", 32 * -1)
    )
    canvas.create_text(
    472.0,
    103.0,
    anchor="nw",
    text=" PRECISON",
    fill="#FFFFFF",
    font=("Yu Gothic UI Light", 32 * -1)
    )
    canvas.create_text(
    721.0,
    103.0,
    anchor="nw",
    text=" F1 SCORE",
    fill="#FFFFFF",
    font=("Yu Gothic UI Light", 32 * -1)
    )
    canvas.create_text(
    971.0,
    103.0,
    anchor="nw",
    text=" RECALL",
    fill="#FFFFFF",
    font=("Yu Gothic UI Light", 32 * -1)
    )
    canvas.create_text(
    308.0,
    334.0,
    anchor="nw",
    text=accuracy_xgb,
    fill="#FFFFFF",
    font=("Yu Gothic UI Light", 32 * -1)
    )
    canvas.create_text(
    37.0,
    481.0,
    anchor="nw",
    text="NAIVE BAYES",
    fill="#FFFFFF",
    font=("Yu Gothic UI Light", 32 * -1)
    )
    canvas.create_text(
    308.0,
    472.0,

    anchor="nw",
    text=accuracy_gnb,
    fill="#FFFFFF",
    font=("Yu Gothic UI Light", 32 * -1)
    )
    canvas.create_text(
    1055.0,
    199.0,
    anchor="nw",
    text=recall_svc,
    fill="#FFFFFF",
    font=("Yu Gothic UI Light", 32 * -1)
    )
    canvas.create_text(
    1055.0,
    334.0,
    anchor="nw",
    text=recall_xgb,
    fill="#FFFFFF",
    font=("Yu Gothic UI Light", 32 * -1)
    )
    canvas.create_text(
    1055.0,
    472.0,
    anchor="nw",
    text=recall_gnb,
    fill="#FFFFFF",
    font=("Yu Gothic UI Light", 32 * -1)
    )
    canvas.create_text(
    804.0,
    199.0,
    anchor="nw",
    text=f1_svc,
    fill="#FFFFFF",
    font=("Yu Gothic UI Light", 32 * -1)
    )
    canvas.create_text(
    804.0,
    334.0,
    anchor="nw",
    text=f1_xgb,
    fill="#FFFFFF",
    font=("Yu Gothic UI Light", 32 * -1)
    )
    canvas.create_text(
    804.0,
    472.0,
    anchor="nw",
    text=f1_gnb,
    fill="#FFFFFF",
    font=("Yu Gothic UI Light", 32 * -1)
    )
    canvas.create_text(

    553.0,
    199.0,
    anchor="nw",
    text=precision_svc,
    fill="#FFFFFF",
    font=("Yu Gothic UI Light", 32 * -1)
    )
    canvas.create_text(
    553.0,
    334.0,
    anchor="nw",
    text=precision_xgb,
    fill="#FFFFFF",
    font=("Yu Gothic UI Light", 32 * -1)
    )
    canvas.create_text(
    553.0,
    472.0,
    anchor="nw",
    text=precision_gnb,
    fill="#FFFFFF",
    font=("Yu Gothic UI Light", 32 * -1)
    )
    canvas.create_text(
    18.0,
    615.0,
    anchor="nw",
    text="Recommended Classifier",
    fill="#181818",
    font=("Yu Gothic UI Light", 32 * -1)
    )
    canvas.create_text(
    121.0,
    713.0,
    anchor="nw",
    text=textb,
    fill="#1E1E1E",
    font=("Yu Gothic UI Light", 32 * -1)
    )
    canvas.create_text(
    45.0,
    675.0,
    anchor="nw",
    text="(based on accuracy)",
    fill="#000000",
    font=("Yu Gothic UI Light", 32 * -1)
    )
    window.resizable(False, False)
    window.mainloop()
