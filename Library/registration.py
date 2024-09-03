from Library.library import Library
from Library.user import User


class Registration:

    def add_user(self, user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library):

        for user_record in library.user_records:
            if user_record.user_id == user.user_id:
                library.user_records.remove(user)
                return

        return "We could not find such user to remove!"

    def change_username(self, user_id, new_username, library: Library):

        for user in library.user_records:
            if user_id == user.user_id:
                if user.username != new_username:
                    old_username = user.username
                    user.username = new_username
                    for username in library.rented_books:
                        if username == old_username:
                            library.rented_books[old_username] = library.rented_books[new_username]
                    return f"Username successfully changed to: {new_username} for user id: {user_id}"
                else:
                    return f"Please check again the provided username - it should be different than the username " \
                           f"used so far!"
            else:
                return f"There is no user with id = {user_id}!"
