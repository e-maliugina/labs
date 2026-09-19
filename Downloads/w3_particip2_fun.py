pythoners = {
    "responses": [
        {
            "name": "Rohullah Assadzay",
            "favorite_color": "blue",
            "favorite_planet": "Venus",
            "fun_fact": "I really like playing games but I suck at them",
        },
        {
            "name": "Raymond",
            "favorite_color": "dark blue",
            "favorite_planet": "Saturn",
            "other_fun_fact": "My male green cheek conure, Harley Quinn, just turned 21 years old in March.",
        },
        {
            "name": "Casey Davis",
            "favorite_planet": "Saturn (use to be pluto before the hatred)",
            "random_fun_fact": "Sharks will go into a Comatose state if you can flip the upside down (first hand experience).",
        },
        {
            "name": "Pattharasittha Deevech",
            "favorite_color": "Red",
            "favorite_planet": "Super Earth",
            "other_fun_fact": "I like Godzilla",
        },
        {
            "Arizona Cardinals": "Glendale, AZ",
            "New York Giants": "East Rutherford, NJ",
            "Kanas City Chiefs": "Kanas City, MO",
        },
        {
            "name": "sarah",
            "favorite color": "purple",
            "favorite planet": "saturn",
            "fun fact": "I just got an ice machine and I'm really excited about it.",
        },
        {
            "name": "Makaden",
            "favorite_color": "Aqua Green",
            "favorite_planet": "Uranus",
            "other_fun_fact": "I have a dog named Leia, like princess leia organa",
        },
        {
            "name": "Yasir",
            "age": 22,
            "favorite_planet": "Saturn",
            "other_fun_fact": "i lived in India",
        },
        {
            "name": "Adryiana",
            "favorite dessert": "Chocolate Chip Cookies",
            "favorite candy": "M&Ms",
            "other_fun_fact": "I like to rollerblade and draw.",
        },
        {
            "name": "Jose",
            "favorite_color": "Black",
            "favorite_planet": "Mars",
            "other_fun_fact": "I am a father of two children",
        },
        {
            "nickname": "Lizzy",
            "hobby": "puzzles",
            "favorite drink": "lemonade",
            "favorite game genre": "metroidvania",
            "least favorite part of school": "writing essays",
        },
        {
            "name": "Janae Mireles",
            "favorite_color": "Red",
            "favorite_planet": "Jupiter",
            "other_fun_fact": "I enjoy playing guitar and hiking on the weekends.",
        },
        {
            "name": "Tasneem M",
            "favorite_color": "Beige and Brown",
            "favorite_planet": "Saturn; Don't get me wrong, I also love Earth, but Saturn to me is very beautiful and interesting :)",
            "fun_fact": "I am a high school student, and I take college credit classes, and I also work a job in retail.",
        },
        {
            "name": "Misker",
            "favorite_color": "blue",
            "favorite_planet": "Earth",
            "other_fun_fact": "I like music and soccer",
        },
        {
            "name": "Hannah",
            "favorite_color": "Pink",
            "favorite_planet": "Earth",
            "other_fun_fact": "I like playing video games",
        },
        {
            "name": "Ali Tarom",
            "favorite_color": "Purple",
            "favorite_planet": "Earth",
            "other_fun_fact": "I like cars, planes, and traveling.",
        },
        {
            "name": "Joe Widdifield",
            "favorite_color": "Blue",
            "favorite_planet": "Neptune",
            "fun_fact": "I have 2 cats, Angus and Junebug :)",
        },
    ],
    "new_users": [
        "Amelia",
        "Adhanet",
        "Claude",
        "Istar",
        "Kieran",
        "Kennedy",
    ],
}

# Explain your function concept
# Write a function that does something interesting with the above dictionary `pythoners`
# ONLY SUBMIT WHAT IS BELOW THIS LINE


def my_custom_function_give_it_a_better_name_please():
    """Explain what your function is doing here"""

def person_and_fact(pythoners):
    """Returns the person's name and fun fact"""
    for person in pythoners["responses"]:
        name = person.get("name", "No name listed")
        if name == "No name listed":
            name = person.get("nickname", "No name listed")
        print(f"Name: {name} ", end=' ')
        fact = person.get("fun_fact", "No fun fact listed")
        if fact == "No fun fact listed":
            fact = person.get("fun fact", "No fun fact listed")
            if fact == "No fun fact listed":
                fact = person.get("random_fun_fact", "No fun fact listed")
                if fact == "No fun fact listed":
                    fact = person.get("other_fun_fact", "No fun fact listed")
        print(f"Fun Fact: '{fact}'")

person_and_fact(pythoners)