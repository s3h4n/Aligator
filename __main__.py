"""
    * @import module Handler from src/handler.py
"""

from .src import Handler


def __main__() -> None:
    """
        * declaring public function __main__().
            - the program will run from here

        * @param None

        * @return None  
    """
    h = Handler()

    h.handler()


if __name__ == '__main__':
    """
        * if __name__ == '__main__' -> run __main__().
    """
    __main__()
