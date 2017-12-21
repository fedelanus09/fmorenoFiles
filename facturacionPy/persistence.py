from json import loads
from json import dump

def loadData():
	inventory = loads(open("database.json").read())
	
def saveData(inventory):	
	with open("database.json", "w") as fout:
		dump(inventory, fout)
