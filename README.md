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
When the docker file runs it will first populate the tables and then run server

## To view Table
1. Open admin page
```sh
http://127.0.0.1:8000/admin
```
Enter following details:
   * Username: gb
   * Password: gb

The table will look like this when you open Satellites in the CORE section
![image](https://github.com/DeepSeaCreature0/Task2/assets/138828627/3805bf82-a72c-4e40-a27e-f56ac97df12b)

The CSV File is also in the directory task/.
