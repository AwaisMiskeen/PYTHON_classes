marks = {
    "Awais" : 90,
    "Asad" : 94,
    "Dani" : 87,
        0 : "Awais"
}
# print(marks.items()) # return alll items of the dictionary
# print(marks.keys()) # return all keys of the dictionary
# print(marks.values()) # return all values of the dictionary
# marks.update({"Awais" : 80 , "Ali" : 50}) # update the dictionary
# print(marks)
marks.pop(0)
print(marks)

# print(marks.get("Awais2")) # prints none
# print(marks["Awais2"]) # prints an error