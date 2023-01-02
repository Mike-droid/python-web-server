import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/')
def get_list():
    return [1, 2, 3]


@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
        <h1>This is the contact page</h1>
        <p>¿Qué te parece?<p>
    """


def run():
    store.get_categories()


if __name__ == '__main__':
    run()
