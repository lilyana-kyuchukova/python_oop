import re


class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @username.setter
    def username(self, value: str):
        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @password.setter
    def password(self, value: str):
        # value.lower == value True
        # [l for l in value if l.isdigit()] True
        if len(value) >= 8 and re.search(r"\d+", value) and re.search(r"[A-Z]+", value):
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        s = ["*" for st in range(len(self.password))]
        return f"You have a profile with username: \"{self.username}\" and password: {''.join(s)}"

        # return f"You have a profile with username: \"{self.username}\" and password: {'*' * len(password)}"


# profile_with_invalid_password = Profile('My_username', 'My-password')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
profile_with_invalid_username = Profile('Too_long_username', 'Any')
