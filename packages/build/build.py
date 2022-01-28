"""
    * @import mkdir from module os
"""

from os import mkdir  # mkdir() -> make directories


class Build:

    """
        * creates documents and directories
    """

    def __init__(self) -> None:
        """
            * declaring method __init__()

            * @param self

            * @return None
        """

        pass

    def directory(self, path) -> int:
        """
            * declaring method directory()
                - creates a directory in given path

            * @param self
            * @param path -> directory name with or without path

            * @return int
        """

        try:

            mkdir(f"{path}", "666")  # 666 -> permissions

            return 0  # success

        except:

            return 1  # failure

    def document(self, path) -> int:
        """
            * declaring method document()
                - creates a document in given path

            * @param self
            * @param path -> document name with or without path

            * @return int
        """

        try:

            open(f"{path}", "w")

            return 0  # success

        except:

            return 1  # failure
