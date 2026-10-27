from fastapi import FastAPI,Path,HTTPException,Query
'''
Path function in FastApi

It is used to provide metadata,validation,rules and documentatins hints for path parameters in your API endpoints
Ex:
Title
Description

greater than
less than 
>=,<=
Min_length
Max_length
regex
'''

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


# dynamic route using path parameter
@app.get('/patient/{patient_id}')
def view_patient(patient_id:str=Path(...,description="ID of the patient in the DB",example='P001')): # ... means required field
    data = load_data()

    if patient_id in data: # it works as dictionary
        return data[patient_id]    

    raise HTTPException(status_code = 404 ,detail='Patient not Found')




# using query parameters route
# sort_order by heigth,weight,bmi

@app.get('/sort')
def sort_patient(sort_by:str=Query(...,description='Sort on the basis of height,weight or bmi'),order:str=Query('asc',description='Sort in asc or desc order')):

    valid_fields = ['height','weight','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400,detatil=f'Invalid field select from {valid_fields}')

    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,details='Invalid order select between asc and desc')

    data = load_data()

    sort_order = True if order == 'desc' else False 
    sorted_data = sorted(data.values(),key=lambda X:X.get(sort_by,0),reverse=sort_order)
    return sorted_data