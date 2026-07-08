class UserRepository:
    def save(self, user):
        print(f"Saving {user.name} to Database")