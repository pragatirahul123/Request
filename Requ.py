import requests
import os
import json

def isFileAvailable(fileName):
    return os.path.exists(fileName)
def readJsonFile(fileName):
    with open(fileName,"r") as f:
        return json.load(f)
def createJsonFile(fileName,responseOfCoursesInText):
    with open(fileName,"w") as f:
        data=json.loads(responseOfCoursesInText)
        json.dump(data,f,indent=4)
def printingCourses(data):
    availableCourses=data["availableCourses"]
    index=1
    for i in availableCourses:
        print(index,":",i["name"],"-",i["id"])
        listOfCourseIds.append(i["id"])
        index+=1
def printingExercises(d,listOfslugs):
    responseOfExercises=(d['data'])
    for i in responseOfExercises:
        print("parent Exercise",i["name"])
        listOfslugs.append(i["slug"])
        if len(i["childExercises"])>0:
            for j in i["childExercises"]:
                listOfslugs.append(j["slug"])
                print("child exercies -", j["name"])
        else:
            print("there is no childexersise[]")


def PrintingSlugs(data):
    index=1
    for i in data:
        print(index,":",i)
        index+=1

def CallingSlugApi(slugNumber,listOfCourseIds,userSelectedCourse,listOfslugs):
    responseOfSlug=requests.get("https://saral.navgurukul.org/api/courses/"+str(listOfCourseIds[userSelectedCourse-1])+"/exercise/getBySlug?slug="+str(listOfslugs[slugNumber-1]))
    print(responseOfSlug.text)

listOfCourseIds=[]



def main():
    listOfslugs=[]
    fileName="courses.json"
    if isFileAvailable(fileName):
        data=readJsonFile(fileName)
        printingCourses(data)
    else:
        responseOfCourses=requests.get("https://saral.navgurukul.org/api/courses")
        responseOfCoursesInText=responseOfCourses.text
        createJsonFile(fileName,responseOfCoursesInText)
        data=readJsonFile(fileName)
        printingCourses(data)

    userSelectedCourse=int(input("select a course: "))
    fileNameOfExercise="Exercise_"+str(listOfCourseIds[userSelectedCourse-1])+".json"
    if isFileAvailable(fileNameOfExercise):
        data=readJsonFile(fileNameOfExercise)
        printingExercises(data,listOfslugs)
    else:
        responseOfCourseExercies=requests.get("https://saral.navgurukul.org/api/courses/"+str(listOfCourseIds[userSelectedCourse-1])+"/exercises")
        responseOfExerciseCoursesInText=responseOfCourseExercies.text
        createJsonFile(fileNameOfExercise,responseOfExerciseCoursesInText)
        data=readJsonFile(fileNameOfExercise)
        printingExercises(data,listOfslugs)

    PrintingSlugs(listOfslugs)    
    userSelectedSlug=int(input("select a slug: "))
    print(listOfCourseIds[userSelectedCourse-1])
    print("*****")
    print(listOfslugs[userSelectedSlug-1])
    print("*******")
    CallingSlugApi(userSelectedSlug,listOfCourseIds,userSelectedCourse,listOfslugs)

    seeAgain=input("enter what you want to do 1. up 2. Next 3. Pre : 4. stop :")

    if seeAgain=="up":
        main()
    elif seeAgain=="Next":
        slugIncreased=userSelectedSlug+1
        CallingSlugApi(slugIncreased,listOfCourseIds,userSelectedCourse,listOfslugs)
    elif seeAgain=="Pre":
        slugIncreased=userSelectedSlug-1
        CallingSlugApi(slugIncreased,listOfCourseIds,userSelectedCourse,listOfslugs)
    else:
        print("Nothing")
main()

