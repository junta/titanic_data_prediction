import csv as csv 
import numpy as np
from sklearn.ensemble import RandomForestClassifier

#learning data
csv_file_object = csv.reader(open('./train.csv', 'rb'))
header = csv_file_object.next()

train_data=[]                          #Create a variable called 'data'
for row in csv_file_object:      #Run through each row in the csv file
    train_data.append(row)             #adding each row to the data variable
train_data = np.array(train_data)

train_data = np.delete(train_data, [0,3,8,10], 1)

for row in train_data:
	if row[2] == "male":
		row[2] = 1
	else:
		row[2] = 2

	if row[-1] == "S":
		row[-1] = 1
	elif row[-1] == "C":
		row[-1] = 2
	else:
		row[-1] = 3

	if row[3] == "":
		row[3] = 0


train_data.astype(np.float)
print train_data


#test data
csv_file_object = csv.reader(open('./test.csv', 'rb'))
header = csv_file_object.next()

test_data=[]                          #Create a variable called 'data'
for row in csv_file_object:      #Run through each row in the csv file
    test_data.append(row)             #adding each row to the data variable
test_data = np.array(test_data)

test_data = np.delete(test_data, [0,2,7,9], 1)

for row in test_data:
	if row[1] == "male":
		row[1] = 1
	else:
		row[1] = 2

	if row[-1] == "S":
		row[-1] = 1
	elif row[-1] == "C":
		row[-1] = 2
	else:
		row[-1] = 3

	if row[2] == "":
		row[2] = 0

	if row[5] == "":
		row[5] = 0	

print test_data

test_data.astype(np.float)

#create forest and predict
Forest = RandomForestClassifier(n_estimators = 100)
Forest = Forest.fit(train_data[0::,1::],train_data[0::,0])
Output = Forest.predict(test_data)

f = open("./randomFmodel.csv", "wb")
open_file_object = csv.writer(f,lineterminator='\n')

row = 0
while row < 418:
	open_file_object.writerow(Output[row])
	row += 1

f.close()	

