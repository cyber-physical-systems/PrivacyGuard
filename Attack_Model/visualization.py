import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import os

path = ''
output_path = ''

devices = ['AmazonIn', 'AmazonOut', 'SwitchIn', 'SwitchOut', 'PrinterIn', 'PrinterOut',
           'BabyIn', 'BabyOut', 'MotionIn', 'MotionOut', 'scaleIn', 'scaleOut', 'LIFXIn', 'LIFXOut',
           'WeatherIn', 'WeatherOut', 'SpeakerIn', 'SpeakerOut', 'PlugIn', 'PlugOut',
           'iPhoneIn', 'iPhoneOut', 'AndroidIn', 'AndroidOut', 'LaptopIn', 'LaptopOut',
           'MacBookIn', 'MacBookOut', 'InsteonIn', 'InsteonOut', 'DropcamIn',
           'DropcamOut', 'SmartCamIn', 'SmartCamOut', 'TabIn', 'TabOut',
           'WelcomeIn', 'WelcomeOut', 'DayIn', 'DayOut']

dates = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
         '19', '20']
# dates = ['01']

for date in dates:

    df = pd.read_csv(path + str(date) + '.csv')

    for device in devices:

        #         data = df[device]
        data = df[df[device] != 0]

        data = data[device]
        #         data = data[~ data[device] == 0]
        #         print(data)

        if data.empty:
            pass

        else:

            ax = data.plot.hist()

            fig = ax.get_figure()

            device_path = output_path + device + '/'
            if not os.path.exists(device_path):
                os.makedirs(device_path)

            fig.savefig(device_path + str(date) + '.pdf')

            fig.clf()

