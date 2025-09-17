#Acess string by index ([],[])

my_str = "Hello Bob"

print(my_str[4])

# Concatenation

first_name = "Frank"
last_name = "Escobar"
full_name = first_name + " " + last_name



result = first_name + " " + last_name
guess = 3
result = "Sorry, your guess ("+ str(guess) + ")  is not correct. Try lower."
print(result)

# Formatted String

guess = 9
result = f"Sorry, your guess ({guess}) is not correct. Try lower."
print(result)


# BUILT IN FUNCTIONS (.upper()) .split() .strip() dir() help()
result = first_name.upper()
result = first_name.lower()
result = full_name.split()
result = first_name+"        "
result = result.strip()
result = result + "."

print(dir(result)) #same as result.      shows all options available to strings
print(help(str.count))




print(result)