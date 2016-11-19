from operator import itemgetter

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

projectToQA = []
resp = requests.get(url="https://acme-3/resource/api/0.1/depts/", auth=('cheng', 'PerGC_822'), verify=False)
jsonResponse = resp.json()
print jsonResponse

depts = jsonResponse["_embedded"]["depts"]
for dept in depts:
    if dept["name"] == "cyclops":
        projectsUrl = dept["_links"]["projects"]["href"]
        resp = requests.get(url=projectsUrl, auth=('cheng', 'PerGC_822'), verify=False)
        jsonResponse =  resp.json()
        break

projects = jsonResponse["_embedded"]["projects"]

for project in projects:
    step = project["step"]
    sequenceUrl = project["_links"]["sequences"]["href"]
    resp = requests.get(sequenceUrl, auth=('cheng', 'PerGC_822'), verify=False)
    sequenceId = resp.json()["_embedded"]["sequences"][0]["id"]
    resp = requests.get("https://acme-3/resource/api/0.1/frames/search/findFramesWithAttributes?sequenceId="+sequenceId+"&committed=true&approved=false&discarded=false&mod=" + str(step), auth=('cheng', 'PerGC_822'), verify=False)
    frames = resp.json()["_embedded"]["frames"]
    page = resp.json()["page"]["totalPages"]
    if len(frames)>0:
        count = 0
        for i in range(page):
            resp = requests.get("https://acme-3/resource/api/0.1/frames/search/findFramesWithAttributes?sequenceId=" + sequenceId + "&committed=true&approved=false&discarded=false&mod=" + str(step) + "&page=" + str(i), auth=('cheng', 'PerGC_822'), verify=False)
            frames = resp.json()["_embedded"]["frames"]
            for frame in frames:
                if not frame["locked"]:
                    count += 1
        if count > 0:
            tup = (project["name"], count)
            projectToQA.append(tup)

projectToQA = sorted(projectToQA,key=itemgetter(1))

print projectToQA