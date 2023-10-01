Remove-Item .\build\assets

#git pull 
.\venv\Scripts\python.exe -m nuitka --follow-imports --standalone .\app.py


Copy-Item -r .\assets .\build
Copy-Item app.exe .\build