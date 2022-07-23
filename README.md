# perfume_shelf
Personal web application for creating perfumes database and making some notes

### Technologies
* [Python: 3.8.10](https://www.python.org/)
* [Django: 2.2.21](https://www.djangoproject.com/)
* [Bootstrap v3.3.7](https://getbootstrap.com/)

### Getting Started
These instructions will allow you to run a copy of the project.

1. Fork repository https://github.com/RaileyHartheim/perfume_shelf
2. Clone your repository
3. Create and activate virtual environment:
```
python -m venv venv
source venv/bin/activate
```
4. Install dependencies:
```
pip install -r requirements.txt
```
5. Create ``.env`` file in directory with ``manage.py`` and fill with DJANGO_KEY
6. Run migrations:
```
python manage.py migrate
```
7. Create superuser:
```
python manage.py createsuperuser
```

8.  Start django server:
```
python manage.py runserver
```

### Functionallity
* Create/edit/delete new perfume record
* Login/logout  

### Todo list
* Add comments
* Add more fields to the perfume model
* Add search by name/brand (optional: perfume group/seasons/gender/etc)
* Create or use existing tag system for notes
* Use parcing for semi-automatic form filling  

### Author of project
Yulia Kazhaeva - [GitHub](https://github.com/RaileyHartheim)