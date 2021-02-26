import csv

import glob

path = ''

output_path = ''

# window_size = 5

with open(output_path + '400_threshold.csv', 'w') as new:
    realnames = ['date', 'TotalIn', 'TotalOut']
    writer = csv.DictWriter(new, fieldnames=realnames)
    writer.writeheader()
new.close()

In = []
Out = []

for file in glob.glob(path + '*.csv'):

    name = file.split('/')[-1]
    i = name.split('.')[0]

    with open(path + str(i) + ".csv") as f:

        reader = csv.DictReader(f)

        TotalIn = 10000
        TotalOut = 10000

        for row in reader:

            if int(float(row['Amazon'])) == 1:
                print(row['TotalIn'])

                if int(float(row['TotalIn'])) < TotalIn:
                    TotalIn = int(float(row['TotalIn']))
                if int(float(row['TotalOut'])) < TotalOut:
                    TotalOut = int(float(row['TotalOut']))

        In.append(TotalIn)
        Out.append(TotalOut)
        with open(output_path + '400_threshold.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([i, TotalIn, TotalOut])
        csvfile.close()

with open(output_path + '400_threshold.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['all', min(In), min(Out)])
csvfile.close()

