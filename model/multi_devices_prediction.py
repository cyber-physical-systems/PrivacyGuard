# univariate lstm example
from numpy import array
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
import pandas as pd 
import numpy as np
import csv
from tensorflow import keras
 
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
    reader = csv.reader(data_file, delimiter=",") 
    MacBook_iPhone= []
    for row in reader:
         MacBook_iPhone.append(int(row[29]))
    return(MacBook_iPhone) 
data_train_path = ' '
raw_seq = data_prepare(data_train_path)  

# define input sequence
# raw_seq = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# choose a number of time steps
n_steps = 3
# split into samples
X, y = split_sequence(raw_seq, n_steps)
# reshape from [samples, timesteps] into [samples, timesteps, features]
n_features = 1
X = X.reshape((X.shape[0], X.shape[1], n_features))
# define model
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(n_steps, n_features)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')
# fit model
model.fit(X, y, epochs=200, verbose=2)
# model.save(' ')
# # demonstrate prediction

# model = keras.models.load_model('')
data_test_path = ' '
raw_seq_test = data_prepare(data_test_path)  

# define input sequence
# raw_seq = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# choose a number of time steps

# split into samples
X_test, y_test = split_sequence(raw_seq_test, n_steps)
# reshape from [samples, timesteps] into [samples, timesteps, features]

X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], n_features))
# define model



# x_input = array([70, 80, 90])
# x_input = x_input.reshape((1, n_steps, n_features))
yhat = np.int64(model.predict(X_test))
# yhat = model.predict(X_test, verbose=0)

print(yhat)
pd.DataFrame(yhat).to_csv(" ",header=None, index=None)