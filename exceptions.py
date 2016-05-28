

def main():
    try:
        fh = open('lines_wrong.txt')
        for line in fh: print(line.strip())
    except IOError as e:
        print(e)



if __name__=='__main__': main()
