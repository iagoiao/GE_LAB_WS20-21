
#Global values
users_list = ['Bob','Alice']
passwords_list = ['123','321']


def check_user (username,password):# check if user provided a known password

    if username in users_list:
        index = users_list.index(username)
        
        if passwords_list[index] == password:

            return True
 
    return False



def add_user (username,password): # Add user to list

    users_list.append(username)
    passwords_list.append(password)
    return True
    


