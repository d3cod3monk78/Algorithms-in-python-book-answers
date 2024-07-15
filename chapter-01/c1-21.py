from typing import TextIO


def write_on_a_file(filepath: str) -> [str]:
    file: TextIO = open(filepath, 'w')

    lines: [str] = []

    while True:
        user_input: str = input('Write the line that you need: ')

        if user_input.strip().lower() == 'done':
            break
        lines.append(user_input.strip())

    for line in lines:
        file.write(line + '\n')
    file.close()
    return lines


def read_lines(filepath: str) -> None:
    file: TextIO = open(filepath, 'r')

    lines: [str] = file.readlines()
    file.close()

    for line in lines:
        print(line.strip()[::-1], end='\n')


filepath: str = 'test.txt'
write_on_a_file(filepath)
read_lines(filepath)
