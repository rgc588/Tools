import requests
import json

json_map = {}
json_map["projectId"] = 1120
json_map["pools"] = [4]
json_map["skipSku"] = False
json_map["skipPNumber"] = False
json_map["skipPlatform"] = False
json_map["forceDisableSLI"] = False
json_map["useTOT"] = False
json_map["winNext"] = False
json_map["sandbag"] = True
json_map["codeCoverage"] = False
json_map["verifier"] = False
json_map["oemId"] = 0
json_map["highPriority"] = True
json_map["driverVersion"] = "378.08"
json_map["doNotInstallDriver"] = False
json_map["overrideDriver"] = True
json_map["jobParameters"] = ""
json_map["leverageFile"] = ""
json_map["oldDB"] = False
json_map["taskFolderIds"] = [114014]
json_map["customDriverPath"] = r"\\builds\NightlyRestricted-bugfix_main\NV\wddm2-x64\bugfix_main-161031-21317638-sandbag\IS"
json_map["machineIds"] = [50200]

json_str = json.dumps(json_map)

print json_str
headers = {'content-type': 'application/json'}

# response = requests.get(url="http://hqswqadb02/atp_api/api/values")

# response = requests.post(url="http://hqswqadb02/atp_api/api/tasks", json=json_str, headers=headers)
response = requests.post(url="http://localhost:57263/api/task", json=json_str, headers=headers)

req = response.request

print req.body

print response.status_code
print response.json()
