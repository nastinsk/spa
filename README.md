#   SPA Project

**Author**: Anastasia Lebedeva

## Challenge
Use Django REST Framework to create an API, then “containerize” it using Docker.  Add Permissions and Postgresql Database.

## Architecture
* Python 3.7
* Pipenv
* Django
* djangorestframework
* Docker
* psycopg2-binary
* djangorestframework-simplejwt 
* gunicorn 
* whitenoise 

## Models:
Reservation:
  customer_name = CharField with max_length=120
  treatment = CharField with max_length=200
  treatment_description = CharField with max_length=480
  reservation_date = DateField
  reservation_time = TimeField
  reservation_created_date = auto DateTimeField
  reservation_updated_date = auto updating DateTimeField
  staff_member_name = field for the user created Reservation


## Routes
* http://127.0.0.1:8000/admin - admin page 
* http://localhost:8000/api/v1/reservations/ - to see the list of all reservations in the db
* http://localhost:8000/api/v1/reservations/reservation.pk/ - to see the reservation details
* http://localhost:8000/api/token/ - to obtain tokens
* http://localhost:8000/api/token/refresh/ - to refresh token