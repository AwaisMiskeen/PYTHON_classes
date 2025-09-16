class employee:
    # name = "Harry"
    language = "Python" #this is class attribute
    salary = "200000"

awais=employee()
awais.name = "M.Awais" # this is an instance atribute
print(awais.name, awais.language, awais.salary)

asad = employee()
asad.name = "M.Asad"
print(asad.name, asad.language, asad.salary)

# here name is instance attribute and salary and language are class attribute as the directly belong to the class
