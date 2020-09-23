from Methods.morse import *
import binascii
import hashlib
import base64

sha = ['sha_256', 'sha_512', 'sha_1', 'sha_384', 'sha_224']
md5 = ['md5_8', 'md5_16']
others = ['morse_code', 'hex']
base = ['base64', 'base32', 'base16']

allm = base + sha + md5 + others

allm.sort()


# md5
def md5_encode_8(str):
    return hashlib.md5(str.encode(encoding='UTF-8')).hexdigest()


def md5_encode_16(str):
    return hashlib.md5(str.encode(encoding='UTF-8')).hexdigest()[8:-8]


# sha
def sha_encode_256(str):
    return hashlib.sha256(str.encode(encoding='UTF-8')).hexdigest()


def sha_encode_512(str):
    return hashlib.sha256(str.encode(encoding='UTF-8')).hexdigest()


def sha_encode_1(str):
    return hashlib.sha1(str.encode(encoding='UTF-8')).hexdigest()


def sha_encode_384(str):
    return hashlib.sha384(str.encode(encoding='UTF-8')).hexdigest()


def sha_encode_224(str):
    return hashlib.sha224(str.encode(encoding='UTF-8')).hexdigest()


# morse
def morse_decode(str, split_char):
    return morse_de(str, split_char)


def morse_encode(str, split_char):
    return morse_en(str, split_char)


# base
def base64_decode(str):
    r = ''
    try:
        r = base64.b64decode(str).decode('utf-8')
    except:
        r = 'Failed: This base64 string is illegal, please check!'
    return r


def base64_encode(str):
    r = ''
    try:
        r = base64.b64encode(str.encode('utf-8')).decode('utf-8')
    except:
        r = 'Failed: Illegal to convert this string to base64 string, please check!'
    return r


def base32_decode(str):
    r = ''
    try:
        r = base64.b32decode(str).decode('utf-8')
    except:
        r = 'Failed: This base32 string is illegal, please check!'
    return r


def base32_encode(str):
    r = ''
    try:
        r = base64.b32encode(str.encode('utf-8')).decode('utf-8')
    except:
        r = 'Failed: Illegal to convert this string to base32 string, please check!'
    return r


def base16_decode(str):
    r = ''
    try:
        r = base64.b16decode(str).decode('utf-8')
    except:
        r = 'Failed: This base16 string is illegal, please check!'
    return r


def base16_encode(str):
    r = ''
    try:
        r = base64.b16encode(str.encode('utf-8')).decode('utf-8')
    except:
        r = 'Failed: Illegal to convert this string to base16 string, please check!'
    return r


def enhex(str):
    r = ''
    try:
        r = str.encode().hex()
    except:
        r = 'Failed: Illegal to convert this string to hex, please check!'
    return r


def dehex(str):
    r = ''
    try:
        r = binascii.a2b_hex(str).decode()
    except:
        r = 'Failed: This hex string is illegal, please check!'
    return r