from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):

    id : int
    name : str 
    surname : str
    url : str
    age : int
    
users_list = [User(id = 1, name = "Brais", surname = "Moure", url = "https://moure.dev", age =35),
         User(id = 2, name = "Moure", surname = "Dev", url = "https://mouredev.com", age = 35),
         User(id = 3, name = "Juanj", surname = "Sanchez", url = "https://juanjsanchez.dev", age = 39)]



@app.get("/usersjson")
async def usersjson():
    return [{"name" : "Brais", "surname" : "moure", "url" : "https://moure.dev", "age" : 35},
            {"name" : "Moure", "surname" : "Dev", "url" : "https://mouredev.com", "age" : 35},
            {"name" : "Juanj", "surname" : "Sanchez", "url" : "https://juanjsanchez.dev", "age" : 39}]


@app.get("/users/")
async def users():
    return users_list

# Path    
@app.get("/user/{id}")
async def user(id : int):
    return search_user(id)
    

# Query
@app.get("/user/")
async def user(id : int):
    return search_user(id)

    
@app.post("/user/")
async def user(user : User):
    if type(search_user(user.id)) == User:
        return {"msg" : "El usuario existe"}
    else: 
        users_list.append(user)
        return user


@app.put("/user/")
async def user(user : User):
    
    found = False
    
    for index, user_saved in enumerate(users_list):
        if user_saved.id == user.id:
            users_list[index] = user
            found = True
            
    if not found:
        return {"error" : "No se ha actualizado el usuario"}
    else:
        return user 

@app.delete("/user/{id}")
async def user(id : int):

    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
            
    if not found:
        return {"error" : "No se ha eliminado el usuario"}


def search_user(id : int):
    users = filter(lambda user : user.id == id, users_list)
    
    try:
        return list(users)[0]
    except:
        return {"error" : "No se ha encontrado el usuario"} 
    
