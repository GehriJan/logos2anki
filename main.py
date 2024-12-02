import sys
import getopt

def processOptions(opts):
    for opt, optarg in opts:
        if opt == "-h" or opt == "--help":
            sys.exit()

if __name__ == '__main__':
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:],
                                       "h",
                                       ["help"])
    except getopt.GetoptError as err:
        print(sys.argv[0],":", err)
        sys.exit(1)

    processOptions(opts)

    for file in args:
        fp = open(file, "r")
        input = fp.read()
        fp.close()

    lines = input.splitlines()
    output: str = ""
    ctr: int = 3
    while ctr<len(lines)-4:
        output+=f"{lines[ctr]}|{lines[ctr+1].strip()}\n"
        ctr+=2
    output = output.strip()
    with open("ankiOutput.txt", "w") as outputFile:
        outputFile.write(output)
        outputFile.close()
        