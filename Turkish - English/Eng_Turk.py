# English - Turkish Dictionary

words = {} # <class 'dict'>

# Read File
with open("Turk-Eng.txt", "r") as file: 
    for line in file:
        splitline = line.split()
        words[splitline[0]] = ",".join(splitline[1:])
                    
# Search
def Search():
    print(" \n 1.) Search Word ")
    print(" 2.) Quit ")
    
    control = input(" Please enter your process number : ")
    if(control == str(1)):
         while True:
             word = input(" Please enter your word : ") # <class 'str'>
             word = word.title() # First letter is capital
             
             if word in words:  
                 print(f" {word} : {words[word]}\n ")
             else:
                 print(" This word is not found ")         
                 
             print(" \n 1.) Continue ")
             print(" 2.) Quit ") 
             control = int(input("Please enter your process number : "))
             if control == 2:
                 break
# Add
def Add():
    print(" \n 1.) Add Word ")
    print(" 2.) Quit ")
    
    control = input("Please enter your process number : ")
    if(control == str(1)):
         
         while True:
             A = ' '
             word = input("Please enter your word : ") # <class 'str'>
             word = word.title() # First letter is capital
             if word.count(' ') > 0: # This code diversify -> Hello_world 
                 for i in word:
                     if i == ' ':
                         i = '_'
                     A += i
                 word = A
             
             syn = False
             for i in word:
                 if syn != True: 
                     if((i =='ü' or i=='Ü')or(i =='ğ' or i =='Ğ')or(i == 'ö' or i=='Ö')
                     or (i =='ş' or i=='Ş')or(i == 'ç' or i=='Ç')or(i == 'ı')):
                         print("Syntax Error")
                         syn = True
             
             if syn == False:
                 mean = input("Please enter your word meaning : ")
                 mean = mean.lower()
                 if mean.count(" ") > 0:
                     for i in mean:
                         if i == " ":
                             i = '_'
                         A += i
                     mean = A
             A = " "
             if mean.count(",") > 0: # This code diversify -> Hello_world 
                 for i in range(len(mean)):
                     cind = mean.index(",") 
                     if (i == cind):
                         A += '' 
                     
                     if ((i != (cind-1) and mean[i] != '_')or(i != (cind+1) and mean[i] != '_')):
                         A += mean[i]    
                 mean = A
             
                 
                 # !!!
                 with open("Turk-Eng.txt", "a") as file:
                     file.writelines(f" {word} ")
                 
                 words[word] = mean
                 with open("Turk-Eng.txt", "a") as file:
                     file.writelines(f" {mean} \n")
                    
                    
             print(" \n 1.) Continue ")
             print(" 2.) Quit ") 
             control = int(input(" Please enter your process number : "))
             if control == 2:

                 break
# Delete
def Delt():
    print(" \n 1.) Delete Word ")
    print(" 2.) Quit ")
    
    control = input(" Please enter your process number : ")
    if(control == str(1)):
         
         while True:
             word = input(" Please enter your word : ") # <class 'str'>
             word = word.title() # First letter is capital
             print()
             if word in words.keys():  
                 print(f" {word} : {words[word]}\n ")
                 
                 # !!!
                 with open("Turk-Eng.txt", "r") as file:
                     lines = file.readlines()
                 with open("Turk-Eng.txt", "w") as file:
                     for line in lines:
                         splitline = line.split()
                         if splitline[0] != word:
                             file.write(line)
                         
                 words.pop(word)
             else:
                 print(" This word is not found ")
                 
             print(" \n 1.) Continue ")
             print(" 2.) Quit ") 
             control = int(input(" Please enter your process number : "))
             if control == 2:
                 break
# Menu         
def Menu():
    print("\n 1.) Search Word : ")
    print(" 2.) Add Word : ")
    print(" 3.) Delete Word : ")
    print(" 4.) Show Words ")
    print(" 5.) Quit : ")                      
   
    pro = input(" Please enter your process number : ")
    

    if(pro == str(1)):
        Search()
    elif(pro == str(2)):
        Add()
    elif(pro == str(3)):
        Delt()
    elif(pro == str(4)):
        print()
        for i in words:
            print(f"{i} : {words[i]}")
        
    return pro 
    
  
# Main Function 
while True:
    res = Menu()
    if( res == str(5)):
        break
    
    

    