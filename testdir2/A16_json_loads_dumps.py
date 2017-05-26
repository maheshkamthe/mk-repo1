import json

print ("Demo - json load start \n")

fh = open("books.json", "r")
books = json.load(fh)
fh.close()
print (books) ### Printing python dictionary after converting/reading from jason 
print (type (books))    ### json to dictionary conversion
print ("Author of Java book is ", books['CompBooks']['Java']['Author'])
print ("Cost of Python book is ", books['CompBooks']['Python']['Cost'])
print ("##### Demo - json load over #####\n \n ")

#################################################################################
print ("Demo - json dumps start \n")

PyDict = {
    "Scrip": "TataPower",
    "Shares": "100",
    "Price": "80"
    }

print (type(PyDict))
print (PyDict)
 
PyStr = json.dumps(PyDict)
print (type(PyStr))
print (PyStr)
print ("##### Demo - json dumps over ##### \n \n")

#################################################################################

