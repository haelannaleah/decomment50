#!/usr/bin/python
# decomment50.py
#
# by Annaleah Ernst and Kareem Omar, jterm 2016
# annaleahernst@college.harvard.edu
#
# intelligently removes the comments from c files and php files
# nested comments, strings, character literals, the lot
#
# amazingly, not less readable than a 45-line version (available upon request)
#
# https://xkcd.com/208/

import re, sys
def decomment(inn, outn):
    try:
        with open(inn, 'r') as inf, open(outn, 'w') as of:
            of.write(re.sub(re.compile(r'^[ \t\f\v]*//.*?(\n|$)|//.*?$|^[ \t\f\v]*/\*.*?\*/(\n|$)|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"' + (r'|^[ \t\f\v]*#.*?(\n|$)|#.*?$' if inn[-4:] == '.php' else ''), re.DOTALL | re.MULTILINE), lambda s : s.group(0) if s.group(0)[0]=="'" or s.group(0)[0]=='"' else '', inf.read()))
        return 'Successfully decommented ' + inn[max(inn.rfind('/'), inn.rfind('\\'))+1:] + ' and saved result in ' + outn[max(outn.rfind('/'), outn.rfind('\\'))+1:]
    except:
        return 'ERROR: failed to open file.'
print('Usage: decomment50.py <file_to_decomment>' if len(sys.argv) != 2 else decomment(sys.argv[1], sys.argv[1][:sys.argv[1].rfind('.')] + '_decommented' + sys.argv[1][sys.argv[1].rfind('.'):]))