__author__ = 'Yih-Yoon Lee'
import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def createDrink(style_answer):
    drink = []
    for pref, ans in style_answer.iteritems():
        if ans == True:
            drink.append(random.choice(ingredients[pref]))
    print drink
    return drink

def drinkStyle(q):
    style_answer = {}
    for ingredient, question in questions.iteritems():

        answer = raw_input(question)

        var = 1
        while var == 1:

            if answer.upper() == 'Y' or answer.upper() == 'yes':
                style_answer[ingredient] = True
                break
            elif answer.upper() == 'N' or answer.upper() == 'no':
                style_answer[ingredient] = False
                break
            else:
                answer2 = raw_input('Invalid answer. Please try again: ')
                if answer2.upper() == 'Y' or answer.upper() == 'yes':
                    style_answer[ingredient] = True
                    break
                elif answer2.upper() == 'N' or answer.upper() == 'no':
                    style_answer[ingredient] = False
                    break
    return style_answer

def cocktail(name):
    print 'cocktail name'


def main():
    askDrink = drinkStyle(questions)
    drinkIngredient = createDrink(askDrink)
    print 'Your drink ingredients are {}'.format(drinkIngredient)

if __name__ == '__main__':
    main()
