import requests, json

x = requests.get('http://saral.navgurukul.org/api/courses')
with open("datafile.json","w") as f:
    json.dump(x.json(),f,indent=4)
with open("datafile.json","r")as file:
    s=json.load(file)
l=[]
c=0
for i in s["availableCourses"]:
    # print(i)
    c+=1
    print(c,i["name"]+"=",i["id"])
    l.append(int(i["id"]))
user=int(input("enter id no.:-"))
if user in l:
    a=requests.get("http://saral.navgurukul.org/api/courses/"+str(l[user])+"/exercises")
    T=a.json()
    slug=[]
    h=0
    j=0
    while j<len(T["data"]):
        print(h+1,"=",T["data"][j]["name"])
        slug.append(T["data"][j]["slug"])
        h=h+1
        j=j+1
    slugname=int(input("enter slug no.:-"))-1
    p=requests.get("http://saral.navgurukul.org/api/courses/"+str(user)+"/exercise/getBySlug?slug="+slug[slugname])
    p2=p.json()
    with open("urlslug.json","w")as g:
        json.dump(p2,g,indent=4)
    print(p2["name"])
    print(p2["slug"])
    print("Content",p2["content"])
else:
    print("your course no. does not exist")


