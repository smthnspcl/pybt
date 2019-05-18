from sys import argv
from os import system


class Installer(object):
    @staticmethod
    def install_dependencies():
        system("./dependencies.sh")

    @staticmethod
    def install():
        system("")


class Configuration(object):
    @staticmethod
    def parse():
        i = 0
        while i < len(argv):
            if argv[i] in ["-h", "--help"]:
                Configuration.help()
            elif argv[i] in ["-d", "-id", "--dependencies", "--install-dependencies"]:
                Installer.install_dependencies()
            elif argv[i] in ["-i", "--install"]:
                Installer.install()
            else:
                Configuration.help()
            i += 1

    @staticmethod
    def help():
        print("usage: python3 install.py {arguments}")
        print("{arguments}:")
        print("\t-h\t--help")
        print("\t-d\t-id\t--dependencies\t--install-dependencies")
        print("\t-i\t--install")
        exit()


if __name__ == '__main__':
    Configuration.parse()
