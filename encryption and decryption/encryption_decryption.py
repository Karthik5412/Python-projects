import json
import random as rd
import string

def encrypt(text, encrypt_text, org_order):
    cipher =''
    for ele in text :
        idx = org_order.index(ele)
        cipher += encrypt_text[idx]
    
    return cipher

def decrypt(text,enc_order,org_order):
    original =''
    for ele in text :
        idx = enc_order.index(ele)
        original += org_order[idx]

    return original
    
def main():
    file = 'encrypted_codes.json'
    org_order = list(string.ascii_letters + string.digits + string.punctuation + ' ')

    with open(file,'r') as f:
        data = json.load(f)

    key_values = tuple(data.keys())
    key = rd.choice(key_values)
    inprogress = True


    while inprogress:
        print('-'*50)
        text = input('Enter text or u can abbot by saying no: \n').strip()
        n = len(text)
        ch = text.lower()
        if ch == 'no':
            print('Thanks for Using Me!')
            print('-'*50)
            break
        text = list(text)

        if text[-1] in key_values and n% 2 == 1:
            flag = text[-1]
            enc_order = data[flag]
            original = decrypt(text,enc_order,org_order)
            original= list(original)
            del original[-1]
            print()
            print(''.join(original))


        elif text[0] in key_values and n%2 == 0 :
            flag = text[0]
            enc_order = data[flag]
            original = decrypt(text,enc_order,org_order)
            original = list(original)
            del original[0]
            print()
            print(''.join(original))

        else:
            encrypt_text = data[key]

            cip = encrypt(text,encrypt_text, org_order)
            if len(cip) % 2 == 0 :
                cipher = cip + key
            else :
                cipher = key + cip 

            print()
            print(cipher)

if __name__ == '__main__':
    main()

