from .exec_handler import Execute


class Get(Execute):
    """
    Get will handle package install/configure operations.

    Args:
        Execute ([class]): Inheritance from the Execute class.
    """

    def __init__(self) -> None:
        super().__init__()

    def apt_repo(self, repo_name: str) -> int:
        """
        apt_repo will add repositories.

        Args:
            repo_name (str): Name of the repository.

        Returns:
            int: Result code. 0 -> success.
        """

        return self.exec_command(
            f"sudo add-apt-repository -y {repo_name}", hide_output=True
        ).returncode

    def update_pkg(self) -> int:
        """
        update_pkg will update system packages.

        Returns:
            int: Result code. 0 -> success.
        """
        return self.exec_command(f"sudo apt -y update", hide_output=True).returncode

    def apt_pkg(self, pkg_name: str) -> int:
        """
        apt_pkg will install apt packages.

        Args:
            pkg_name (str): Name of the package.

        Returns:
            int: Result code. 0 -> success.
        """

        return self.exec_command(
            f"sudo apt -y install {pkg_name}", hide_output=True
        ).returncode

    def git_repo(self, repo_name: str, output_path: str) -> int:
        """
        git_repo will add git repositories.

        Args:
            repo_name (str): Name of the git repository.
            output_path (str): Path that reposiory should be cloned.

        Returns:
            int: Result code. 0 -> success.
        """

        return self.exec_command(
            f"git clone {repo_name} {output_path}", hide_output=False
        ).returncode

    def from_net(self, url: str, output_path: str) -> int:
        """
        from_net will download files from the internet.

        Args:
            url (str): Downlaod link.
            output_path (str): Path that downloaded file should be placed.

        Returns:
            int: Result code. 0 -> success.
        """

        return self.exec_command(
            f"wget -q --show-progress -O {output_path} {url}",
            hide_output=False,
        ).returncode

    def anything(self, instruction: str) -> int:
        """
        anything will do any given command task.

        Args:
            instruction (str): any linux instruction.

        Returns:
            int: Result code. 0 -> success.
        """

        return self.exec_command(f"{instruction}", hide_output=False).returncode
