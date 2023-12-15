from sqlalchemy import select
from celery_app import celery
from database import async_session_maker
from model import Notification


@celery.task()
def create_logfile(id: int, title: str, body: str):
    with open("notification.txt", "a") as file:
        file.write(f"{title}: {body}\n")

    async def process_notification():
        async with async_session_maker() as session:
            query = select(Notification).filter(Notification.id == id)
            result = await session.execute(query)
            notification = result.scalar()
            if notification:
                notification.is_sent = True
                await session.commit()

    import asyncio

    asyncio.run(process_notification())
