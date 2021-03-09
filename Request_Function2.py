import json
import requests
import os

list_for_id=[]
list_for_name=[]
list_for_slug=[]
def showingcourses():
    if os.path.exists('courses.json'):
        with open("courses.json","r") as f:
            data=json.load(f)
        availableCourses=(data['availableCourses'])
        count=0

        for i in availableCourses:
            print(count,":",i["name"] ,"-", i["id"])
            list_for_id.append(i['id'])
            list_for_name.append(i['name'])
            count=count+1
    else:
        response=requests.get("http://merakilearn.org/api/courses")
        response_in_text=response.text
        with open("courses.json","w") as f:
            data=json.loads(response_in_text)
            # print(data)
            json.dump(data,f,indent=4)
            
        availableCourses=(data['availableCourses'])
        count=0
        for i in availableCourses:
            print(count,":",i["name"] ,"-", i["id"])
            list_for_id.append(i['id'])
            list_for_name.append(i['name'])
            count=count+1

showingcourses()
userSelectedCourse= int(input("enter an id "))
def showingExercisesOfCourse(userSelectedCourse):
    exerciseFile="exercise_"+str(userSelectedCourse)+".json"
    if os.path.exists(exerciseFile):
        with open(exerciseFile,"r") as f:
            d=json.load(f)
        reqOfExercises=(d['data'])
        for i in reqOfExercises:
            print("parent Exercise",i["name"])
            list_for_slug.append(i["slug"])
            if len(i["childExercises"])>0:
                for j in i["childExercises"]:
                    list_for_slug.append(j["slug"])
                    print("child exercies -", j["name"])
    else:
        responseOfExercises= requests.get("https://merakilearn.org/api/courses/"+str(list_for_id[userSelectedCourse])+"/exercises")
        var=responseOfExercises.text
        with open(exerciseFile,"w") as f:
            data=json.loads(var)
            json.dump(data,f,indent=4)
        reqOfExercises=(data['data'])
        for i in reqOfExercises:
            print("parent Exercise",i["name"])
            print(i["slug"]," ")
            list_for_slug.append(i["slug"])
            if len(i["childExercises"])>0:   
                for j in i["childExercises"]:
                    print("child exercies -", j["name"])
                    list_for_slug.append(j["slug"])

showingExercisesOfCourse(userSelectedCourse)
count=1
for i in list_for_slug:
    print(count,":",i)
    count+=1
SlugNumber=int(input("enter a slug number"))
def ShowingSlugContent(SlugNumber):
    slugContent=requests.get("http://merakilearn.org/api/courses/"+str(list_for_id[userSelectedCourse])+"/exercise/getBySlug?slug="+str(list_for_slug[SlugNumber-1]))
    slugContentInText=slugContent.text
    print(slugContentInText)
ShowingSlugContent(SlugNumber)
while True:
    Play=input("Do u want to see again 1. up 2. next 3. pre 4. stop:")
    if Play=="up":
        showingcourses()
    elif Play=="next":
        SlugNumber=SlugNumber+1
        ShowingSlugContent(SlugNumber)
    elif Play =="pre":
        SlugNumber=SlugNumber-1
        ShowingSlugContent(SlugNumber)
    else:
        break



    

