import re
'''
In a file called numb3rs.py, implement a function called validate that expects an IPv4 address
as input as a str and then returns True or False
,respectively, if that input is a valid IPv4 address or not.
'''
def validate(ip):
    if re.search(r"^((25[0-5]|2[0-4][0-9]|([0-1])?[0-9]([0-9])?)\.){3}(25[0-5]|2[0-4][0-9]|([0-1])?[0-9]([0-9])?)$",ip):
        return True
    return False
def main():
    ...
if __name__=="__main__":
    main()

