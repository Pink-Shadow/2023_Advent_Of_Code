from dataclasses import dataclass



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
        print(max(self.red) , max(self.green) , max(self.blue))
        return (max(self.red) * max(self.green) * max(self.blue))

    def get_id(self):
        return self.ID

    def __repr__(self):
        return f"id: {self.ID} - red: {self.red} - green: {self.green} - blue: {self.blue}"




if __name__ == "__main__":
    solution = 1
    valids = []
    with open("puzzle_input.txt", "r") as infile:
        content = infile.readlines()
        if solution==1:
            for line in content:
                stripped = line.strip()
                splitted = stripped.split(": ") # ["game x", "green red blue.."]
                gameid = splitted[0].split(" ")[1] # ["game", "3"]
                grabs = splitted[1].split("; ") # ["x green x blue x red", ...]
                tmp = Game(int(gameid))
                for set in grabs:
                    colour = set.split(", ") # ['3 blue', ...]
                    for col in colour:
                        a = col.split(" ") # ['3', 'blue']
                        tmp.update_count(int(a[0]), a[1])

                if tmp.is_valid(12, 13, 14):
                    valids.append(tmp)
            print(sum([game.get_id() for game in valids]))
        else:
            products = []
            for line in content:
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


                products.append(tmp.return_product_of_minimum())
            print(products)
            print(sum(products))

