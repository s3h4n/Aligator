from ..packages import File
from ..packages import Get
from ..packages import Find
from ..packages import Color
from ..packages import View
from .constants import PKG_SET as pkg_set
from .constants import REPO_SET as repos


class Handler(Color):
    """
    Handler will all tasks.

    Args:
        Color (Class): Inheritance from the Color class.
    """

    def __init__(self) -> None:

        self.view = View()
        self.file = File()
        self.get = Get()
        self.find = Find()

    def handler(self) -> None:
        """
        handler will handle all the tasks.
        """

        print(f"\n{self.LIGHT_GREEN}Updating system...{self.END}\n")

        state = self.get.update_pkg()

        print(
            f"\n✅ {self.LIGHT_GREEN}Successful."
            if (state == 0)
            else f"\n❌ {self.LIGHT_RED}Failed.",
            f"{self.END}",
        )

        self.view.header("2.1")
        self.view.pkg_list(pkg_set)

        if self.view.user_prompt() == 0:

            self.repo_adder()
            self.pkg_adder()

    def repo_adder(self) -> None:
        """
        repo_adder will add repositories.
        """

        for repo in repos:

            repo_name = repos[repo][0]
            repo_link = repos[repo][1]

            if self.find.apt_repo(repo_link) == 0:

                print(
                    f"\n{self.LIGHT_GREEN}Repository for {repo} has found.{self.END}\n\nSkipping..."
                )

            else:

                print(f"\n{self.BOLD}Adding repository for{repo}...{self.END}")

                state = self.get.apt_repo(repo_name)

                print(
                    f"\n✅ {self.LIGHT_GREEN}Successful."
                    if (state == 0)
                    else f"\n❌ {self.LIGHT_RED}Failed.",
                    f"{self.END}",
                )

    def pkg_adder(self) -> None:
        """
        pkg_adder will add packages.
        """

        for catagory in pkg_set:

            pkg_list = pkg_set[catagory]

            for pkg in pkg_list:

                if pkg[1] == "":

                    print(f"\n{self.BOLD}Installing {pkg[0]}...{self.END}")

                    state = self.get.anything(pkg[3])

                    print(
                        f"\n✅ {self.LIGHT_GREEN}Successful."
                        if (state == 0)
                        else f"\n❌ {self.LIGHT_RED}Failed.",
                        f"{self.END}",
                    )

                else:

                    print(f"\n{self.BOLD}Installing {pkg[0]}...{self.END}")

                    state = self.get.apt_pkg(pkg[1])

                    print(
                        f"\n✅ {self.LIGHT_GREEN}Successful."
                        if (state == 0)
                        else f"\n❌ {self.LIGHT_RED}Failed.",
                        f"{self.END}",
                    )

    def file_adder(self) -> None:
        """
        file_adder will add files.
        """

        f = self.file

        f.make_dir("~/.config/nvim/autoload")
        f.make_dir("~/.config/fish")
        f.make_dir("~/.config/kitty")
        f.make_dir("~/.themes")
        f.make_dir("~/.icons")

    def config_maker(self) -> None:
        """
        config_maker will make configurations.
        """

        self.get.anything(
            "sudo update-alternatives --set x-terminal-emulator /usr/bin/kitty"
        )  # set kitty terminal as default.
