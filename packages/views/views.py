from .colors import Color


class View(Color):
    """
    View will display predefined outputs.

    Args:
        Color ([class]): Inheritance from the Color class.
    """

    def __init__(self) -> None:
        pass

    def header(self, version: str) -> None:
        """
        header will print the program title.

        Args:
            version (str): Version of the application.
        """
        emoji = "🐊"
        title = " ALIGATOR"
        description = "A Post Installation Script for Ubuntu."
        author = "S3H4N"

        string_line_01 = f"{self.BOLD + self.LIGHT_WHITE + self.NEGATIVE}{title} {emoji} : {description}{self.END}"
        string_line_02 = f"{self.BOLD}Author : {author} {self.END}"
        string_line_03 = f"{self.BOLD}Version : {version}{self.END}"

        print(f"\n{string_line_01}\n\n{string_line_02}\t\t\t\t{string_line_03}")
        print("\n", "=" * 53, sep="")

    def pkg_list(self, pkg_set: dict) -> None:
        """
        pkg_list will print the list of packages.

        Args:
            pkg_set (dict): Predefined package set.
        """

        print(f"\nFollowing packages will be installed.")

        for catagory in pkg_set:

            print(f"\n📦 {self.BOLD + self.UNDERLINE}{catagory.upper()}{self.END}\n")
            pkg_list = pkg_set[catagory]

            for pkg in pkg_list:

                print(f"➔ {self.BOLD + pkg[0] + self.END} \n\t- {pkg[2]}")

    def user_prompt(self) -> int:
        """
        user_prompt will print the confirmation message.

        Returns:
            int: 0 -> User approval.
        """

        print("\n", "=" * 53, sep="")

        while True:

            opt = input(
                f"\n🚀 {self.BOLD}Do you wish to continue ? Y/y, N/n :: {self.END}"
            ).upper()

            if opt == "Y":

                print("\n", "=" * 53, sep="")
                return 0

            elif opt == "N":

                print("\n", "=" * 53, sep="")
                return 1
