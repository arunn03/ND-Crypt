from cryptography.fernet import Fernet
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilenames
import os
from datetime import datetime

en_key = open('hacker.png', 'rb').read()[-44:]

def encrypt(filepath):
    now = datetime.now()
    string = now.strftime("%d-%m-%Y %H:%M:%S")
    fernet = Fernet(en_key)
    if os.path.exists(filepath):
        with open(filepath, 'rb') as RF:
            enc_data = fernet.encrypt(RF.read())
        RF.close()
        with open(filepath, 'wb') as WF:
            WF.write(enc_data)
        WF.close()
    else:
        log = f'{string} : File path "{filepath}" does not exist'
        with open('log.txt', 'a') as f:
            f.write(log + '\n')
            print(log)
        f.close()

def decrypt(filepath):
    now = datetime.now()
    string = now.strftime("%d-%m-%Y %H:%M:%S")
    fernet = Fernet(en_key)
    if os.path.exists(filepath):
        with open(filepath, 'rb') as RF:
            dec_data = fernet.decrypt(RF.read())
        RF.close()
        with open(filepath, 'wb') as WF:
            WF.write(dec_data)
        WF.close()
    else:
        log = f'{string} : File path "{filepath}" does not exist'
        with open('log.txt', 'a') as f:
            f.write(log + '\n')
            print(log)
        f.close()

def select():
    global files
    try:
        files += askopenfilenames(initialdir='./', title='Select files',
                                 filetypes=(('All files', '*.*'), ))
        list_files.delete(0, END)
        for file in files:
            list_files.insert(END, file)
    except:
        pass

def start(event=None):
    now = datetime.now()
    string = now.strftime("%d-%m-%Y %H:%M:%S")
    temp = option.get()
    if temp in options:
        msg = "Do you want to execute this event?"
        win = messagebox.askyesno('Confirmation', msg)
        if win > 0:
            if temp == 'Encrypt':
                for file in files:
                    with open('log.txt', 'a') as f:
                        try:
                            encrypt(file)
                            log = f'{string} : "{file}" has been encrypted'
                            f.write(log + '\n')
                        except:
                            log = f'{string} : "{file}" cannot be encrypted'
                            f.write(log + '\n')
                    f.close()
                    print(log)
            else:
                for file in files:
                    with open('log.txt', 'a') as f:
                        try:
                            decrypt(file)
                            log = f'{string} : "{file}" has been decrypted'
                            f.write(log + '\n')
                        except:
                            log = f'{string} : "{file}" cannot be decrypted'
                            f.write(log + '\n')
                    f.close()
                    print(log)

def clear(event=None):
    list_files.delete(0, END)
    global files
    files = tuple()
    option.set('Select')

root = Tk()
root.title('ND Crypt')
root.geometry('391x324+450+150')
root.config(bg='white')
root.resizable(0, 0)

files = tuple()
option = StringVar()
option.set('Select')
options = ['Encrypt', 'Decrypt']

main_frame = Frame(root, bg='white')
main_frame.pack(padx=20, pady=20)

lbl_pmt = Label(main_frame, text="Select Files:", bg='white', font=('Helvetica', 10, 'bold'))
lbl_pmt.grid(row=0, column=0, padx=5)

btn_sel = ttk.Button(main_frame, text="Select", command=select)
btn_sel.grid(row=0, column=1, padx=5)

lbl_opt = Label(main_frame, text='Option:', bg='white', font=('Helvetica', 10, 'bold'))
lbl_opt.grid(row=0, column=2, padx=5)

combo_opt = ttk.Combobox(main_frame, textvariable=option, values=options, state='readonly',
                         width=10)
combo_opt.grid(row=0, column=3, padx=5)

list_frame = Frame(main_frame, bg='white')
list_frame.grid(row=1, column=0, columnspan=4, pady=15)

list_files = Listbox(list_frame, width=55, relief=FLAT)
list_files.pack(side=LEFT, fill='x')

yScroll = ttk.Scrollbar(list_frame, orient='vertical', command=list_files.yview)
yScroll.pack(side=RIGHT, fill='y')
list_files.configure(yscroll=yScroll.set)

btn_frame = Frame(root, bg='white')
btn_frame.pack(side=BOTTOM, pady=10)

lbl_msg = Label(root, text='All actions will be saved in log.txt', bg='white', fg='red',
                font=('Helvetica', 10, 'bold'))
lbl_msg.pack(side=BOTTOM)

btn_clear = ttk.Button(btn_frame, text='Clear', command=clear)
btn_clear.grid(row=0, column=0, padx=5)

btn_start = ttk.Button(btn_frame, text='Start', command=start)
btn_start.grid(row=0, column=1, padx=5)

root.bind('<F5>', clear)
root.bind('<Return>', start)
root.mainloop()
