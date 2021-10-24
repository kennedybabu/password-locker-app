class User:
    '''
    class that generates a new instance of user
    '''

    user_list =[]

    def __init__(self, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        '''
        save_user method saves a user object into a user_list array
        '''
        User.user_list.append(self)

    @classmethod
    def display_users(cls):
        '''
        Function that returns the user_list array
        '''

        return cls.user_list

    @classmethod
    def find_by_username(cls, username):
        '''
        Method that takes in a number and returns a user that matches the username
        
        Args: 
            username: username object that matches the username
        Returns:
            User that matches the username
        '''

        for user in cls.user_list:
            if user.first_name == username:
                return user

