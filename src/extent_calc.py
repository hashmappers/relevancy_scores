import os
import math
import json
import numpy as np

'''
Declare consts
'''
max_l2 = float('-inf')
min_l2 = float('inf')
num_data = 100
mu_long = -117.1825381
sigma = 4
# longitudes = np.random.normal(mu_long, sigma, num_data)
longitudes = list()


mu_lat = 34.0555693
sigma = 4
# latitudes = np.random.normal(mu_lat, sigma, num_data)
latitudes = list()

avg_longitude = 0.0
avg_latitude = 0.0

'''
Read in from output_coordinates
'''
file_path = "../data_LiesPeopleTellThemselves/output_ordinates.json"
json_data=open(file_path).read()
data = json.loads(json_data)
for item in data['data']:
	if item['latitude'] != None and item['longitude'] != None:
		# print("lat:"+str(item['latitude'])+"long:"+str(item['longitude']))
		latitudes.append(item['latitude'])
		longitudes.append(item['longitude'])

# for item in range(len(latitudes)):
# 	print("@@@"+str(latitudes[item])+" " + str(longitudes[item]))
'''
Normalize score between 0 and 1
'''
def normalized(x, min_x, max_x):
	return (x-min_x)/(max_x-min_x)

def l2norm(x, y):
	return math.pow(math.pow(x-avg_longitude,2.0) + math.pow(y-avg_latitude,2.0), 0.5)



for i in range(num_data):
	avg_longitude = (avg_longitude * i + longitudes[i])/(i+1)
	avg_latitude = (avg_latitude * i + latitudes[i])/(i+1)

print("avg_longitude:"+str(avg_longitude))
print("avg_latitude:"+str(avg_latitude))

# find min/max l2 norm to centroid
for i in range(num_data):
	if l2norm(longitudes[i],latitudes[i]) > max_l2:
		max_l2 = l2norm(longitudes[i],latitudes[i]);
	if l2norm(longitudes[i],latitudes[i]) < min_l2:
		min_l2 = l2norm(longitudes[i],latitudes[i]);


'''
test 1
similar latitude and longitudes:
'''

long_test1 = -100.0
lat_test1 = 50.0

l2_test1 = l2norm(long_test1,lat_test1)
print("normalized score for test 1: " + str(normalized(l2_test1, min_l2, max_l2)))

'''
test2
very different latitude and longitude:
'''


long_test2 = 50.0
lat_test2 = -100.0

l2_test2 = l2norm(long_test2,lat_test2)
print("normalized score for test2: " + str(normalized(l2_test2, min_l2, max_l2)))