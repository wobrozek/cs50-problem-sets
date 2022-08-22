from validator_collection import validators

def validate_email(emial):
    try:
        email = validators.email(emial)
        return "Valid"
    except ValueError:
        return "Invalid"

def main():
    ...

if __name__=="__main__":
    ...