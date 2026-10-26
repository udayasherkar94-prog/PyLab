from fastapi import FastAPI
import json

# Object of FastAPI()
app = FastAPI()


# helper function 

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)

    return data    



# route define '/' listen get method
@app.get("/")
def hello():
    return {'message':"Patient Management System API"}



@app.get('/about')
def about():
    return {'Message':'A fully Functional API to manage your patient records'}


# view all the paients data 

@app.get('/view')
def view():
    data = load_data()
    return data