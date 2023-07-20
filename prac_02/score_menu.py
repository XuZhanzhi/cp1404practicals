MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Enter score: "))
            while score < 0 or score > 100:
                print("Invalid score")
                score = int(input("Enter score: "))
        elif choice == "P":
            print(get_score_status(score))
        elif choice == "S":
            for i in range(score):
                print("*", end="")
            print()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Bye,thank you.")


def get_score_status(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
