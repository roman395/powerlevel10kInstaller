import subprocess as sub
from os import geteuid

installCom: str
isArch: bool

distros = {
    "debian": "apt install",
    "rhel": "yum install",
    "arch": "pacman -S",
    "opensuse": "zypper install",
    "gentoo": "emerge",
}


def init() -> None:
    global installCom
    global isArch
    if geteuid() != 0:
        print("Exec with sudo")
        exit(2)
    print("Init start")
    # TODO:change parh to normal
    out: sub.CompletedProcess = sub.run(
        'cat /etc/*release | grep "^ID="',
        stdout=sub.PIPE,
        encoding="utf-8",
        shell=True,
    )
    idLike = out.stdout.split("=", 1)[-1].strip()

    if idLike == "arch":
        isArch = True
    else:
        isArch = False

    try:
        installCom = distros[idLike]
        if input(f"Your install command is {installCom} \nIs it?(Y/n):") in [
            "y",
            "Y",
            "",
        ]:
            print("ok")
        else:
            installCom = input(
                "Please input install comand(like: apt install, pacman -S, etc):"
            )
    except KeyError:
        print("ERROR:PACKAGE MANAGER NOT FOUND! ABORDING")
        exit(1)
    print("Init complete")


def dependencies() -> None:
    print("Installation start")
    if not isArch:
        sub.run(f"{installCom} -y zsh curl", shell=True)
    else:
        sub.run(f"{installCom} --noconfirm zsh curl", shell=True)
    sub.run(
        'sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"',
        shell=True,
    )
    sub.run(
        'git clone --depth=1 https://github.com/romkatv/powerlevel10k.git "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k"',
        shell=True,
    )
    print("Installation complete")


def main():
    init()
    dependencies()


if __name__ == "__main__":
    main()
