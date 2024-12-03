

def part1():
    total = 0

    with open("input", "r") as input_file:
        curr_char = input_file.read(1)

        while curr_char != '':
            if curr_char != 'm':
                curr_char = input_file.read(1)
                continue

            curr_char = input_file.read(1)
            if curr_char != "u":
                continue

            curr_char = input_file.read(1)
            if curr_char != "l":
                continue

            curr_char = input_file.read(1)
            if curr_char != "(":
                continue

            num1 = ""

            curr_char = input_file.read(1)

            while is_num_str(curr_char):
                num1 += curr_char
                curr_char = input_file.read(1)

            # Check if comma
            if curr_char != ',':
                continue

            num2 = ""

            curr_char = input_file.read(1)

            while is_num_str(curr_char):
                num2 += curr_char
                curr_char = input_file.read(1)

            # Check for )
            if curr_char != ")":
                continue


            total += (int(num1) * int(num2))

    print(f"Part 1 total is {total}")


def part2():
    total = 0
    do_flag = True

    with open("input", "r") as input_file:
        curr_char = input_file.read(1)

        while curr_char != '':
            if curr_char != 'm' and curr_char != 'd':
                curr_char = input_file.read(1)
                continue

            # Start do/dont checks
            if curr_char == 'd':
                curr_char = input_file.read(1)
                if curr_char != 'o':
                    continue

                # need to check both n and (
                curr_char = input_file.read(1)
                if curr_char != 'n' and curr_char != '(':
                    continue

                # if do, finish checking for parentheses
                if curr_char == '(':
                    curr_char = input_file.read(1)
                    if curr_char == ')':
                        do_flag = True
                        curr_char = input_file.read(1)
                    continue

                # if don't, finish checking for 'n't()'
                if curr_char == 'n':
                    curr_char = input_file.read(1)
                    if curr_char != '\'':
                        continue

                    curr_char = input_file.read(1)
                    if curr_char != 't':
                        continue

                    curr_char = input_file.read(1)
                    if curr_char != '(':
                        continue

                    curr_char = input_file.read(1)
                    if curr_char == ')':
                        do_flag = False
                        curr_char = input_file.read(1)

                    continue

            # Start mul checks
            curr_char = input_file.read(1)
            if curr_char != "u":
                continue

            curr_char = input_file.read(1)
            if curr_char != "l":
                continue

            curr_char = input_file.read(1)
            if curr_char != "(":
                continue

            num1 = ""

            curr_char = input_file.read(1)

            while is_num_str(curr_char):
                num1 += curr_char
                curr_char = input_file.read(1)

            # Check if comma
            if curr_char != ',':
                continue

            num2 = ""

            curr_char = input_file.read(1)

            while is_num_str(curr_char):
                num2 += curr_char
                curr_char = input_file.read(1)

            # Check for )
            if curr_char != ")":
                continue

            if do_flag:
                total += (int(num1) * int(num2))

    print(f"Part 2 Total is {total}")


def do_check(input_file):
    """
    returns 0 on bad check
    returns 1 on do
    returns -1 on don't
    """


def is_num_str(in_char):
    num_strs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if in_char in num_strs:
        return True
    else:
        return False



def main():
    part1()

    part2()


if __name__ == "__main__":
    main()
