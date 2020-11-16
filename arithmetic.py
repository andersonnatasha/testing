def adder(x, y):
    """Adds two numbers together.

    x: an integer
    y: an integer
    returns: an integer of their sum

    Does some very difficult mathematical things.

        >>> adder(1, 1)
        2

    Well, that seems easy. But how about this?

        >>> adder(-1, 1)
        0
    """

    return x + y


def things_from_db():
    """Get list of things from a database."""

    # (well, we're obviously faking the DB here :) )
    return ["Python", "Javascript", "Kittens"]
