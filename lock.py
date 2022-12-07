#Encode and decode tool for various cryptographic algorithms
import base64
import codecs

string_to_encode = b""
encode_flag = b""

#Base64 encode 
def encode_base64(string_to_encode, encode_flag):
    base64_msg = base64.b64encode(string_to_encode)
    print("Here is your encoded string:\n ")
    print(base64_msg)

#Base64 decode 
def decode_base64():
    
    print("Here is your decoded string:\n ")
    print()


#Caesar cipher encode 
def encode_caesar(string_to_encode):
    ABC = '0123456789abcdefghijklmnopqrstuvwxyz'

    print("Here is your encoded string:\n ")
    print()

#Caesar cipher decode 
def decode_caesar():
    print("Here is your decoded string:\n ")
    print()


#rot13 cipher encode 
def encode_rot13(string_to_encode):
    x = codecs.encode(string_test, 'rot_13')
    print("ROT13 string Encoded: ")
    print(x)


#rot13 cipher decode
def decode_rot13():
    print("Here is your decoded string:\n ")
    print() 

def main():
    string_to_encode = input("Please enter the string you wish to encode:\n")
    encode_flag = input("Please enter the cipher you wish to use:\n")
    
#main()
string_test = input("Please enter the string you wish to encode:\n")
#string_test = bytes(string_test, 'ascii')
print(string_test)
encode_rot13(string_test)