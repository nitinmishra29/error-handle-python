file = open ("youtube.txt","w") # its open a fie with write it id doesn't exist then its create with same name

try:
    file.write(" lala jija")
finally:
    file.close()


    # or 

with open ("youtube.txt",'w') as file:
    file.write("dncdnf")