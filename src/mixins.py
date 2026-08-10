from __future__ import annotations


class CreationInfoMixin:
    """Print the concrete class and constructor arguments for each new object."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        self.__creation_args = args
        self.__creation_kwargs = kwargs
        super().__init__()
        print(repr(self))

    def __repr__(self) -> str:
        positional = [repr(argument) for argument in self.__creation_args]
        named = [f"{name}={value!r}" for name, value in self.__creation_kwargs.items()]
        parameters = ", ".join([*positional, *named])
        return f"{type(self).__name__}({parameters})"


MixinLog = CreationInfoMixin
