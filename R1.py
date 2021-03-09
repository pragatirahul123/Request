import requests
import json
res = requests.get("https://merakilearn.org/api/courses")
a=(res.text)
# print(a)
#print(type(a))
# print(req.text)


with open("courses.json","w")  as f:
    data=json.loads(a)
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
re=requests.get("https://merakilearn.org/api/courses/"+id+"/exercises")
var2=re.text
with open("id.json","w") as f:
    d=json.loads(var2)
    json.dump(d,f,indent=4)

rev=(d['data'])

print("main courses",empty2[user])

s=0
empty_slug=[]
for i in rev:
    print(s,"   ",i['name'])
    empty_slug.append(i['slug'])
    s=s+1
    if len(i["childExercises"]):
        c1=0
        for j in i['childExercises']:
            print(c1,"    ",j['name'])
            c1=c1+1
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



user_input=input("what you want, 1.up or 2.next,3.pre :")
if user_input =="up":
    availableCourses = (data["availableCourses"])
    index=0
    empty=[]
    empty2=[]
    for i  in availableCourses:
        print((index)," ",i['name'],i['id'])
        empty.append(i['id'])
        empty2.append(i['name'])
        index=index+1
  
