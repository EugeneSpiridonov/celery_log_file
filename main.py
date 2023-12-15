from fastapi import FastAPI, HTTPException
from database import async_session_maker
from model import Notification
from tasks import create_logfile

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/send")
async def send_me_task(title: str, body: str):
    try:
        async with async_session_maker() as session:
            new_notification = Notification(title=title, body=body)
            session.add(new_notification)
            await session.commit()  # Явно завершаем транзакцию
            create_logfile.apply_async(
                args=(
                    new_notification.id,
                    new_notification.title,
                    new_notification.body,
                )
            )
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Transaction failed: {e}")

    return {"message": "Запись прошла успешно!"}
