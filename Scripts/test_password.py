from test_working_pytest import is_valid_password


def test_negative():
    my_password = "lkdjsflkjhs"

    assert is_valid_password(my_password)