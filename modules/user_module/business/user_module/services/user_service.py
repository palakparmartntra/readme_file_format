from adapters.db_adapters.db_query import QueryExecuter
from pypika import Table, PostgreSQLQuery
from modules.user_module.business.user_module.Dtos.user_dto import UserDto
from adapters.db_adapters.db_exeptions import CustomExeption
from typing import List, Set


class UserService:
    def __init__(self, query: QueryExecuter):
        """

        @rtype: object
        """
        self.query = query
        self.Table = Table
        self.Query = PostgreSQLQuery

    def register(self, data: UserDto) -> dict[UserDto]:
        """

        @param data:
        @type data:
        """
        table = self.Table("accounts_user")
        q = (
            self.Query.into(table)
                .columns("username", "first_name", "last_name", "email", "birthdate", "gender", "password", "is_superuser", "is_staff", "is_active", "date_joined")
                .insert(data.username, data.first_name, data.last_name, data.email, data.birthdate, data.gender, data.password, True, True, True, '2022-04-04 05:30:00+5:30')
        )
        try:
            self.query.execute(q.get_sql())
        except CustomExeption:
            return {"data": "registered"}

    def get_users(self) -> List[UserDto]:
        """ get users list """
        table = self.Table("accounts_user")
        q = self.Query.from_(table).select("*").where(table.username == 'shlokp')
        return self.query.execute(q.get_sql())

    def login_user(self, data: UserDto) -> Set[str]:
        """ for login """
        table = self.Table("accounts_user")
        q = self.Query.from_(table).select(table.username, table.password)
        a = self.query.execute(q.get_sql())
        b = a.fetchone()
        try:
            if b.username == data.username and b.password == data.password:
                return {" login successfully."}
        except CustomExeption:
            return {" your credentials are not valid."}
