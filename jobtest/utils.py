from django.core.validators import ValidationError
import datetime

# takes in a string, returns True if valid, else False


def present_or_future_date(value):
    if value < datetime.date.today():
        raise ValidationError('The date cannot be in the past!')
    return value


def card_validator(card_number):
    groups = card_number.split("-")
    if len(groups) != 4:  # check if there's 4 groups of 4 digits
        return False

    for group in groups:  # check if there's 4 element in each group
        if len(group) != 4:
            return False

    for group in groups:  # check if elements are numbers
        if not group.isdigit():
            return False
    return True


if __name__ == '__main__':
    # group lenght checks
    assert card_validator(
        "1234-1234-1234-1234") == False, "this should be valid"
    assert card_validator("1234-1234-1234") == False
    assert card_validator("1234-1234-1234-1234-1234") == False
    # inside group length checks
    assert card_validator("12345-1234-1234-1234") == False
    assert card_validator("1234-1234-1234-12345") == False
    # check special chars
    assert card_validator("%$#@-1234-1234-1234") == False
    assert card_validator("1234-1234-1234-*$&@") == False
    # check letters
    assert card_validator("abcd-1234-1234-0000") == False
    assert card_validator("1234-1234-1234-abcd") == False
    print('worked')
