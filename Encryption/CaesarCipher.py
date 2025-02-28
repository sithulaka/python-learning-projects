key_value = 3
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def Encrypt():
    encrypt_text= str()

    user_input = input("Enter Your Encryption Text: ").replace(" ", "").lower()

    for i in user_input:
        index = alphabet.index(i) 
        encrypt_text += alphabet[(index+key_value) % 26]

    return encrypt_text.upper()

def Decrypt():
    decrypt_text= str()

    user_input = input("Enter Your Cipher: ").lower()
    change_key()

    for i in user_input:
        index = alphabet.index(i) 
        decrypt_text += alphabet[(index-key_value) % 26]
        
    return decrypt_text.lower()

def exit():
    print("\nThank You For Using Our Service!")
    quit()

def change_key():
    global key_value
    try:
        key_value = int(input("Enter Your Key Value (Defult is 03): "))
    except:
        print("Please Enter Value Number And Try Again!")
        change_key()


while True:
    print ("\n\nCeasar Cipher Encryption\n01. Press Number \"1\" for Encrypt Your Text.\n02. Press Number \"2\" for Decrypt Your Cipher. \n03. Press Number \"3\" for Change Key Value. \n04. Press Number \"0\" for Exit.")
    try:
        Number = int(input("\nEnter Your Number: "))
    except:
        print("Please Enter Value Number And Try Again!")
        continue

    if Number == 0:
        exit()
    elif Number == 1:
        encryption = Encrypt()
        print(f"Cipher: \"{encryption}\"\nKey Value: 03 (defult Value)")
    elif Number == 2:
        decryption = Decrypt()
        print(f"Your Text: \"{decryption}\"")
    elif Number == 3:
        change_key()
    else:
        print("Please Enter Number Between 0-3!")
