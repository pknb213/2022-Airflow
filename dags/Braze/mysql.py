import aiomysql
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')


class MysqlMain():
    def __init__(self):
        pass

    async def create_pool(self):
        return await aiomysql.create_pool(
            host=os.getenv("INTERNAL_MYSQL_HOST"),
            port=int(os.getenv("INTERNAL_MYSQL_PORT")),
            user=os.getenv("INTERNAL_MYSQL_USER"),
            password=os.getenv("INTERNAL_MYSQL_PWD"),
            db=os.getenv("INTERNAL_MYSQL"),
            autocommit=True,
            minsize=1,
            maxsize=10
        )

    async def fetch_member(self, **kwargs):
        return [ # Todo: Dummy
            {"name": "mr.1", "age": 35, "address": "Africa"},
            {"name": "mr.2", "age": 21, "address": "Africa"},
            {"name": "mr.3", "age": 17, "address": "Seoul"},
            {"name": "mr.4", "age": 24, "address": "Japan"},
        ]
        # pool = await self.create_pool()
        # async with pool.acquire() as conn:
        #     async with conn.cursor() as cur:
        #         await cur.execute(f"""
        #             select * from member
        #             """)
        #         data = await cur.fetchall()
        #         if data is None:
        #             print("DB is Empty !!")
        #             return False
        #         print(f"DB Count: {len(data)}, \n Ex.[0]: {list(data[0])}\n Ex.[-1]: {list(data[-1])}")
        #         return data