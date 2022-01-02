listOfUsers = []

class user_management:

    def add_user(name, role, email, password):
        listOfUsers.append([name, role, email, password])


    def check_user (email,password): # check if user and password are correct

        for i in range(0,len(listOfUsers)):
            if listOfUsers[i][2] == email:
                if listOfUsers[i][3] == password:
                    return True
                else:
                    return False
            else:
                return False


