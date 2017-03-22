import glob

interesting_files = glob.glob("C:\\*.csv")

header_saved = False
with open('outputdre121.csv','wb') as fout:
    for filename in interesting_files:
        with open(filename) as fin:
            header = next(fin)
            if not header_saved:
                fout.write(header)
                header_saved = True
            for line in fin:
                fout.write(line)
print "Starte naechstes Script: regexParser.py"
execfile("regexParser.py")
