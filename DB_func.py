import csv

class user:
    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance

def load_db(load_to):
    with open('users.csv','r') as db_r:
        load_from_db = csv.reader(db_r)
        for line in load_from_db:
            if not len(line)==0:
                new_user = user(line[0],line[1],int(line[2]))
                load_to.append(new_user)
    return load_to


def save_db(save_to):
    with open('users.csv','w',newline='') as db_s:
        write_to_db = csv.writer(db_s,delimiter=',')
        for i in range(len(save_to)):
            data_line = save_to[i].username, save_to[i].password, save_to[i].balance
            write_to_db.writerow(data_line)

user1 = user('kri','123',500)
user2 = user('geir','456',6000)
user3 = user('kasp','666',900)
test_list=[user1,user2,user3]

empty_list = []
load_db(empty_list)
