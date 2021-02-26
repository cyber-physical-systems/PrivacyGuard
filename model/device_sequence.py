# univariate lstm example
from numpy import array
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
import pandas as pd 
import numpy as np
np.random.seed(7) 
import csv
from tensorflow import keras
from keras.utils import to_categorical
from pandas import Series
from sklearn.preprocessing import MinMaxScaler
from keras.utils import to_categorical
from keras.layers import Flatten
from keras.layers import Dropout

# split a univariate sequence into samples
def split_sequence(sequence, n_steps):
	X, y = list(), list()
	for i in range(len(sequence)):
		# find the end of this pattern
		end_ix = i + n_steps
		# check if we are beyond the sequence
		if end_ix > len(sequence)-1:
			break
		# gather input and output parts of the pattern
		seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
		X.append(seq_x)
		y.append(seq_y)
	return array(X), array(y)


def data_prepare(data_train_path):
    data_file = open(data_train_path)
#     reader = csv.reader(data_file, delimiter=",")
    reader = csv.reader(data_file) 
    sequence= []
    for row in reader:
        sequence.append(int(row[0]))
#     print(sequence)     
    return(sequence) 


data_train_path = ' '
raw_seq = data_prepare(data_train_path)  

# choose a number of time steps
n_steps = 10
# split into samples
X, y = split_sequence(raw_seq, n_steps)
print(X.shape)
# reshape from [samples, timesteps] into [samples, timesteps, features]
n_features = 1
X = np.atleast_2d(X)
X = X.reshape((X.shape[0], X.shape[1], n_features))
y = to_categorical(y)

# define model
model = Sequential()
model.add(LSTM(100, input_shape=(n_steps, n_features)))
model.add(Dropout(0.5))
model.add(Dense(100, activation='relu'))
model.add(Dense(6, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit model
model.fit(X, y, epochs=100, verbose=2)
model.save(' ')
