import os
import pandas as pd

read_path = 'C:/penv/IPSN/data/labeled/'
os.chdir(read_path)
file_list = os.listdir()

for i in file_list:
    df = pd.read_csv(i)
# --------------------------------------Total Traffic------------------------------------------------
    total = df[(df['DeviceIn'].str.contains('TPLink')) | (df['DeviceOut'].str.contains('TPLink'))]
    totalin = df[(df['DeviceOut'].str.contains('TPLink'))]
    totalout = df[(df['DeviceIn'].str.contains('TPLink'))]
    totalin = totalin.drop('DeviceOut', axis=1)
    totalin = totalin.drop('DeviceIn', axis=1)
    totalout = totalout.drop('DeviceOut', axis=1)
    totalout = totalout.drop('DeviceIn', axis=1)
    totalin['TIME'] = pd.to_datetime(totalin['TIME'], unit='s')
    totalin.index = totalin['TIME']
    totalin = totalin.Size.resample('1s').sum()
    totalout['TIME'] = pd.to_datetime(totalout['TIME'], unit='s')
    totalout.index = totalout['TIME']
    totalout = totalout.Size.resample('1s').sum()

    total = pd.concat([totalin, totalout], axis=1)
    col = ['TotalIn', 'TotalOut']
    total.columns = col
# --------------------------------------Total Traffic------------------------------------------------

# --------------------------------------Amazon Echo--------------------------------------------------
    out = df[(df['DeviceOut'].str.contains('Amazon')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('Amazon')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    Amazon = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    Amazon.columns = col
    Amazon['Amazon'] = Amazon.In.apply(lambda x: 1 if x > 400 else 0)
    Amazon.Amazon[Amazon.Out > 250] = 1
# --------------------------------------Amazon Echo--------------------------------------------------

# --------------------------------------Belkin Switch------------------------------------------------
    out = df[(df['DeviceOut'].str.contains('Switch')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('Switch')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    Switch = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    Switch.columns = col
    Switch['Switch'] = Switch.In.apply(lambda x: 1 if x > 600 else 0)
    Switch.Switch[Switch.Out > 500] = 1
# --------------------------------------Belkin Switch------------------------------------------------

# --------------------------------------HP Printer---------------------------------------------------
    out = df[(df['DeviceOut'].str.contains('Printer')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('Printer')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    Printer = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    Printer.columns = col
    Printer['Printer'] = Printer.In.apply(lambda x: 1 if x > 250 else 0)
    Printer.Printer[Printer.Out > 250] = 1
# --------------------------------------HP Printer---------------------------------------------------

# --------------------------------------Withings Smart Baby Monitor----------------------------------
    out = df[(df['DeviceOut'].str.contains('Baby')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('Baby')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    Baby = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    Baby.columns = col
    Baby['Baby'] = Baby.In.apply(lambda x: 1 if x > 400 else 0)
    Baby.Baby[Baby.Out > 500] = 1
# --------------------------------------Withings Smart Baby Monitor----------------------------------

# --------------------------------------Belkin Motion------------------------------------------------
    out = df[(df['DeviceOut'].str.contains('Motion')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('Motion')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    Motion = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    Motion.columns = col
    Motion['Motion'] = Motion.In.apply(lambda x: 1 if x > 661 else 0)
    Motion.Motion[Motion.Out > 281] = 1
# --------------------------------------Belkin Motion------------------------------------------------

# --------------------------------------Withings Smart scale-----------------------------------------
    out = df[(df['DeviceOut'].str.contains('scale')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('scale')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    scale = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    scale.columns = col
    scale['scale'] = scale.In.apply(lambda x: 1 if x > 0 else 0)
    scale.scale[scale.Out > 0] = 1
# --------------------------------------Withings Smart scale-----------------------------------------

# --------------------------------------LiFX Smart Bulb----------------------------------------------
    out = df[(df['DeviceOut'].str.contains('LIFX')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('LIFX')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    LIFX = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    LIFX.columns = col
    LIFX['LIFX'] = LIFX.In.apply(lambda x: 1 if x > 800 else 0)
    LIFX.LIFX[LIFX.Out > 300] = 1
# --------------------------------------LiFX Smart Bulb----------------------------------------------

# --------------------------------------Netatmo Weather Station--------------------------------------
    out = df[(df['DeviceOut'].str.contains('Weather')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('Weather')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    Weather = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    Weather.columns = col
    Weather['Weather'] = Weather.In.apply(lambda x: 1 if x > 1000 else 0)
    Weather.Weather[Weather.Out > 500] = 1
# --------------------------------------Netatmo Weather Station--------------------------------------

# --------------------------------------Triby Speaker------------------------------------------------
    out = df[(df['DeviceOut'].str.contains('Triby')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('Triby')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    Triby = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    Triby.columns = col
    Triby['Triby'] = Triby.In.apply(lambda x: 1 if x > 700 else 0)
    Triby.Triby[Triby.Out > 700] = 1
# --------------------------------------Triby Speaker------------------------------------------------

# --------------------------------------TPLink Plug & iHome Plug------------------------------------------------
    out = df[(df['DeviceOut'].str.contains('lug')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('lug')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    lug = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    lug.columns = col
    lug['lug'] = lug.In.apply(lambda x: 1 if x > 1000 else 0)
    lug.lug[lug.Out > 1000] = 1
# --------------------------------------Triby Speaker------------------------------------------------

# --------------------------------------iPhone--------------------------------------------------------
    out = df[(df['DeviceOut'].str.contains('iPhone')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('iPhone')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    iPhone = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    iPhone.columns = col
    iPhone['iPhone'] = iPhone.In.apply(lambda x: 1 if x > 5000 else 0)
    iPhone.iPhone[iPhone.Out > 2000] = 1
# --------------------------------------iPhone--------------------------------------------------------

# --------------------------------------Android--------------------------------------------------------
    out = df[(df['DeviceOut'].str.contains('Android')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('Android')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    Android = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    Android.columns = col
    Android['Android'] = Android.In.apply(lambda x: 1 if x > 5000 else 0)
    Android.Android[Android.Out > 2000] = 1
# --------------------------------------Android--------------------------------------------------------

# --------------------------------------Laptop-------------------------------------------------------
    out = df[(df['DeviceOut'].str.contains('Laptop')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('Laptop')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    Laptop = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    Laptop.columns = col
    Laptop['Laptop'] = Laptop.In.apply(lambda x: 1 if x > 5000 else 0)
    Laptop.Laptop[Laptop.Out > 2000] = 1
# --------------------------------------Laptop-------------------------------------------------------

# --------------------------------------MacBook------------------------------------------------------
    out = df[(df['DeviceOut'].str.contains('MacBook')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('MacBook')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    MacBook = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    MacBook.columns = col
    MacBook['MacBook'] = MacBook.In.apply(lambda x: 1 if x > 5000 else 0)
    MacBook.MacBook[MacBook.In > 2000] = 1
# --------------------------------------MacBook------------------------------------------------------

# --------------------------------------Insteon Camera-----------------------------------------------
    out = df[(df['DeviceOut'].str.contains('Insteon')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('Insteon')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    Insteon = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    Insteon.columns = col
    Insteon['Insteon'] = Insteon.In.apply(lambda x: 1 if x > 4000 else 0)
    Insteon.Insteon[Insteon.Out > 8000] = 1
# --------------------------------------Insteon Camera-----------------------------------------------
# --------------------------------------Dropcam------------------------------------------------------
    out = df[(df['DeviceOut'].str.contains('Dropcam')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('Dropcam')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    Dropcam = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    Dropcam.columns = col
    Dropcam['Dropcam'] = Dropcam.In.apply(lambda x: 1 if x > 200 else 0)
    Dropcam.Dropcam[Dropcam.Out > 400] = 1
# --------------------------------------Dropcam------------------------------------------------------
# --------------------------------------Samsung SmartCam---------------------------------------------
    out = df[(df['DeviceOut'].str.contains('SmartCam')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('SmartCam')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    SmartCam = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    SmartCam.columns = col
    SmartCam['SmartCam'] = SmartCam.In.apply(lambda x: 1 if x > 1000 else 0)
    SmartCam.SmartCam[SmartCam.Out > 500] = 1
# --------------------------------------Samsung SmartCam--------------------------------------------

# --------------------------------------Samsung Tab---------------------------------------------
    out = df[(df['DeviceOut'].str.contains('Tab')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('Tab')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    Tab = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    Tab.columns = col
    Tab['Tab'] = Tab.In.apply(lambda x: 1 if x > 5000 else 0)
    Tab.Tab[Tab.Out > 2000] = 1
# --------------------------------------Samsung Tab--------------------------------------------

# --------------------------------------Netatmo Welcome Camera---------------------------------
    out = df[(df['DeviceOut'].str.contains('Welcome')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('Welcome')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    Welcome = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    Welcome.columns = col
    Welcome['Welcome'] = Welcome.In.apply(lambda x: 1 if x > 1000 else 0)
    Welcome.Welcome[Welcome.Out > 1000] = 1
# --------------------------------------Netatmo Welcome Camera----------------------------------

# --------------------------------------TP-Link Day Night Cloud camera--------------------------
    out = df[(df['DeviceOut'].str.contains('Day Night')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('Day Night')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    Day = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    Day.columns = col
    Day['Day'] = Day.In.apply(lambda x: 1 if x > 1000 else 0)
    Day.Day[Day.Out > 1000] = 1
# --------------------------------------TP-Link Day Night Cloud camera--------------------------

# --------------------------------------Smart Things--------------------------------------------
    out = df[(df['DeviceOut'].str.contains('Smart Things')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('Smart Things')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    Things = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    Things.columns = col
    Things['Things'] = Things.In.apply(lambda x: 1 if x > 600 else 0)
    Things.Things[Things.Out > 200] = 1
# --------------------------------------Smart Things--------------------------------------------

# --------------------------------------Smoke Alarm---------------------------------------------
    out = df[(df['DeviceOut'].str.contains('Smoke')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('Smoke')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    Smoke = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    Smoke.columns = col
    Smoke['Smoke'] = Smoke.In.apply(lambda x: 1 if x > 1000 else 0)
    Smoke.Smoke[Smoke.Out > 2500] = 1
# --------------------------------------Smoke Alarm---------------------------------------------

# --------------------------------------BloodPressure-------------------------------------------
    out = df[(df['DeviceOut'].str.contains('BloodPressure')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('BloodPressure')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    BloodPressure = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    BloodPressure.columns = col
    BloodPressure['BloodPressure'] = BloodPressure.In.apply(lambda x: 1 if x > 1000 else 0)
    BloodPressure.BloodPressure[BloodPressure.Out > 400] = 1
# --------------------------------------BloodPressure-------------------------------------------

# --------------------------------------sleep---------------------------------------------------
    out = df[(df['DeviceOut'].str.contains('sleep')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('sleep')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    sleep = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    sleep.columns = col
    sleep['sleep'] = sleep.In.apply(lambda x: 1 if x > 1000 else 0)
    sleep.sleep[sleep.Out > 1000] = 1
# --------------------------------------sleep---------------------------------------------------

# --------------------------------------Photo-frame---------------------------------------------
    out = df[(df['DeviceOut'].str.contains('Photo')) & (df['DeviceIn'].str.contains('TPLink'))]
    out = out.drop('DeviceOut', axis=1)
    out = out.drop('DeviceIn', axis=1)
    out['TIME'] = pd.to_datetime(out['TIME'], unit='s')
    out.index = out['TIME']
    out = out.Size.resample('1s').sum()

    inn = df[(df['DeviceIn'].str.contains('Photo')) & (df['DeviceOut'].str.contains('TPLink'))]
    inn = inn.drop('DeviceOut', axis=1)
    inn = inn.drop('DeviceIn', axis=1)
    inn['TIME'] = pd.to_datetime(inn['TIME'], unit='s')
    inn.index = inn['TIME']
    inn = inn.Size.resample('1s').sum()

    Photo = pd.concat([inn, out], axis=1)
    col = ['In', 'Out']
    Photo.columns = col
    Photo['Photo'] = Photo.In.apply(lambda x: 1 if x > 4500 else 0)
    Photo.Photo[Photo.Out > 900] = 1
# --------------------------------------Photo-frame--------------------------------------------
    device = pd.concat([total, Amazon['Amazon'], Switch['Switch'], Printer['Printer'], Baby['Baby'], Motion['Motion'],
                        scale['scale'], LIFX['LIFX'], Weather['Weather'], Triby['Triby'], lug['lug'], iPhone['iPhone'], Android['Android'],
                        Laptop['Laptop'], MacBook['MacBook'], Insteon['Insteon'], Dropcam['Dropcam'],
                        SmartCam['SmartCam'], Tab['Tab'], Welcome['Welcome'], Day['Day'], Things['Things'], Smoke['Smoke'], BloodPressure['BloodPressure'], sleep['sleep'], Photo['Photo']], axis=1)
    device = device.fillna(0)

    device['Movement'] = device.Motion.apply(lambda x: 1 if x > 0 else 0)
    device.Movement[device.Insteon > 0] = 1
    device.Movement[device.Dropcam > 0] = 1
    device.Movement[device.SmartCam > 0] = 1
    device.Movement[device.Welcome > 0] = 1
    device.Movement[device.Day > 0] = 1

    device['NonIoT'] = device.iPhone.apply(lambda x: 1 if x > 0 else 0)
    device.NonIoT[device.Android > 0] = 1
    device.NonIoT[device.Laptop > 0] = 1
    device.NonIoT[device.MacBook > 0] = 1
    device.NonIoT[device.Tab > 0] = 1

    device['Print'] = device.Printer.apply(lambda x: 1 if x > 0 else 0)
    device.Print[device.Laptop > 0] = 1
    device.Print[device.MacBook > 0] = 1

    device['CheckBodyCondition'] = device.scale.apply(lambda x: 1 if x > 0 else 0)
    device.CheckBodyCondition[device.BloodPressure > 0] = 1
    device.CheckBodyCondition[device.sleep > 0] = 1

    device['ControlLights'] = device.Switch.apply(lambda x: 1 if x > 0 else 0)
    device.ControlLights[device.LIFX > 0] = 1
    device.ControlLights[device.lug > 0] = 1

    device['MultiMedia'] = device.Triby.apply(lambda x: 1 if x > 0 else 0)
    device.MultiMedia[device.Photo > 0] = 1

    device = device.drop(labels=['Motion', "Insteon", 'Dropcam', 'SmartCam', 'Welcome', 'Day'], axis=1)
    device = device.drop(labels=['iPhone', "Android", 'Laptop', 'MacBook', 'Tab'], axis=1)
    device = device.drop(labels=['Printer'], axis=1)
    device = device.drop(labels=['scale', "BloodPressure", 'sleep'], axis=1)
    device = device.drop(labels=['Switch', "LIFX", 'lug'], axis=1)
    device = device.drop(labels=['Triby', "Photo"], axis=1)

    device = device.resample('1min').sum()
    for x in range(2, len(device.columns)):
        temp = str(device.columns[x])
        device[temp][device[temp] > 0] = 1
    device.to_csv('C:/penv/IPSN/data/groundtruth/1min/' + i)
