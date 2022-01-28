class UserDto:
    """User Dto"""

    id: int
    username: str
    first_name: str
    last_name: str
    email: str
    birthdate: str
    gender: str
    password: str

    def __init__(self, username: str, first_name: str,  last_name: str, email: str, birthdate: str, gender: str, password: str , _id=None):
        """[summary]

        Args:
            _id ([type], optional): [description]. Defaults to user id.
            username (str): [ username of user ]
            first_name (str): [ first name of user ]
            last_name (str): [ last name of user ]

        """
        self.id = _id if _id is not None else 0
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.birthdate = birthdate
        self.gender = gender
        self.password = password
