from repository import reopsitory
from termcolor import colored


def main():
    repo = reopsitory()
    repo.run()
    cheap = 20000
    cheapList = []
    for elem in repo:
        if elem.median_house_value < cheap:
            cheapList.append(elem)
    cheapList.sort(key=lambda x: x.median_house_value)

    print(colored('billige Distrikte: ', 'blue'))
    for i in cheapList:
        print(i)


main()
