#Alphabet String
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#The list will print the ASCII value of each character besides the letters in Grants name
alphabetList = [i if i in ["G","R","A","N","T"] else print(f"the ASCII Value of {i} is {ord(i)}") for i in alphabet]
print("feature 1")
