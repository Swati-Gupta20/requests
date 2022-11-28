import requests
import json

x = requests.get('http://saral.navgurukul.org/api/courses')
x2=x.json()
with open("courses.json",'w') as f:
    json.dump(x2,f,indent=4)
# print(x2)
l=[]
with open("courses.json",'r+') as file:
    s=json.load(file)
# print(s['availableCourses'][0])
i=0
while i<len(s['availableCourses']):
    print(i+1,".",s['availableCourses'][i]['name']+'......'+s['availableCourses'][i]['id'])
    l.append(int(s["availableCourses"][i]['id']))
    i+=1
# print(l)

user=int(input("enter serial no.:-"))-1
if user in l:
    a=requests.get("http://saral.navgurukul.org/api/courses/"+str(l[user])+"/exercises")
    a2=a.json()
    j=0
    sl=0
    slug=[]
    while j<len(a2["data"]):
        print(sl+1,a2["data"][j]["name"])
        j+=1
        sl+=1
    with open("urlfile.json","w") as f:
        json.dump(a2,f,indent=4)


# import requests,json
# def request():
#     x=requests.get("http://saral.navgurukul.org/api/courses")
#     with open("ram.json","w") as f:
#         json.dump(x.json(),f,indent=4)
#     with open("ram.json","r") as f:
#         data=json.load(f)
#     a=[]
#     c=0
#     for i in data[ "availableCourses"]:
#         c+=1
#         print(c,i["name"],"=",i["id"])
#         a.append(int(i["id"]))
#     print()
#     choose=int(input("select you choice:-"))
#     if choose in a:
#         at=requests.get("http://saral.navgurukul.org/api/courses/"+str(a[choose])+"/exercises")
#         T=at.json()
#         slug=[]
#         h=0
#         j=0
#         while j<len(T["data"]):
#             print(h+1,"=",T["data"][j]["name"])
#             slug.append(T["data"][j]["slug"])
#             h=h+1
#             j=j+1 
#         slugname=int(input("enter your slug number:-"))
#         list=requests.get("http://saral.navgurukul.org/api/courses/"+str(choose)+"/exercise/getBySlug?slug="+slug[slugname])
#         t=list.json()
#         print(t["name"])
#         print(t["slug"])
#         print("content",t["content"])   
#     else:
#         print("your course number does not exist")
# request()