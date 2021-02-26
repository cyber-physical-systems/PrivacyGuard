import pandas as pd 
import numpy as np
import csv


def data_prepare(data_path):
    data_file = open(data_path)
    reader = csv.reader(data_file, delimiter=",")
    Amazon = []
    Motion = []
    Switch = []
    Printer = []
    SmartCam = []
    Baby = []
    Phone1 = []
    Laptop = []
    Macbook = []
    Phone2 = []
    iphone = []
    Mac_iphone = []
    Activity = []
    for row in reader:
        # get the data sequence
        Amazon.append(int(row[2]))
        Motion.append(int(row[3]))
        Switch.append(int(row[4]))
        Printer.append(int(row[6]))
        SmartCam.append(int(row[14]))
        Baby.append(int(row[19]))
        Phone1.append(int(row[24]))
        Laptop.append(int(row[25]))
        Macbook.append(int(row[26]))
        Phone2.append(int(row[27]))
        iphone.append(int(row[28]))
        Mac_iphone.append(int(row[29]))
        Activity.append(int(row[30]))
    data_file.close()
    Amazon = np.array(Amazon).reshape((len(Amazon), 1))
    Motion = np.array(Motion).reshape((len(Motion), 1))
    Switch = np.array(Switch).reshape((len(Switch), 1))
    Printer = np.array(Printer).reshape((len(Printer), 1))
    SmartCam = np.array(SmartCam).reshape((len(SmartCam), 1))
    Baby = np.array(Baby).reshape((len(Baby), 1))
    Phone1 = np.array(Phone1).reshape((len(Phone1), 1))
    Laptop = np.array(Laptop).reshape((len(Laptop), 1))
    Macbook = np.array(Macbook).reshape((len(Macbook), 1))
    Phone2 = np.array(Phone2).reshape((len(Phone2), 1))
    iphone = np.array(iphone).reshape((len(iphone), 1))
    Mac_iphone = np.array(Mac_iphone).reshape((len(Mac_iphone), 1))
    Activity = np.array(Activity).reshape((len(Activity), 1))
    # horizontally stack columns
    dataset = hstack((Amazon, Motion, Switch,Printer, SmartCam, Baby, Phone1, Laptop, Macbook, Phone2, iphone, Mac_iphone,Activity))
    return(dataset)


from numpy import array
from numpy import hstack
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.utils import to_categorical
from keras.layers import Flatten
from keras.layers import Dropout
from tensorflow import keras
 
# split a multivariate sequence into samples
def split_sequences(sequences, n_steps):
	X, y = list(), list()
	for i in range(len(sequences)):
		# find the end of this pattern
		end_ix = i + n_steps
		# check if we are beyond the dataset
		if end_ix > len(sequences):
			break
		# gather input and output parts of the pattern
		seq_x, seq_y = sequences[i:end_ix, :-1], sequences[end_ix-1, -1]
		X.append(seq_x)
		y.append(seq_y)
	return array(X), array(y)
 

# choose a number of time steps
for n_steps in range(11,21):
#     n_steps = 3
    data_path = ' '
    dataset = data_prepare(data_path)
    # convert into input/output
    X, y = split_sequences(dataset, n_steps)
#     df = pd.DataFrame(y)

    y = to_categorical(y)
    # the dataset knows the number of features, e.g. 2
    n_features = X.shape[2]

#     define model
    model = Sequential()
    model.add(LSTM(100, input_shape=(n_steps, n_features)))
    model.add(Dropout(0.5))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(8, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    # fit model
    model.fit(X, y, epochs=50, verbose=2)
# model.save(' '+ str(n_steps))
# model = keras.models.load_model(' '+ str(n_steps))
# demonstrate prediction
    data_path_test = ' '
    dataset_test = data_prepare(data_path_test)
    # convert into input/output
    X_test, y_test = split_sequences(dataset_test, n_steps)
    df = pd.DataFrame(y_test)

    y_test = to_categorical(y_test)
    x_input = X_test
    yhat =model.predict_classes(x_input)
    yhat = pd.DataFrame(yhat)
    df = pd.concat([df, yhat], axis=1)
    pd.DataFrame(df).to_csv("predict_timestamps_" + str(n_steps)+ '.csv',header=None, index=None)