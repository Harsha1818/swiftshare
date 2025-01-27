from celery import Celery

app = Celery("tasks", broker="redis://localhost:6379/0")

@app.task
def process_file(file_name):
    # File processing logic
    return f"File {file_name} processed successfully."
