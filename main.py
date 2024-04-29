from fastapi import FastAPI,HTTPException, Depends
from routers import employee
from fastapi_pagination import add_pagination
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()
app.include_router(employee.router)
add_pagination(app)

oauth_scheme = OAuth2PasswordBearer(tokenUrl='token')

#For simplicity no password encryption done
@app.post("/token")
async def create_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != "admin":
        raise HTTPException(status_code=401, detail="Invalid username or password")
    if form_data.password != "password":
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"access_token" : form_data.username + 'token'}

@app.get("/")
def index(token: str = Depends(oauth_scheme)):
    return {"token" : token}