from collections import defaultdict

def read_input(filename):
    right_list = defaultdict(int)
    left_list = []
    with open(filename, 'r') as file:
        for line in file:
            nums = line.strip().split()
            if len(nums) == 2:
                left_list.append(int(nums[0]))
                right_list[int(nums[1])] += 1
    
    return left_list, right_list

input = read_input('day1_input.txt')

def solution(input):
    left, right = input
    similar_score = 0
    for i in range(len(left)):
        similar_score += (left[i] * right[left[i]])
    return similar_score

if __name__ == "__main__":
    print(solution(input))
