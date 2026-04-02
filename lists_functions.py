# 7.4 
things = ["mozzarella", "cinderella", "salmonella"]

# 7.5
things[1].capitalize()
print(things)

# 7.6
things[0] = things[0].upper()
print(things) 

# 7.7
things.remove("salmonella")
print(things) 

# 9.1 
def good():
    return ['Harry', 'Ron', 'Hermoine']
print(good())

# 9.2
def get_odds():
    for number in range(10):
        if number % 2 != 0:
            yield number

count = 0
for number in get_odds():
    count += 1
    if count == 3:
        print(number) 
        break 