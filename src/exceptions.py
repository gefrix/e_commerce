class ZeroQuantityError(ValueError):
    """Report an attempt to add a product with zero quantity."""

    default_message = "Товар с нулевым количеством не может быть добавлен"

    def __init__(self, message: str = default_message) -> None:
        super().__init__(message)


ZeroProductQuantityError = ZeroQuantityError
