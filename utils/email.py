import logging

from email_validator import validate_email, EmailNotValidError

logger = logging.getLogger('anubis')


def validity_mail(email):
    try:
        validate_email(email)
        return True
    except EmailNotValidError as e:
        logger.error(str(e))
