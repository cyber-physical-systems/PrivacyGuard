import csv

import glob

path = ''

output_path = ''

for file in glob.glob(path + '*.csv'):

    name = file.split('/')[-1]
    date = name.split('.')[0]

    with open(file) as f:

        reader = csv.DictReader(f)
        header = reader.fieldnames
        #         print(header)

        with open(output_path + name, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header)
            #             writer.writerow(fieldnames)
            writer.writeheader()

            for row in reader:
                #             Amazon,Switch,Printer,Baby,Motion,scale,LIFX,Weather,Triby,lug,Phone,Laptop,MacBook,Insteon,Dropcam,SmartCam

                if (int(float(row['Amazon'])) or int(float(row['Switch'])) or int(float(row['Printer']))
                    or int(float(row['Baby'])) or int(float(row['Motion'])) or int(float(row['scale']))
                    or int(float(row['LIFX'])) or int(float(row['Weather'])) or int(float(row['Triby'])) or int(
                            float(row['lug']))
                    or int(float(row['Phone'])) or int(float(row['Laptop'])) or int(float(row['MacBook']))
                    or int(float(row['Insteon'])) or int(float(row['Dropcam'])) or int(float(row['SmartCam']))) == 1:
                    writer.writerow(row)
        csvfile.close()
    f.close()



