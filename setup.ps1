python -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.venv\Scripts\activate
pip install -r app/config/requirements.txt
set FLASK_APP=app.py
python run.py