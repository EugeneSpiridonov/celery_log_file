from celery import Celery

# from kombu.serialization import register

# register(
#     "asynctojson",
#     lambda x: x,
#     lambda x: x,
#     content_type="application/x-asynctojson",
#     content_encoding="utf-8",
# )

celery = Celery(
    "tasks",
    broker="redis://localhost:6379",
    backend="redis://localhost:6379/0",
    include=["tasks"],
    # accept_content=[
    #     "json",
    #     "asynctojson",
    # ],  # Добавление asynctojson в список допустимых форматов
)
