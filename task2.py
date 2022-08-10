#!/usr/bin/env python3

import requests
import json
import os

# response = requests.get("http://www.google.com")
# if not response.ok:
#     raise Exception("GET failed with status code {}".format(response.status_code))
# print(response.status_code)


# p = {"search": "grey kitten","max_results": 15}
# response = requests.get("https://google.com", params=p)
# print(response.request.url)
# # 'https://google.com?search=grey+kitten&max_results=15'


# people = [
#   {
#     "name": "Sabrina Green",
#     "username": "sgreen",
#     "phone": {
#       "office": "802-867-5309",
#       "cell": "802-867-5310"
#     },
#     "department": "IT Infrastructure",
#     "role": "Systems Administrator"
#   },
#   {
#     "name": "Eli Jones",
#     "username": "ejones",
#     "phone": {
#       "office": "684-348-1127"
#     },
#     "department": "IT Infrastructure",
#     "role": "IT Specialist"
#   },
# ]
# with open('people.json', 'w') as people_json:
#     json.dump(people, people_json, indent=2)

test_list=[]
keys=["title","name","date","feedback"]
test_dict={}

# with open("feedback/feedback.txt","r") as feedback:
#     i=0
#     for line in feedback:
#         test_dict[keys[i]] = line.strip()
#         # print(line.strip())
#         i+=1
# test_list.append(test_dict)
# print(test_list)




yourpath = "feedback/"
#for name in os.listdir(yourpath):
for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:
        print(name)
        test_dict={}
        with open (yourpath+name,"r") as feedback:
            i=0
            for line in feedback:
                test_dict[keys[i]] = line.strip()
                i+=1
            test_list.append(test_dict)
        response = requests.post("url",json=test_dict)
print(test_list)