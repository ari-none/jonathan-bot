import random as r
from json import loads

def diceroll(dices: int, faces: int) -> str:
    dices = max(dices, 1)
    faces = max(faces, 1)
    resultString = f"## Dice roll (d{faces}) :\n\n"
    for dice in range(dices):
        roll = r.randint(1, faces)
        resultString += f"**Die {dice+1}** : `{roll}`\n"
    return  resultString

tipsList = loads(open("./jsonfiles/tips.json").read())
def tips() -> str:
    rtip1 = tipsList["game"][r.randint(0, len(tipsList["game"]) - 1)]
    rtip2 = tipsList["real"][r.randint(0, len(tipsList["real"]) - 1)]
    result = f"""## ——Gameplay Tips——
```{rtip1}```
## ——Real world Tips——
```{rtip2}```"""

    return result

