#Encode and decode tool for various cryptographic algorithms
import base64

string_to_encode = b""
encode_flag = b""

#Base64 encode 
def encode_base64(string_to_encode, encode_flag):
    base64_msg = base64.b64encode(string_to_encode)
    print("Here is your encoded string:\n ")
    print(base64_msg)

#Base64 decode 
def decode_base64():
    base64_msg_dec = base64.b64decode("ascii")
    print("Here is your decoded string:\n ")
    print(base64_msg_dec)


#Caesar cipher encode 
def encode_caesar(string_to_encode):
    ABC = '0123456789abcdefghijklmnopqrstuvwxyz'
    cc = ''
    key = 3

    for i in string_to_encode:
        lower_i = i.lower()
    
    if lower_i in ABC:
        cced = ''

        if ABC.find(lower_i) > len(ABC) - (key + 1):
            cced = ABC[(ABC.find(lower_i) + key) % len(ABC)]
        else:
            cced = ABC[ABC.find(lower_i) + key]

        cc += ciphered.upper() if i.isupper() else cced

    else:
        cc += i
    return cc
    print("Here is your encoded string:\n ")
    print()

#Caesar cipher decode 
def decode_caesar():
    print("Here is your decoded string:\n ")
    print()


#rot13 cipher encode 
def encode_rot13(string_to_encode):
    def lookup(x):
        order, char = ord(x), x.lower()
        if 'a' <= char <= 'm':
            return chr(order + 13)
        if 'n' <= char <= 'z':
            return chr(order - 13)
        return x
    return ''.join(map(lookup, message))
    print("Here is your encoded string:\n ")
    print()

#rot13 cipher decode
def decode_rot13():
    print("Here is your decoded string:\n ")
    print()

def main():
    string_to_encode = input("Please enter the string you wish to encode:\n")
    encode_flag = input("Please enter the cipher you wish to use:\n")
    
main()
encode_caesar("test")