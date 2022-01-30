from .src import Handler


def main() -> None:
    """
    main is the Main section of the app.
    """

    handle = Handler()
    handle.handler()


if __name__ == "__main__":

    main()
