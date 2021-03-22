# MODULE: A file containing a set of functions we want to include in our application.
    # we can use the module, by using the import statement.
    # we can choose to import only parts from a module, by using the from keyword.
    # The randint() method returns an integer number between given min and max integers.
    
from random import randint

# VARIABLES: Variables are containers for storing data values.
# DATA TYPES: Variables can store data of different types, and different types can do different things, for example : Numeric Types: int, float; Boolean Type: bool; Sequence Types: list ...etc.

#player_name = 'Amir'
#player_attack = 10
#player_heal = 15
#player_health = 100

# PRINT(): The print() function prints the specified message to the screen, the object will be converted into a string before written to the screen.

#print('Hello!')
#print(player_name)

# LIST: Lists are used to store multiple items in a single variable.

#player = ['Amir', 10, 15, 100]

# TYPE(): The type() function returns the type of the specified object.

#print(type(player))

# INDEX: List items are indexed, the first item has index [0], the second item has index [1] etc. We can access a specific item in list by it's Index.

#print(player[0])
#print(player[3])

# CHANGABLE: List items are ordered, changeable, and allow duplicate values.

#player[1] = 20
#print(player[1])

# FUNCTION : A function is a block of code which only runs when it is called.
    # We can pass data, known as parameters, into a function.
    # A function can return data as a result.
    # In Python a function is defined using the def keyword.
    # Block of code inside a function should be indented. 
    # To call a function, use the function name followed by parenthesis
    # Information can be passed into functions as arguments when it is called.
    # Code in python is read from top to bottom therefore function should be defined in the code before calling it, else python will not be aware of our function and will throw error.

# INDENTATION: Indentation refers to the spaces at the beginning of a code line. Python uses indentation to indicate a block of code.
# PARAMETER: A parameter is the variable listed inside the parentheses in the function definition.
# ARGUMENT: An argument is the value that is sent to the function when it is called.

def calculate_monster_attack(min, max):
    return randint(min, max)

def game_over(winner_name):

# F-STRING: f-string or formated string literals allow us to dynamically inject content into a strings.
    # We use f keyword and wrap content that we want dynamically inject into our string with curly braces.
    
    print(f'{winner_name} Won')

# BOOLEAN: Booleans represent one of two values: True or False.

game_running = True
game_results = []

#Python has two primitive loop commands
    #WHILE LOOP: while loop we can execute a set of statements as long as a condition is true.
    #FOR LOOP: A for loop is used for iterating over a sequence (that is either a list, a dictionary, or a string).

while game_running == True:
    
    counter = 0
    new_game = True
    
# DICTIONARY: Dictionary allow us to store multiple items in a single variable in key:value pairs.
    # Dictionary items are presented in key:value pairs, hence can be accessed by using the key name.

    player = {'name': 'Placeholder', 'attack': 10, 'heal': 15, 'health': 100}
    monster = {'name': 'Dragon', 'attack_min': 10, 'attack_max': 15, 'health': 100}

    #print(player['name'])
    #print(player['health'])

# OPERATORS: Operators are used to perform operations on variables and values.
    #Arithmetic operators are used with numeric values to perform common mathematical operations.(+, -, *, /, %)
    #Assignment operators are used to assign values to variables.(=, +=, -=, *=, /=, %=)
    #Comparison operators are used to compare two values.(==, !=, <, >, <=, >=)
    #Logical operators are used to combine conditional statements.(and, or, not)

    print('---' * 7)
    print('WELCOME TO MONSTER SLAYER')
    print('---' * 7)
    print('Enter Player name')
    player['name'] = input()
    print('---' * 7)

# STRING CONCATENATION: String concatenation means add strings together. Use the + character to add a variable to another variable.
# STR(): The str() function converts the specified value into a string.

    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health')

    while new_game == True:

        counter = counter + 1
        player_won = False
        monster_won = False

        print('---' * 7)
        print('Please select an action')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit')
        print('4) Leaderboard')

# INPUT(): The input() function allows user input. It always returns a string

        #input()
        player_choice = input()

# IF: If statements are control flow statements that help us to run a particular code, but only when a certain condition is met or satisfied.

        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:

# PASS: The pass statement is used as a placeholder for future code.

                #pass
                player_won = True

#ELSE: If the condition of if statement is False, then the body of else is executed.
                
            else:

#The randint() method returns an integer number between given min and max integers.

                player['health'] = player['health'] - calculate_monster_attack(monster['attack_min'], monster['attack_max'])
                if player['health'] <= 0:
                    monster_won = True

# Elif: If the previous if statement conditions are not true, then its condition is checked.

        elif player_choice == '2':
            player['health'] = player['health'] + player['heal']

            player['health'] = player['health'] - calculate_monster_attack(monster['attack_min'], monster['attack_max'])
            if player['health'] <= 0:
                monster_won = True
            
        elif player_choice == '3':
            new_game = False
            game_running = False

        elif player_choice == '4':
            
#FOR LOOP: A for loop is used for iterating over a sequence (that is either a list, a dictionary, or a string).

            for item in game_results:
                print(item)

        else:
            print('Invalid Input')

        if player_won == False and monster_won == False:
            print(player['name'] + ' has ' + str(player['health']) + ' health left')
            print(monster['name'] + ' has ' + str(monster['health']) + ' health left')

        elif player_won == True:
            game_over(player['name'])
            
# We can also add dictionary as an item to the list.
            
            round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter}

# APPEND: Append is the default method availale to the list, it allow us to append an item to the end of an existing list.
            
            game_results.append(round_result)
            new_game = False

        elif monster_won:
            game_over(monster['name'])
            round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter}
            game_results.append(round_result)
            new_game = False


