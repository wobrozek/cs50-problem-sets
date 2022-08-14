"""
convert expects a str in X/Y format as input, wherein each of X and Y is an integer,
and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive.
If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError.
If Y is 0, then convert should raise a ZeroDivisionError.
gauge expects an int and returns a str that is:
"E" if that int is less than or equal to 1,
"F" if that int is greater than or equal to 99,
and "Z%" otherwise, wherein Z is that same int.
"""

def main():
    convert("3/4")


def convert(fraction):
    try:
        x,y=map(int,fraction.strip().split("/"))

        if y == 0:
            raise ZeroDivisionError

        if x > y :
            raise ValueError

    except ValueError:
        print("Podaj dane w formacie x/y gdze x<y")
        raise

    score=round(x/y,2)
    return score*100


def gauge(percentage):
    if percentage >100:
        raise ValueError
    if percentage >= 99:
        return "F"
    if percentage <= 1:
        return "E"

    return f"{percentage}%"


if __name__ == "__main__":
    main()