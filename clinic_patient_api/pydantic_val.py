# pydantic

from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional

# validation on Data
class Patient(BaseModel):
    # by default all the fields are required
    # if one is miss to pass then object of this class will not create

    # to avoid this use Optional[type description] but it should be a value which is None
    name: str
    age: int
    email:EmailStr # build-in Email validation  custom datype
    Linkedin:AnyUrl # for Url validation must include http and .com or 
    weight:float= Field(gt>0) # apply contraints
    married:bool
    allergies:Optional[List[str]] = None # two level validation in list every element should be string dtype
    contact_details :Dict[str,str]


patient_info = {"name":"nitish","age":30,"weight":67,"married":1,"allergies":['pollen','dust'],"contact_details":{'email':'abc@gmail.com','phone':"006787970"}}
# if age : "thirty" : pydantic_core._pydantic_core.ValidationError: 1 validation error for Patient
# age Input should be a valid integer,

# object
patient1 = Patient(**patient_info) # unlock the dictionary using **






# insert 
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)


insert_patient_data(patient1)



# update
def update_patient_data(patient:Patient):
    patient.name = input("enter the name:")
    patient.age = int(input("enter the age"))

    print(patient.name)
    print(patient.age)


update_patient_data(patient1)

