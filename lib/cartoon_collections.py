def roll_call_dwarves(dwarves):
    for index, item in enumerate(dwarves):
        print(f"{index + 1}. {item}")

def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + "!" for call in planeteer_calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(ingredients):
    cheese_types = ["cheddar", "gouda", "camembert"]
    for ingredient in ingredients:
        if ingredient in cheese_types:
            return ingredient 
    return None 


