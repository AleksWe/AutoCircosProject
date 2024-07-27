import uvicorn
from typing import List
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, File, UploadFile
import subprocess

app = FastAPI()

@app.post("/upload")
def upload(files: List[UploadFile] = File(...)):
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
    return {"message": f"Successfuly uploaded {[file.filename for file in files]}. Circos generator proceeding..."}
    # Bash file


# Access the form at 'http://0.0.0.0:8000/' from your browser
@app.get('/')
async def main():
    content = '''
    <body>
    <form action='/upload' enctype='multipart/form-data' method='post'>
    <input name='files' type='file' multiple>
    <input type='submit'>
    </form>
    </body>
    '''
    return HTMLResponse(content=content)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)