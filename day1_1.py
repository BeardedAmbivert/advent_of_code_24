
def read_input(filename):
    list1 = []
    list2 = []
    with open(filename, 'r') as file:
        for line in file:
            nums = line.strip().split()
            if len(nums) == 2:
                list1.append(int(nums[0]))
                list2.append(int(nums[1]))
    
    return [sorted(list1), sorted(list2)]

input = read_input('day1_input.txt')


def solution(input):
    total = 0
    for j in range(len(input[0])):
        total += abs(input[0][j] - input[1][j])
    return total

if __name__ == "__main__":
    print(solution(input))
