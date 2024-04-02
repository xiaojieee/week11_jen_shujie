from datetime import datetime, timedelta


def create_collection_time():
    current_time = datetime.now()
    add_time = current_time + timedelta(minutes=30)
    collection_time = add_time.strftime("%H:%M")

    return collection_time