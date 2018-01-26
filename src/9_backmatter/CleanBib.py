#!/usr/bin/python

def main():
    f = open("PhDThesis.bib","r")
    lines = f.readlines()
    f.close()
    f = open("PhDThesis.bib","w")
    for line in lines:
        splited_line = line.split(' ')
        if splited_line[0] != "file" and splited_line[0] != "url" and splited_line[0] != "doi" and splited_line[0] != "issn" and splited_line[0] != "isbn":
            f.write(line)
    f.close()

if __name__ == "__main__":
    main()