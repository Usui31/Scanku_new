from fastapi import FastAPI, Request, Depends
#File, UploadFile, BackgroundTasks
from starlette.templating import Jinja2Templates
#from starlette.websockets import WebSocket
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
# from database import SessionLocal
# from sqlalchemy.orm import Session
# from deta import Deta

# deta = Deta()

# users = deta.Base("ScanKuy")
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

class User(BaseModel):
    id: int

class Image(BaseModel):
    image_id : int
    name : str
    format : str

class Scanner(BaseModel):
    scan_id : int
    user_id : int
    image_id : int
    data_time : str

class text(BaseModel):
    text_id : int
    scan_id : int
    words_count : int
    text : str

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about_us", response_class=HTMLResponse)
async def about_us(request: Request):
    return templates.TemplateResponse("about-us.html", {"request": request})

# @app.post("/users", status_code=201)
# def create_user(user : User):
#     u = users.put(user.dict())
#     return next(users.fetch())

# @app.get("/users")
# def list_user():
#     us = next(users.fetch())
#     return us

# @app.get("/users/<keys>")
# def create_iser(key):
#     us = users.get(key)
#     return us

# @app.get("/users")
# def list_user():
#     res = users.fetch
#     all_item = res.items
#     while res.last:
#         res = users.fetch(last=res.last)
#         all_item += res.items
#     return all_item


# @app.post("/api/v1/extract_text")
# async def extract_text(image: UploadFile = File(...), db:Session=Depends(get_db)):
#     file_format = image.filename.split('.')
#     try:
#         db.execute("INSERT INTO image VALUES(null, '%s', '%s')"%(file_format[0], file_format[1]))
#         db.commit()
#         db.close()
#     except:
#         return "ERROR"
    
#     try:

#         db.execute("INSERT INTO user_scankuy VALUES(null)")
#         db.commit()
#         db.close()
#     except:
#         return "EROR"

#     hasil = db.execute("SELECT User_ID from user_scankuy ORDER BY User_ID DESC").fetchone()
#     for i in hasil:
#         user_id = i
#         db.close()
#         hasil_image_id = db.execute("SELECT Image_ID from image ORDER BY Image_ID DESC").fetchone()
#         for j in hasil_image_id:
#             image_id = j
#             db.execute("INSERT INTO scanner VALUES(null, %d, %d, null, null)"%(image_id, user_id))
#             db.commit()
#             db.close()
    
#     hasil_scan_id = db.execute("SELECT Scan_ID from text_digital ORDER BY Scan_ID DESC").fetchone()
#     for k in hasil_scan_id:
#         scan_id = k
#         db.execute("INSERT INTO text_digital VALUES(null, %d, '%s')"%(scan_id, text))
#         db.commit()
#         db.close()
#     return {"filename": file_format[0], "format": file_format[1], "text": text}