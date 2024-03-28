import os
import requests
import zipfile
import threading
from time import sleep
from bs4 import BeautifulSoup

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
	


	def alt_instal(self, name, path=""):
		if path != "":
			self.path = path
		os.makedirs("downloads/" + self.path, exist_ok=True)
    
		# Відправляємо початковий запит
		response = requests.get(self.url)
		if response.status_code == 200:
			# Перевірка наявності попередження про вірус
			if "Google Drive - Virus scan warning" in response.text:
				print("Warning: This file may contain viruses.")
				# Тут ви можете запросити користувача про продовження завантаження або ні
				# Наприклад, використовуючи input()
				user_input = input("Do you want to continue downloading? (yes/no): ")
				if user_input.lower() != 'yes':
					print("Download canceled.")
					return
				else:
					# Повторно відправляємо запит з підтвердженням завантаження
					soup = BeautifulSoup(response.text, 'html.parser')
					confirm_input = soup.find('input', {'name': 'confirm'})
					if confirm_input:
						confirm_value = confirm_input.get('value')
						if confirm_value:
							download_url = f"{self.url}&confirm={confirm_value}"
							response = requests.get(download_url)
						else:
							print("Confirmation value not found.")
							return
					else:
						print("Confirmation input not found.")
						return
        
			# Якщо попередження вірусів відсутнє або користувач погодився продовжити завантаження
			with open("downloads/" + self.path + "/" + name, "wb") as f:
				f.write(response.content)
				print("Download completed successfully.")
		else:
			print("Error:", response.status_code)

				
adress_global=[
	"https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/start.py",#0
	"https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/ex1.py",#1
	"https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/base.py", 
	"https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/dc.py", 
	"https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/file_os.py", 
	"https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/node.py", #5
	"https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/start.spec", 
	"https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/testdc.py", 
	"https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/перевірка коду.txt", 
	"https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/data/setting.txt", 
	"https://raw.githubusercontent.com/BOTX2000/vois_addon/main/vois-addon/data/data/command.txt",#10
	"https://raw.githubusercontent.com/BOTX2000/map/main/map_exe.py", #посилання на інсталювання оновлення
	"https://alphacephei.com/vosk/models/vosk-model-en-us-daanzu-20200905-lgraph.zip",
	"https://drive.google.com/uc?id=1EFw5vpWO1Nz-J9kMi7bv8fpKd34_5_eZ&export=download", 
	"https://drive.google.com/uc?id=1w-JT9BKzTdtQ_Y1SEmibZs7Ng__pGBjK&export=download"
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
		
class vosk_model_en(my_opinion_exemplar_1):
	def __init__(self):
		super().__init__(adress_global[12], "vois-addon/data/data")
		
class unzip:
	def process(zip_name, extract=None):
		 if extract==None: extract=zip_name
		 with zipfile.ZipFile(zip_name, 'r') as zipf:
			 zipf.extractall(extract)
			 
class test:
	def install():
		pass

def process1():
	vosk_model_en.install("vois-addon/data/data")
	unzip.process("downloads/vois-addon/data/data/vosk-model-en-us-daanzu-20200905-lgraph.zip", "downloads/vois-addon/data/data")
	os.remove("downloads/vois-addon/data/data/vosk-model-en-us-daanzu-20200905-lgraph.zip")

class vois_addon:
	def install(self):
		t=threading.Thread(target=process1).start()
		name=["start", "ex1", "base", "dc", "file_os", "node", "start_spec", "testdc", "перевірка"]
		for i in name:
			eval(f"{i}.install('vois-addon')")
		command.install("vois-addon/data/data")
		setting.install("vois-addon/data")
		os.makedirs("downloads/vois-addon/data/cache", exist_ok=True)
		t.join()
		
		
class update:
	def install():
		with open("map_exe.py", "w") as f:
			response = requests.get(adress_global[11])
			if response.status_code == 200:
				f.write(response.content)
				
class int_map(my_opinion_exemplar_1):
	def __init__(self):
		super().__init__(adress_global[13])
				
class tort_interactive_map():
	def install():
		int_map.alt_instal("exe.zip")
		sleep(1)
		unzip.process("exe.zip", "")
		
def download_file_from_google_drive(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        download_link = soup.find('input', {'id': 'uc-download-link'}).get('value')
        if download_link:
            file_response = requests.get(download_link)
            if file_response.status_code == 200:
                with open('downloaded_file.zip', 'wb') as f:
                    f.write(file_response.content)
                print("File downloaded successfully.")
            else:
                print("Failed to download file.")
        else:
            print("Download link not found in the HTML content.")
    else:
        print("Failed to fetch HTML content.")

url = "https://drive.google.com/uc?id=1w-JT9BKzTdtQ_Y1SEmibZs7Ng__pGBjK&export=download"
download_file_from_google_drive(url)

def argsin():
	args=input().split()
	return args
	
clas=["start", "ex1", "base", "dc", "file_os", "node", "start_spec", "testdc", "перевірка", "vois_addon", "setting", "command", "vosk_model_en", "update",
	  "int_map"]
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
