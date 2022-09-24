class BasicMenu():
    """basic menu that can be used on Windows"""

    def __init__(self, choices):
        self.choices = choices

    def BuildMenu(self):
        num_item_pairs = []

        for num, choice in enumerate(self.choices):
            num_item_pairs.append((num+1, choice))

        for num, choice in num_item_pairs:
            print(f"{num}) {choice}")

        try:
            choice_input = int(input("What is your choice?: "))
        except ValueError:
            print("Integers only please :)")
            from sys import exit
            exit(1)

        for num, choice in num_item_pairs:
            if num == choice_input:
                return choice
        return "Wrong input"


#m = BasicMenu(["a", "b", "c"])
#menu = m.BuildMenu()
#print(menu)



