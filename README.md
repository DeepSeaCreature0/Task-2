# Task2

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
