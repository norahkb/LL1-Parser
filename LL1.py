print("LL(1) Parsing For the following grammar\n")


# Parser Table
table = {
    "E": {"(": "T E'", "i": "T E'"},
    "E'": {"+": "+ T E'", ")": "epsilon", "$": "epsilon"},
    "T": {"(": "F T'", "i": "F T'"},
    "T'": {"": " F T'", "+": "epsilon", ")": "epsilon", "$": "epsilon"},
    "F": {"(": "( E )", "i": "i"}
}


def F():
    if match("("):
        if E():
            if match(")"):
                return True
            else:
                return False
        else:
            return False
    elif match("i"):
        return True
    else:
        return False

def Tx():
    if match("*"):
        if F():
            if Tx():
                return True
            else:
                return False
        else:
            return False
    else:
        return True

def T():
    if F():
        if Tx():
            return True
        else:
            return False
    else:
        return False

def Ex():
    if match("+"):
        if T():
            if Ex():
                return True
            else:
                return False
        else:
            return False
    else:
        return True

def E():
    if T():
        if Ex():
            return True
        else:
            return False
    else:
        return False


def display_parser_table():
    non_terminals = list(table.keys())
    terminals = set()
    for productions in table.values():
        terminals.update(productions.keys())
    terminals = sorted(list(terminals))

    print("Parser Table:")
    header = " " * 5
    for terminal in terminals:
        header += f" | {terminal: ^8}"
    print(header)
    print("-" * len(header))

    for non_terminal in non_terminals:
        row = f"{non_terminal: <5}"
        for terminal in terminals:
            if terminal in table[non_terminal]:
                production = table[non_terminal][terminal]
                row += f" | {production: <8}"
            else:
                row += " |        "
        print(row)

display_parser_table()

print("Enter the string you want to check\n")
s = list(input())
i = 0

def match(a):
    global s
    global i
    if i >= len(s):
        return False
    elif s[i] == a:
        i += 1
        return True
    else:
        return False

if E():
    if i == len(s):
        print("String is accepted")
    else:
        print("String is not accepted")
else:
    print("String is not accepted")
