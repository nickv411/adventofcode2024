
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
    :return: Similarity Score
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

        # Utilize the Counter object to get a count of items in the right list
        counter = Counter(right_list)

        # Iterate through the left list and add to the total similarity
        for num in left_list:
            if num in counter:
                # Similarity is number * occurrences
                total_similarity += counter[num] * num

    return total_similarity


def main():
    dist = part1()
    print(f"Total distance found to be {dist}")

    similar = part2()
    print(f"Total similarity found to be {similar}")


if __name__ == "__main__":
    main()
