import re


COLORS = dict()
TARTANS = dict()


# All tartan data was copy-pasted as presented in project directions.
# Function serves to iterate through this text document with the pasted data and
# sort line by line into appropriate dictionaries (COLORS, TARTANS)
#
# *** NOTE: have not accounted for various formats, nor different locations,
# ***       just meant to represent the idea ***
#
# {path} is the location of text file with data.
def init_data(path = "tartans"):

    with open(path) as file:
        data = [a.rstrip() for a in file]

        tartan = ""
        for line in data:
            # Ignore empty lines and file names
            if len(line) == 0 or '.' in line:
                continue

            if ':' in line: # Found "COLOR : VALUE" line
                init_colors(line)

            elif '(' in line: # Found "Name (num)" line
                tartan = line.split(' (')[0] # Extract name and save temporarily
                TARTANS[tartan] = ""

            # Remaining possible lines are color patterns
            else:
                TARTANS[tartan] = f"{TARTANS[tartan]} {line}"

# {line} : string
def init_colors(line):

    if ':' not in line:
        return

    line = line.split(" : ")

    key = line[0].lower()
    value = [int(a) for a in re.findall('\d+', line[1])]

    print(f"key: {key}, value: {value}")

    if key not in COLORS:
        COLORS[key] = value


def is_color_existing(color):
    return color in COLORS


def is_tartan_existing(name):
    return name in TARTANS


def list_colors():
    print(f"{c}\n" for c in COLORS)