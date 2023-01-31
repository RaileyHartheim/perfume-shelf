# Railey Hartheim's perfume shelf
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
* Add/delete comments to perfume records
* Search perfume by name or brand/perfume group/seasons/gender/etc

### Todo list
* Make desigh more accurate and mobile-friendly
* Create or use existing tag system for notes
* Slugify brand and perfume name for link readability
* Use parcing for semi-automatic form filling

### Author of project
[Yulia Kazhaeva (Railey Hartheim)](https://github.com/RaileyHartheim)