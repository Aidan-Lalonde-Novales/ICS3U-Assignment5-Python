#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created May 2022
# This program shows the factors of an inputed number.


def main():
    # this function finds and returns factors

    # input
    user_number_string = input("Enter a positive integer to see it’s factors: ")

    # process & output
    try:

        user_number = int(user_number_string)

        if user_number > 0:
            for counter in range(1, user_number + 1):
                if user_number % counter == 0:
                    print(counter)
                else:
                    continue
        else:
            print("\nPlease ensure that your integer is positive.")

    except Exception:
        print("\nThat integer is invalid.")

    print("\nDone.")


if __name__ == "__main__":
    main()
