import re

def validate_pincode(pincode):
    return len(pincode) == 6

def validate_agelimit(agelimit):
    return age_limit in [18, 45]

def validate_email(email):
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
    return EMAIL_REGEX.match(email)