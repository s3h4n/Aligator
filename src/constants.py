"""
    Following dictionary will store the repository details.

    Format : 
    {
        Name (str) : [
            Repo keyword (str),
            Repo URL (str)
        ]
    }
"""

REPO_SET = {
    "php8.0": ["ppa:ondrej/php", "http://ppa.launchpad.net/ondrej/php/ubuntu"],
    "obs-studio": [
        "ppa:obsproject/obs-studio",
        "http://ppa.launchpad.net/obsproject/obs-studio/ubuntu",
    ],
}

"""
    Following dictionary will store the data of all packages
    that needed to be installed.

    Format :
    {
        Catagory (str) : {
            [
                Package Name (str)
                Package keyword (str),
                Package description (str),
                Instructions (tuple),
            ],
        }
    }
"""


PKG_SET = {
    "Download Tools": [
        ["Wget", "wget", "Cli tool for downloading files"],
        ["Curl", "curl", "Cli tool for downloading files"],
    ],
    "Developer Tools": [
        ["Apache2", "apache2", "Apache HTTP server"],
        ["Gcc", "gcc", "C compiler"],
        ["Clang", "clang", "C, C++ and Objective-C compiler"],
        ["Nodejs", "nodejs", "Nodejs platform"],
        ["Npm", "npm", "Package manager for Node.js"],
        ["Php8.0", "php8.0", "Php version 8"],
        ["Mysql-server", "mysql-server", "MySQL database server"],
        [
            "Libapache2-mod-php8.0 Php-Mysql",
            "libapache2-mod-php8.0 php-mysql",
            "Required modules",
        ],
        ["Python3-pip", "python3-pip", "Python package installer"],
        ["Openjdk-18-jdk", "openjdk-18-jdk", "OpenJDK Development Kit (JDK)"],
        ["Openjdk-18-jre", "openjdk-18-jre", "OpenJDK Java runtime"],
    ],
    "Entertainment": [
        ["Vlc", "vlc", "Multimedia player and streamer"],
        [
            "Ffmpeg",
            "ffmpeg",
            "Tools for transcoding, streaming and playing of multimedia files",
        ],
        ["Obs-studio", "obs-studio", "Recorder and streamer for live video content"],
    ],
    "Extra": [
        ["Gnome-tweak-tool", "gnome-tweak-tool", "Gnome customization tool"],
        ["Figlet", "figlet", "Make large character ASCII banners out of ordinary text"],
        ["Cmatrix", "cmatrix", "Simulates the display from 'The Matrix'"],
        [
            "Neofetch",
            "neofetch",
            "Shows Linux System Information with Distribution Logo",
        ],
    ],
    "IDE/Text Editors": [
        ["Neovim", "neovim", "Heavily refactored vim fork"],
        [
            "Vim-plug",
            "",
            "Plugin manager for Neovim",
            (
                "wget -N -q --show-progress -O ~/.config/nvim/autoload/plug.vim https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim"
            ),
        ],
    ],
    "Network Tools": [
        ["Tor", "tor", "Anonymizing overlay network for TCP"],
        ["Net-tools", "net-tools", "NET-3 networking toolkit"],
    ],
    "Optimization Tools": [
        ["Preload", "preload", "Makes frequently used softwares to load faster"],
        ["Stacer", "stacer", "Linux system optimizer and monitoring"],
    ],
    "Terminal Emulators": [
        ["Kitty", "kitty", "Fast, featureful, GPU based terminal emulator"],
    ],
    "Utilities": [
        [
            "Starship",
            "",
            "Minimal, fast, customizable prompt for any shell!",
            ('sh -c "$(curl -fsSL https://starship.rs/install.sh)"'),
        ],
        ["Timeshift", "timeshift", "System backup/restore utility"],
        ["Dconf-cli", "dconf-cli", "Simple configuration storage system"],
        ["Htop", "htop", "Interactive processes/tasks viewer"],
        ["Ranger", "ranger", "Console File Manager with VI Key Bindings"],
        ["Fish", "fish", "Friendly interactive shell"],
    ],
}


CONFIGS = {
    ".bashrc": [
        "https://raw.githubusercontent.com/s3h4n/aligator/main/configs/.bashrc",
        "~/.bashrc",
    ],
    "cofig.fish": [
        "https://raw.githubusercontent.com/s3h4n/aligator/main/configs/config.fish",
        "~/.config/fish/config.fish",
    ],
    "dracula.conf": [
        "https://raw.githubusercontent.com/s3h4n/aligator/main/configs/dracula.conf",
        "~/.config/kitty/dracula.conf",
    ],
    "init.vim": [
        "https://raw.githubusercontent.com/s3h4n/aligator/main/configs/init.vim",
        "~/.config/nvim/init.vim",
    ],
    "kitty.conf": [
        "https://raw.githubusercontent.com/s3h4n/aligator/main/configs/kitty.conf",
        "~/.config/kitty/kitty.conf",
    ],
    "starship.toml": [
        "https://raw.githubusercontent.com/s3h4n/aligator/main/configs/starship.toml",
        "~/.config/starship.toml",
    ],
}
