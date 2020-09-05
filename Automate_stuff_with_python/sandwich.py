import pyinputplus as pyip
import time
import re
d = {
    "Wheat":1,
    "White":2,
    "Sourdough":3,
    "Chicken":10,
    "Turkey":20,
    "Ham":15,
    "Tofu":10,
    "Cheddar":12,
    "Swiss":15,
    "Mozarella":20,
    }

total_amount = 0
def sandwich():
    global total_amount
    print("Please choose your items for the sandwich")
    time.sleep(2)
    bread = pyip.inputMenu(['Wheat', 'White', 'Sourdough'],numbered=True)
    protien = pyip.inputMenu(['Chicken','Turkey','Ham','Tofu'],numbered=True)
    cheese_y = pyip.inputYesNo(prompt="Do you want cheese?")
    cheese_regex = re.compile(r'^([yY])?$|(yes|YES)?')
    if cheese_regex.search(cheese_y):
        cheese = pyip.inputMenu(['Cheddar','Swiss','Mozarella'],numbered=True)
        total_amount+=d[cheese]
    mayo = pyip.inputYesNo(prompt="Do you want mustard,mayo and tomato?")
    mayo_regex = re.compile(r'^([yY])?$|(yes|YES)?')
    if mayo_regex.search(mayo):
        total_amount+=6
    no_sandwich = pyip.inputInt(prompt="How many sandwiches do you want?",blockRegexes=[r'^0$'])
    total_amount+=d[bread]+d[protien]
    total_amount*=no_sandwich
sandwich()
print("Your total bill is %d\nThank you!"%(total_amount))
    


    
    

    

    

