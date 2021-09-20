
# PrivacyGuard: Enhancing Smart Home User Privacy

Keyang Yu, Qi Li, Dong Chen, Mohammad Rahman and Shiqiang Wang. 2021. PrivacyGuard: Enhancing Smart Home User Privacy. In The 20th International Conference on Information Processing in Sensor Networks (co- located with CPS-IoT Week 2021) (IPSN ’21), May 18–21, 2021, Nashville, TN, USA. ACM, New York, NY, USA, 15 pages. https://doi.org/10.1145/ 3412382.3458257

The Internet of Things (IoT) devices have been increasingly deployed in smart homes and smart buildings to monitor and control their environments. The Internet traffic data produced by these IoT devices are collected by Internet Service Providers (ISPs) and IoT device manufacturers, and often shared with third-parties to maintain and enhance user services. Unfortunately, extensive recent research has shown that on-path adversaries can infer and fingerprint users’ sensitive privacy information such as occupancy and user in-home activities by analyzing IoT network traffic traces. Most recent approaches that aim at defending against these malicious IoT traffic analytics can not sufficiently protect user privacy with reasonable traffic overhead. In particular, many approaches did not consider practical limitations, e.g., network bandwidth, maximum package injection rate or actual user in-home behavior in their design. To address this problem, we design a new low-cost, open-source user “tunable” defense system—PrivacyGuard that enables users to significantly reduce the private information leaked through IoT device network traffic data, while still permitting sophisticated data analytics or control that is necessary in smart home management. In essence, our approach employs intelligent deep convolutional generative adversarial networks (DCGANs)-based IoT device traffic signature learning, long short-term memory (LSTM)-based artificial traffic signature injection, and partial traffic reshaping to obfuscate private information that can be observed in IoT device traffic traces. We evaluate PrivacyGuard using IoT network traffic traces of 31 IoT devices from 5 smart homes. We find that PrivacyGuard can effectively prevent a wide range of state-of-the-art machine learning-based and deep learning-based occupancy and other 9 user in-home activity detection attacks. We release the source code and datasets of PrivacyGuard to the IoT research community.

# Attacking Model
Section 3 Privacy Leakage Identification

## `FeatureSelection.py`
Section 3.1 Feature Selection

`peak_find.py` is used to find spikes, you can set the "distance" value by yourself. 
"peak_features_extraction.py" is used to extract statistical features based on the time series motifs of each IoT device. 

## `Model.py`
Section 3.2 Machine Learning-based Attacks

`Model.py` contains 16 Machine learn-based attack models.

Change the path:
```
data_path = '/desinated/read/path/'
evaluation_path = '/desinated/save/path/' + str(model) + '/'
```
Add additional features according to the feature selection result"
```
feature_cols = ['total_in', 'total_out', 'peak_in_range', 'peak_out_range', 'peak_in_var', 'peak_out_var',
                'peak_in_std', 'peak_out_std', 'peak_in_duration', 'peak_out_duration',
                'peak_in_mean', 'peak_out_mean', 'peak_in_area',
                'peak_out_area', 'peak_in_skew', 'peak_in_skew',
                'peak_in_cv', 'peak_out_cv']
```

## `DeepLearning.py`
Section 3.3 Deep Learning-based Attacks

`human_activity_recognition_rnn.py` uses the recurrent neural network model to attack. You can set  n_steps as ticks of time. The input is time-series traffic data, the output is user activity. 

# Data Preprocessing
Section 4.3 Intelligent Traffic Rate Signature Learning

The pcap data captured from TCPDump/Wireshark have to be processed to CSV format before putting into PrivacyGuard. You can use Tshark commands such as:
```
tshark -r traffic.pcap > traffic.csv
```
The CSV file should have the following columns:
```
'Packet ID','TIME','Size','eth.src','eth.dst','IP.src','IP.dst','IP.proto','port.src','port.dst'
```

## `DeviceLabeling.py`
`DeviceLabeling.py` is used to label IoT devices with the device names. 

Change the path:
```
read_path = '/desinated/read/path/'
save_path = '/desinated/save/path/'
```

Add additional device MAC address and device name pair in the following format:
```
df.loc[df['eth.src'].str.contains('44:65:0d:56:cc:d3'), 'DeviceOut'] = 'Amazon Echo'
df.loc[df['eth.dst'].str.contains('44:65:0d:56:cc:d3'), 'DeviceIn'] = 'Amazon Echo'
```

The output CSV file should have the following columns:
```
'TIME','Size','DeviceOut','DeviceIn'
```

## `GroundTruth.py`
`GroundTruth.py` is used to label the groundtruth for user activities.

Change the path:
```
read_path = '/desinated/read/path/'
save_path = '/desinated/save/path/'
```

Customize the device traffic threshold by:
```
Device['Device'] = Device.In.apply(lambda x: 1 if x > 'int threshold' else 0)
```

Summarize user activities by:
```
device['Activity1'] = device.Device1.apply(lambda x: 1 if x > 0 else 0)
device.Activity1[device.Device2 > 0] = 1
device.Activity1[device.Device3 > 0] = 1
...
```


## `LocalMax.py`
`LocalMax.py` is used to filter out background traffics and find traffic pattern motifs.

Sequentially read the file by:
```
labelin = pd.read_csv('/file/path/In_fileNo.csv', header=None)
labelout = pd.read_csv('/file/path/Out_fileNo.csv', header=None)
```
Rename the columns by:
```
cols = ['Time', 'TotalIn', 'TotalOut', 'A', 'B', 'C', ..., 'Label']
```


# PrivacyGuard

## `PrivacyGuard.py`
Section 4.4 Artificial Traffic Signature Injection

Section 4.5 User Tunable Partial Traffic Reshaping

`PrivacyGuard.py` is simulating the basic version of PrivacyGuard. 

Change the path:
```
read_path = '/desinated/read/path/'
save_path = '/desinated/save/path/'
```

##  `PrivacyGuardPlus.py`
Section 4.6 Online Optimizations

Change the path:
```
df = pd.read_csv('/desinated/read/path/original.csv')
df.to_csv('C:/desinated/read/path/filename.csv', index=False)
```

Customize the inserting traffic load: 
```
insert = df[df[colum] > df[colum].quantile(.97)]
```
Customize the flattening threshold:
```
q = pd.Series([df[colum].quantile(0), df[colum].quantile(0.96)])
```

# Evaluation

## `Occupancy.py`
Section 6.4.1 Preventing Occupancy Detection

`Occupancy.py` is for detecting smart home occupancy.

## `Pearson.py`
Section 6.4.1 Preventing Occupancy Detection

 `Pearson.py` is used to calculate the Pearson Correlation Coefficient (PCC) and Spearman’s Rank Correlation Coefficient (SRCC).

## `UserActivity.py` 
Section 6.4.2 Preventing User Activities Detection Attacks

`UserActivity.py` is for detecting smart home user activity.
We have 16 models for attacking user activities in the smart home based on 8 traffic volume features.

Change the path:
```
data_path = '/desinated/read/path/'
evaluation_path = '/desinated/save/path/' + str(model) + '/'
```
Add additional features according to the feature selection result"
```
feature_cols = ['total_in', 'total_out', 'peak_in_range', 'peak_out_range', 'peak_in_var', 'peak_out_var',
                'peak_in_std', 'peak_out_std', 'peak_in_duration', 'peak_out_duration',
                'peak_in_mean', 'peak_out_mean', 'peak_in_area',
                'peak_out_area', 'peak_in_skew', 'peak_in_skew',
                'peak_in_cv', 'peak_out_cv']
```

## `AdditionalTraffic.py`
Section 6.4.3 Quantifying Traffic Overhead

`AdditionalTraffic.py` is used to compare the traffic overhead for different privacy-preserving models.

## Datasets

[UNSW Dataset](https://iotanalytics.unsw.edu.au/iottraces).
[SmartFIU Dataset](https://www.kaggle.com/keyangyu0421/cpslab-iot).
[Real Smart Homes](https://www.kaggle.com/keyangyu0421/smarthome-iot).
[Kaggle Dataset #1](https://www.kaggle.com/drwardog/iot-device-captures).
[Kaggle Dataset #2](https://www.kaggle.com/speedwall10/iot-device-network-logs).
