"""Here we are using the request module to download some web data and then convert them into a list then pickling followed by unpickling"""


import requests
import pickle
#Data download
Download = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
#Listing
list1 = Download.split("\n")
list2 = [item.split(",") for item in list1 if len(item)!=0]
# print(list2)
#Pickling
file = "IrisData.pkl"
fileobj = open(file, "wb")
pickle.dump(list2, fileobj)
fileobj.close()

#Unpickling
# file = "IrisData.pkl"
# fileobj = open(file, "rb")
# mycar = pickle.load(fileobj)
# print(mycar)
