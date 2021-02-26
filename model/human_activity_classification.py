import glob
import csv
import pandas

# this is used to train the model, try different model, generate the csv file of the result

import pandas
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
# from pycm import *
from sklearn.metrics import f1_score
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import  cohen_kappa_score
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
import numpy as np


# evaluation_path = ' '
# # activity = ['work','go_back_home','baby_present','entertainment','smoke','alexa','others','print','check_body_condition']
# for i in range (0,9):
#     with open(evaluation_path + str(i) +'.csv', 'w') as new:
#         realnames = ['model','TP','FN','TN','FP']
#         writer = csv.DictWriter(new, fieldnames = realnames)
#         writer.writeheader()
#     new.close()




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

def random_forest(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, max_depth=2,random_state=0,class_weight='balanced')
    model = model.fit(X_train, y_train)
    return (model)


def ridgeClassifierCV(X_train, y_train):
    model = RidgeClassifierCV(alphas=[1e-3, 1e-2, 1e-1, 1],class_weight='balanced')
    model = model.fit(X_train, y_train)
    return (model)

def evaluation_result(y_test, y_pred,model):
    
    cnf_matrix = confusion_matrix(y_test, y_pred,labels=[0,1,2,3,4,5,6,7,8])
    print(cnf_matrix)

    FP = cnf_matrix.sum(axis=0) - np.diag(cnf_matrix)
    FN = cnf_matrix.sum(axis=1) - np.diag(cnf_matrix)
    TP = np.diag(cnf_matrix)
    TN = cnf_matrix.sum() - (FP + FN + TP)

    FP = FP.astype(int)
    FN = FN.astype(int)
    TP = TP.astype(int)
    TN = TN.astype(int)
    print(TP,TN,FP,FN)


    evaluation_path = ' '
    for i in range (0,9):
        with open(evaluation_path + str(i) +'.csv',  'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([model,TP[i], FN[i],TN[i],FP[i]])
        csvfile.close()
#
    


data = pd.read_csv(" ")
data = data.dropna()

feature_cols = ['Size', 'Amazon Echo',  'Belkin Motion',
                'Belkin Switch','Blipcare BloodPressure Meter','HP Printer','Dropcam','Insteon Camera',
                'LIFX Smart Bulb',   'NEST Smoke Alarm','Netatmo Welcome Camera', 'Netatmo Weather Station',
                'PIX-STAR Photo-frame','Samsung SmartCam','Smart Things', 'TP-Link Day Night Cloud camera',
                'TP-Link Smart plug','Triby Speaker','Withings Smart Baby Monitor','Withings Smart scale', 
                 'Withings Aura smart sleep sensor','iHome Plug', 'Samsung Galaxy Tab',  'Android Phone 1', 
                 'Laptop',  'MacBook',  'Android Phone 2','iPhone','MacBookiPhone']

X = data[feature_cols]
scaler = StandardScaler()
X = scaler.fit_transform(X)# Features
y = data['User Activity'] # Target variable

# instantiate the model (using the default parameters)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30)

# d = [decisionTree, logisticRegression,knn, svm_linear, svm_2,svm_3,svm_rbf,ridgeClassifierCV,naiveBayes,cnn_3layers,random_forest]
model =decisionTree(X_train, y_train)
y_pred = model.predict(X_test)
evaluation_result(y_test, y_pred,'random96_day_decisionTree')

model =logisticRegression(X_train, y_train)
y_pred = model.predict(X_test)
evaluation_result(y_test, y_pred,'random96_day_logisticRegression')


model =knn(X_train, y_train)
y_pred = model.predict(X_test)
evaluation_result(y_test, y_pred,'random96_day_knn')


model =svm_linear(X_train, y_train)
y_pred = model.predict(X_test)
evaluation_result(y_test, y_pred,'random96_day_svm_linear')


model =svm_rbf(X_train, y_train)
y_pred = model.predict(X_test)
evaluation_result(y_test, y_pred,'random96_day_svm_rbf')


model =naiveBayes(X_train, y_train)
y_pred = model.predict(X_test)
evaluation_result(y_test, y_pred,'random96_day_naiveBayes')


model =random_forest(X_train, y_train)
y_pred = model.predict(X_test)
evaluation_result(y_test, y_pred,'random96_day_random_forest')

















