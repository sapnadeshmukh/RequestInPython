import requests
import json
import os
print("**********WELCOME TO SARAL PAGE*********************")
list_for_id=[]
list_for_name=[]
list_for_slug=[]
def getCourses():
    if os.path.exists('courses.json'):
        print("From caching")
        with open("courses.json",'r') as response_data:
            data=json.load(response_data)
            # json.dump(data,response_data,indent=4)
        dict_data=data["availableCourses"]
        index=0
        while index <len (data["availableCourses"]):
            dic=(data["availableCourses"][index])
            print(index,dic["name"],dic ["id"])
            list_for_id.append(dic["id"])
            list_for_name.append(dic["name"])
            index=index+1


    else:
        request=requests.get("http://merakilearn.org/api/courses")
        response=request.text
        with open("courses.json",'w') as response_data:
            data=json.loads(response)
            json.dump(data,response_data,indent=4)

        dict_data=data["availableCourses"]
        index=0
        
        while index <len (data["availableCourses"]):
            dic=(data["availableCourses"][index])
            print(index,dic["name"],dic ["id"])
            list_for_id.append(dic["id"])
            list_for_name.append(dic["name"])
            index=index+1

getCourses()
print("*************************ParentExercise**********************************")
user=int(input("enter  course id:--"))
def parentExercise(user):
        parentsFile="exercise_"+str(user)+".json"
        if os.path.exists(parentsFile): 
            with open(parentsFile,'r') as user_url_data:
                url_data=json.load(user_url_data)
            # json.dump(url_data,user_url_data,indent=4)

            listFromDict=(url_data["data"])
            print("COURSE NAME:---",list_for_name[user])
            index=0
            for i in listFromDict:
                print(index,"ParentExercise:---",i["name"])
                list_for_slug.append(i["slug"])

                index=index+1
                
                if  len (i["childExercises"])>0:
                    count=0
                    for j in i["childExercises"]:
                        print("       ",count,j["name"])
                        count=count+1

                else:
                    print("child_exercise not available")
        else:
            user_url=requests.get("https://merakilearn.org/api/courses/"+list_for_id[user] +"/exercises")
            response_url=(user_url.text)
            with open(parentsFile,'w') as user_url_data:
                
                url_data=json.loads(response_url)

                json.dump(url_data,user_url_data,indent=4)
            listFromDict=(url_data["data"])
            print("COURSE NAME:---",list_for_name[user])
            index=0
            for i in listFromDict:
                print(index,"ParentExercise:---",i["name"])
                # list_for_slug.append(i["slug"])

                index=index+1
                
                if  len (i["childExercises"])>0:
                    count=0
                    for j in i["childExercises"]:
                        list_for_slug.append(j["slug"])

                        print(count,j["name"])
                        count=count+1

                else:
                    print("child_exercise not available")

parentExercise(user)
print("************************slug********************************************")
count =0
for i in list_for_slug:
    print(count,":",i)
    count=count+1

slugUser=int(input("enter slug id:--"))
def getSlug(slugUser):
    slug_of_user=list_for_slug[slugUser]
    # print(slug_of_user)
    user_content=requests.get("https://merakilearn.org/api/courses/"+list_for_id[user] +" /exercise/getBySlug?slug=" +slug_of_user)
    response_of_content=(user_content.text)
    # print(type(response_of_content))
    # print("in dict:----",response_of_content)
    with open("fresh_content_data.json",'w') as content_file:
        data_of_content=json.loads(response_of_content)
        json.dump(data_of_content,content_file,indent=2)


    content=data_of_content["content"]
    # print(content)
    return(content)
print(getSlug(slugUser))



while True:
    seeAgain=input("enter what you want to do 1. up 2. next 3. previous : 4. stop")
    if seeAgain=="up":
        getCourses()
    elif seeAgain=="next":
        slugUser=slugUser+1
        print(getSlug(slugUser))
       
    elif seeAgain=="previous":
        slugUser=slugUser-1
        print(getSlug(slugUser) )    
    else:
        print("Thank For Visit To Saral Page!!!!!!!!!")
        break






 







    



