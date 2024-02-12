import requests

#json format: https://10015.io/tools/json-tree-viewer
#url_base = "https://www.el-tiempo.net/api"
url = "https://www.el-tiempo.net/api/json/v2/provincias"

provincies = requests.get(url)
print("status code: ", provincies.status_code, "\n")
#print (provincies.headers)
#print (provincies.text)

prov = provincies.json()
#print(type(prov)) #dict

for key1 in prov.keys():
	print("{{", key1, "}}")
	if "dict" in str(type(prov[key1])):
		for key2 in prov[key1].keys():
			print("   ◻️", key2, ": ", end="")
			print(prov[key1][key2])
	elif "list" in str(type(prov[key1])):
		for num, (info) in enumerate(prov[key1]):
			print(f"   {num})")
			for key, value in info.items():
				print("   ◻️", key, ":", value)
			print()
	else:
		print("   ◻️", prov[key1])
	print()
	
print()

temps = requests.get("https://www.el-tiempo.net/api/json/v2/provincias/08", timeout=5)
print(temps.status_code)