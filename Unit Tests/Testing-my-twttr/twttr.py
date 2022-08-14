"""
implement a program that prompts the user for a str of text and then outputs that same 
text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""

def shorten(word):

    none_list={"A","E","I","O","U"}
    score=""

    for x in word:
        if x.upper() not in none_list:
            score+=x
    return score

def main():
    data=input("Input: ")
    print(shorten(data))

if __name__=="__main__":
    main()