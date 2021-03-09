import requests
import json
response = requests.get("https://merakilearn.org/api/courses")
var=(response.text)
# print(a)
#print(type(a))
# print(req.text)


with open("courses.json","w")  as f:
    data=json.loads(var)
    json.dump(data,f,indent=4)

    
availableCourses = (data["availableCourses"])
index=0
empty=[]
empty2=[]
for i  in availableCourses:
    print((index)," ",i['name'],i['id'])
    empty.append(i['id'])
    empty2.append(i['name'])
    index=index+1

user=int(input("enter your id :"))
id=empty[user]
resofexersice=requests.get("https://merakilearn.org/api/courses/"+id+"/exercises")
var2=resofexersice.text
with open("id.json","w") as f:
    d=json.loads(var2)
    json.dump(d,f,indent=4)

req=(d['data'])

print("main courses",empty2[user])
