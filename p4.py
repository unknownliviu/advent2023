import pdb
def read_txt(file_name):
    with open(file_name, 'r') as f:
        for x in f.readlines():
            yield x.replace("\n", '')



def solve1(path):
    def parse_line(line):
        cleaned = line.split(":")[1]
        winners, ours = [[int(x) for x in group.strip().split(" ") if x] for group in cleaned.split("|")]
        counter = 0
        for winner in winners:
            if winner in ours:
                counter+=1
        if counter == 0:
            return 0
        return 2 ** (counter -1)        
    sum = 0
    for line in read_txt(path):
        sum += parse_line(line)
    return sum

def solve2(path):
    def parse_line(line):
        cleaned = line.split(":")[1]
        winners, ours = [[int(x) for x in group.strip().split(" ") if x] for group in cleaned.split("|")]
        counter = 0
        for winner in winners:
            if winner in ours:
                counter+=1
        return counter
    line_values = [parse_line(line) for line in read_txt(path)]
    print(line_values)

    def process_line(idx):
        counter = 1
        for y in range(idx+1, idx + line_values[idx] + 1):
            counter+= process_line(y)

        return counter
    sum =0
    for idx, _ in enumerate(line_values):
        sum += process_line(idx)
    return sum

    # (idx+1, idx + x + 1)

print(solve2("inputs/p4.txt"))