from sys import argv
import sys

sand_ingd = list(('ham', 'cheese', 'tomatoes'))
cake_ingd = list(('flour', 'sugar', 'eggs'))
salad_ingd = list(('avocado', 'arugula', 'tomatoes', 'spinach'))
s_dict = dict(ingredients=sand_ingd, meal='lunch', prep_time=10)
c_dict = dict(ingredients=cake_ingd, meal='desert', prep_time=60)
s_dict = dict(ingredients=salad_ingd, meal='lunch', prep_time=15)
cookbook = dict(sandwich=s_dict, cake=c_dict, salad=s_dict)


def print_recipe(recipe_name):
    recipe_data = cookbook.get(recipe_name)
    print(f"""\nRecipe for {recipe_name}:
Ingredients list: {recipe_data.get('ingredients')}
To be eaten for {recipe_data.get('meal')}
Takes {recipe_data.get('prep_time')} of cooking.""")


def delete_recipe(recipe_name):
    del cookbook[recipe_name]


def add_recipe():
    print('Let\'s add a new recipe!')
    print('Enter a name')
    new_name = str(input())
    print('Enter the ingredients (separate each one by a space)')
    raw_ing = str(input())
    new_ing = raw_ing.split(' ')
    print('Enter the meal type')
    new_meal = str(input())
    print('Enter the number of minutes needed (ex: 15)')
    new_time = str(input())
    new_rec = dict(ingredients=new_ing, meal=new_meal, prep_time=new_time)
    final_rec = {f"{new_name}": new_rec}
    print(final_rec)
    cookbook[f"{new_name}"] = new_rec
    print(f'{new_name} has successfuly been added to your cookbook!')


def print_all_recipes():
    output = "\nHere are all the recipes of your cookbook: "
    len_book = len(cookbook)
    i = 0
    for n in cookbook:
        if i < len_book-1:
            cond = True
        else:
            cond = False
        liaison = ('.', ',')[cond]
        output += str(n) + liaison
        i += 1
    print(output)


usage = """Please select an option by typing one of the following numbers:
1. Print a recipe
2. Delete a recipe
3. Add a recipe
4. Print all recipes
5. Quit
        """
print(usage)
while True:
    try:
        response = int(input())
        if response == 5:
            print('Cookbook closed.')
            sys.exit()
        if response == 4:
            print_all_recipes()
            continue
        if response == 3:
            add_recipe()
            continue
        if response == 1:
            print_all_recipes()
            print('Please chose one by writting it\'s name')
            resp = input()
            # check if recipe exists in dict
            if cookbook.get(resp) is None:
                print('Sorry, this recipe is not in this cookbook.')
                print_all_recipes()
                continue
            else:
                print_recipe(resp)
            continue
        if response == 2:
            print_all_recipes()
            print("""
            Please choose the one you wish to delete by writting it\'s name""")
            resp = input()
            # check if recipe exixts in dict
            if cookbook.get(resp) is None:
                print('Sorry, this recipe is not in this cookbook.')
                print_all_recipes()
                continue
            else:
                del cookbook[resp]
                print(f'{resp} has been deleted.')
                continue
        else:
            print('This option does not exist.')
            print(usage)
            continue
    except SystemExit:
        sys.exit()
    except ValueError:
        print('This option does not exist.')
        print(usage)
