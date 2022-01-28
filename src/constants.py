
# color constants
PURPLE = "\033[95m"
CYAN = "\033[96m"
DARKCYAN = "\033[36m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
END = "\033[0m"


"""
    * following dictionary will store the repository list
    * format -> repo name : [ link , keyword ]
"""


REPOS = {

    "php8.0": ["ppa:ondrej/php", "PPA-ondrej-php"],
    "obs-studio": ["ppa:obsproject/obs-studio", "PPA-obsproject-obs-studio"]
}


"""
    * following dictionary will store the installing packages list (apt)
    * format -> Catagory : { tool : description }

"""


APT_TOOLS = {

    "Download":
    {
        "curl": "Cli tool for downloading files",
        "wget": "Cli tool for downloading files",
    },

    "Developer":
    {
        "apache2": "Apache HTTP server",
        "gcc": "C compiler",
        "clang": "C, C++ and Objective-C compiler",
        "nodejs": "Nodejs platform",
        "npm": "Package manager for Node.js",
        "php8.0": "Php version 8",
        "mysql-server": "MySQL database server",
        "libapache2-mod-php8.0 php-mysql": "Required modules",
        "python3-pip": "Python package installer",
        "openjdk-18-jdk": "OpenJDK Development Kit (JDK)",
        "openjdk-18-jre": "OpenJDK Java runtime",
    },

    "Entertainment":
    {
        "vlc": "Multimedia player and streamer",
        "ffmpeg": "Tools for transcoding, streaming and playing of multimedia files",
        "obs-studio": "Recorder and streamer for live video content",
    },

    "Extra":
    {
        "gnome-tweak-tool": "Gnome customization tool",
        "figlet": "Make large character ASCII banners out of ordinary text",
        "cmatrix": "Simulates the display from 'The Matrix'",
        "neofetch": "Shows Linux System Information with Distribution Logo",
    },

    "IDE/Text Editors":
    {
        "neovim": "Heavily refactored vim fork",
    },

    "Network":
    {
        "tor": "Anonymizing overlay network for TCP",
        "net-tools": "NET-3 networking toolkit",
    },

    "Optimization":
    {
        "preload": "Makes frequently used softwares to load faster",
        "stacer": "Linux system optimizer and monitoring",
    },

    "Terminal Emulators":

    {
        "kitty": "Fast, featureful, GPU based terminal emulator",
    },

    "Utility":
    {
        "timeshift": "System backup/restore utility",
        "dconf-cli": "Simple configuration storage system",
        "htop": "Interactive processes/tasks viewer",
        "ranger": "Console File Manager with VI Key Bindings",
        "fish": "Friendly interactive shell",
    },

}

"""
    * following dictionary will store the installing packages list (other sources)
    * format -> tool : [ commands ]

"""

OTHER_TOOLS = {

    "starship": [
        'sh -c "$(curl -fsSL https://starship.rs/install.sh)"',
    ],

}

CONFIGS = {

    "kitty": [
        "sudo update-alternatives --install /usr/bin/x-terminal-emulator x-terminal-emulator ~/.local/bin/kitty 50",
        "sudo update-alternatives --config x-terminal-emulator",
    ],

}

DIR_PATHS = {
    ".themes": "~/.themes",
    ".icons": "~/.icons",
    ".local": "~/.local",
    "bin": "~/.local/bin",
    ".config": "~/.config",
    "kitty": "~/.config/kitty",
    "fish": "~/.config/fish",
    "nvim": "~/.config/nvim",
}
