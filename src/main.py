from fastapi import FastAPI
from database import *
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, Body
from fastapi.responses import JSONResponse, FileResponse
 
 
Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@app.get("/")
def main():
    return FileResponse("public/index.html")

 
@app.get("/api/articles")
def get_articles(db: Session = Depends(get_db)):
    return db.query(Articles).all()


@app.get("/api/articles/{id}")
def get_article(id, db: Session = Depends(get_db)):
    article = db.query(Articles).filter(Articles.id == id).first()
    
    if not article:  
        return JSONResponse(status_code=404, content={ "message": "Пользователь не найден"})
    
    return article


@app.post("/api/articles")
def create_article(data  = Body(), db: Session = Depends(get_db)):
    article = Articles(title=data["title"], content=data["content"], category=data["category"])
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


@app.put("/api/articles")
def edit_article(data  = Body(), db: Session = Depends(get_db)):
   
    article = db.query(Articles).filter(Articles.id == data["id"]).first()
   
    if article == None: 
        return JSONResponse(status_code=404, content={ "message": "Пользователь не найден"})
  
    article.title = data["title"]
    article.content = data["content"]
    article.category = data["category"]
    db.commit()
    db.refresh(article)
    return article


@app.delete("/api/articles/{id}")
def delete_article(id, db: Session = Depends(get_db)):
 
    article = db.query(Articles).filter(Articles.id == id).first()
   
    if article == None:
        return JSONResponse( status_code=404, content={ "message": "Пользователь не найден"})
   
    db.delete(article)  
    db.commit()     
    return article