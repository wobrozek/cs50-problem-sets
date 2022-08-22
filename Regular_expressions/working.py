import re
"""
convert working hours from 12-hours clock to 24-hour clock
np 9 AM to 5 PM   to   09:00 to 17:00
"""
def convert(hours):
    if match:=re.search(r"^([1][0-2]|0?[0-9]):?([0-5]?[0-9])?\s(PM|AM) to ([1][0-2]|0?[0-9]):?([0-5]?[0-9])?\s(PM|AM)$",hours,flags=re.IGNORECASE):
        strScore=""
        strScore += hours_american_to_europe(match.group(1), match.group(2), match.group(3))
        strScore +=" to "
        strScore += hours_american_to_europe(match.group(4), match.group(5), match.group(6))
        return strScore
    return ValueError


# function that returns "22:30" for (10,30,PM)
def hours_american_to_europe(hours,minutes,type):
    score=""
# remember that 12 pm- 12:00 and 12am- 00:00
    if type=="PM":
        if hours == "12":
            return "12"
        hours=str(int(hours)+12)
    else:
        if hours =="12":
            return "00"
        if(int(hours) < 10):
            hours=f"0{hours}"

    score+= hours

    if minutes ==None:
        minutes="00"

    if (int(minutes) < 10 and minutes!="00"):
        minutes = f"0{minutes}"

    score+=f":{minutes}"

    return score


def main():
    ...

if __name__=="__main__":
    main()
