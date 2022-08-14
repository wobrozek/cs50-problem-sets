"""
In a file called bank.py, implement a program that prompts the user for a greeting.
If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”),
output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting,
and treat the user’s greeting case-insensitively.
"""

def bank(word):
    word=word.lower().strip()

    if word == "hello":
        return 100
    if word[0]== 'h':
        return 20
    return 0

def main():
    data=input("Input: ")
    print(f"{bank(data)}$")

if __name__=="__main__":
    main()