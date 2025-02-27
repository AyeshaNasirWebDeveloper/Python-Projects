def game():
    print("Welcome to Mad Libs: The Quest for the Lost Treasure!")
    print("\n Please provide the following words to create your story. Hints are provided to guide you!\n")

    # Collect user input with hints
    adjective1 = input("\n Adjective (e.g., mysterious, magical): ")
    plural_noun = input("\n Plural Noun (e.g., pirates, bananas): ")
    animal = input("\n Animal (e.g., parrot, tiger): ")
    verb_ing = input("\n Verb ending in -ing (e.g., running, singing): ")
    color = input("\n Color (e.g., blue, golden): ")
    exclamation = input("\n Exclamation (e.g., Wow, Oh no!): ")
    food = input("\n Type of Food (e.g., pizza, spaghetti): ")
    adverb = input("\n Adverb (e.g., quickly, mysteriously): ")
    number = input("\n Number (e.g., 3, 100): ")
    mythical_creature = input("\n Mythical Creature (e.g., dragon, unicorn): ")
    body_part = input("\n Body Part (e.g., nose, elbow): ")
    adjective2 = input("\n Adjective (e.g., frightened, confused): ")
    verb = input("\n Verb (e.g., run, disappear): ")
    noun = input("\n Noun (e.g., rock, door): ")
    adjective3 = input("\n Adjective (e.g., shiny, ancient): ")

    # Automatically decide "a" or "an" for the adjective
    if adjective1[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        article = "an"
    else:
        article = "a"

    # Create the story
    story = f"""
    Once upon a time, in {article} {adjective1} land far, far away, there was a brave adventurer named Captain {plural_noun}. 
    Captain {plural_noun} was no ordinary explorer—they traveled with their trusty {animal} named Sparky, who was always {verb_ing} by their side.

    One day, while sailing across the {color} ocean, Captain {plural_noun} spotted a mysterious island. "{exclamation}!" they shouted. 
    "This must be the island of the lost treasure!" The crew quickly docked their ship and set off into the jungle, armed with nothing but a map and a basket of {food}.

    As they ventured deeper into the jungle, they encountered {adverb} glowing tree. Suddenly, {number}-headed {mythical_creature} jumped out and roared, 
    "Who dares enter my domain?" Captain {plural_noun} bravely stepped forward and said, "We seek the lost treasure! Stand aside, or I'll tickle your {body_part}!"

    The creature, clearly {adjective2}, decided to {verb} away into the shadows. The crew pressed on until they found a massive {noun} blocking their path. 
    With a mighty heave, they moved it aside and discovered a chest filled with {adjective3} gold, jewels, and ancient artifacts.

    Captain {plural_noun} and Sparky cheered, "We did it! The treasure is ours!" And so, they sailed back home, richer and more famous than ever before.

    The End.

    Created by: Ayesha Nasir
    """

    # Print the story
    print("\n Here's your Mad Libs story:\n")
    print(story)


game()