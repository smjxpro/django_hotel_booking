### Django Hotel Booking
#

1. Install virtualenv using pip: `pip install virtualenv`

2. Create a virtual env: `virtualenv -p python3 venv`

3. Activate the virtual env: `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)

4. Install dependencies: `pip install -r requirements.txt`

5. Create `local_settings.py` file in `django_hotel_booking/` (where `settings.py` is) directory

6. Migrate database changes: `python manage.py migrate`

7. Create a superuser: `python manage.py createsuperuser`

8. Run the dev server: `python manage.py runserver`
