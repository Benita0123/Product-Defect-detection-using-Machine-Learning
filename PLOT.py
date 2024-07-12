
def show(svc,xgb,gnb,precision_svc, precision_xgb, precision_gnb, 
recall_svc, recall_xgb, recall_gnb, f1_svc, f1_xgb, f1_gnb):
 import numpy as np
 import matplotlib.pyplot as plt
 # creating the dataset
 data = {'SVC': svc, 'GNB': gnb, 'XGBoost': xgb}
 models = list(data.keys())
 accuracies = list(data.values())
 fig = plt.figure(figsize=(5, 2.71875))
 plt.bar(models, accuracies, color='maroon',
 width=0.3125)
 plt.xlabel("Model")
 plt.ylabel("Accuracy in %")
 plt.title("Accuracy Score")
 # creating the bar plot
 plt.savefig("C:/Users/moham/Desktop/PRODA NEW/Acc.png")
 plt.close()
 data = {'SVC': precision_svc, 'GNB': precision_gnb, 'XGBoost': 
precision_xgb}
 models = list(data.keys())
 accuracies = list(data.values())
 fig = plt.figure(figsize=(5, 2.71875))
 plt.bar(models, accuracies, color='maroon',
 width=0.3125)
 plt.xlabel("Model")
 plt.ylabel("Precision in %")
 plt.title("Precision Score")
 # creating the bar plot
 plt.savefig("C:/Users/moham/Desktop/PRODA NEW/Prec.png")
 plt.close()
 data = {'SVC': recall_svc, 'GNB': recall_gnb, 'XGBoost': recall_xgb}
 models = list(data.keys())
 accuracies = list(data.values())
 fig = plt.figure(figsize=(5, 2.71875))
 plt.bar(models, accuracies, color='maroon',
 width=0.3125)
 plt.xlabel("Model")
 plt.ylabel("Recall in %")
 plt.title("Recall Score")
 # creating the bar plot
 plt.savefig("C:/Users/moham/Desktop/PRODA NEW/Recall.png")
 plt.close()
 data = {'SVC': f1_svc, 'GNB': f1_gnb, 'XGBoost': f1_xgb}
 models = list(data.keys())
 accuracies = list(data.values())

 fig = plt.figure(figsize=(5, 2.71875))
 plt.bar(models, accuracies, color='maroon',
 width=0.3125)
 plt.xlabel("Model")
 plt.ylabel("F1 Score in %")
 plt.title("F1 Score")
 # creating the bar plot
 plt.savefig("C:/Users/moham/Desktop/PRODA NEW/F1Score.png")
 plt.close()
 # This file was generated by the Tkinter Designer by Parth Jadhav
 # https://github.com/ParthJadhav/Tkinter-Designer
 from pathlib import Path
 # from tkinter import *
 # Explicit imports to satisfy Flake8
 from tkinter import Tk, Toplevel, Canvas, Entry, Text, Button, PhotoImage
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\Tkinter designer\Metric Graphs\build\assets\frame0")
def relative_to_assets(path: str) -> Path:
 return ASSETS_PATH / Path(path)
 window = Toplevel()
 window.geometry("1300x768")
 window.configure(bg="#181818")
 canvas = Canvas(
 window,
 bg="#181818",
 height=768,
 width=1300,
 bd=0,
 highlightthickness=0,
 relief="ridge"
 )
 canvas.place(x=0, y=0)
 image_image_1 = PhotoImage(
 file=relative_to_assets("image_1.png"))
 image_1 = canvas.create_image(
 650.0,
 34.0,
 image=image_image_1
 )
 image_image_2 = PhotoImage(
 file="C:/Users/moham/Desktop/PRODA NEW/Acc.png")
 image_2 = canvas.create_image(
 311.0,
 261.0,
 image=image_image_2
 )

 canvas.create_text(
 71.0,
 417.0,
 anchor="nw",
 text="F1 SCORE",
 fill="#FFFFFF",
 font=("Inter", 30 * -1)
 )
 image_image_3 = PhotoImage(
 file="C:/Users/moham/Desktop/PRODA NEW/Recall.png")
 image_3 = canvas.create_image(
 918.0,
 598.0,
 image=image_image_3
 )
 image_image_4 = PhotoImage(
 file="C:/Users/moham/Desktop/PRODA NEW/F1Score.png")
 image_4 = canvas.create_image(
 311.0,
 598.0,
 image=image_image_4
 )
 image_image_5 = PhotoImage(
 file="C:/Users/moham/Desktop/PRODA NEW/Prec.png")
 image_5 = canvas.create_image(
 918.0,
 261.0,
 image=image_image_5
 )
 canvas.create_text(
 71.0,
 87.0,
 anchor="nw",
 text="ACCURACY",
 fill="#FFFFFF",
 font=("Inter", 30 * -1)
 )
 canvas.create_text(
 678.0,
 417.0,
 anchor="nw",
 text="RECALL",
 fill="#FFFFFF",
 font=("Inter", 30 * -1)
 )
 canvas.create_text(
 678.0,
 89.0,
 anchor="nw",
 text="PRECISION",
 fill="#FFFFFF",
 font=("Inter", 30 * -1)
 )
 window.resizable(False, False)
 window.mainloop()



