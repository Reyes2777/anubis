from email_validator import validate_email, EmailNotValidError


def validity_mail(email):
    try:
        response = validate_email(email)
        return True
    except EmailNotValidError as e:
        print(str(e))
