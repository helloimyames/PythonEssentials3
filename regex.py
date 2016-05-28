import re


def main():
    fh = open('raven.txt')
    for line in fh:
        locate(line)
        replace(line)


def locate(line, text = 'Nevermore'):
    match = re.search(text, line)
    if match:
        print(line, end='')
        print(match.group())


def replace(line, find = 'Nevermore', insert = '###---###'):
    match = re.search(find,line)
    if match:
        print(line.replace(match.group(),'###---###'), end='')

if __name__ =="__main__": main()
