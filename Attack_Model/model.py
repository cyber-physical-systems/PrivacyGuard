import glob
import csv
import pandas
import os
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
from sklearn.metrics import cohen_kappa_score
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
import numpy as np


def naiveBayes(X_train, y_train):
    model = GaussianNB()
    model = model.fit(X_train, y_train)
    return (model)


def knn(X_train, y_train):
    model = KNeighborsClassifier()
    model = model.fit(X_train, y_train)
    return (model)


def decisionTree(X_train, y_train):
    model = tree.DecisionTreeClassifier(class_weight='balanced')
    model = model.fit(X_train, y_train)
    return (model)


def svm_linear(X_train, y_train):
    model = SVC(kernel='linear', class_weight='balanced')
    model = model.fit(X_train, y_train)
    return (model)


def svm_2(X_train, y_train):
    model = SVC(kernel='poly', class_weight='balanced', degree=2, random_state=0)
    model = model.fit(X_train, y_train)
    return (model)


def svm_3(X_train, y_train):
    model = SVC(kernel='poly', class_weight='balanced', degree=3, random_state=0)
    model = model.fit(X_train, y_train)
    return (model)


def svm_4(X_train, y_train):
    model = SVC(kernel='poly', class_weight='balanced', degree=4, random_state=0)
    model = model.fit(X_train, y_train)
    return (model)


def svm_5(X_train, y_train):
    model = SVC(kernel='poly', class_weight='balanced', degree=5, random_state=0)
    model = model.fit(X_train, y_train)
    return (model)


def svm_6(X_train, y_train):
    model = SVC(kernel='poly', class_weight='balanced', degree=6, random_state=0)
    model = model.fit(X_train, y_train)
    return (model)


def svm_7(X_train, y_train):
    model = SVC(kernel='poly', class_weight='balanced', degree=7, random_state=0)
    model = model.fit(X_train, y_train)
    return (model)


def svm_8(X_train, y_train):
    model = SVC(kernel='poly', class_weight='balanced', degree=8, random_state=0)
    model = model.fit(X_train, y_train)
    return (model)


def logisticRegression(X_train, y_train):
    model = LogisticRegression(class_weight='balanced')
    model = model.fit(X_train, y_train)
    return (model)


def passiveAggressiveClassifier(X_train, y_train):
    model = PassiveAggressiveClassifier(max_iter=1000, random_state=0, tol=1e-3, class_weight='balanced')
    model = model.fit(X_train, y_train)
    return (model)


def svm_rbf(X_train, y_train):
    model = SVC(kernel='rbf', class_weight='balanced')
    model = model.fit(X_train, y_train)
    return (model)


def random_forest(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0, class_weight='balanced')
    model = model.fit(X_train, y_train)
    return (model)


def ridgeClassifierCV(X_train, y_train):
    model = RidgeClassifierCV(alphas=[1e-3, 1e-2, 1e-1, 1], class_weight='balanced')
    model = model.fit(X_train, y_train)
    return (model)


def evaluation_result(y_test, y_pred, model, evaluation_path):
    cnf_matrix = confusion_matrix(y_test, y_pred, labels=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(cnf_matrix)

    FP = cnf_matrix.sum(axis=0) - np.diag(cnf_matrix)
    FN = cnf_matrix.sum(axis=1) - np.diag(cnf_matrix)
    TP = np.diag(cnf_matrix)
    TN = cnf_matrix.sum() - (FP + FN + TP)

    FP = FP.astype(int)
    FN = FN.astype(int)
    TP = TP.astype(int)
    TN = TN.astype(int)
    #     print(TP,TN,FP,FN)

    for i in range(0, 10):
        with open(evaluation_path + str(i) + '.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([model, TP[i], FN[i], TN[i], FP[i]])
        csvfile.close()


#
models = ['original', 'HTR', 'RTP', 'PrivacyGuard']

for model in models:

    evaluation_path = '' + str(
        model) + '/'
    if not os.path.exists(evaluation_path):
        os.makedirs(evaluation_path)

    for i in range(0, 10):
        with open(evaluation_path + str(i) + '.csv', 'w') as new:
            realnames = ['model', 'TP', 'FN', 'TN', 'FP']
            writer = csv.DictWriter(new, fieldnames=realnames)
            writer.writeheader()
        new.close()

    data_path = ""

    data = pd.read_csv(data_path + str(model) + '_feature.csv')

    feature_cols = ['total_in', 'total_out', 'peak_in_range', 'peak_out_range', 'peak_in_var', 'peak_out_var',
                    'peak_in_std', 'peak_out_std', 'peak_in_duration', 'peak_out_duration',
                    'peak_in_mean', 'peak_out_mean', 'peak_in_area',
                    'peak_out_area', 'peak_in_skew', 'peak_in_skew',
                    'peak_in_cv', 'peak_out_cv']

    X_train = data[feature_cols]
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)  # Features

    y_train = data['label'].astype(int)

    data_test = pd.read_csv(data_path + str(model) + '_feature.csv')

    X_test = data_test[feature_cols]
    scaler = StandardScaler()
    X_test = scaler.fit_transform(X_test)  # Features
    y_test = data_test['label'].astype(int)  # Target variable

    model = decisionTree(X_train, y_train)
    y_pred = model.predict(X_test)
    evaluation_result(y_test, y_pred, 'decisionTree', evaluation_path)

    model = logisticRegression(X_train, y_train)
    y_pred = model.predict(X_test)
    evaluation_result(y_test, y_pred, 'logisticRegression', evaluation_path)

    model = svm_linear(X_train, y_train)
    y_pred = model.predict(X_test)
    evaluation_result(y_test, y_pred, 'svm_linear', evaluation_path)

    model = svm_rbf(X_train, y_train)
    y_pred = model.predict(X_test)
    evaluation_result(y_test, y_pred, 'svm_rbf', evaluation_path)

    model = knn(X_train, y_train)
    y_pred = model.predict(X_test)
    evaluation_result(y_test, y_pred, 'knn', evaluation_path)

    model = naiveBayes(X_train, y_train)
    y_pred = model.predict(X_test)
    evaluation_result(y_test, y_pred, 'naiveBayes', evaluation_path)

    model = random_forest(X_train, y_train)
    y_pred = model.predict(X_test)
    evaluation_result(y_test, y_pred, 'random_forest', evaluation_path)




















