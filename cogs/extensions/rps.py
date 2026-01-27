from discord import Color

# String array of available choices
e_list = ["rock", "scissors", "gun", "fennec", "paper", "dude", "water"]

# List of elements (and what can they beat)
e_match = {
    "rock": ["scissors", "gun", "fennec"],
    "scissors": ["gun", "fennec", "paper"],
    "gun": ["fennec", "paper", "dude"],
    "fennec": ["paper", "dude", "water"],
    "paper": ["dude", "water", "rock"],
    "dude": ["water", "rock", "scissors"],
    "water": ["rock", "scissors", "gun"]
}

# List of messages for each match
e_message = {
    "rock": {
        "scissors": "The rock breaks the scissors.",
        "gun": "The rock breaks the gun.",
        "fennec": "The rock smashes the fennec's skull."
    },
    "scissors": {
        "gun": "The scissors jams the gun.",
        "fennec": "The scissors stabs the fennec.",
        "paper": "The scissors cuts the paper."
    },
    "gun": {
        "fennec": "The gun shoots the fennec.",
        "paper": "The gun shoots the paper.",
        "dude": "The gun shoots the dude."
    },
    "fennec": {
        "paper": "The fennec eats the paper.",
        "dude": "The fennec devours the dude.",
        "water": "The fennec drinks the water."
    },
    "paper": {
        "dude": "The paper applies the dude for a job.",
        "water": "The paper absorbs the water.",
        "rock": "The paper covers the rock."
    },
    "dude": {
        "water": "The dude drinks the water.",
        "rock": "The dude breaks the rock.",
        "scissors": "The dude disassembles the scissors."
    },
    "water": {
        "rock": "The water wets the rock.",
        "scissors": "The water rusts the scissors",
        "gun": "The water jams the gun."
    }
}

# Messages for ties
e_tie = {
    "rock": "The rocks are chilling together.",
    "scissors": "The scissors started an arts & crafts project.",
    "gun": "The guns are staring at each other, MENACINGLY.",
    "fennec": "The fennecs became best friends !",
    "paper": "The papers folded into airplanes & flew away.",
    "dude": "The dudes kissed each other.",
    "water": "The, uhh, idk ? Water unified I guess ?"
}



# Actual code
def match(a: str, b:str) -> bool:
    return b in e_match[a]

def rps (user_choice: str, bot_choice:str) -> tuple[str, str, Color]:
    """Takes the user & bot's choices. Returns a title conclusion, match conclusion and color."""
    if user_choice == bot_choice:
        return "It's a tie !", e_tie[user_choice], Color.blue()
    elif match(user_choice, bot_choice):
        return "You won !", e_message[user_choice][bot_choice], Color.green()
    else:
        return "You lost !", e_message[bot_choice][user_choice], Color.red()