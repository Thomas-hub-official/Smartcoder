MorseList = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G",
    "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
    "---": "O", ".--．": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z",

    "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
    ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",

    ".-.-.-": ".", "---...": ":", "--..--": ",", "-.-.-.": ";", "..--..": "?",
    "-...-": "=", ".----.": "'", "-..-.": "/", "-.-.--": "!", "-....-": "-",
    "..--.-": "_", ".-..-.": '"', "-.--.": "(", "-.--.-": ")", "...-..-": "$",
    "....": "&", ".--.-.": "@", ".-.-.": "+",

    "":""
}
reverse_MorseList = {v: k for k, v in MorseList.items()}


def morse_legal(str, sign):
    for x in str:
        if x != '.' and x != '-' and x != sign and x!=' ':
            return False
    return True


def morse_de(string, sign):
    if morse_legal(string, sign):
        # 分割，字符串string，分割标识符sign
        lists = string.split(sign)
        str = ''
        for code in lists:
            str += MorseList.get(code)
        return str
    else:
        return 'Failed: The morse_code string is illegal, please check!!!'


def morse_en(string, sign):
    str = ''
    for char in string:
        str += reverse_MorseList.get(char)
        str += sign
    return str
