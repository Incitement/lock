#Encode and decode tool for various cryptographic algorithms
import base64
import codecs
import argparse
import sys


string_to_encode = b""
encode_flag = b""



#Base64 encode 
def encode_base64(string_to_encode):
    base64_msg = base64.b64encode(string_to_encode.encode('utf-8'))
    print("Here is your Base64-encoded string:\n ")
    print(base64_msg)

#Base64 decode 
def decode_base64():
    
    print("Here is your decoded string:\n ")
    print()


#Caesar cipher encode 
def encode_caesar(string_to_encode):
    string_to_encode = bytes(string_to_encode, 'utf-8')
    ABC = '0123456789abcdefghijklmnopqrstuvwxyz'
    key = 3

    unshifted_values = [b for b in string_to_encode]

    shifted_values = [(val + key) % 256 for val in unshifted_values]

    print("Here is your Caesar-encoded string:\n ")
    print(bytes(shifted_values))

#Caesar cipher decode 
def decode_caesar():
    print("Here is your decoded string:\n ")
    print()

#rot13 cipher encode 
def encode_rot13(string_to_encode):
    x = codecs.encode(string_to_encode, 'rot_13')
    print("Here is your ROT13-encoded string:")
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
print("BREAK")
print("BREAK")
encode_base64(string_test)
encode_caesar(string_test)