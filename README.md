# hotel-reservations-system

## Steps for adding new data models:

#### 1. Create the reservation app: (commit [link](https://github.com/liornoy/hotel-reservations-system/commit/5c2a758e4876cbff2e25b5ebc3f64a45dea092fa))
```
python manage.py startapp reservations
```

#### 2. Add the new app to settings.py: (commit [link](https://github.com/liornoy/hotel-reservations-system/commit/899a59c5b2c55f9ea0d2cdac68c3c28c8c40092e))

#### 3. Create the data model classes: (commit [link](https://github.com/liornoy/hotel-reservations-system/commit/1eba08f8758deab7b064dd59d12d8d00e2810369))

Here we add the data models (Guest, Room, Reservation, Review) just like in the ERD.

#### 4. Add migration files for initializing the data models: (commit [link](https://github.com/liornoy/hotel-reservations-system/commit/0cbb083e621cc087d8d403c3f9a6fba12d48f0a9))
```
python manage.py makemigrations reservations
```

#### 5. Add migration files for adding test data for the DEV environment: (commit [link](https://github.com/liornoy/hotel-reservations-system/commit/bd4d38f5c7a7e161d1220afa77afc1567fdc73fd))

In this step, we want to create test data for our development environment,
so we'll be able to test the data models logically and 
later also from a graphical aspect, when we will create a UI.

After writing the 0002_test_data.py, we run the database migrations with:
```
python manage.py migrate
```
#### 6. Create an admin user to access the admin page: (performed locally)
Run the command below and follow the instructions:
```
python manage.py createsuperuser
```
This will create a user that you can access the admin page with.

#### 7. Register the data models to admin.py: (commit [link](https://github.com/liornoy/hotel-reservations-system/commit/12729aa66c3f73b3d06ce0bb8fbefacecfbde445))

This will make the new data model appear in the admin UI.

#### 8. Watch the data models via the Django admin UI:
Enter http://127.0.0.1:8000/admin/
Insert the credentials of the superuser,
watch the data models.

![Screenshot from 2022-11-01 19-58-04](https://user-images.githubusercontent.com/40122521/199304699-eb13cb07-1225-4931-95d4-e333bae47cf1.png)

