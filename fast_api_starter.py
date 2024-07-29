from pathlib import Path

import uvicorn
from typing import List
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Form, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
import subprocess
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)

@app.post("/upload")
def upload(request: Request,
           option: str = Form(...),
           files: List[UploadFile] = File(...)):
    # For now, we will just print the option and the file name
    print(f"Selected Option: {option}")
    print(f"Uploaded Files: {[file.filename for file in files]}")

    for file in files:
        try:
            contents = file.file.read()
            with open(file.filename, "wb") as f:
                f.write(contents)
        except Exception:
            return {"message": "There was an error uploading the file(s)"}
        finally:
            file.file.close()
    subprocess.run('./circos_project.sh', shell=True)
    return {"message": f"Successfuly uploaded. Circos generator proceeding..."}


# Access the form at 'http://0.0.0.0:8000/' from your browser
@app.get("/", response_class=HTMLResponse)
def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

#@app.get('/')
#async def main():
#    content = '''
#    <body>
#    <form action='/upload' enctype='multipart/form-data' method='post'>
#    <input name='files' type='file' multiple>
#    <input type='submit'>
#    </form>
#    </body>
#    '''
#    return HTMLResponse(content=content)

# Only for testing
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
