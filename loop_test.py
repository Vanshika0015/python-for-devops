for i in range(101):
    env= input(print("Please give the envir0nment name"))
print("The environment is",env)
if env=="prod":
    print("Dont deploy on friday")
elif env=="stg":
    print("Take backup and test well")
else:
    print("Safe to deploy on any day")    
