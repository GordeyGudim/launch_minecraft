
import subprocess
import json
with open('users_data.json', 'r') as users_file:
    dict_users = json.load(users_file)  
def update_count(entered_login):
    dict_users[entered_login]['count']+=1
    with open('users_data.json', 'w') as users_file:
        json.dump(dict_users, users_file, indent = 4)
    return dict_users[entered_login]['count']

def launch_minecraft():
    subprocess.Popen('cd ~/Documents/;cd Minecraft; ./Minecraft.sh', shell = True)
def creat_user(dict_users=dict_users):
    user=input('Enter Your Login: ')
    login = user
    password= input('Enter Your Password: ')
    dict_users[user] = {'login':login, 'password':password, 'count':0}
    with open('password.json', 'w') as users_file:
        json.dump(dict_users, users_file, indent = 4)

def check_admin(list_commands = ['/info', '/exit'],command = None, admin_login = None,admin_password=None):
    while admin_login != dict_users['admin']['login'] and admin_password != dict_users['admin']['password']:
        admin_login = input('Enter admin login: ')
        admin_password = input('Enter admin password: ')
        command = input('enter your command: ')
        for i in list_commands:
            if i == '/info' and i == command:
                print(json.dumps(dict_users, indent = 4))
            if i == '/exit' and i == command:
                controle_password()
def controle_password(entered_login = None, entered_password = None):    
    list_usesrs = [i for i in dict_users.keys()]
    signInOrRegistration = input('Press "e" for log in/ Press "n" for creat new password: ')
    if signInOrRegistration == 'n':
        creat_user()
    if signInOrRegistration == 'e':
        while entered_login not in list_usesrs:
            entered_login = input('Enter your login: ')
        while entered_password != dict_users[entered_login]['password']:
            entered_password = input('Enter your password: ')
        
        count_signIn = update_count(entered_login)
        users_answer = input(f'You play {count_signIn} time! Press "ok" to continue: ')
        if users_answer == 'ok':          
            launch_minecraft()
    if signInOrRegistration == 'admin':
        check_admin()
if dict_users == {}:
    creat_user(dict_users)
    controle_password()
else:
    controle_password()



