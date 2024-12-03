

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

            print(f"Found num1 {num1} and num2 {num2}")

            total += (int(num1) * int(num2))

    print(f"Total is {total}")


def is_num_str(in_char):
    num_strs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if in_char in num_strs:
        return True
    else:
        return False


def main():
    part1()


if __name__ == "__main__":
    main()
