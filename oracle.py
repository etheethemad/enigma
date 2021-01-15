import util

def ask(mod=0):
    roll = util.roll(1,100)[0] + mod

    if roll < 15:
        return "Yes, and..."
    elif roll < 35:
        return "Yes."
    elif roll < 50:
        return "Yes, but..."
    elif roll < 65:
        return "No, but..."
    elif roll < 85:
        return "No."
    else:
        return "No, and..."
