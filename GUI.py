# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 20:18:16 2020

@author: Asus
"""

import pandas as pd
import tkinter as tk

encryptionkey = pd.read_csv(r'decodekeynew.csv',
                            sep=',', names=['Character', 'Byte'], header=None, skiprows=[0]) #instead of just the file name , mention  "location of your hardrive\decodekeynew.csv

df = pd.DataFrame(data=encryptionkey)

df['Character'] = df['Character'].astype(str)
df['Byte'] = df['Byte'].astype(str)

def split(message):
    return [char for char in message]

"""my_message = 'My secret'
message_split = split(my_message)

print(message_split) #printing the split message"""




#Encrypting the message

def code_message(message):
    message_split = [char for char in message]
    coded_message = ""

    for i in range(len(message_split)):
        j = message_split[i]
        try:
            coded_char = encryptionkey.loc[encryptionkey['Character'] == j, 'Byte'].iloc[0]
          
        except:
            print('Character not recognized')
            coded_char = '@@@'
    
        coded_message = coded_message + coded_char
    "print(type(coded_char))"
    return coded_message

"""print('Your coded message:', code_message(), '\n')
coded_message = code_message()"""


#Decrypting the message 

def decode_message(message):
    new_word = ''
    decoded_message = []

    for i in range(0, len(message), 2):
        j = message[i:i + 2]
        index_nb = df[df.eq(j).any(1)]

        df2 = index_nb['Character'].tolist()

        s = [str(x) for x in df2]

        decoded_message = decoded_message + s

    new_word = ''.join(decoded_message)

    return new_word

"""coded_message_str = str(coded_message)
print('Your decoded message:', decode_message(coded_message_str))"""

#GUI for Character-Byte Encryptor-Decryptor program


def GUI():
    def getResult():
        choice = v.get()
        if choice == 'e':

            x1 = entry1.get()
            label1['text'] = code_message(x1)
            canvas1.create_window(150, 200, window=label1)

        else:
            x1 = entry1.get()
            label1['text'] = decode_message(x1)
            canvas1.create_window(150, 200, window=label1)

    root = tk.Tk()
    root.title('Byte Encryptor ')
    root.minsize(width=300, height=230)
    canvas1 = tk.Canvas(root, width=300, height=230)
    canvas1.pack()
    entry1 = tk.Entry(root)
    canvas1.create_window(150, 120, window=entry1)
    label1 = tk.Label()
    button1 = tk.Button(text='Submit', command=getResult)
    canvas1.create_window(150, 160, window=button1)

    v = tk.StringVar()
    v.set("e")

    b = tk.Radiobutton(root, text='Encrypt', variable=v, value='e')
    canvas1.create_window(150, 45, window=b)

    b2 = tk.Radiobutton(root, text='Decrypt', variable=v, value='d')
    canvas1.create_window(150, 70, window=b2)

    root.mainloop()


GUI()






