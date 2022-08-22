import re
"""
Count the um word but not inside other word like albUM
"""
def count(sentence):
    score=re.findall(r"(\W|^)um\W",sentence,flags=re.IGNORECASE)
    return len(score)


def main():
    ...

if __name__=="__main__":
    ...