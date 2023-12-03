import pdb
def read_txt(file_name):
    with open(file_name, 'r') as f:
        for x in f.readlines():
            yield x


def solve1(path):
    def parse_line(line):
        game_id = line.split(" ")[1][:-1]
        minigames = " ".join(line.split(" ")[2:]).split(';')
        limits = dict(red=12,green=13,blue=14)
        for minigame in minigames:
            color_counter = dict(red=0,green=0,blue=0)
            minigame = minigame.strip()
            for group in minigame.split(","):
                for color in color_counter.keys():
                    if color in group:
                        color_counter[color] += int(group.replace(color, ''))
                        if color_counter[color] > limits[color]:
                            return 0
        return int(game_id)
    sum = 0
    for line in read_txt(path):
        sum += parse_line(line)
    return sum

# print(solve1("inputs/p2_1.txt"))

def solve2(path):
    def parse_line(line):
        minigames = " ".join(line.split(" ")[2:]).split(';')
        max_counter = dict(red=0,green=0,blue=0)
        for minigame in minigames:
            color_counter = dict(red=0,green=0,blue=0)
            minigame = minigame.strip()
            for group in minigame.split(","):
                for color in color_counter.keys():
                    if color in group:
                        color_counter[color] += int(group.replace(color, ''))
                        if color_counter[color] > max_counter[color]:
                            max_counter[color] = color_counter[color]
            
        return max_counter['red'] * max_counter['green'] * max_counter['blue']
    sum = 0
    for line in read_txt(path):
        sum += parse_line(line)
    return sum

print(solve2("inputs/p2_1.txt"))
