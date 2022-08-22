from validator_collection import validators
"""
validate emial using either validator_collection or validators from PyPI
"""
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