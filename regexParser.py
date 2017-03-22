import re
import matchParser

lines = [line.strip() for line in open(matchParser.fout.name)]

with open('outputregexdre15.csv', "w") as output_csv:

    for result in lines:
        match = re.search(r'((\s\d+?[1-9])!?[ ])', result)
        if match: output_csv.write(match.group(0) + '\n')
print "Prozess abgeschlossen"
