#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on October 2019
# This program prints from 1000 to 2001 in only 5 outputs per line


def main():
    # This function prints from 1000 to 2001 in only 5 outputs per line
    for counter1 in range(1001, 2001):
        print(counter1-1, end=' ')
        if counter1 % 5 == 0:
            print("")


if __name__ == "__main__":
    main()
