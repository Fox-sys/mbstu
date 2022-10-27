LETTERS = [chr(i).lower() for i in range(65, 91)]


def encode(word: str, step: int = 1) -> str:
    moved_letters = LETTERS[step:] + LETTERS[:step]
    dc = {i[0]: i[1] for i in zip(LETTERS, moved_letters)}
    result = ''
    for letter in word.lower():
        result += dc[letter]
    return result


def decode(word: str, step: int = 1) -> str:
    return encode(word, -step)


a = encode('boris')
print(a)
print(decode(a))
