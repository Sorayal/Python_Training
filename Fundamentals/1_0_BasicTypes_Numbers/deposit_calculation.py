def calculate():
    deposit = int(input())
    years = 0
    while deposit <= 700000:
        deposit *= 1.071
        years += 1
    print(years)


def main():
    calculate()


if __name__ == "__main__":
    main()


