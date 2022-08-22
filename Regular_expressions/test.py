from ip_v4 import validate
from yt import parse
from working import convert, hours_american_to_europe
from um import count
from response import validate_email

def test_validate():
    assert validate("250.45.1.1") == True
    assert validate("4.145.207.1") == True

def test_validate_corect():
    assert validate("1.250.20.1") == True
    assert validate("1.255.20.1") == True

def test_validate_wrong():
    assert validate("270.144.52.1") == False
    assert validate("cat") == False
    assert validate("1.255.20") == False
    assert validate("1.255.20.1.1") == False

def test_parse():
    assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"

def test_parse_html():
    assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"

def test_parse_not_yt():
    assert parse('<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>') == None

def test_conver():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_cover_pm():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_cover_minuts():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_cover_range():
    assert convert("10:60 PM to 8:50 AM") == ValueError

def test_cover_without_to():
    assert convert("09:00 AM - 17:00 PM") == ValueError


def test_hours_american_to_europe():
    assert hours_american_to_europe("10","30","AM") == "10:30"
    assert hours_american_to_europe("5", "20", "PM") == "17:20"

def test_um():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("um?") == 1

def test_validate_Valid():
    assert validate_email("malan@harvard.edu") == "Valid"
    assert validate_email("wobrozek@gmail.com") == "Valid"

def test_validate_Invalid():
    assert validate_email("malan@@@harvard.edu") == "Invalid"
    assert validate_email("wobrozek@gmailcom") == "Invalid"

