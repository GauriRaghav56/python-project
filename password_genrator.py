import random # randome cheze choose karne ke liye hota h
import string # module m ready made letters numbers or symbols hote h
length = int(input("password ki length enter karo:")) # password ki length
characters = string.ascii_letters + string.digits + string.punctuation # sabi charecter ko jodne ke liye
gauri = ""  # ye ek khali string bnai h jisme password store hoga 
for i in range(length):  # loop utni baar chlega jitni password ki length h
    gauri += random.choice(characters)  # har baar character m se ek random charecter utha kar jod dega 
print("Genrated Password:",gauri) # final password screen par dika dega 8