import csv
import os

lines = list()
trg = 'C:/Users/noha.omar/Desktop/Govee1/'
for filename in os.listdir(trg):
    print(filename)
    x=trg+filename


    with open(x, 'r') as readFile:

        reader = csv.reader(readFile)

        for row in reader:

            lines.append(row)

            for field in row:

                if field ==  47740:


                    lines.remove(row)

                with open(x, 'w') as writeFile:
                   writer = csv.writer(writeFile)

                   writer.writerows(lines)




