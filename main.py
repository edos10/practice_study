from redis import Redis
from fastapi import FastAPI, Response
from string import ascii_letters, digits
from random import choice


app = FastAPI()
redis = Redis(port=6379, host='127.0.0.1')
gen_rand_symbols = ascii_letters + digits
print(gen_rand_symbols)
len_token = 10


@app.post("/create")
def create(url: str, response: Response):
    encode_url = ''.join([choice(gen_rand_symbols) for _ in range(len_token)])
    redis.set(encode_url, url)
    response.status_code = 201
    return {"id": encode_url}


@app.get("/link/{id}")
def link(id: str, response: Response):
    url = redis.get(id)
    if not url:
        response.status_code = 404
        return {"error": "Id of URL isn't found, try again"}
    return {"url": url}
