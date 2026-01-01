info ={
    "name" :'mubeen',
    "age" : 12,
    "marks": 94.1,
    "surname":"khan",
}
print(info)
print(info["name"])
info["name"] = "mujtaba"
print(info)     #####simple program of dictionaries in python

marks ={
 "subjects" : ["english","urud","maths","science"],  ###using lists in dic
 "marks" : (94,100,102,90) #### using tuple
}




student={
    "name": "mubeen khan",
    "subject":{
        "phy":90,
        "chem":100,
        "maths":80

    }
}                          ####nested dict
print(student)
print(student.keys()) ####will get all keys
print(student.values())   ### will get all vaules
print(student.items())    ####converts all items into tuples
print(student.get("name"))  ### will get a specific vaule according to the key
student.update({"city":"swat"}) ### will update the dict with key vaule pairs mentioned

print(student)


school={
    "name": "khyber",
    "subjet":{               
      "english":89,
      "urdu":98, 
      "maths":100
    }
}
print(school)
print(school.keys())
print(school.values())
print(school.items())
print(school.get("name"))
school.update({"subject":"science"})
print(school)
