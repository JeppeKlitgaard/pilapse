"""Defines the exceptions used by Pilapse."""


class ParameterException(Exception):
    """Raised when an invalid combination of CLI parameters is found."""


class ParameterWarning(Warning):
    """Raised when an ill-advised combination of CLI parameters is found."""
