# core/management/commands/add_challenges.py

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from core.models import CodeChallenge, ProgrammingLanguage

class Command(BaseCommand):
    help = 'Populates the database with a set of initial code challenges.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting to add code challenges...")

        # This will get the 'Python' language object, or create it if it doesn't exist.
        python_lang, created = ProgrammingLanguage.objects.get_or_create(
            slug='Python',
            defaults={'name': 'python'}
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created ProgrammingLanguage: Python'))

        # --- THIS IS WHERE YOU DEFINE ALL YOUR CHALLENGES ---
        # It's a list of dictionaries. Just add a new dictionary for each new challenge.
        
                # --- THIS IS WHERE YOU DEFINE ALL YOUR CHALLENGES ---
        # It's a list of dictionaries. Just add a new dictionary for each new challenge.
        challenges_to_add = [
    {
        'title': 'The First Impression',
        'description': 'Every coding journey starts here. No cap. Your first mission is to tell the computer to say "I am a coder!". Use the print function.',
        'code_template': 'print("___")',
        'correct_answers': ['I am a coder!'],
        'difficulty': 1,
        'points': 5,
    },
    {
        'title': 'The Naming Ceremony',
        'description': 'Hard-coding text is... not the vibe. Let\'s store your username in a variable. Variables are like labels for your stuff. Create a variable called `user` and give it the value "notacoder".',
        'code_template': '___ = "notacoder"',
        'correct_answers': ['user'],
        'difficulty': 1,
        'points': 5,
    },
    {
        'title': 'Number Crunching',
        'description': 'Let\'s do some math. Your character just found 2 health potions, but used 1. Calculate the final potion count.',
        'code_template': 'potions_found = 2\npotions_used = 1\nfinal_potions = potions_found - ___',
        'correct_answers': ['potions_used'],
        'difficulty': 1,
        'points': 10,
    },
    {
        'title': 'The Mashup',
        'description': 'Time to combine some text. This is called "concatenation" (fancy, right?). Combine the `greeting` and `name` to introduce your character.',
        'code_template': 'greeting = "A new challenger appears: "\nname = "Nikita"\nintro = greeting + ___',
        'correct_answers': ['name'],
        'difficulty': 2,
        'points': 10,
    },
    {
        'title': 'The f-string Glow Up',
        'description': 'Okay, the `+` sign for strings is kinda clunky. The cool kids use f-strings. They let you put variables right inside your string. It\'s a whole mood. Print the score using an f-string.',
        'code_template': 'score = 100\nprint(f"Your score is: {___}")',
        'correct_answers': ['score'],
        'difficulty': 2,
        'points': 12,
    },
    {
        'title': 'ALL CAPS ENERGY',
        'description': 'Sometimes you need to yell. The `.upper()` method converts a string to all uppercase. Let\'s make your game title shout.',
        'code_template': 'game_title = "Quest for Python"\nloud_title = game_title.___()',
        'correct_answers': ['upper'],
        'difficulty': 2,
        'points': 15,
    },
    {
        'title': 'The Inventory',
        'description': 'In games, you have an inventory. In Python, you have lists! They hold a bunch of items in order. Access the first item in your inventory (a "sword"). Btw, computers start counting from 0. It\'s a thing.',
        'code_template': 'inventory = ["sword", "shield", "potion"]\nfirst_item = inventory[___]',
        'correct_answers': ['0'],
        'difficulty': 3,
        'points': 10,
    },
    {
        'title': 'Loot Drop!',
        'description': 'You just found a "gem"! You need to add it to the end of your inventory list. The `.append()` method is your bestie here.',
        'code_template': 'inventory = ["sword", "shield"]\ninventory.___("gem")',
        'correct_answers': ['append'],
        'difficulty': 3,
        'points': 15,
    },
    {
        'title': 'How Many Things?',
        'description': 'Is your inventory full? The `len()` function tells you how many items are in a list. Find out how many items are in your inventory.',
        'code_template': 'inventory = ["sword", "shield", "gem", "map"]\nitem_count = ___(inventory)',
        'correct_answers': ['len'],
        'difficulty': 3,
        'points': 15,
    },
    {
        'title': 'The Vibe Check',
        'description': 'Time to make decisions. The `if` statement runs code ONLY if a condition is true. Check if the player\'s level is high enough to enter the dungeon.',
        'code_template': 'level = 12\n___ level > 10:\n    print("You may enter.")',
        'correct_answers': ['if'],
        'difficulty': 4,
        'points': 15,
    },
    {
        'title': 'This or That',
        'description': 'What if the condition is false? That\'s where `else` comes in. It\'s the "otherwise" part of your logic. Let\'s check a password.',
        'code_template': 'password_guess = "12345"\nif password_guess == "secret_code":\n    print("Access granted.")\n___:\n    print("Access denied.")',
        'correct_answers': ['else'],
        'difficulty': 4,
        'points': 20,
    },
    {
        'title': 'The VIP Lounge',
        'description': 'Let\'s combine checks. The `and` keyword checks if BOTH conditions are true. You need to be a VIP *and* have enough gold to get in.',
        'code_template': 'is_vip = True\ngold = 150\nif is_vip ___ gold > 100:\n    print("Welcome to the lounge.")',
        'correct_answers': ['and'],
        'difficulty': 4,
        'points': 20,
    },
    {
        'title': 'The To-Do List',
        'description': 'A `for` loop goes through each item in a list, one by one. It\'s perfect for printing every item in your quest log.',
        'code_template': 'quests = ["Find the sword", "Defeat the dragon", "Save the village"]\nfor ___ in quests:\n    print(quest)',
        'correct_answers': ['quest'],
        'difficulty': 5,
        'points': 20,
    },
    {
        'title': 'Counting Up',
        'description': 'Don\'t want to loop over a list? The `range()` function creates a sequence of numbers for you. This will count from 0 to 4.',
        'code_template': 'for number in range(___):\n    print(number)',
        'correct_answers': ['5'],
        'difficulty': 5,
        'points': 20,
    },
    {
        'title': 'Character Sheet',
        'description': 'Lists are cool for order, but dictionaries are for labeled info using key-value pairs. It\'s the main character energy of data storage. Let\'s create a profile for your hero.',
        'code_template': 'player_profile = {\n    "name": "Alex",\n    "class": "Mage",\n    "level": ___\n}',
        'correct_answers': ['5'],
        'difficulty': 6,
        'points': 25,
    },
    {
        'title': 'Accessing Your Stats',
        'description': 'To get info from a dictionary, you use the key inside square brackets. It\'s way more readable than a random number. Grab your character\'s weapon from their stats.',
        'code_template': 'stats = {"weapon": "Fire Staff", "armor": "Robe"}\ncurrent_weapon = stats["___"]',
        'correct_answers': ['weapon'],
        'difficulty': 6,
        'points': 25,
    },
    {
        'title': 'Leveled Up!',
        'description': 'Your character gained a level! Time to update their profile. You can change a value in a dictionary by accessing the key and assigning a new value.',
        'code_template': 'player_profile = {"name": "Alex", "level": 5}\nplayer_profile["level"] = ___',
        'correct_answers': ['6'],
        'difficulty': 6,
        'points': 25,
    },
    {
        'title': 'Your First Spell',
        'description': 'Typing the same code over and over is a drag. Functions are reusable blocks of code. Let\'s make a function that calculates damage. The `return` keyword is how a function sends a value back.',
        'code_template': 'def calculate_damage(base_attack, bonus):\n    total = base_attack + bonus\n    ___ total',
        'correct_answers': ['return'],
        'difficulty': 7,
        'points': 30,
    },
    {
        'title': 'Default Greetings',
        'description': 'What if a function argument is optional? You can set a default value! This `greet` function will say "Hello, Adventurer!" if you don\'t provide a name.',
        'code_template': 'def greet(name="___"):\n    print(f"Hello, {name}!")',
        'correct_answers': ['Adventurer'],
        'difficulty': 7,
        'points': 30,
    },
    {
        'title': 'Casting the Spell',
        'description': 'You\'ve defined the `calculate_damage` function. Now, let\'s *call* it to actually use it. Calculate the damage with a `base_attack` of 50 and a `bonus` of 10.',
        'code_template': 'def calculate_damage(base_attack, bonus):\n    return base_attack + bonus\n\nfireball_damage = ___(50, 10)',
        'correct_answers': ['calculate_damage'],
        'difficulty': 7,
        'points': 30,
    },
]

        

        # This loop creates the challenges in the database.
        for chal_data in challenges_to_add:
            # get_or_create is the key: it prevents creating duplicates.
            # It looks for a challenge with the same title. If it finds one, it skips it.
            # If not, it creates a new one.
            challenge, created = CodeChallenge.objects.get_or_create(
                title=chal_data['title'],
                defaults={
                    'slug': slugify(chal_data['title']),
                    'language': python_lang,
                    'description': chal_data['description'],
                    'code_template': chal_data['code_template'],
                    'correct_answers_list': chal_data['correct_answers'], # This matches your model field name
                    'difficulty': chal_data['difficulty'],
                    'points_reward': chal_data['points'],
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully created challenge: '{chal_data['title']}'"))
            else:
                self.stdout.write(self.style.WARNING(f"Challenge '{chal_data['title']}' already exists. Skipping."))
        
        self.stdout.write(self.style.SUCCESS("\nFinished adding challenges!"))