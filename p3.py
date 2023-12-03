import pdb
def read_txt(file_name):
    with open(file_name, 'r') as f:
        for x in f.readlines():
            yield x.replace("\n", '')

def solve1(path):
    matrix = []
    for line in read_txt(path):
        matrix.append(line)

    def has_symbol_neighbor(row, col, matrix):
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if i==0 and j==0:
                    continue
                if row+i < 0 or row+i >= len(matrix[0]):
                    continue
                if col+j < 0 or col+j >= len(matrix):
                    continue
                neighbor = matrix[row+i][col+j]
                if not neighbor.isnumeric() and neighbor != '.':
                    return True
        return False
    sum = 0       
    for idx, line in enumerate(matrix):
        current_number = ""
        has_neighbors = False
        for jdx, char in enumerate(line):
            if char.isnumeric():
                current_number = f"{current_number}{char}"
                if has_symbol_neighbor(idx, jdx, matrix):
                    has_neighbors = True
            else:
                if has_neighbors:
                    sum += int(current_number)
                current_number = ""
                has_neighbors = False
        if has_neighbors:
            sum += int(current_number)
        current_number = ""
        has_neighbors = False
    return sum


# print(solve1('inputs/p3_1.txt'))

def solve2(path):
    matrix = []
    for line in read_txt(path):
        matrix.append(line)

    def star_neighbors(row, col, matrix):
        stars = []
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if i==0 and j==0:
                    continue
                if row+i < 0 or row+i >= len(matrix[0]):
                    continue
                if col+j < 0 or col+j >= len(matrix):
                    continue
                neighbor = matrix[row+i][col+j]
                if neighbor == '*':
                    stars.append(f"{row+i}_{col+j}")
        return stars
    star_map = dict()
    for idx, line in enumerate(matrix):
        current_number = ""
        adjacent_stars = []
        for jdx, char in enumerate(line):
            if char.isnumeric():
                if current_number == '':
                    current_number = f"{idx}_{jdx}#"
                current_number = f"{current_number}{char}"
                stars = star_neighbors(idx,jdx,matrix)
                adjacent_stars += stars
            else:
                for star in adjacent_stars:
                    star_map[star] = star_map.get(star,[]) + [current_number]
                current_number = ""
                adjacent_stars = []
        for star in adjacent_stars:
            star_map[star] = star_map.get(star,[]) + [current_number]
        current_number = ""
        adjacent_stars = []
    for k, val in star_map.items():
        star_map[k] = list(set(val))
    sum = 0
    for star, points in star_map.items():
        if len(points) == 2:
            points = [int(x.split('#')[-1]) for x in points]
            sum += points[0] * points[1]
    return sum


print(solve2('inputs/p3_1.txt'))
            
                    