def getname():
    name=str(input("What is your name?"))
    return name
def getMfeet():
    mfeet=str(input("What is your chosen unit metres or feet?"))
    return mfeet
def getHeight():
    height=float(input("What is your height?"))
    return height
def getKgpounds():
    kgpounds=str(input("What is your chosen unit kilograms or pounds?"))
    return kgpounds
def getWeight():
    weight=float(input("What is your weight?"))
    return weight

def getBMI(getname,getMfeet, getHeight, getKgpounds, getWeight):
    if mfeet=="metres" "m" and kgpounds=="kilograms" "kg" "kilogram":
        BMI==(weight/height**2)
        print (BMI)
                
    elif mfeet=="feet" "ft" "f" and kgpounds=="kilograms" "kg" "kilogram":
        metres =(height/3.2808)
        BMI==(weight/metres**2)
        print (BMI)
                
    elif mfeet=="metres" "m" and kgpounds=="pounds" "lb":
        kilograms =(weight/2.2)
        BMI==(kilograms/weight**2)
        print (BMI)
    
            
    elif mfeet=="feet" "ft" "f" and kgpounds=="pounds" "lb":
        BMI==(weight*4.88/height**2)
        print (BMI)
    return BMI

def getResults(getBMI):
    if BMI<18.4:
        print (name,"you are underweight, this is as your BMI is ",BMI)
        print ("In order to raise your BMIA BMI below 18.5 classifies you as underweight. The Academy of Nutrition and Dietetics has some healthy ways to add extra calories to your diet. The first step is to eat more frequently and")
        print ("increase the number of meals you eat each day to five or six. Consume nutrient-rich foods such as pasta, whole-grain bread, fruits and vegetables. Supplement your diet with protein shakes and smoothies that contain")
        print ("ample calories. Eat calorie-dense snack foods such as peanut butter, nuts, meats and cheese. Other healthy snack options include bran muffins, yogurt and granola bars. Be sure to exercise; it can increase your muscle")
        print ("mass, which increases your weight, and it may stimulate your appetite.")

    elif BMI<=18.5>=24.9:
        print (name,"you have a normal BMI, this is as your BMI is ",BMI)
        print ("keep going about your daily life and as you have been adn you will fine")

    elif BMI<=25>=29.9:
        print (name,"you are overweight, this is as your BMI is ",BMI)
        print ("A couple of extra pounds are not a health risk for most people. But being overweight can lead to health problems that is why it is best to act now by exercising more and eating healthier")

    elif BMI<=30>=39.9:
        print (name,"you are obese, this is as your BMI is ",BMI)
        print("")

    elif BMI>=40:
        print (name,"you are very obsese, this is as your BMI is ",BMI)

name=getname()
mfeet=getMfeet()
height=getHeight()
kgpounds=getKgpounds()
weight=getWeight()
BMI=getBMI(getname,getMfeet, getHeight, getKgpounds, getWeight)

print (getResults(getBMI(getname,getMfeet, getHeight, getKgpounds, getWeight)))
