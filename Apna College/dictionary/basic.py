dict = {
    "Game Name" : "Clash Of Clans",
    "Start Year" : 2015,
    "End Year" : "Running",
    "Some Defense Name" : ["Air Defense", "Wizard Tower"],
    "Some Troops Name" : ("Barbrain", "Archer"),
    "is_any_hero" : True,
}
print(dict)
print(type(dict))
print(dict["Game Name"])

dict["Game Name"] = "COC"
print(dict["Game Name"])

dict["TH lvl"] = 17
print(dict)