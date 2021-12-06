import pandas as pd 
choices= ["A","B","C","D","E"]
choicesB = ["A","B"]
Status=[]
GenderList =[]
AgeList=[]
WeightList=[]
HeightList=[]
BMRList=[]
Data = [GenderList,AgeList,WeightList,HeightList,BMRList,Status]



def Sedentary():
    while True:
        BMR = Data[4][0]
        BMMR = float(BMR)
        Sedent = BMMR * 1.2
        if Data[5][0] == "Severely UnderWeight" or Data[5][0] == "UnderWeight" :
            print("Please Select From choices")
            GainorLose = input("[A] Gain (Only Choice)\n").upper()
            while GainorLose.strip()== "" or GainorLose.upper() not in choicesB:
                print("Input was invalid, Please Select only the choices provided. ThankYou!")
                GainorLose= str(input("Please select among the list:")).upper()

            if GainorLose == "A":
                Sedent += 300
                SedentDivided = Sedent/3
                print ("Your New Calorie Count is:",Sedent)
                print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
                print("")
                print("")
                print("Hi! this is your Calorie Count Assistant! i would high recommend following\nthe prescribed calorie intake. the disregard to follow the prescribed calorie count could lead to an\nunhealthy increase or decrease of weight. Thankyou!")
                            
        elif Data[5][0] == "Healthy":
            print("Congrats, You are Healthy!\nno need for calorie modification!")
            print ("Your New Calorie Count is:",Sedent)
            SedentDivided = Sedent/3
            print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
            print("")
            print("")
            print("Hi! this is your Calorie Count Assistant! i would high recommend following\nthe prescribed calorie intake. the disregard to follow the prescribed calorie count could lead to an\nunhealthy increase or decrease of weight. Thankyou!")
                
            
        elif Data[5][0] == "OverWeight":
            print("Please Select From choices")
            GainorLose = input("[A] Gain [B] Reduce\n").upper()
            while GainorLose.strip()== "" or GainorLose.upper() not in choicesB:
                print("Input was invalid, Please Select only the choices provided. ThankYou!")
                GainorLose= str(input("Please select among the list:")).upper()

            if GainorLose == "A":
                Sedent += 300
                SedentDivided = Sedent/3
                print ("Your New Calorie Count is:",Sedent)
                print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
                print("")
                print("")
                print("Hi! this is your Calorie Count Assistant! i would high recommend following\nthe prescribed calorie intake. the disregard to follow the prescribed calorie count could lead to an\nunhealthy increase or decrease of weight. Thankyou!")
                
            else:
                Sedent -= 500
                SedentDivided = Sedent/3
                print ("Your New Calorie Count is:",Sedent)
                print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
                print("")
                print("")
                print("Hi! this is your Calorie Count Assistant! i would high recommend following\nthe prescribed calorie intake. the disregard to follow the prescribed calorie count could lead to an\nunhealthy increase or decrease of weight. Thankyou!")
                
            
        elif Data[5][0] == "Obese":
        
            print("Please Select From choices")
            GainorLose = input("[B] Reduce(Only Choice)\n").upper()
            while GainorLose.strip()== "" or GainorLose.upper() not in choicesB:
                
                print("Input was invalid, Please Select only the choices provided. ThankYou!")
                GainorLose= str(input("Please select among the list:")).upper()

            if GainorLose == "B":
                Sedent -= 500
                SedentDivided = Sedent/3
                print ("Your New Calorie Count is:",Sedent)
                print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
                print("")
                print("")
                print("Hi! this is your Calorie Count Assistant! i would high recommend following\nthe prescribed calorie intake. the disregard to follow the prescribed calorie count could lead to an\nunhealthy increase or decrease of weight. Thankyou!")
        print ("---------------------------------")
        print("Thankyou for Using the program!\nProgram will now exit, Goodbye!")
        quit()


  
    
    

def LightAct():

    while True:
        BMR = Data[4][0]
        BMMR = float(BMR)
        Sedent = BMMR * 1.375
        if Data[5][0] == "Severely UnderWeight" or Data[5][0] == "UnderWeight" :
            print("Please Select From choices")
            GainorLose = input("[A] Gain (Only Choice)\n").upper()
            while GainorLose.strip()== "" or GainorLose.upper() not in choicesB:
                print("Input was invalid, Please Select only the choices provided. ThankYou!")
                GainorLose= str(input("Please select among the list:")).upper()

            if GainorLose == "A":
                Sedent += 300
                SedentDivided = Sedent/3
                print ("Your New Calorie Count is:",Sedent)
                print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
                print("")
                print("")
               
        elif Data[5][0] == "Healthy":
            print("Congrats, You are Healthy!\nno need for calorie modification!")
            print ("Your New Calorie Count is:",Sedent)
            SedentDivided = Sedent/3
            print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
            print("")
            print("")
           
        elif Data[5][0] == "OverWeight":
            print("Please Select From choices")
            GainorLose = input("[A] Gain [B] Reduce\n").upper()
            while GainorLose.strip()== "" or GainorLose.upper() not in choicesB:
                print("Input was invalid, Please Select only the choices provided. ThankYou!")
                GainorLose= str(input("Please select among the list:")).upper()

            if GainorLose == "A":
                Sedent += 300
                SedentDivided = Sedent/3
                print ("Your New Calorie Count is:",Sedent)
                print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
                print("")
                print("")
                
            else:
                Sedent -= 500
                SedentDivided = Sedent/3
                print ("Your New Calorie Count is:",Sedent)
                print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
                print("")
                print("")
                
        elif Data[5][0] == "Obese":

            print("Please Select From choices")
            GainorLose = input("[B] Reduce(Only Choice)\n").upper()
            while GainorLose.strip()== "" or GainorLose.upper() not in choicesB:
                print("Input was invalid, Please Select only the choices provided. ThankYou!")
                GainorLose= str(input("Please select among the list:")).upper()

            if GainorLose == "B":
                Sedent -= 500
                SedentDivided = Sedent/3
                print ("Your New Calorie Count is:",Sedent)
                print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
                print("")
                print("")
               
        print ("---------------------------------")
        print("Thankyou for Using the program!\nProgram will now exit, Goodbye!")
        quit()



        
    
def Moderate():
    while True:
        BMR = Data[4][0]
        BMMR = float(BMR)
        Sedent = BMMR * 1.55
        if Data[5][0] == "Severely UnderWeight" or Data[5][0] == "UnderWeight" :
            print("Please Select From choices")
            GainorLose = input("[A] Gain (Only Choice)\n").upper()
            while GainorLose.strip()== "" or GainorLose.upper() not in choicesB:
                print("Input was invalid, Please Select only the choices provided. ThankYou!")
                GainorLose= str(input("Please select among the list:")).upper()

            if GainorLose == "A":
                Sedent += 300
                SedentDivided = Sedent/3
                print ("Your New Calorie Count is:",Sedent)
                print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
                print("")
                print("")
                
        elif Data[5][0] == "Healthy":
            print("Congrats, You are Healthy!\nno need for calorie modification!")
            print ("Your New Calorie Count is:",Sedent)
            SedentDivided = Sedent/3
            print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
            print("")
            print("")
           
        elif Data[5][0] == "OverWeight":
            
            print("Please Select From choices")
            GainorLose = input("[A] Gain [B] Reduce\n").upper()
            while GainorLose.strip()== "" or GainorLose.upper() not in choicesB:
                print("Input was invalid, Please Select only the choices provided. ThankYou!")
                GainorLose= str(input("Please select among the list:")).upper()

            if GainorLose == "A":
                Sedent += 300
                SedentDivided = Sedent/3
                print ("Your New Calorie Count is:",Sedent)
                print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
                print("")
                print("")
               
            else:
                Sedent -= 500
                SedentDivided = Sedent/3
                print ("Your New Calorie Count is:",Sedent)
                print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
                print("")
                print("")
                
        elif Data[5][0] == "Obese":

            print("Please Select From choices")
            GainorLose = input("[B] Reduce(Only Choice)\n").upper()
            while GainorLose.strip()== "" or GainorLose.upper() not in choicesB:
                print("Input was invalid, Please Select only the choices provided. ThankYou!")
                GainorLose= str(input("Please select among the list:")).upper()

            if GainorLose == "B":
                Sedent -= 500
                SedentDivided = Sedent/3
                print ("Your New Calorie Count is:",Sedent)
                print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
        
        print ("---------------------------------")
        print("Thankyou for Using the program!\nProgram will now exit, Goodbye!")
        quit()
    
def Active():
    while True:
        BMR = Data[4][0]
        BMMR = float(BMR)
        Sedent = BMMR * 1.725
        if Data[5][0] == "Severely UnderWeight" or Data[5][0] == "UnderWeight" :
            print("Please Select From choices")
            GainorLose = input("[A] Gain (Only Choice)\n").upper()
            while GainorLose.strip()== "" or GainorLose.upper() not in choicesB:
                print("Input was invalid, Please Select only the choices provided. ThankYou!")
                GainorLose= str(input("Please select among the list:")).upper()

            if GainorLose == "A":
                Sedent += 300
                SedentDivided = Sedent/3
                print ("Your New Calorie Count is:",Sedent)
                print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
                print("")
                print("")
                
        elif Data[5][0] == "Healthy":
            
            print("Congrats, You are Healthy!\nno need for calorie modification!")
            print ("Your New Calorie Count is:",Sedent)
            SedentDivided = Sedent/3
            print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
            print("")
            print("")
            
        elif Data[5][0] == "OverWeight":
            
           
            print("Please Select From choices")
            GainorLose = input("[A] Gain [B] Reduce\n").upper()
            while GainorLose.strip()== "" or GainorLose.upper() not in choicesB:
                print("Input was invalid, Please Select only the choices provided. ThankYou!")
                GainorLose= str(input("Please select among the list:")).upper()

            if GainorLose == "A":
                Sedent += 300
                SedentDivided = Sedent/3
                print ("Your New Calorie Count is:",Sedent)
                print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
                print("")
                print("")
                
            else:
                Sedent -= 500
                SedentDivided = Sedent/3
                print ("Your New Calorie Count is:",Sedent)
                print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
                print("")
                print("")
                
        elif Data[5][0] == "Obese":

            print("Please Select From choices")
            GainorLose = input("[B] Reduce(Only Choice)\n").upper()
            while GainorLose.strip()== "" or GainorLose.upper() not in choicesB:
                print("Input was invalid, Please Select only the choices provided. ThankYou!")
                GainorLose= str(input("Please select among the list:")).upper()

            if GainorLose == "B":
                Sedent -= 500
                SedentDivided = Sedent/3
                print ("Your New Calorie Count is:",Sedent)
                print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
                print("")
                print("")
               
        print ("---------------------------------")
        print("Thankyou for Using the program!\nProgram will now exit, Goodbye!")
        quit()
    
def VeryAct():
    while True:
        BMR = Data[4][0]
        BMMR = float(BMR)
        Sedent = BMMR * 1.9
        if Data[5][0] == "Severely UnderWeight" or Data[5][0] == "UnderWeight" :
            print("Please Select From choices")
            GainorLose = input("[A] Gain (Only Choice)\n").upper()
            while GainorLose.strip()== "" or GainorLose.upper() not in choicesB:
                print("Input was invalid, Please Select only the choices provided. ThankYou!")
                GainorLose= str(input("Please select among the list:")).upper()

            if GainorLose == "A":
                Sedent += 300
                SedentDivided = Sedent/3
                print ("Your New Calorie Count is:",Sedent)
                print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
                print("")
                print("")
                
        elif Data[5][0] == "Healthy":
            print("Congrats, You are Healthy!\nno need for calorie modification!")
            print ("Your New Calorie Count is:",Sedent)
            SedentDivided = Sedent/3
            print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
            print("")
            print("")
           
        elif Data[5][0] == "OverWeight":
            print("Please Select From choices")
            GainorLose = input("[A] Gain [B] Reduce\n").upper()
            while GainorLose.strip()== "" or GainorLose.upper() not in choicesB:
                print("Input was invalid, Please Select only the choices provided. ThankYou!")
                GainorLose= str(input("Please select among the list:")).upper()

            if GainorLose == "A":
                Sedent += 300
                SedentDivided = Sedent/3
                print ("Your New Calorie Count is:",Sedent)
                print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
                print("")
                print("")
                
            else:
                Sedent -= 500
                SedentDivided = Sedent/3
                print ("Your New Calorie Count is:",Sedent)
                print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
                print("")
                print("")
                
        elif Data[5][0] == "Obese":

            print("Please Select From choices")
            GainorLose = input("[B] Reduce(Only Choice)\n").upper()
            while GainorLose.strip()== "" or GainorLose.upper() not in choicesB:
                print("Input was invalid, Please Select only the choices provided. ThankYou!")
                GainorLose= str(input("Please select among the list:")).upper()

            if GainorLose == "B":
                Sedent -= 500
                SedentDivided = Sedent/3
                print ("Your New Calorie Count is:",Sedent)
                print("Your 3 Daily Meals should be:",SedentDivided,"Calories Each")
                print("")
                print("")
               
        print ("---------------------------------")
        print("Thankyou for Using the program!\nProgram will now exit, Goodbye!")
        quit()
    
    



def ChooseActivity():
    while True:
        print ("Please Select Activity Factor")
        ActFactor = input("[A] Sedentary ---- (1.2)\n[B] Light Active ---- (1.375)\n[C] Moderate ---- (1.55)\n[D] Active ---- (1.725)\n[E] Very Active ---- (1.9)\n---------------------------------\n").upper()
        
        while ActFactor.strip()== "" or ActFactor.upper() not in choices:
            print("Input was invalid, Please Select only the choices provided. ThankYou!")
            ActFactor= str(input("Please select among the list:")).upper()

        if ActFactor =="A":
            Sedentary()
        elif ActFactor =="B":
            LightAct()
        elif ActFactor =="C":
            Moderate()
        elif ActFactor =="D":
            Active()
        elif ActFactor =="E":
            VeryAct()
        
        
        
def main():
    while True:
        
        print ("---------------------------------")
        print (" Please Select Gender ")
         
        gender = input("[A] Male , [B] Female\n---------------------------------\n")
        print ("---------------------------------")
        

        while gender.strip()== "" or gender.upper() not in choicesB:
            
            print("Input was invalid, Please Select only the choices provided. ThankYou!")
            gender= str(input("Please select among the list:")).upper()
        while True:
            
            try:
                
                Height = float(input("Please Enter Height in cm: "))
                print ("---------------------------------")
                Weight = float(input("Please Enter Weight in Kg: "))
                print ("---------------------------------")
                Age = int(input("Please Enter Age: "))
                print ("---------------------------------")
                break
            
            except ValueError:
                print("value not a number")
        BMI = Weight /((Height/100)**2)
        if ( BMI < 16):
            Status.append("Severely UnderWeight")
        elif ( BMI >= 16 and BMI < 18.5):
           Status.append("UnderWeight")
        elif ( BMI >= 18.5 and BMI < 25):
           Status.append("Healthy")
        elif ( BMI >= 25 and BMI < 30):
           Status.append("OverWeight")
        elif ( BMI >=30):
           Status.append("Obese")
        if (gender == "A"):
            BMR = 88.362 +(13.397*Weight)+(4.799*Height)-(5.677 * Age)
        else:
            BMR = 447.593 +(9.247*Weight)+(3.098*Height)-(4.330 * Age)
        
        print("Body Mass Index of Person:",BMI)
        print("Status of Person:",Data[5])
        print("---------------------------------")
        
        GenderList.append(gender)
        AgeList.append(Age)
        WeightList.append(Weight)
        HeightList.append(Height)
        BMRList.append(BMR)
        
        dict = {'Gender':Data[0]}
        df = pd.DataFrame(dict)
        df.to_csv('GenderCSV.csv')
        
        dict = {'Age':Data[1]}
        df = pd.DataFrame(dict)
        df.to_csv('AgeCSV.csv')

        dict = {'WeightList':Data[2]}
        df = pd.DataFrame(dict)
        df.to_csv('WeightCSV.csv')

        dict = {'HeightList':Data[3]}
        df = pd.DataFrame(dict)
        df.to_csv('HeightCSV.csv')

        dict = {'BMR':Data[4]}
        df = pd.DataFrame(dict)
        df.to_csv('BMRCSV.csv')

        dict = {'Status':Data[5]}
        df = pd.DataFrame(dict)
        df.to_csv('StatusCSV.csv')

        ChooseActivity()

        

        
main()
