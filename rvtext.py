import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tabulate import tabulate


class Contact:
    def __init__(self, idname, comment):
        self.id = idname
        self.comment = comment

    def print_info(self):

        dataname = ['매장관리명', '사장님댓글내용']
        datac = ['평점5점댓글']
        commentid = [self.id]
        commentdata = [self.comment]
        commentout = pd.DataFrame([commentid, commentdata], index=dataname, columns=datac)
        print(tabulate(commentout, showindex=False, headers=commentout.columns))

        print(commentout.iloc[1,0])

def set_contact():
    idname = input("관리매장ID : ")
    comment = input("사장님댓글 : ")
    contact = Contact(idname, comment)
    return contact

def print_menu():
    print("1. 사장님댓글 입력")
    print("2. 댓글 출력")
    print("3. 댓글 삭제")
    print("4. 저장 & 종료")
    menu = input("메뉴선택 : ")
    return int(menu)

def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

def delete_contact(contact_list, idname):
    for i, contact in enumerate(contact_list):
        if contact.idname == idname:
            del contact_list[i]

def store_contact(contact_list):
    f = open("comment_db.txt", "wt")
    for contact in contact_list:
        f.write(contact.id + '\n')
        f.write(contact.comment + '\n')
    f.close()

def load_contact(contact_list):
    f = open("comment_db.txt", "rt")
    lines = f.readlines()
    num = len(lines) / 2
    num = int(num)

    for i in range(num):
        idname = lines[2*i].rstrip('\n')
        comment = lines[2*i+1].rstrip('\n')
        contact = Contact(idname, comment)
        contact_list.append(contact)
    f.close()

def run():
    contact_list = []
    load_contact(contact_list)
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            idname = input("삭제할ID내용 : ")
            delete_contact(contact_list, idname)
        elif menu == 4:
            store_contact(contact_list)
            break


if __name__ == "__main__":
    run()