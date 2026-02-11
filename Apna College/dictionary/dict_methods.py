student = {
    "Name" : "SHOVON",
    "Subject" : {
        "PHY" : 98.5,
        "CHE" : 98,
    }
}

print(student.keys())
print(student["Subject"].keys())
print(list(student.keys())) # type casting


# total number of key value
print(len(student))
print(len(list(student)))


# all values
print(student.values())
print(list(student.values()))


# return all key:value pair as tupple
print(student.items())
print(list(student.items()))
pairs = list(student.items())
print(pairs[0])



# get method -> return the key accourding to value
print(student["Name"])
print(student.get("Name"))  # eita use hoi jate oi key exist na korleu error na dia None return kore...but uporer ta korle jdi key exist na kore thle error dei


# update methods
student.update({
    "city" : "Satkhira"
})

new_dict = {
    "Game Name" : "Clash Of Clans",
    "Start Year" : 2015,
    "End Year" : "Running",
    "Some Defense Name" : ["Air Defense", "Wizard Tower"],
    "Some Troops Name" : ("Barbrain", "Archer"),
    "is_any_hero" : True,
}

student.update(new_dict)
print(student)