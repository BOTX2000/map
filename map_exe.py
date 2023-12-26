import os
import requests

class my_opinion_exemplar_1:
	def __init__(self, url, path=""):
		self.path = path
		self.url = url
		a = url.split("/")
		a.reverse()
		self.name = a[0]

	def install(self, path=""):
		if path!="": self.path=path
		os.makedirs("downloads/" + self.path, exist_ok=True)
		with open("downloads/" + self.path + "/" + self.name, "wb") as f:
			response = requests.get(self.url)
			if response.status_code == 200:
				f.write(response.content)

				
adress_global=[
	"https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/start.py",
	"https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/ex1.py",
	"https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/base.py", 
	"https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/dc.py", 
	"https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/file_os.py", 
	"https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/node.py", 
	"https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/start.spec", 
	"https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/testdc.py", 
	"https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/перевірка коду.txt", 
	"https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/data/setting.txt", 
	"https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/data/data/command.txt"
	]
def a():
	global adress_global
a()

class start(my_opinion_exemplar_1):
	def __init__(self):
		super().__init__(adress_global[0])
		
class ex1(my_opinion_exemplar_1):
	def __init__(self):
		super().__init__(adress_global[1])
		
class base(my_opinion_exemplar_1):
	def __init__(self):
		super().__init__(adress_global[2])
	
class dc(my_opinion_exemplar_1):
	def __init__(self):
		super().__init__(adress_global[3])
		
class file_os(my_opinion_exemplar_1):
	def __init__(self):
		super().__init__(adress_global[4])
		
class node(my_opinion_exemplar_1):
	def __init__(self):
		super().__init__(adress_global[5])
		
class start_spec(my_opinion_exemplar_1):
	def __init__(self):
		super().__init__(adress_global[6])
		
class testdc(my_opinion_exemplar_1):
	def __init__(self):
		super().__init__(adress_global[7])
		
class перевірка(my_opinion_exemplar_1):
	def __init__(self):
		super().__init__(adress_global[8])
		
class setting(my_opinion_exemplar_1):
	def __init__(self): 
		super().__init__(adress_global[9])
		
class command(my_opinion_exemplar_1):
	def __init__(self):
		super().__init__(adress_global[10])
"""
class (my_opinion_exemplar_1):
	def __init__(self):
		super().__init__("")
		
class (my_opinion_exemplar_1):
	def __init__(self):
		super().__init__("")
"""
class vois_addon:
	def install(self):
		name=["start", "ex1", "base", "dc", "file_os", "node", "start_spec", "testdc", "перевірка"]
		for i in name:
			eval(f"{i}.install('vois-addon')")
		command.install("vois-addon/data/data")
		setting.install("vois-addon/data")
		os.makedirs("downloads/vois-addon/data/cache", exist_ok=True)

def argsin():
	args=input().split()
	return args
	
clas=["start", "ex1", "base", "dc", "file_os", "node", "start_spec", "testdc", "перевірка", "vois_addon", "setting", "command"]
for i in clas:
	globals()[i.lower()] = globals()[i]()

def analising(arg:str):
	#"""
	try:
		eval(f"{arg}.install()")
		print("файл інстальовано")
	except NameError:
		print("Файлу не було знайде в базі данних")
	"""
	eval(f"{arg}.install()")
	print("файл інстальовано")
	#"""

def base_code():
	args=argsin()
	try:
		if args[0]!="map":
			print("Невідома команда")
			return
		if args[1]=="help":
			print("install [name] - інсталює файл який є в базі данних за", 
			"імям файлу без розширення")
		elif args[1]=="install":
			analising(args[2])
		else:
			print('Невідома команда, використайте команду "help" для отримання довідки')
	except IndexError: pass
	
print("код запущено")
while True:
	base_code()
