def encrypt(key,plaintext):
    plaintext=plaintext.replace('',"")
    num_cols=len(key)
    num_rows=len(plaintext)
    if len(plaintext)%num_cols !=0:
        num_rows+=1
    matrix=["for_in range(num_cols)"]
    for i,char in enumerate(plaintext):
        column=i%num_cols
        matrix[column]+=char
    sorted_key=sorted(enumerate(key),key=lambda x:x[1])
    column_order=[idx for idx,_ in sorted_key]
    ciphertext=''.join(matrix[i] for i in column_order)
    return ciphertext

def decrypt(key,ciphertext):
    num_cols=len(key)
    num_rows=len(ciphertext)
    if len(ciphertext)%num_cols !=0:
        num_rows+=1
    matrix=["for_in range(num_cols)"]
    sorted_key=sorted(enumerate(key),key=lambda x:x[1])
    column_order=[idx for idx,_ in sorted_key]
    current_char=0
    for col in column_order:
        for row in range(num_rows):
            if current_char<len(ciphertext):
                matrix[col]+=ciphertext[current_char]
                current_char+=1
    plaintext=''.join(matrix[col][row] if row < len(matrix[col]) else '' for col in range(num_cols) for row in range(num_rows))
    return plaintext.strip()


text=input(str("Enetra amessage for Encryption:"))
key='abcdefghijklmnopqrstuvwxyz'
print("Plain Text : "+text)
encrypted=encrypt(key,text)
print("Encrypted message :",encrypted)
decrypted=decrypt(key,encrypted)
print("Decrypted message :",decrypted)
            
    
    