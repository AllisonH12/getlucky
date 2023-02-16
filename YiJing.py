import random
from flask import Flask, render_template, request


app = Flask(__name__)

class YiJing:

    HEXAGRAMS = { 
    "111111": "乾 - Qián - The Creative",
    "000000": "坤 - Kūn - The Receptive",
    "010001": "震 - Zhèn - The Arousing",
    "100010": "巽 - Xùn - The Gentle",
    "010111": "坎 - Kǎn - The Abysmal",
    "111010": "离 - Lí - The Clinging",
    "001010": "艮 - Gèn - Keeping Still",
    "101111": "兑 - Duì - The Joyous",
    "111011": "涉 - Shè - The Army",
    "110111": "泰 - Tài - The Clinging Fire",
    "111110": "否 - Pǐ - The Arousing Thunder",
    "010010": "小过 - Xiǎo Guò - The Gentle Wind",
    "101001": "履 - Lǚ - The Penetrating",
    "110000": "泰 - Tài - The Joyous Lake",
    "000011": "乾 - Qián - The Creative Heaven",
    "111000": "夬 - Guài - The Joyous Earth",
    "000111": "大壮 - Dà Zhuàng - The Great Accumulating",
    "100000": "颐 - Yí - The Penetrating Wind",
    "000001": "蛊 - Gu - The Joyous Lake",
    "100110": "临 - Lín - Approach",
    "011001": "观 - Guān - The Clinging",
    "010011": "剥 - Bō - Dispersion",
    "110100": "复 - Fù - Return",
    "001100": "小畜 - Xiǎo Xù - The Gentle",
    "101101": "大畜 - Dà Xù - The Great Possessing",
    "001111": "归妹 - Guī Mèi - The Abysmal Water",
    "111100": "仙姑 - Xiān Gū - The Sojourning",
    "000100": "节 - Jié - The Clinging Fire",
    "001000": "葵 - Kuí - Opposition",
    "100111": "归妹 - Guī Mèi - The Joyous Lake",
    "111001": "萃 - Cuì - The Taming Power of the Great",
    "100101": "兑 - Duì - The Joyous Lake",
    "101100": "恒 - Héng - Duration",
    "001110": "遁 - Dùn - Retiring",
    "011100": "大有 - Dà Yǒu - The Great Taming",
    "001001": "升 - Shēng - Pushing Upward",
    "110110": "观 - Guān - The Keeping Still Mountain",
    "011010": "否 - Pǐ - The Arousing Fire",
    "101010": "解 - Jiě - The Clinging Wood",
    "010100": "坎 - Kǎn - The Abysmal Water",
    "110010": "离 - Lí - The Clinging Flame",
    "010011": "渐 - Jiàn - The Infiltrating",
    "010101": "大过 - Dà Guò - The Preponderance of the Small",
    "110011": "恒 - Héng - The Arousing Thunder",
    "001100": "益 - Yì - The Clinging Earth",
    "011010": "震 - Zhèn - The Arousing",
    "101110": "小过 - Xiǎo Guò - The Clinging",
    "011001": "渐 - Jiàn - The Gentle Wind",
    "100110": "节 - Jié - The Joyous Lake",
    "001010": "中孚 - Zhōng Fú - The Joyous Lake",
    "101001": "小畜 - Xiǎo Xù - The Clinging Wood",
    "110000": "大壮 - Dà Zhuàng - The Joyous Lake",
    "000011": "夬 - Guài - The Creative Heaven",
    "111000": "萃 - Cuì - The Taming Power of the Small",
    "000111": "随 - Suí - The Clinging Water",
    "100000": "讼 - Sòng - The Clinging Wood",
    "000001": "未济 - Wèi Jì - The Clinging Fire",
    "100111": "旅 - Lǚ - The Taming Power of the Small",
    "111001": "巽 - Xùn - The Arousing Wind",
    "100101": "困 - Kùn - The Receptive Earth",
    "101100": "鼎 - Dǐng - The Clinging Fire",
    "001110": "大过 - Dà Guò - The Joyous Water",
    "011100": "既济 - Jì Jì - The Arousing Thunder",
    "001001": "革 - Gé - The Clinging Fire",
    "110110": "兑 - Duì - The Joyous Lake",
    "011010": "小畜 - Xiǎo Xù - The Arousing Thunder",
    "101010": "未济 - Wèi Jì - The Clinging Wood",
    "010100": "咸 - Xián - The Joyous Lake",
    "110010": "涣 - Huàn - Dissolution",
    "010011": "大壮 - Dà Zhuàng - The Clinging Thunder",
    "101101": "夬 - Guài - The Creative Earth",
    "001101": "恒 - Héng - The Abysmal Water",
    "001011": "明夷 - Míng Yí - The Abysmal Water",
    "110100": "震 - Zhèn - The Sojourning",
    "010110": "家人 - Jiā Rén - The Clinging Wind",
    "011100": "归妹 - Guī Mèi - The Clinging Mountain",
    "001010": "履 - Lǚ - The Clinging Thunder",
    "101011": "泰 - Tài - The Receptive Earth",
    "010100": "大畜 - Dà Xù - The Clinging Mountain",
    "001001": "需 - Xū - The Clinging Water",
    "100010": "明夷 - Míng Yí - The Clinging Earth"

    }

    @staticmethod
    def get_binary_code(word):
        binary_code = ""
        for char in word:
            binary_code += bin(ord(char))[2:].zfill(8)
        return binary_code

    @staticmethod
    def get_fragments(binary_code):
        fragments = []
        for i in range(0, len(binary_code), 6):
            fragments.append(binary_code[i:i+6])
        return fragments

    @staticmethod
    def lookup_hexagram(fragment):
        if fragment in YiJing.HEXAGRAMS:
            return YiJing.HEXAGRAMS[fragment]


def get_luck():
    #word = input("Enter a word: ")
    word = ''
    #word = request.form['word']
    #word = 'abc'

    try:
        word = request.form['word1']
    except KeyError:
        word = ''

    word += str(random.randint(0, 65))
    #binary_code = YiJing.get_binary_code(word)
    binary_code = YiJing.get_binary_code(word)
    fragments = YiJing.get_fragments(binary_code)
    luck = {}
    for fragment in fragments:
        if YiJing.lookup_hexagram(fragment) in luck:
            luck[YiJing.lookup_hexagram(fragment)] += 1
        else:
            luck[YiJing.lookup_hexagram(fragment)] = 1

    sorted_dict = {k: v for k, v in sorted(luck.items(), key=lambda item: item[1], reverse=True)}
    ct = 0
    out = ""
    for key, value in sorted_dict.items():
        ct += 1 
        if ct < 4 and key is not None:
            out += key + "    "
    return out

@app.route('/', methods=['GET', 'POST'])
def home():
    luck = get_luck()
    return render_template('home.html', luck=luck)

if __name__ == '__main__':
    app.run(debug=True)
