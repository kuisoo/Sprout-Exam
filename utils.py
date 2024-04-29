import json
from fastapi import HTTPException
from schema import * 

EMPLOYEES_TABLE = "data/employees.json"
EMPLOYEE_TYPE_TABLE = "data/employee_type.json"
EMPLOYEE_BENEFITS_TABLE = "data/benefits.json"

def load_employee_database():
    try:
        with open(EMPLOYEES_TABLE, 'r') as file:
            items = json.load(file)
    except FileNotFoundError:
        items = []
    return items

def update_employee_db(data):
    with open(EMPLOYEES_TABLE, 'w') as file:
        json.dump(data, file, indent=2)

def load_employee_types():
    try:
        with open(EMPLOYEE_TYPE_TABLE, 'r') as file:
            items = json.load(file)
    except FileNotFoundError:
        items = ["regular" , "contractual"]
    return items

def load_employee_benefits():
    try:
        with open(EMPLOYEE_BENEFITS_TABLE, 'r') as file:
            items = json.load(file)
    except FileNotFoundError:
        items = ["HMO" , "13th month pay"]
    return items

def validate_employee(employee: Employee):
    types = load_employee_types()
    benefits = load_employee_benefits()
    
    if employee.type is not None and employee.type not in types:
        raise HTTPException(status_code=400, detail="Invalid field value provided")
    
    if employee.benefits is not None:
        for item in employee.benefits:
            if item not in benefits:
                raise HTTPException(status_code=400, detail="Invalid field value provided")
            
    if employee.type == "regular":
        if employee.number_of_leaves is None:
            raise HTTPException(status_code=400, detail="Missing required field")
        if employee.benefits is None:
            raise HTTPException(status_code=400, detail="Missing required field")
        if employee.contract_end_date is not None:
            raise HTTPException(status_code=401, detail="Bad request")
        if employee.project is not None:
            raise HTTPException(status_code=402, detail="Bad request")

    if employee.type == "contractual":
        if employee.number_of_leaves is not None:
            raise HTTPException(status_code=400, detail="Bad request")
        if employee.benefits is not None:
            raise HTTPException(status_code=400, detail="Bad request")
        if employee.contract_end_date is None:
            raise HTTPException(status_code=400, detail="Missing required field")
        if employee.project is None:
            raise HTTPException(status_code=400, detail="Missing required field")

    return



