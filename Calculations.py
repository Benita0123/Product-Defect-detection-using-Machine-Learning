import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import xgboost as xgb

def calculations(sec_window, image_folder, loading_window, percent_label, wait_label):

    global y_test, svc_classifier, nb_classifier ,xgb_classifier, svc_accuracy,nb_accuracy,xgb_accuracy,svc_predictions,nb_predictions,xgb_predictions


    non_def_images = load_images_from_folder(os.path.join(image_folder, "ok_front"))
    def_images = load_images_from_folder(os.path.join(image_folder, "def_front"))


    # Combine images and labels
    X = np.array(non_def_images + def_images)          #image data
    y = np.array([0] * len(non_def_images) + [1] * len(def_images))   #labels 0 - non def   1 - def


    # Resize and flattening images
    X = np.array([cv2.resize(img, (100, 100)).flatten() for img in X])
    X = X / 255.0


    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize classifiers
    svc_classifier = SVC(kernel='linear')
    nb_classifier = GaussianNB()
    xgb_classifier = xgb.XGBClassifier()

    # Train classifiers
    svc_classifier.fit(X_train, y_train)
    nb_classifier.fit(X_train, y_train)
    xgb_classifier.fit(X_train, y_train)

    # Make predictions on test set
    svc_predictions = svc_classifier.predict(X_test)
    nb_predictions = nb_classifier.predict(X_test)
    xgb_predictions = xgb_classifier.predict(X_test)

    # Calculate accuracies
    svc_accuracy = accuracy_score(y_test, svc_predictions)
    nb_accuracy = accuracy_score(y_test, nb_predictions)
    xgb_accuracy = accuracy_score(y_test, xgb_predictions)

    # Precision
    svc_precision = precision_score(y_test, svc_predictions)
    nb_precision = precision_score(y_test, nb_predictions)
    xgb_precision = precision_score(y_test, xgb_predictions)

    # Recall
    svc_recall = recall_score(y_test, svc_predictions)
    nb_recall = recall_score(y_test, nb_predictions)
    xgb_recall = recall_score(y_test, xgb_predictions)

    # F1-score
    svc_f1score = f1_score(y_test, svc_predictions)
    nb_f1score = f1_score(y_test, nb_predictions)
    xgb_f1score = f1_score(y_test, xgb_predictions)

    # Specificity (True Negative Rate)
    def calculate_specificity(cm):
        TN = cm[0, 0]
        FP = cm[0, 1]
        return TN / (TN + FP)

    specificity_svc = calculate_specificity(confusion_matrix(y_test, svc_predictions))
    specificity_nb = calculate_specificity(confusion_matrix(y_test, nb_predictions))
    specificity_xgb = calculate_specificity(confusion_matrix(y_test, xgb_predictions))

     

calculations()