from fastapi import FastAPI
from app.models import Todo 
#Import the fastpi ule
app = FastAPI()
#Instantiate the fast api class
@app.get("/")
async def read_root():
    return {"message": "Hello World FUNCIONA? "}
#whatever method is below slash is handling the root request. Returns the json specified
\
todos = []
#Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}
#Get single todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"error": "Todo not found"}    
    return {"todos": todos}
#Create a todo
@app.post("/todos")#Que parametros le creo? Para que sea prolijo recibe direcmente el objeto
async def create_todos(todo: Todo): #Aca le creo que el todo como un objeto, pega uan restriccion ahi
    todos.append(todo)  # ✅
    return {"todos": "Todo created Successfully"}
#Update a todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_obj: Todo):#Le paso que id quiero cambiar apra ver le objeto que cambia y el objeto que tiene que pasar
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {"todo":todo}
    return {"todos": "No todos found to update"}
#Delete a todo
#Create a todo
@app.delete("/todos/{todo_id}")#Que parametros le creo? Para que sea prolijo recibe direcmente el objeto
async def delete_todo(todo_id: int): #Aca le creo que el todo como un objeto, pega uan restriccion ahi
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"todos": "Todo deleted Successfully"}
    return {"todos": "Todo not found"}