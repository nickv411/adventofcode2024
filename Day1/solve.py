
from collections import Counter

def part1():
    """
    Challenge requires sorting lists of numbers and then summing the distances between
    items in the sorted lists
    :return: Returns the solved distance
    """
    # Set total distance to zero
    total_distance = 0

    # Open the file
    with open("input", 'r') as input_file:

        # Since the list need to be sorted, create them to pull from the input file
        left_list = []
        right_list = []

        # Loop through lines and add to lists
        for line in input_file:
            # Pull the numbers out of the lines
            # Input is "#####  #####"
            num1 = int(line[0:5])
            num2 = int(line[6:13])

            left_list.append(num1)
            right_list.append(num2)

        # Sort the lists
        left_list.sort()
        right_list.sort()

        # Loop through the lists and find differences, add to total_distance
        for i in range(0, len(left_list)):
            left_num = left_list[i]
            right_num = right_list[i]

            diff = left_num - right_num

            # if negative, flip sign
            if diff < 0:
                diff *= -1

            # Add to total distance
            total_distance += diff

    return total_distance

def part2():
    """
    Need to determine similarity scores
    :return:
    """
    # Set total to 0
    total_similarity = 0

    # Open file for reading
    with open("input", "r") as input_file:
        # Create lists of numbers
        left_list = []
        right_list = []

        # Create dict of the same numbers, which is incremented when the number is found in the right list
        left_dict = {}

        # Loop through lines and add to lists
        for line in input_file:
            # Pull the numbers out of the lines
            # Input is "#####  #####"
            num1 = int(line[0:5])
            num2 = int(line[6:13])

            left_list.append(num1)
            right_list.append(num2)

            left_dict[num1] = 0

        temp_diff = 0
        for num in left_list:
            if num in right_list:
                temp_diff += 1

        print(f"Temp diff = {temp_diff}")

        # Now that the lists are complete at the dict is ready, loop through the right list
        # and add 1 to every entry in the left_dict for that number
        for num in right_list:
            if num in left_dict:
                left_dict[num] += 1

        # Now that the dict is set up, do one more loop, this time through the left list
        # to add to the similarity score for each item in the left list that has a dict value that is non zero
        for i in range(0, len(left_list)):
            if left_list[i] in left_dict:
                total_similarity += left_dict[left_list[i]]
                if left_dict[left_list[i]] != 0:
                    print(f"Found number {left_list[i]}, with value {left_dict[left_list[i]]}. New total: {total_similarity}")
                    print(f"Number {left_list[i]} is in the left_list {left_list.count(left_list[i])} times")

    return total_similarity


def main():
    dist = part1()
    print(f"Total distance found to be {dist}")

    similar = part2()
    print(f"Total similarity found to be {similar}")


if __name__ == "__main__":
    main()
