# dj_sdude
Sdude is a website that hosts exams and feedbacks about Suleyman Demirel University courses and professors.

### Installation Guide
#### installing virtualenv
```
sudo apt-get install pip
sudo pip install virtualenv
```

#### create virtualenv with python3
```
virtualenv -p python3 venv_sdude
```

#### enter virtualenv
```
source venv_sdude/bin/activate
```

#### installing requirements.txt (inside virtualenv)
```
cd dj_sdude
pip install -r requirements.txt
```

#### migrate db and create superuser
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
