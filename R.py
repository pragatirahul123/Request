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

c=0
empty_slug=[]
for i in req:
    print(c,"   ",i['name'])
    empty_slug.append(i['slug'])
    c=c+1
    if len(i["childExercises"]):
        c2=0
        for j in i['childExercises']:
            print(c2,"    ",j['name'])
            c2=c2+1
    else:
        print("[]")
print(empty_slug)

user1=int(input("enter a slug:"))
b=empty_slug[user1]
print(b)

slug=requests.get("http://merakilearn.org/api/courses/"+id+"/exercise/getBySlug?slug="+b)
z=(slug.text)
print(z)

with open("s_id.json","w") as f:
    m=json.loads(z)
    json.dump(m,f,indent=4)
    print(m)












    










       












 