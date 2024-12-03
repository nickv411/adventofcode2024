
def part1():
    total_safe = 0
    bad_list_count = 0

    # Open file
    with open("input", "r") as input_file:

        # Loop through and parse each line
        for line in input_file:

            str_list = line.split()
            int_list = []

            for item in str_list:
                int_list.append(int(item))

            # If list is not sorted or reverse sorted, continue to next list
            if int_list != sorted(int_list) and int_list != sorted(int_list, key=None, reverse=True):
                continue
            else:
                # Else, check level steps
                # Levels must increase or decrease by 1-3 between numbers
                bad_list_flag = False

                # Pop first item to check
                item1 = int_list.pop()
                while len(int_list) > 0:
                    # Pop second item to check
                    item2 = int_list.pop()

                    diff = abs(item1 - item2)

                    if diff < 1 or diff > 3:
                        bad_list_flag = True
                        break

                    # Set for next iteration
                    item1 = item2

                if bad_list_flag is False:
                    total_safe += 1

    print(f"Total safe: {total_safe}")


def part2():
    total_safe = 0
    total_check = 0

    # Open file
    with open("input", "r") as input_file:

        # Loop through and parse each line
        for line in input_file:

            str_list = line.split()
            int_list = []

            for item in str_list:
                int_list.append(int(item))

            # If list is not sorted or reverse sorted, check for problem dampener
            if int_list != sorted(int_list) and int_list != sorted(int_list, key=None, reverse=True):
                # Need to see if removing one item from the list allows it to be sorted
                print("Check bad")

                for item in int_list:
                    new_list = int_list[:]
                    new_list.remove(item)

                    if sorted(new_list) == new_list or sorted(new_list, key=None, reverse=True) == new_list:
                        print_list = new_list[:]
                        is_safe = check_list_for_diff(new_list)
                        print(f"Checking rejected new list: {print_list} - found {is_safe}")
                        total_safe += is_safe
                        break
                    else:
                        pass

            else:
                total_check += 1
                # Else, check level steps
                # Levels must increase or decrease by 1-3 between numbers
                total_safe += check_list_for_diff(int_list)

    print(f"Total safe: {total_safe}")
    print(f"Total check: {total_check}")


def check_list_for_diff(int_list):
    bad_list_flag = False
    bad_level_flag = False

    # Pop first item to check
    item1 = int_list.pop()
    while len(int_list) > 0:
        # Pop second item to check
        item2 = int_list.pop()

        diff = abs(item1 - item2)

        if diff < 1 or diff > 3:
            if bad_level_flag:
                bad_list_flag = True
                break
            else:
                bad_level_flag = True

        # Set for next iteration
        item1 = item2

    if bad_list_flag is False:
        return 1
    else:
        return 0


def main():
    part1()

    part2()


if __name__ == "__main__":
    main()
