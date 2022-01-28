"""
    * @import run from module subprocess
    * @import chdir from module os
"""

from subprocess import run  # run() -> run given linux system commands
from os import chdir  # chdir() -> change directories
from sys import exit  # exit() -> exit the program


class Command:

    """
        * performs commands based on given inputs.
    """

    def __init__(self) -> None:
        """
            * declaring method __init__()

            * @param self

            * @return None
        """

        pass

    def apt(self, attr: str = "",  command: str = "", package_name: str = "") -> int:
        """
            * declaring method apt()
                - run apt command with given arguments

            * @param self
            * @param attr         -> attributes of the apt command
            * @param command      -> any apt command
            * @param package_name -> name of the application needs to be installed

            * @return int
        """

        try:

            result = run(f"sudo apt {attr} {command} {package_name}",
                         shell=True, capture_output=True, text=True)

            return result.returncode  # success = 0

        except:

            return 1  # failure

    def copy(self, attr: str = "",  source: str = "", dest: str = "") -> int:
        """
            * declaring method copy()
                - run cp command with given arguments

            * @param self
            * @param attr   -> attributes of the apt command
            * @param source -> source of the file to be copied
            * @param dest   -> final destination

            * @return int
        """

        try:

            result = run(f"cp {attr} {source} {dest}",
                         shell=True, capture_output=True, text=True)

            return result.returncode  # success = 0

        except:

            return 1  # failure

    def add_repo(self, attr: str = "", repo_name: str = "") -> int:
        """
            * declaring method add_repo()
                - add given repository to system

            * @param self
            * @param attr      -> attributes of the apt-add-repository command
            * @param repo_name -> repository name

            * @return int
        """

        try:

            result = run(f"sudo add-apt-repository {attr} {repo_name}",
                         shell=True, capture_output=True, text=True)

            return result.returncode  # success = 0

        except:

            return 1  # failure

    def cd(self, path: str = "") -> int:
        """
            * declaring method cd()
                - change directory

            * @param self
            * @param path -> directory path

            * @return int
        """

        try:

            result = run(f"cd {path}",
                         shell=True, capture_output=True, text=True)

            return result.returncode  # success = 0

        except:

            return 1  # failure

    def git_c(self, repo_name: str = "", output_name: str = "") -> int:
        """
            * declaring method git_clone()
                - clone any repository from github

            * @param self
            * @param repo_name   -> name of the repository
            * @param output_name -> output file name

            * @return int
        """

        try:

            result = run(f"git clone {repo_name} {output_name}",
                         shell=True, capture_output=True, text=True)

            return result.returncode  # success = 0

        except:

            return 1  # failure

    def find_apt(self, package_name) -> int:
        """
            * declaring method find_apt()
                - search given package in system

            * @param self
            * @param package_name -> name of the application needs to be searched

            * @return int
        """

        try:

            result = run(f"apt list {package_name}",
                         shell=True, capture_output=True, text=True)

            if ("INSTALLED" in result.stdout.upper()):

                return 0  # installed

            else:

                return 1  # not installed

        except:

            return 1  # failure

    def find_repo(self, repo_name) -> int:
        """
            * declaring method find_repo()
                - search given repository in the repo list.

            * @param self
            * @param repo_name -> name of the repository

            * @return int
        """

        # path of the file repository list needs to be written into
        path = f"repository_list.txt"
        # command to get repository list
        cmd = f"apt-cache policy"
        # removes the recently created file
        rm = f"sudo rm -rf"

        # creates a text file that contains installed repository list
        state = self.other(f"{cmd} > {path}")

        if (state == 0):

            try:

                with open(f"{path}", "r") as f:

                    repo_list = f.readlines()

                for item in repo_list:

                    rp = item.find(f"{repo_name}")

                    if (rp != -1):

                        # remove repository-list.txt
                        self.other(f"{rm} {path}")

                        return 0  # found

                # remove repository-list.txt
                self.other(f"{rm} {path}")

                return 1  # not found

            except:

                print(f"\nAn internal error occurred while reading {path}")

                exit()  # exits the program

        else:

            print(f"\nAn internal error occurred while creating {path}")

            exit()  # exits the program

    def other(self, command) -> int:
        """
            * declaring method other()
                - run any shell command

            * @param self
            * @param command -> shell command

            * @return int
        """

        try:

            result = run(f"{command}", shell=True,
                         capture_output=True, text=True)

            return result.returncode  # success = 0

        except:

            return 1  # failure
