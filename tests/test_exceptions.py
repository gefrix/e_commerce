from src.exceptions import ZeroProductQuantityError, ZeroQuantityError


def test_zero_quantity_error_is_value_error_with_required_message() -> None:
    error = ZeroQuantityError()

    assert isinstance(error, ValueError)
    assert str(error) == "Товар с нулевым количеством не может быть добавлен"
    assert ZeroProductQuantityError is ZeroQuantityError
