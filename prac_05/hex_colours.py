COLOUR_CODE = {"AbsoluteZero": "#0048ba", "AcidGreen": "#b0bf1a", "AliceBlue": "#f0f8ff",
               "AlizarinCrimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00",
               "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7", "Apricot": "#fbceb1",
               "Aqua": "#00ffff"}

colour_name = input("Please enter a colour name: ")
while colour_name != "":
    if colour_name in COLOUR_CODE:
        print(colour_name, "is", COLOUR_CODE[colour_name])
    else:
        print("Invalid colour name.")
    colour_name = input("Please enter a colour name: ")
