import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix


# Define functions to calculate confusion matrices for each classifier
def svc_cn():
    global y_test, svc_predictions
    svc_cm = confusion_matrix(y_test, svc_predictions)
    plot_confusion_matrix(svc_cm, 'Confusion Matrix - Support Vector Classifier')

def nb_cn():
    global y_test, nb_predictions
    nb_cm = confusion_matrix(y_test, nb_predictions)
    plot_confusion_matrix(nb_cm, 'Confusion Matrix - Naive Bayes Classifier')

def xgb_cn():
    global y_test, xgb_predictions
    xgb_cm = confusion_matrix(y_test, xgb_predictions)
    plot_confusion_matrix(xgb_cm, 'Confusion Matrix - XGBoost Classifier')

# Function to plot confusion matrix
def plot_confusion_matrix(cm, title):
    plt.figure(figsize=(8, 6))
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title(title)
    plt.colorbar()
    plt.xlabel('Predicted Labels')
    plt.ylabel('True Labels')
    classes = ['Non-Def', 'Def'] 
    plt.xticks(np.arange(len(classes)), classes)
    plt.yticks(np.arange(len(classes)), classes)

    # Define positions for TN, TP, FP, FN based on 2x2 matrix
    tn = cm[0, 0]
    fp = cm[0, 1]
    fn = cm[1, 0]
    tp = cm[1, 1]

    # Add annotations (TN, TP, FP, FN) to the plot
    plt.text(0, 0, f'\n\n{tn}\nTN\n(True Negative)', horizontalalignment="center", color="white", fontsize=12)
    plt.text(1, 1, f'\n\n{tp}\nTP\n(True Positive)', horizontalalignment="center", color="black", fontsize=12)
    plt.text(1, 0, f'\n\n{fn}\nFN\n(False Negative)', horizontalalignment="center", color="black", fontsize=12)
    plt.text(0, 1, f'\n\n{fp}\nFP\n(False Positive)', horizontalalignment="center", color="black", fontsize=12)


    plt.tight_layout()
    plt.show()

svc_cn()
nb_cn()
xgb_cn()
    