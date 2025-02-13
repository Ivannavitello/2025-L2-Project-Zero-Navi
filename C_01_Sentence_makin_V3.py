# functions goes here
def make_statement(statement, decoration, lines= 1):
    """Emphasises headings by adding decoration
    at the start and End"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)

    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)


# Main routine here
make_statement("Programing is cool and Fun", "👍", 1)
print()
make_statement("PRohraming is Stil foinee!?!!,", "1", 2)
print()
make_statement("Emoji in Action", "=")
