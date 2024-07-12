
def show(data, labels, Gvalue, Cvalue):
 import warnings
 warnings.simplefilter("ignore")
 import matplotlib.pyplot as plt
 import numpy as np
 from sklearn.svm import SVC
 from PIL import Image
 from sklearn.naive_bayes import GaussianNB
 from sklearn.model_selection import learning_curve, ShuffleSplit
 svcp = SVC(gamma=Gvalue, C=Cvalue)
 X = data
 y = labels
 train_sizes, train_scores, test_scores = learning_curve(svcp, X, y, 
cv=10,
 
scoring='accuracy', n_jobs=-1,
 
train_sizes=np.linspace(0.01, 1.0, 50))
 train_mean = np.mean(train_scores, axis=1)
 train_std = np.std(train_scores, axis=1)
 test_mean = np.mean(test_scores, axis=1)
 test_std = np.std(test_scores, axis=1)
 plt.subplots(1, figsize=(10, 10))
 plt.plot(train_sizes, train_mean, '--', color="#111111", 
label="Training score")
 plt.plot(train_sizes, test_mean, color="#111111", label="Cross￾validation score")
 plt.fill_between(train_sizes, train_mean - train_std, train_mean + 
train_std, color="#DDDDDD")
 plt.fill_between(train_sizes, test_mean - test_std, test_mean + 
test_std, color="#DDDDDD")
 plt.title("Learning Curve for SVC")
 plt.xlabel("Training Set Size"), plt.ylabel("Accuracy Score"), 
 plt.legend(loc="best")
 plt.tight_layout()
 plt.savefig("C:/Users/moham/Desktop/PRODA NEW/SVCLC.png")
 plt.close()
 image = Image.open("C:/Users/moham/Desktop/PRODA NEW/SVCLC.png")
 print("Finished SVC")
 image = image.resize((480, 261))
 image.save("C:/Users/moham/Desktop/PRODA NEW/SVCLC.png")
 import warnings
 warnings.filterwarnings("ignore")
 # load libraries
 import numpy as np
 from xgboost import XGBClassifier
 import matplotlib.pyplot as plt
 plt.style.use('ggplot')

 from sklearn import datasets
 import matplotlib.pyplot as plt
 from sklearn.model_selection import learning_curve
 # Create CV training and test scores for various training set sizes
 train_sizes, train_scores, test_scores = learning_curve(XGBClassifier(),
 X, y, cv=10, 
scoring='accuracy', n_jobs=-1,
 # 50 different sizes of the training set
 
train_sizes=np.linspace(0.01, 1.0, 50))
 # Create means and standard deviations of training set scores
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
 # Create means and standard deviations of test set scores
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)
 # Draw lines
plt.subplots(1, figsize=(7, 7))
plt.plot(train_sizes, train_mean, '--', color="#111111", 
label="Training score")
plt.plot(train_sizes, test_mean, color="#111111", label="Cross￾validation score")
 # Draw bands
plt.fill_between(train_sizes, train_mean - train_std, train_mean + 
train_std, color="#DDDDDD")
plt.fill_between(train_sizes, test_mean - test_std, test_mean + 
test_std, color="#DDDDDD")
 # Create plot
plt.title("Learning Curve of XGBoost")
plt.xlabel("Training Set Size"), plt.ylabel("Accuracy Score"), 
plt.legend(loc="best")
plt.tight_layout();
plt.savefig("C:/Users/moham/Desktop/PRODA NEW/XGBLC.png")
plt.close()
image = Image.open("C:/Users/moham/Desktop/PRODA NEW/XGBLC.png")
image = image.resize((480, 261))
image.save("C:/Users/moham/Desktop/PRODA NEW/XGBLC.png")
print("Finished XGB")
X = data
y = labels
train_sizes, train_scores, test_scores = learning_curve(GaussianNB(), 
X, y, cv=10,
 
scoring='accuracy', n_jobs=-1,
 
train_sizes=np.linspace(0.01, 1.0, 50))
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)
plt.subplots(1, figsize=(10, 10))
plt.plot(train_sizes, train_mean, '--', color="#111111", 
label="Training score")
plt.plot(train_sizes, test_mean, color="#111111", label="Cross￾validation score")
plt.fill_between(train_sizes, train_mean - train_std, train_mean + 
train_std, color="#DDDDDD")
plt.fill_between(train_sizes, test_mean - test_std, test_mean + 
test_std, color="#DDDDDD")
plt.title("Learning Curve for Naive Bayes")
plt.xlabel("Training Set Size"), plt.ylabel("Accuracy Score"), 
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("C:/Users/moham/Desktop/PRODA NEW/GNBLC.png")
plt.close()
image = Image.open("C:/Users/moham/Desktop/PRODA NEW/GNBLC.png")
image = image.resize((480, 261))
image.save("C:/Users/moham/Desktop/PRODA NEW/GNBLC.png")
print("Finished GNB")
from pathlib import Path
 # from tkinter import *
 # Explicit imports to satisfy Flake8
from tkinter import Tk, Toplevel, Canvas, Entry, Text, Button, PhotoImage
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\Tkinter designer\Accuracy Loss\build\assets\frame0")
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
 33.0,
 image=image_image_1
 )
 image_image_2 = PhotoImage(
 file="C:/Users/moham/Desktop/PRODA NEW/SVCLC.png")
 image_2 = canvas.create_image(
 311.0,
 261.0,
 image=image_image_2
 )
 image_image_3 = PhotoImage(
 file="C:/Users/moham/Desktop/PRODA NEW/XGBLC.png")
 image_3 = canvas.create_image(
 311.0,
 598.0,
 image=image_image_3
 )
 image_image_4 = PhotoImage(
 file="C:/Users/moham/Desktop/PRODA NEW/GNBLC.png")
 image_4 = canvas.create_image(
 918.0,
 261.0,
 image=image_image_4
 )
 window.resizable(False, False)
 window.mainloop()
