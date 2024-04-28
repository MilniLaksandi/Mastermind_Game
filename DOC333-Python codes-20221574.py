import random

is_run = True

while is_run:
    
    #get the player name 
    Student_Name=str(input("\t\t\tEnter Student Name:"))
    #output with player name
    print("\t\tHi!!! ",Student_Name+"\tWelcome to GameInt")
    
    Start=input("Do You Need Instructions Or Otherwise Directly Into The Game.\t[I/G]:")
    if Start=="I"or Start=="i":
         print("There will be 1 to 6 numbers according to the colour.")
         print("Player just need to enter the correct number of the colour.")
         print("For ex:Red colour, Player should enter number 2.")
         print("Player should guess 4 numbers.")
         print("Computer also will michanically create 4 numbers based on colour and if they are maching with the player entered numbers... ")
         print("Player can win the Game...")
         print("\t\t\t\tGOOD LUCK!!!")
    

    print("\t\t Number to Guess - XXXX "+"\t Colour Mapping 1-Blue 2-Red 3-Purple 4-White 5-Yellow 6-Green")
    score = 0
    for i in range(8):
        
        #Variables
        listplayer =[]
        listmachine =[]
        result=0;
        display=[]
        repeat_Num=1
        atampt =str(i+1)
        num1=1

        #get user values
        while repeat_Num<=4:
            repeat=str(repeat_Num)
            num = int(input("Entered number "+repeat+" :",))
            #checking input values between 1 to 6
            if(1<=num<=6):
                listplayer.append(num)
                repeat_Num+=1
            else:
                print("Numbers Should Be Between 1 to 6")

        #random number genarate
        while num1<=4:
            number = random.randint(1,6)
            #checking the random number exists in the list
            if(number in listmachine):
                continue
            else:
                listmachine.append(number)
                num1=num1+1;
    

        #Iterate the user input list
        for i in listplayer:
            #check one value exists in the system genarated values list
            if (i in listmachine):
                #if it is true then check both player guessed numbers and machine generated numbers are same
                if(listplayer.index(i)==listmachine.index(i)):
                    result=1
                    display.append(result)
                else:
                    result=0
                    display.append(result)
            else:
                result="-"
                display.append(result)
                
        #calculate the score        
        status = 1
        outPut = True

        #repeat the display list
        for i in display:
            #check all the values not equal to the status value
            if (status != i):
                output =False
                break

        #checking the output True or false , if it is true score increment by one
        if(output):
            score = score+1

        #display number of attempts and machine generated values and results  
        print("\tAttempt No\t\tGuess\t\t\tResult")       
        print("\t\t"+atampt+"\t\t"+str(listmachine)+"\t\t"+str(display))


    #after the 8 attempts display the attempts are over and the final score    
    print("Your Attempts Are Over")
    print("score "+ str(score))

    #if the score is 0 then machine will display win or lost
    if (score!=0):
        print("Congratulations !!! You won the game")
    else:
        print("Sorry !!! Try again")
        
    answer = str(input("Do You Want To Play Again (yes/no) : "))
    
    if answer=="yes":
        is_run=True
    else:
        is_run=False
