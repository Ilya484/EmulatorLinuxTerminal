from os import system

from confg import USER, PC


def main():
    system("cls")
    startLine = f"{USER}@{PC}> "
    # TODO: rewritte
    while True:
        string = input(startLine)



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
