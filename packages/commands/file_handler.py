from .exec_handler import Execute


class File(Execute):
    """
    File will handle basic file operations.

    Args:
        Execute ([class]): Inheritance from the Execute class.
    """

    def __init__(self) -> None:
        super().__init__()

    def make_dir(self, path: str) -> int:
        """
        make_dir will create directories.

        Args:
            path (str): path that directory should be created.

        Returns:
            int: Result code. 0 -> success.
        """

        return self.exec_command(f"mkdir -p {path}", hide_output=False).returncode

    def make_doc(self, path: str) -> int:
        """
        make_doc will create documents.

        Args:
            path (str): path that document should be created.

        Returns:
            int: Result code. 0 -> success.
        """

        return self.exec_command(f"touch {path}", hide_output=False).returncode

    def go_to(self, path: str) -> int:
        """
        go_to will change directories.

        Args:
            path (str): destination.

        Returns:
            int: Result code. 0 -> success.
        """

        return self.exec_command(f"cd {path}", hide_output=False).returncode

    def copy(self, source: str, dest: str) -> int:
        """
        copy will copy and paste files.

        Args:
            source (str): File to be copied.p
            dest (str): Path that output file should be placed.

        Returns:
            int: Result code. 0 -> success.
        """

        return self.exec_command(f"cp -r {source} {dest}", hide_output=False).returncode
