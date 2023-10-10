def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:  #-sig即去除/ufeff
        for line in f:
            lines.append(line.strip()) #將換行符號去掉後,再裝入清單內
    return lines




def convert(lines):
    person = None   #person = none 為預設值
    allen_word_count = 0
    viki_word_count = 0
    allen_sticker_count = 0
    viki_sticker_count = 0
    allen_picture_count = 0
    viki_picture_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_picture_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_picture_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
    print('Allen說了 ', allen_word_count, '個字 ; 傳了', allen_sticker_count, '個貼圖', ' ; 傳了', allen_picture_count, '個圖片')
    print('Viki說了 ', viki_word_count, '個字 ; 傳了', viki_sticker_count, '個貼圖', ' ; 傳了', viki_picture_count, '個圖片')


def write_file(filename, lines):     #把filename 和 lines創一個txt檔並輸出
    with open(filename, 'w', encoding='utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)  #convert後把lines清單覆蓋掉
    write_file('output.txt', lines)

main()
