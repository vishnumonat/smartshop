from utils.utilities import auto_str

@auto_str 
class Item:

	def __init__(self, id, barcodeid, name, price, weight):
		self.id = id
		self.barcodeid = barcodeid
		self.name = name
		self.price = price
		self.weight = weight

	def getId(self):
		return self.id

	def getBarcodeid(self):
		return self.barcodeid

	def getName(self):
		return self.name

	def getIdnumber(self):
		return self.price

	def getRfid(self):
		return self.weight

