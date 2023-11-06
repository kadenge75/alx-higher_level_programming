#!/usr/bin/python3

"""Defines an empty class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""
    pass

0x0A-python-inheritance/6-base_geometry.py

#!/usr/bin/python3

"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")
