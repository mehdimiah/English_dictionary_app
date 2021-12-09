import json
from difflib import SequenceMatcher,get_close_matches

data = json.load(open("data.json"))

def foo(key):
    w = key.lower()
    if w in data:
        return data[w]
    elif w.capitalize() in data:
        return data[w.capitalize()]
    elif w.upper() in data:
        return data[w.upper()]

    elif len(get_close_matches(w, data.keys(),cutoff=0.88)) > 0:
        yn = input('Did you mean {} instead? press Y if yes and N if no'.format(get_close_matches(w, data.keys(),cutoff=0.88)[0]))
        if yn == 'Y':
            return data[get_close_matches(w, data.keys(),cutoff=0.88)[0]]
        elif yn == 'N':
            return "This word doesn't exist"
        else:
            return 'We didnt understand your entry'
    else:
        return "This word doesn't exist"  #none is to ignore the junk lines like commas or something

x = input('enter word here: ')

output = foo(x)
count = 0
if type(output) == list:
    for x in output:
        count += 1
        print('{}.{}'.format(count,x))
else:
    print(output)

