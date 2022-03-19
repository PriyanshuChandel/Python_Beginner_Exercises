"""Here we are using the request module to download some web data and then convert them into a list then pickling followed by unpickling"""


import requests
import pickle
Download = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
Data = [Download]
file = "tut85_exercise10.txt"
fileobj = open(file, "wb")
pickle.dump(Data, fileobj)
fileobj.close()

file1 = open("tut85_exercise10.txt")
for line in file1:
    list = [file1.readlines()]
file2 = "tut85_exercise10.pkl"
fileobj2 = open(file2, "wb")
pickle.dump(list, fileobj2)
fileobj2.close()

file3 = "tut85_exercise10.pkl"
fileobj3 = open(file3, "rb")
Unpick = pickle.load(fileobj3)
print(Unpick)
