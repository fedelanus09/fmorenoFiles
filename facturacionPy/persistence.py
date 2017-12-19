from json import loads
from json import dump

def loadData():
	inventory = loads(open("outfile.json").read())
		
def saveData():
	inventory.append(product)
	
	with open("outfile.json", "w") as fout:
		dump(inventory, fout)