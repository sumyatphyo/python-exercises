import sys
script, enconding, error = sys.argv


def main(language_file, enconding, errors):
    line = language_file.readline()

    if line:
        print_line(line, enconding, errors)
        return main(language_file, enconding, errors)

def print_line(line, enconding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(enconding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)
