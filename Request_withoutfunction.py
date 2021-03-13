import requests
import json
print("**********WELCOME TO SARAL PAGE*********************")
request=requests.get("http://merakilearn.org/api/courses")
response=request.text
with open("courses.json",'w') as response_data:
    data=json.loads(response)
    json.dump(data,response_data,indent=4)

dict_data=data["availableCourses"]
index=0
id_list=[]
course_id=[]
while index <len (data["availableCourses"]):
    dic=(data["availableCourses"][index])
    print(index,dic["name"],dic ["id"])
    id_list.append(dic["id"])
    course_id.append(dic["name"])
    index=index+1


print("*************************ParentExercise**********************************")
user=int(input("enter  course id:--"))
user_url=requests.get("https://merakilearn.org/api/courses/"+id_list[user] +"/exercises")
response_url=(user_url.text)
with open("data.json",'w') as user_url_data:
    
    url_data=json.loads(response_url)

    json.dump(url_data,user_url_data,indent=4)
listFromDict=(url_data["data"])
slug_id=[]
print("COURSE NAME:---",course_id[user])
index=0
for i in listFromDict:
    print(index,"ParentExercise:---",i["name"])
    slug_id.append(i["slug"])

    index=index+1
    
    if  len (i["childExercises"])>0:
        count=0
        for j in i["childExercises"]:
            print(count,j["name"])
            count=count+1

    else:
        print("child_exercise not available")


print("************************slug********************************************")

 
    
slugUser=int(input("enter slug id:--"))
slug_of_user=slug_id[slugUser]
print(slug_of_user)
user_content=requests.get("https://merakilearn.org/api/courses/"+id_list[user] +" /exercise/getBySlug?slug=" +slug_of_user)
response_of_content=(user_content.text)
# print(z)
with open("content_data.json",'w') as content_file:
    data_of_content=json.loads(response_of_content)
    json.dump(data_of_content,content_file,indent=2)


# data2=json.loads(z)
print(data_of_content)
print(slug_id)

print("***********************UP,NEXT,PREVIOUS**************************")

user_forwhat_next=input("what you want to do up,next or previous:--------")
if user_forwhat_next=="up":
    request=requests.get("http://merakilearn.org/api/courses")
    response=request.text
    with open("courses.json",'w') as response_data:
        data=json.loads(response)
        json.dump(data,response_data,indent=4)
 
    dict_data=data["availableCourses"]
    index=0
    id_list=[]
    course_id=[]
    while index <len (data["availableCourses"]):
        dic=(data["availableCourses"][index])
        print(index,dic["name"],dic ["id"])
        id_list.append(dic["id"])
        course_id.append(dic["name"])
        index=index+1
    print("*************************ParentExercise**********************************")
    user=int(input("enter  course id:--"))
    user_url=requests.get("https://merakilearn.org/api/courses/"+id_list[user] +"/exercises")
    response_url=(user_url.text)
    with open("data.json",'w') as user_url_data:
        
        url_data=json.loads(response_url)

        json.dump(url_data,user_url_data,indent=4)
    listFromDict=(url_data["data"])
    slug_id=[]
    print("COURSE NAME:---",course_id[user])
    index=0
    for i in listFromDict:
        print(index,"ParentExercise:---",i["name"])
        slug_id.append(i["slug"])

        index=index+1
        
        if  len (i["childExercises"])>0:
            count=0
            for j in i["childExercises"]:
                print(count,j["name"])
                count=count+1

        else:
            print("child_exercise not available")


    print("************************slug********************************************")

    
        
    slugUser=int(input("enter slug id:--"))
    slug_of_user=slug_id[slugUser]
    print(slug_of_user)
    user_content=requests.get("https://merakilearn.org/api/courses/"+id_list[user] +" /exercise/getBySlug?slug=" +slug_of_user)
    response_of_content=(user_content.text)
    # print(z)
    with open("content_data.json",'w') as content_file:
        data_of_content=json.loads(response_of_content)
        json.dump(data_of_content,content_file,indent=2)


    # data2=json.loads(z)
    print(data_of_content)
    print(slug_id)


        

elif user_forwhat_next=="next":
    slugUseragain=1+slugUser

    slug_of_user=slug_id[slugUseragain]
    print(type(slug_id[slugUser]))
    print(slug_of_user)
    user_content=requests.get("https://merakilearn.org/api/courses/"+id_list[user] +" /exercise/getBySlug?slug=" +slug_of_user)
    response_of_content=(user_content.text)
    with open("content_data.json",'w') as content_file:
        data_of_content=json.loads(response_of_content)
        json.dump(data_of_content,content_file,indent=2)

    print(data_of_content)
elif user_forwhat_next=="previous":
    slugUseragain=slugUser-1

    slug_of_user=slug_id[slugUseragain]
    print(slug_of_user)
    user_content=requests.get("https://merakilearn.org/api/courses/"+id_list[user] +" /exercise/getBySlug?slug=" +slug_of_user)
    response_of_content=(user_content.text)
    
    with open("content_data.json",'w') as content_file:
        data_of_content=json.loads(response_of_content)
        json.dump(data_of_content,content_file,indent=2)


    
    print(data_of_content)


print("************THANK TO VISIT***********************")





 







    



