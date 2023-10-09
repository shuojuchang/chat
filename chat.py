def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:  #-sig即去除/ufeff
        for line in f:
            lines.append(line.strip()) #將換行符號去掉後,再裝入清單內
    return lines


def convert(lines):
    new = []
    person = None   #person = none 為預設值
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:
            new.append(person + ': ' + line)
    return new


def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('input.txt')
    lines = convert(lines)  #convert後把lines清單覆蓋掉
    write_file('output.txt', lines)

main()
