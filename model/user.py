from utils.utilities import auto_str

@auto_str 
class User:

	def __init__(self, id, name, idnumber, rfid):
		self.id = id
		self.name = name
		self.idnumber = idnumber
		self.rfid = rfid

	def getId(self):
		return self.id

	def getName(self):
		return self.name

	def getIdnumber(self):
		return self.idnumber

	def getRfid(self):
		return self.rfid

