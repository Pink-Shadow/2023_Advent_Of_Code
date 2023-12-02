class Game():
    def __init__(self, ID = -1):
        self.ID: int = ID
        self.red = []
        self.green = []
        self.blue = []

    def update_count(self, count: int, colour: str):
        if colour == "red":
            self.red.append(count)
        elif colour == "green":
            self.green.append(count)
        elif colour == "blue":
            self.blue.append(count)

    def is_valid(self, limit_red, limit_green, limit_blue):
        if max(self.red) <= limit_red and max(self.green) <= limit_green and max(self.blue) <= limit_blue:
            return True
        return False

    def return_product_of_minimum(self):
        return (max(self.red) * max(self.green) * max(self.blue))

    def get_id(self):
        return self.ID

    def __repr__(self):
        return f"id: {self.ID} - red: {self.red} - green: {self.green} - blue: {self.blue}"


def generate_class_from_line(line):
    stripped = line.strip()
    splitted = stripped.split(": ")  # ["game x", "green red blue.."]
    gameid = splitted[0].split(" ")[1]  # ["game", "3"]
    grabs = splitted[1].split("; ")  # ["x green x blue x red", ...]
    tmp = Game(int(gameid))
    for set in grabs:
        colour = set.split(", ")  # ['3 blue', ...]
        for col in colour:
            a = col.split(" ")  # ['3', 'blue']
            tmp.update_count(int(a[0]), a[1])
    return tmp

if __name__ == "__main__":
    valids = []
    products = []
    with open("puzzle_input.txt", "r") as infile:
        content = infile.readlines()
        for line in content:
            game = generate_class_from_line(line)
            if game.is_valid(12, 13, 14):
                valids.append(game)
            products.append(game.return_product_of_minimum())

    answer1 = sum([game.get_id() for game in valids])
    answer2 = sum(products)
    print(f"Answer star 1:\t{answer1}\nAnswer star 2:\t{answer2}")

