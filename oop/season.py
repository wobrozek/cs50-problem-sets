from datetime import datetime
import inflect

"""
implement a program that prompts the user for their date of birth in YYYY-MM-DD format 
and then prints how old they are in minutes, rounded to the nearest integer
,using English words instead of numerals, just like the song from Rent 
"""

def number_of_minuts(data):
    try:
        data=datetime.strptime(data,"%d-%m-%Y")
    except ValueError:
        raise ValueError("Invalid date format")
    now=datetime.today()
    now=now.replace(hour=0,second=0,minute=0)
    minuts = now-data
    return round(minuts.total_seconds()/60)


def main():
    while True:
        try:
            data=input("write your birth date in format DD-MM-YYYY")
            minuts=number_of_minuts(data)
            print(f"{inflect.engine().number_to_words(minuts)} minutes")
            break
        except ValueError:
            print("Invalid date")
            pass

if __name__=="__main__":
    main()