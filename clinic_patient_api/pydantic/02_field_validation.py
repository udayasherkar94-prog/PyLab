from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):

    name:str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details : Dict[str,str]


    # custom validation function 

    @field_validator('email',mode='after') # by default mode is after which gives the value after the typer corsion
                                           # we cahnge to 'before' it pass the value before type corsion if value not maching accurate data type it throughs an error


    @classmethod
    def check_email_domain(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split("@")[-1].lower()

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value


    # name in upper

    @field_validator('name')
    @classmethod
    def transform_name(cls,value):

        return value.upper()



    # for age
    @field_validator('age',mode='after')
    @classmethod
    def age_validator(cls,value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("age must be in between 0 to 100") 



    # custom model validator if age > 65 there must be emergency number in contact details 
    # @model_validator(mode='after')
    #old way
    # def validate_emergency_contact(cls,model):

    #     if model.age > 65 and 'emergency' not in model.contact_details:
    #         raise ValueError("Patient older than 65 must have an emergency number")
    #     return model
    
    # new way
    @model_validator(mode='after')
    def validate_emergency_contact(self):
        if self.age > 60 and 'emergency' not in self.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return self

        
    
patient_info = {"name":"nitish","age":"30","weight":67,"married":1,"email":"abc@icici.com","allergies":['pollen','dust'],"contact_details":{'phone':"006787970"}}
                                # if "age":"30" it throughs an error if mode is "before"
                                # if "age":"30" and mode is "after" it works because type cursion happens it conver to str to int and then pass
    # object
patient1 = Patient(**patient_info) # unpack the dictionary using **




# insert 
def insert_patient_data(patient:Patient):
    print("Name:",patient.name)
    print("Age:",patient.age)
    print("Is Married:",patient.married)
    print("allergies:",patient.allergies)
    print("contact details:",patient.contact_details)
    print("email:",patient.email)
    


insert_patient_data(patient1)


