from dataclasses import dataclass, field
from json import dumps

import allure
from aiohttp import ClientSession
from pydantic import BaseModel


class Post(BaseModel):
    userId: str
    id: str = None
    title: str = ''
    body: str = ''


@dataclass
class Client:
    base_url: str = 'https://jsonplaceholder.typicode.com'
    session: ClientSession = field(default_factory=ClientSession)

    async def post(self, id_):
        url = f'{self.base_url}/posts/{id_}'
        with allure.step(f'GET {url}'):
            response = await self.session.get(
                url,
                ssl=False
            )
            result = await response.json()
            allure.attach(
                dumps(result, indent=4, ensure_ascii=False),
                'Result',
                attachment_type=allure.attachment_type.JSON
            )

        return Post.parse_obj(result)
