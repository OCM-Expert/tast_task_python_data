import json
from fastapi import FastAPI
from playhouse.shortcuts import model_to_dict
from db import Doc

app = FastAPI()


@app.get('/api/')
def get_info(city: str):
    """
    :param city: str - город, передаваемый в get-запросе
    :return: json с информацией по всем записям по совпадению города
    """
    all_models = []
    for item in Doc.select().where(Doc.organization == city):
        model_obj = model_to_dict(item)
        all_models.append(model_obj)
    return json.dumps(all_models, ensure_ascii=False).encode('utf8').decode()
