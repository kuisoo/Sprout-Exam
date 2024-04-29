from fastapi import APIRouter, HTTPException, Depends
from fastapi_pagination import Page, paginate
from fastapi.security import OAuth2PasswordBearer
from utils import *
from schema import *

oauth_scheme = OAuth2PasswordBearer(tokenUrl='token')
router = APIRouter(prefix="/employees",dependencies=[Depends(oauth_scheme)])

@router.get("/types")
async def get_employee_types():
    items = load_employee_types()
    return items

@router.get("/benefits")
async def get_employee_benefits():
    items = load_employee_benefits()
    return items

#Fetch all the employees
@router.get("/")
async def get_all_employees() -> Page[Employee]:
    items = load_employee_database()
    return paginate(items)

#Fetch employee with the corresponding employee_id
@router.get("/view/{employee_id}")
async def get_employee(employee_id: int):
    items = load_employee_database()
    employee =  [x for x in items if x['employee_id'] == employee_id]

    if employee == []:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return employee[0]

#Edit employee with the corresponding employee_id
@router.put("/edit")
async def edit_employee(employee: Employee):
    validate_employee(employee)
    items = load_employee_database()
    employee_index = None

    for index, i in enumerate(items):
        if i['employee_id'] == employee.employee_id:
            employee_index = index
            break 

    if employee_index is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    items[employee_index] = employee.model_dump() 
    update_employee_db(items)
    return items[employee_index]

#Add new employee
@router.post("/add")
async def add_employee(employee: Employee):
    items = load_employee_database()
    validate_employee(employee)
    try:
        employee.employee_id = max(items, key=lambda ev: ev['employee_id'])["employee_id"] + 1
    except ValueError:
        employee.employee_id = 1

    items.append(employee.model_dump())
    update_employee_db(items)
    return employee

#Delete employee with the corresponding employee_id
@router.delete("/delete/{employee_id}")
async def delete_employee(employee_id: int):
    items = load_employee_database()
    employee_index = None
    employee = None

    for index, i in enumerate(items):
        if i['employee_id'] == employee_id:
            employee_index = index
            employee = i
            break

    if employee_index is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    del items[employee_index]
    update_employee_db(items)
    return employee
