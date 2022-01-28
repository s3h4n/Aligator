"""
    * @import constants from src/constants.py
    * @import module Build from packages/build/build.py
    * @import module Command from packages/cmd/cmd.py
"""

from . import constants  # constant variables
from ..packages import Build  # build directories and documents
from ..packages import Command  # runs given shell commands


class Handler:

    """
        * Handles the whole program.
    """

    def __init__(self) -> None:
        """
            * declaring public function __init__()

            * @param self

            * @return None
        """

        self.cmd = Command()  # instance from Command class

        # color variables
        self.BOLD = constants.BOLD
        self.RED = constants.RED
        self.GREEN = constants.GREEN
        self.YELLOW = constants.YELLOW
        self.CYAN = constants.CYAN
        self.END = constants.END

    def handler(self) -> None:

        self.install_apt_pckgs()
        self.install_other_pckgs()

    def install_apt_pckgs(self) -> None:
        """
            * declaring method install_apt_pckgs()
                - install packages from apt repository

            * @param self

            * @return None
        """

        cmd = self.cmd

        b = self.BOLD
        r = self.RED
        g = self.GREEN
        y = self.YELLOW
        c = self.CYAN
        e = self.END

        tool_sets = []  # list to store tool sets
        tool_catagory = []  # list to store tool catagory

        # for loop -> store each set of tools in constants.APT_TOOLS
        for catagory in constants.APT_TOOLS:
            tool_catagory.append(catagory)
            tool_sets.append(constants.APT_TOOLS[catagory])

        def install(tool_set) -> None:
            """
            * declaring function install()
                - installs the packages one by one

            * @param tool_set -> set of packages that needs to be installed.

            * @return None
            """

            for item in tool_set:  # for loop -> for each package in package set

                if (cmd.find_apt(item) == 0):  # if package is pre-installed -> skip

                    print(f"\n{g}{item} has found.{e}\nSkipping...")

                else:  # else -> continue to install

                    print(f"\n{y}{item} has not found.{e}\nInstalling...")

                    # state = o -> success
                    state = cmd.apt(attr="-y",
                                    command="install",
                                    package_name=item)

                    print(f"{g}Done{e}" if (state == 0) else f"{r}Failed{e}")

        # for loop -> for each repository in the list
        for item in constants.REPOS:

            repo_name = constants.REPOS[item]

            # if repository already added -> skip
            if (cmd.find_repo(repo_name[1]) == 0):

                print(
                    f"\n{g}Repository {repo_name[1]} has found.{e}\nSkipping...")

            else:  # else -> continue to add it

                print(
                    f"\n{y}Repository {repo_name[1]} has not found.{e}\nAdding...")

                # state = 0 -> success
                state = cmd.add_repo(
                    attr="-y", repo_name=repo_name[0])

                print(f"{g}Done{e}" if (state == 0) else f"{r}Failed{e}")

        # update the system
        print("\nUpdating system...\n")

        # state = 0 -> success
        state = cmd.apt(attr="-y", command="update")

        print(f"\n{g}Done{e}" if (state == 0) else f"\n{r}Failed{e}")

        # display a list of softwares that's going to be installed.
        print(f"\nFollowing packages will be installed.")

        index = 0

        # for loop -> print catagory and and its own tool set
        for item in tool_sets:

            print(f"\n{b}# {tool_catagory[index]} Tools{e}\n")
            index += 1

            for i in item:

                print(f"{c+b}{i} {e}: {item[i]}")

        # asks user for the confirmation
        while True:

            opt = input(f"\n{b}Do you want to continue? y/Y or n/N :: {e}")

            if (opt.upper() == "Y"):  # if yes -> continue and exit

                # check and install every tool in the list
                for item in tool_sets:
                    install(item)

                break

            elif (opt.upper() == "N"):  # if no -> exit

                print(f"\n{b+r}Aborted.{e}")

                break

    def install_other_pckgs(self) -> None:
        """
            * declaring method install_other_pckgs()
                - install packages from other sources

            * @param self

            * @return None
        """

        cmd = self.cmd

        b = self.BOLD
        r = self.RED
        g = self.GREEN
        y = self.YELLOW
        c = self.CYAN
        e = self.END

        tools = []
        instructions = []

        for tool in constants.OTHER_TOOLS:
            tools.append(tool)
            instructions.append(constants.OTHER_TOOLS[tool])

        def install(tool, instructions_set):
            """
            * declaring function installer()
                - installs the packages one by one

            * @param tool             -> name of the tool 
            * @param instructions_set -> instructions of installation process

            * @return None
            """

            for line in instructions_set:  # for loop -> for each package in package set

                print(f"\nInstall {tool} ? Y/N ")

                # state = o -> success
                state = cmd.other(line)

                print(f"{g}Done{e}" if (state == 0) else f"{r}Failed{e}")

        index = 0

        for tool in tools:

            install(tool, instructions[index])
            index += 1
