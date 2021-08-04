from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create_users(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,  # этот фетч означает, что хотим забрать все данные
                      fetchval: bool = False,  # доставать одно значение
                      fetchrow: bool = False,  # данные в одной строке
                      execute: bool = False  # никакие данные возвращать не надо
                      ):

        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(55) NOT NULL,
        username varchar(55) NULL,
        telegram_id BIGINT NOT NULL UNIQUE,
        age varchar(55),
        sex VARCHAR(15)
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, full_name, username, telegram_id, age):
        sql = "INSERT INTO users (full_name, username, telegram_id, age) VALUES($1, $2, $3, $4) returning *"
        return await self.execute(sql, full_name, username, telegram_id, age, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE Users SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def update_user_fullname(self, full_name, age, telegram_id):
        sql = "UPDATE Users SET full_name=$1, age=$2 WHERE telegram_id=$3"
        return await self.execute(sql, full_name, age,telegram_id, execute=True)

    async def update_user_sex(self, sex, telegram_id):
        sql = "UPDATE Users SET sex=$1 WHERE telegram_id=$2"
        return await self.execute(sql, sex, telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    # async def update_user_email(self, email, telegram_id):
    #     sql = "UPDATE Users SET email=$1 where telegram_id=$2"
    #     return await self.execute(sql, email, telegram_id, execute=True)
    #
    # async def update_user_phone_number(self, phone_number, telegram_id):
    #     sql = "UPDATE Users SET phone_number=$1 where telegram_id=$2"
    #     return await self.execute(sql, phone_number, telegram_id, execute=True)

    # async def drop_users(self):
    #     await self.execute("DROP TABLE Users", execute=True)

    async def select_contacts(self, **kwargs):
        sql = "SELECT full_name, phone_number, email, username FROM Users"
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetch=True)

    async def select_full_name_id(self):
        sql = "SELECT full_name, telegram_id FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_full_name_all_users(self):
        sql = "SELECT full_name FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_all_telegram_id(self):
        sql = "SELECT telegram_id FROM Users"
        return await self.execute(sql, fetch=True)


##############################################################################################################################

class save_answer:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create_answer(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,  # этот фетч означает, что хотим забрать все данные
                      fetchval: bool = False,  # доставать одно значение
                      fetchrow: bool = False,  # данные в одной строке
                      execute: bool = False  # никакие данные возвращать не надо
                      ):

        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_answer(self):
        sql = """
        CREATE TABLE IF NOT EXISTS users_answer (
        id SERIAL PRIMARY KEY,
        username varchar(55) NULL,
        from_user varchar(250),
        from_bot varchar(250)

        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_line(self, username,  from_bot, from_user):
        sql = "INSERT INTO users_answer (username,  from_bot, from_user) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, username,  from_bot, from_user, fetchrow=True)
