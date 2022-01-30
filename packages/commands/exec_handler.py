from subprocess import run
from sys import exit


class Execute:
    """
    Execute shell commands.
    """

    def __init__(self) -> None:
        pass

    def exec_command(self, command: str, hide_output: bool = False) -> function:
        """
        exec_command will run any given linux shell command.

        Args:
            command (str): Any linux command.
            hide_output (bool, optional): If this is True, proccess output will be
                        hidden from the console. Defaults to False.
        Returns:
            function: subprocess.run() function will return.
        """

        try:

            return run(command, shell=True, text=True, capture_output=hide_output)

        except:

            # Display error message and exit program if execution process failed.
            print(f"\nAn error occurred while executing command '{command}'")
            exit(1)
