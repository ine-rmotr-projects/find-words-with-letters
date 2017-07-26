import click
"""
Tests:
finds ok
wrong order
finds with upercase
"""


def find_words_with_letters(words_iterator, letters, ignore_case=True):
    lower_letters = letters.lower()
    for word in words_iterator:
        if not all([l in word.lower() for l in lower_letters]):
            continue

        positions = [word.lower().index(l) for l in lower_letters]
        if positions != sorted(positions):
            continue

        yield word


@click.command()
@click.argument('words', type=click.File('r'))
@click.option('-l', '--letters', prompt='Letters (or chars) to look for',
              required=True, help='The person to greet.')
def main(words, letters):
    words_iterator = (word.strip() for word in words if word.strip())
    for word in find_words_with_letters(words_iterator, letters):
        if word == 'samba':
            print("YEY! SAMBA!")
            exit()
        print(word)


if __name__ == '__main__':
    main()
