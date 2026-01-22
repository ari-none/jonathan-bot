import random as r
from json import loads
from discord import User, Embed, Color


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



def coolness_rd(user: User) -> str:
    preval = r.gauss(mu=75, sigma=40)  # center at 75
    val = max(0, min(100, round(preval)))

    # val = r.randint(0, 100) --Old code
    if val == 100:
        return "[100%] The coolest user you'll ever see :sunglasses:"
    elif val >= 75:
        return f"[{val}%] {user.display_name} is really cool ! :star2:"
    elif val >= 50:
        return f"[{val}%] {user.display_name} is pretty cool actually :kissing_smiling_eyes:"
    elif val >= 30:
        return f"[{val}%] I guess {user.display_name} is somewhat okay :neutral_face:"
    elif val >= 15:
        return f"[{val}%] {user.display_name} ain't cool."
    elif val >= 1:
        return f"[{val}%] {user.display_name} REALLY ain't cool."
    else:
        return f"[{val}%] {user.display_name} ! GET YOUR BITCH ASS OUT !"

def coolness(user: User) -> tuple[Embed, bool]:
    if not user:
        return Embed(), False

    emb = Embed(color=Color.green(), title="Coolness meter")

    match user.id:
        case 1:
            emb.description = "Value"
            return emb, True
        case 1463098594016886969:
            emb.description = f"[∞%] It's me. No one's cooler than I am :sunglasses:"
            return emb, True
        case 877550294785986571:
            emb.description = f"[0%] Nah we ain't talking about this fetus."
            return emb, True
        case 703959508489207838:
            emb.description = f"[100%] It's Arinone. Who could hate such a cute jolteon ?~ Aight ok I'll stop acting corny. Or not :upside_down:"
            return emb, True
        case 1221056132504621152:
            emb.description = f"[15%] It's Pandoro, the funny italian guy ! I gave him a 15% because he forgot to put pineapple & chicken on my pizza :face_with_symbols_over_mouth:"
            return emb, True
        case 812837395493027921:
            emb.description = f"[100%] Forob cool. Forob nimble. Forob quick. :fire:"
            return emb, True
        case 1080187557498851478:
            emb.description = f"[100%] Funny wheel guy. I like your vids. Also don't worry about the haters, they're as unintelligent as Jeepsy."
            return emb, True
        case _:
            emb.description = coolness_rd(user)
            return emb, True