from pydantic import BaseModel, Field, EmailStr

class Employee(BaseModel):
    employee_id: int | None = None
    first_name: str = Field(min_length=2)
    last_name: str = Field(min_length=2)
    email: EmailStr
    type: str
    number_of_leaves: int | None = Field(None, gt=0)    #Only for regular employees
    benefits: list | None = None                 #Only for regular employees
    contract_end_date: str | None = None         #Only for contractual employees
    project: str | None = None                   #Only for contractual employees