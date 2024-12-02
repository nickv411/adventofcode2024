
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



def main():
    part1()


if __name__ == "__main__":
    main()
