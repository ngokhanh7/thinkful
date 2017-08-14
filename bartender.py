import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

# Write a function to ask what style of drink a customer likes

# The function should ask each of the questions in the questions dictionary,
# and gather the responses in a new dictionary. The new dictionary should contain
# the type of ingredient (for example "salty", or "sweet"), mapped to a Boolean value.
# If the customer answers y or yes to the question then the value should be True,
# otherwise the value should be False. The function should return the new dictionary.

# Remember that you can use the input function to get an answer from the customer.
# If you can't remember how this works then take a look back over the instructions
# for the FizzBuzz project.

valid = {"yes": True, "y": True, "no": False, "n": False}
drink_response = {"strong": False, "salty": False, "bitter": False, "sweet": False, "fruity": False}


def drink_type():
    salty = input(questions["salty"])
    strong = input(questions["strong"])
    bitter = input(questions["bitter"])
    sweet = input(questions["sweet"])
    fruity = input(questions["fruity"])

    if salty in valid:
        drink_response["salty"] = valid[salty]
    if bitter in valid:
        drink_response["bitter"] = valid[bitter]
    if strong in valid:
        drink_response["strong"] = valid[strong]
    if fruity in valid:
        drink_response["fruity"] = valid[fruity]
    if sweet in valid:
        drink_response["sweet"] = valid[sweet]

    return drink_response


def make_drink(responses):
    drink = []
    if responses["salty"] == True:
        drink.append(random.choice(ingredients["salty"]))
    if responses["bitter"] == True:
        drink.append(random.choice(ingredients["bitter"]))
    if responses["strong"] == True:
        drink.append(random.choice(ingredients["strong"]))
    if responses["fruity"] == True:
        drink.append(random.choice(ingredients["fruity"]))
    if responses["sweet"] == True:
        drink.append(random.choice(ingredients["sweet"]))

    return drink


if __name__ == "__main__":
    drink_type()
    print (make_drink(drink_response))