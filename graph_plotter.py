import csv
import matplotlib.pyplot as plt

data = []
with open('g6.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print row
        new_row = map(float, row)
        data.append(new_row)
print len(data)
print data[0]
print data[1]
data[1] = map(lambda x: x*2, data[0])

plt.plot(data[0])
plt.plot(data[1])
plt.show()


