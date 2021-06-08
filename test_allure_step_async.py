import asyncio

import allure
import pytest


@pytest.mark.asyncio
@allure.title('Test')
async def test_async(client):
    await asyncio.gather(*(client.post(i) for i in range(1, 10)))
