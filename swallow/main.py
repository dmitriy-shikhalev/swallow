import atexit


def bootstrap():
    """
    Startup initialization function.
    """
    raise NotImplementedError


def main():
    """
    Main process.
    """
    raise NotImplementedError


def shutdown():
    """
    Final everything at the end of process.
    """
    raise NotImplementedError


bootstrap()
atexit.register(shutdown())

main()
