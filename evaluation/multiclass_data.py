import glob
import csv
import pandas


# get the rows whose label is 1
# realnames = ['Time', 'Size', 'TPLink Router Bridge LAN (Gateway)', 'Samsung SmartCam', 'Belkin Motion',
#                      'Belkin Switch', 'LIFX Smart Bulb', 'Insteon Camera Wired',
#                      'PIX-STAR Photo-frame', 'Netatmo Weather Station', 'NEST Smoke Alarm',
#                      'Amazon Echo', 'Samsung Galaxy Tab', 'Withings Smart scale', 'Netatmo Welcome Camera',
#                      'HP Printer', 'MacBook', 'Smart Things', 'Withings Smart Baby Monitor',
#                      'iHome Plug', 'Laptop', 'TP-Link Day Night Cloud camera', 'Android Phone 2',
#                      'Triby Speaker', 'Android Phone 1', 'Dropcam', 'Withings Aura smart sleep sensor',
#                      '', 'Nest Dropcam', 'iPhone', 'Blipcare BloodPressure Meter', 'Insteon Camera Wireless',
#                     'MacBookiPhone','label']
# # realnames = ['Time','Size','label']
#
# with open('/final/multiclass_update/basic/label_1.csv', 'w') as new:
#     writer = csv.DictWriter(new, fieldnames=realnames)
#     writer.writeheader()
# new.close()
#
# for test in glob.glob("./final/PG_plus/all.csv"):
#     with open(test, 'r') as csv_file:
#         reader = csv.DictReader(csv_file)
#         for row in reader:
#             if row['label'] == '1':
#                 with open('./final/multiclass/plus/label_1.csv', 'a') as new:
#                     new_data = csv.writer(new)
#                     new_data.writerow([row['Time'], row['Size'],row['label']])
#                     new_data.writerow(
#                         [row['Time'], row['Size'], row['TPLink Router Bridge LAN (Gateway)'], row['Samsung SmartCam'],
#                          row['Belkin Switch'],
#                          row['Belkin Motion'], row['PIX-STAR Photo-frame'], row['Netatmo Weather Station'],
#                          row['Amazon Echo'],
#                          row['Smart Things'], row['Withings Smart scale'], row['NEST Smoke Alarm'],
#                          row['Netatmo Welcome Camera'],
#                          row['Android Phone 2'], row['Laptop'], row['HP Printer'],
#                          row['TP-Link Day Night Cloud camera'], row['iPhone'],
#                          row['Samsung Galaxy Tab'], row['Blipcare BloodPressure Meter'], row['LIFX Smart Bulb'],
#                          row['Insteon Camera Wired'],
#                          row['MacBook'], row['Withings Smart Baby Monitor'], row['iHome Plug'], row['Triby Speaker'],
#                          row['Android Phone 1'],
#                          row['Dropcam'], row['Withings Aura smart sleep sensor'], row[''], row['Nest Dropcam'],
#                          row['Insteon Camera Wireless'], row['MacBook/iPhone'], row['label']])
#                     new.close()
#
#     csv_file.close()
#
#


# get the sensor lists to label the user activity
# realnames = ['Time', 'Size','LIFX Smart Bulb', 'Insteon Camera Wired',
#                      'PIX-STAR Photo-frame', 'Netatmo Weather Station', 'NEST Smoke Alarm',
#                      'Amazon Echo', 'Samsung Galaxy Tab', 'Withings Smart scale', 'Netatmo Welcome Camera',
#                      'HP Printer', 'MacBook', 'Smart Things', 'Withings Smart Baby Monitor',
#                      'iHome Plug', 'Laptop', 'TP-Link Day Night Cloud camera', 'Android Phone 2',
#                      'Triby Speaker', 'Android Phone 1', 'Dropcam', 'Withings Aura smart sleep sensor',
#                      '', 'Nest Dropcam', 'iPhone', 'Blipcare BloodPressure Meter', 'Insteon Camera Wireless',
#                     'MacBookiPhone']
#
#
# with open('./multiclass/label_1.csv','r') as csv_file:
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         sensor =[]
#         for element in realnames:
#             if (row[element] == '1'):
#                 sensor.append(element)
#         time = row['Time']
#         size = row["Size"]
#         with open('./multiclass/sensor_list.csv', 'a') as new:
#             writer = csv.writer(new)
#             writer.writerow([time, size, sensor])
#             # print(time,size,label)
#         new.close()

# train the multi_class label


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
from pycm import *
from sklearn.metrics import f1_score
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import  cohen_kappa_score
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
import numpy as np




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

data = pd.read_csv("./final/multiclass_update/plus/multi_class_data.csv")
data = data.dropna()

feature_cols = ['Size', 'TPLink Router Bridge LAN (Gateway)', 'Samsung SmartCam', 'Belkin Motion',
                     'Belkin Switch', 'LIFX Smart Bulb', 'Insteon Camera Wired',
                     'PIX-STAR Photo-frame', 'Netatmo Weather Station', 'NEST Smoke Alarm',
                     'Amazon Echo', 'Samsung Galaxy Tab', 'Withings Smart scale', 'Netatmo Welcome Camera',
                     'HP Printer', 'MacBook', 'Smart Things', 'Withings Smart Baby Monitor',
                     'iHome Plug', 'Laptop', 'TP-Link Day Night Cloud camera', 'Android Phone 2',
                     'Triby Speaker', 'Android Phone 1', 'Dropcam', 'Withings Aura smart sleep sensor',
                    'Nest Dropcam', 'iPhone', 'Blipcare BloodPressure Meter', 'Insteon Camera Wireless',
                    'MacBookiPhone']
# feature_cols = ['Size']
X = data[feature_cols]
scaler = StandardScaler()
X = scaler.fit_transform(X)# Features
y = data.label # Target variable

# instantiate the model (using the default parameters)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30)

# d = [decisionTree, logisticRegression,knn, svm_linear, svm_2,svm_3,svm_rbf,ridgeClassifierCV,naiveBayes,cnn_3layers]
model = naiveBayes(X_train, y_train)

y_pred = model.predict(X_test)

cnf_matrix = confusion_matrix(y_test, y_pred)

FP = cnf_matrix.sum(axis=0) - np.diag(cnf_matrix)
FN = cnf_matrix.sum(axis=1) - np.diag(cnf_matrix)
TP = np.diag(cnf_matrix)
TN = cnf_matrix.sum() - (FP + FN + TP)

FP = FP.astype(int)
FN = FN.astype(int)
TP = TP.astype(int)
TN = TN.astype(int)
print(TP,TN,FP,FN)


activity = ['work','go_back_home','baby_present','entertainment','smoke','alexa','others','print','check_body_condition']
for i in range (0,9):
    # with open('./final/multiclass_update/plus/' + activity[i] +' .csv', 'w') as new:
    #     realnames = ['model','TP','FN','TN','FP']
    #     writer = csv.DictWriter(new, fieldnames = realnames)
    #     writer.writeheader()
    # new.close()

    csvpath = './final/multiclass_update/plus/' + activity[i] +' .csv'
    with open(csvpath,  'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['naiveBayes',TP[i], FN[i],TN[i],FP[i]])
    csvfile.close()
#












