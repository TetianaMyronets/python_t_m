# import pytest
#
# @pytest.mark.smoke
#
# def test_addition():
#     wrong_number = '12683476238'
#     print("Hello!")
#     assert '+' not in wrong_number
#
# @pytest.mark.xfail
# def test_without_my_key_word():
#     assert 1 is True

def is_valid_password(password: str) -> bool:
    """
    Validates the password string based on security requirements.
    Requirements:
    - Must be a string
    - Length between 8 and 128 characters
    :param password: Should be string
    :return
    """

    if not isinstance(password, str):
        return  False

    if not (8 <= len(password) <= 128):
        return False

    special_characters = set('!@#$%^&*()_-+=?<>')

    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in special_characters for c in password)

    return all([has_upper, has_special, has_digit])
