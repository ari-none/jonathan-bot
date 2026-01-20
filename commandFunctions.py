import random as r

def diceroll(dices: int, faces: int) -> str:
    dices = max(dices, 1)
    faces = max(faces, 1)
    resultString = f"## Dice roll (d{faces}) :\n\n"
    for dice in range(dices):
        roll = r.randint(1, faces)
        resultString += f"**Die {dice+1}** : `{roll}`\n"
    return  resultString