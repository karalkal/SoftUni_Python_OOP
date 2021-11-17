import project.user


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}  # authors: str and the books available (list)
        self.rented_books = {}  # {usernames: {book names: days to return}}

    def add_user(self, user: project.user.User):
        if user not in self.user_records:
            self.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: project.user.User):
        if user not in self.user_records:
            return f"We could not find such user to remove!"
        else:
            self.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str):
        for user in self.user_records:
            if user.user_id == user_id:
                if user.username == new_username:
                    return "Please check again the provided username - it should be different than the username used so far!"
                else:
                    amend_at_this_index = self.user_records.index(user)
                    self.user_records[amend_at_this_index] = project.user.User.__init__(self, user.user_id, new_username)
                    return f"Username successfully changed to: {new_username} for userid: {user.user_id}"
            return f"There is no user with id = {user_id}!"