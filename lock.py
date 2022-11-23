#Encode and decode tool for various cryptographic algorithms
import base64

string_to_encode = b""
encode_flag = b""

#Base64 encode 
def encode_base64():
    base64_string = base64.b64encode(string_to_encode)
    print("Here is your encoded string:\n ")
    print(base64_string)

#Base64 decode 
def decode_base64():
    base64_string_dec = base64.decode("ascii")
    print("Here is your decoded string:\n ")
    print(base64_string_dec)


#Caesar cipher encode 
def encode_caesar():
    print("Here is your encoded string:\n ")
    print()

#Caesar cipher decode 
def decode_caesar():
    print("Here is your decoded string:\n ")
    print()


#rot13 cipher encode 
def encode_rot13():
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
encode_base64()