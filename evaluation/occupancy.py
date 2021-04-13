# this is used to train the model, try different model, generate the csv file of the result

import math
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import csv
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.linear_model import RidgeClassifierCV
import attr
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB


def  naiveBayes(X_train, y_train):
    model = GaussianNB()
    model = model.fit(X_train, y_train)
    return (model)


def  knn(X_train, y_train):
    model = KNeighborsClassifier()
    model = model.fit(X_train, y_train)
    return (model)

def  decisionTree(X_train, y_train):
    model = tree.DecisionTreeClassifier(class_weight='balanced')
    model = model.fit(X_train, y_train)
    return (model)

def svm_linear(X_train, y_train):
    model = SVC(kernel='linear', class_weight='balanced')
    model = model.fit(X_train, y_train)
    return (model)


def svm_2(X_train, y_train):
    model = SVC(kernel='poly',class_weight='balanced', degree=2, random_state=0)
    model = model.fit(X_train, y_train)
    return (model)

def svm_3(X_train, y_train):
    model = SVC(kernel='poly',class_weight='balanced', degree=3, random_state=0)
    model = model.fit(X_train, y_train)
    return (model)

def svm_4(X_train, y_train):
    model = SVC(kernel='poly',class_weight='balanced', degree=4, random_state=0)
    model = model.fit(X_train, y_train)
    return (model)

def svm_5(X_train, y_train):
    model = SVC(kernel='poly',class_weight='balanced', degree=5, random_state=0)
    model = model.fit(X_train, y_train)
    return (model)

def svm_6(X_train, y_train):
    model = SVC(kernel='poly',class_weight='balanced', degree=6, random_state=0)
    model = model.fit(X_train, y_train)
    return (model)

def svm_7(X_train, y_train):
    model = SVC(kernel='poly',class_weight='balanced', degree=7, random_state=0)
    model = model.fit(X_train, y_train)
    return (model)

def svm_8(X_train, y_train):
    model = SVC(kernel='poly',class_weight='balanced', degree=8, random_state=0)
    model = model.fit(X_train, y_train)
    return (model)

def logisticRegression(X_train, y_train):
    model = LogisticRegression(class_weight = 'balanced')
    model = model.fit(X_train, y_train)
    return (model)

def passiveAggressiveClassifier(X_train, y_train):
    model =PassiveAggressiveClassifier(max_iter=1000, random_state=0,tol=1e-3,class_weight='balanced')
    model = model.fit(X_train, y_train)
    return (model)


def svm_rbf(X_train, y_train):
    model = SVC(kernel='rbf',class_weight='balanced')
    model = model.fit(X_train, y_train)
    return (model)

def ridgeClassifierCV(X_train, y_train):
    model = RidgeClassifierCV(alphas=[1e-3, 1e-2, 1e-1, 1],class_weight='balanced')
    model = model.fit(X_train, y_train)
    return (model)


data = pd.read_csv('C:/penv/PGOnline/groundtruth_data/merged.csv')
data = data.dropna()
# feature_cols = ['TPLink Router Bridge LAN (Gateway)', 'Samsung SmartCam', 'Belkin Switch',
#             'Belkin Motion', 'PIX-STAR Photo-frame', 'Netatmo Weather Station', 'Amazon Echo',
#             'Smart Things', 'Withings Smart scale', 'NEST Smoke Alarm', 'Netatmo Welcome Camera',
#             'Android Phone 2', 'Laptop', 'HP Printer', 'TP-Link Day Night Cloud camera', 'iPhone',
#             'Samsung Galaxy Tab', 'Blipcare BloodPressure Meter']
feature_cols = ['Size']
X = data[feature_cols]
scaler = StandardScaler()
X = scaler.fit_transform(X)  # Features
y = data.label  # Target variable

# instantiate the model (using the default parameters)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30)

# d = [decisionTree, logisticRegression,knn, svm_linear, svm_2,svm_3,svm_rbf,ridgeClassifierCV,naiveBayes]
model = ridgeClassifierCV(X_train, y_train)   # need to choose we use which model
y_pred = model.predict(X_test)

tn, fp, fn, tp = confusion_matrix(y_test,y_pred).ravel()
mcc = ((tp * tn) - (fp * fn)) / math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
print(tn, fp, fn, tp, mcc)


with open('C:/penv/PGOnline/groundtruth_data/testresult/result.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ridgeClassifierCV', tn, fp, fn, tp, mcc])
csvfile.close()

