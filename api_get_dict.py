import requests

#json format: https://10015.io/tools/json-tree-viewer
#url_base = "https://www.el-tiempo.net/api"
url = "https://www.el-tiempo.net/api/json/v2/provincias"

provincies = requests.get(url)
print("status code: ", provincies.status_code, "\n")
#print (provincies.headers)
#print (provincies.text)
provincies_dict = provincies.json()
#print(type(provincies_dict))

for key1 in provincies_dict.keys():
	print("{{", key1, "}}")
	if "dict" in str(type(provincies_dict[key1])):
		for key2 in provincies_dict[key1].keys():
			print("   ◻️", key2, ": ", end="")
			print(provincies_dict[key1][key2])
	elif "list" in str(type(provincies_dict[key1])):
		for num, (info) in enumerate(provincies_dict[key1]):
			print(f"   {num})")
			for key, value in info.items():
				print("   ◻️", key, ":", value)
			print()
	else:
		print("   ◻️", provincies_dict[key1])
	print()
	
print()
print()

temps = requests.get("https://www.el-tiempo.net/api/json/v2/provincias/08", timeout=5)
print(temps.status_code)