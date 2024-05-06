# Task-2
1. Create a Django application for the company's satellite tracking system.
2. Need two main tables: Satellites and Launch Country (For this populate dummy data)
3. Populate the Satellites table with at least 600 entries from 10 satellites by pulling in the data from the information system,.
4. Use the field names based on what the JSON file has.
5. Use a database system of your choice.
6. Dockerize the Django application.

Run these commands after going to task/ directory
```sh
docker build -t my_django_app .
```
```sh
docker run -p 8000:8000 my_django_app
```

Open Exec tab in Docker and run this command to start populating data
```sh
python manage.py populate
```
![image](https://github.com/DeepSeaCreature0/Task-2/assets/138828627/0bd35669-fb99-4e33-a199-b9040a64b437)
![image](https://github.com/DeepSeaCreature0/Task-2/assets/138828627/4de3911d-4efc-4669-acba-cc9e3acfefc7)


## To view Table
1. Open admin page
```sh
http://127.0.0.1:8000/admin
```

Enter following details:
   * Username: gb
   * Password: gb

Note: The data will be checked once in 10 min, if new data is found the data is entered in the database.
### LaunchCountry Table
![image](https://github.com/DeepSeaCreature0/Task-2/assets/138828627/9b252c28-931e-4d36-b58e-1094e0bf1311)

### Satellite Table
![image](https://github.com/DeepSeaCreature0/Task-2/assets/138828627/307c4bef-41df-4dc9-98af-e774d21d2850)

### Data Associated with each satellite
![image](https://github.com/DeepSeaCreature0/Task-2/assets/138828627/fc4577db-38a9-4616-b89b-715947ae266f)

Note: The data will keep increasing with time since the data from the API keep getting updated occasionally .

