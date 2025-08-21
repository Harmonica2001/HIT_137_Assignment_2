enc_count={}
dec_count={}
enc_map={}

def encryption(shift1,shift2):
    with open('raw_text.txt', 'r', encoding='utf-8') as file_obj:
        with open('encrypted_text.txt', 'w', encoding='utf-8') as write_file:
        
            for n in file_obj.read():
                if (n.islower()==True) &  ("a"<=n<="m"):    
                    shift_amount=shift1*shift2
                    shifted_value=ord(n) + shift_amount
                    final_value=chr(shifted_value)                
                elif (n.islower()==True) &  ("n"<=n<="z"):
                    shift_amount=shift1 + shift2
                    shifted_value=ord(n) - shift_amount
                    final_value=chr(shifted_value)
                elif (n.isupper()==True) &  ("A"<=n<="M"):
                    shifted_value=ord(n) - shift1 
                    final_value=chr(shifted_value)                
                elif (n.isupper()==True) &  ("N"<=n<="Z"):
                    shift_amount=shift2**2
                    shifted_value=ord(n) + shift_amount 
                    final_value=chr(shifted_value)
                else:
                    final_value=n    
                #calculates how many times 'final_value' appears and assigns it to count
                count = enc_count.get(final_value, 0) + 1
                #adds entries to a dictionary called enc_count, where 'final_value' is the key and the 'count' is the value
                enc_count[final_value] = count
                #creates a key value for the encryption map dictionary in the format x# where x is the final_value and # is the count
                map_key = f'{final_value}{count}'
                #adds entries to encryption map where the map_key is the key and the original value 'n' is the value
                enc_map[map_key] = n
                write_file.write(final_value)
           
        return enc_map
 

def comparing():
    with open('raw_text.txt', 'r', encoding='utf-8') as file_obj_1:
        with open('decrypted_text.txt', 'r', encoding='utf-8') as file_obj_2:
            if file_obj_1.read()==file_obj_2.read():
                print("Decryption successfull")
            else:
                print("Decryption failed")


def decryption(enc_map):
    with open('encrypted_text.txt', 'r', encoding='utf-8') as file_obj:
        with open('decrypted_text.txt', 'w', encoding='utf-8') as write_file:
            for n in file_obj.read():
                #calculates how many times the character being decrypted appears in the file and assigns it to count
                count = dec_count.get(n, 0) + 1
                #adds entries to a dictionary dec_count where the key is the encrypted character being decrypted and the value is the count
                dec_count[n] = count
                #creates a key identical to keys in enc_map
                dec_key = f'{n}{count}'
                #searches for the keys in enc_map and writes the corresponding value to the decypted_text file
                write_file.write(enc_map.get(dec_key, n))


       
value_one=int(input("Please enter a number between 1 to 9 :"))
value_two=int(input("Please enter a number between 1 to 9 :"))
#calling encryption function
encryption(value_one,value_two)
#calling decryption function
decryption(enc_map)
#comparing the rat_text and decrpyted text
comparing()
       


