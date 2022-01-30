from .exec_handler import Execute


class Find(Execute):
    """
    Find the existance of a package or a repository within the system.

    Args:
        Execute ([type]): Inheriance from the Execute class.
    """

    def __init__(self) -> None:
        super().__init__()

    def apt_pkg(self, pkg_name: str) -> int:
        """
        apt_pkg will find the existance of a package.

        Args:
            pkg_name (str): Name of the package.

        Returns:
            int: 0 -> package exists.
        """

        result_1 = self.exec_command(f"which {pkg_name}", hide_output=True)
        result_2 = self.exec_command(f"apt list {pkg_name}", hide_output=True)

        is_installed = (
            result_2.stdout.find("installed") != -1
        )  # Returns True if pkg is installed.
        is_path_exists = (
            result_1.stdout != ""
        )  # "" -> Returns True if pkg path is available.

        return (
            0
            if (
                (is_path_exists == True or is_installed == True)
                and result_2.returncode == 0
            )
            else 1
        )

    def apt_repo(self, repo_url: str) -> int:
        """
        apt_repo will find the existance of a repository.

        Args:
            repo_url (str): Repository URL.

        Returns:
            int: 0 -> Repository exists.
        """

        result = self.exec_command(f"apt-cache policy", hide_output=True)

        return (
            0 if (result.stdout.find(repo_url) != -1 and result.returncode == 0) else 1
        )
