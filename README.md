# Meetings using Python, and Django

I am learning Meetings Application using Python Django from different Video Courses, Books, and Websites.

## Few Commands

```powershell
python -m venv .venv
.\.venv\Scripts\activate

python.exe -m pip install --upgrade pip

py -m pip install Django~=5.0.7
django-admin startproject meeting_planner

cd meeting_planner
py .\manage.py runserver

py .\manage.py startapp website

py .\manage.py showmigrations
py .\manage.py migrate

py .\manage.py startapp meetings
py .\manage.py makemigrations
py .\manage.py showmigrations
py .\manage.py migrate
py .\manage.py sqlmigrate meetings 0001

py .\manage.py createsuperuser
```

![Create Super User](documentation/images/CreateSuperUser.PNG)

## Reference(s)

> 1. <https://docs.python.org/3/library/venv.html>


@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

* {
    box-sizing: border-box;
}

body {
    font-family: 'Roboto', sans-serif;
    color: rgb(19, 98, 245);
    /* background-color: floralwhite; */
    height: 100vh;
    margin: 0;
}

.meeting-container {
    width: 90%;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 20px;
    background-color: #fff;
    border: 2px solid #f2f2f2;
    margin: 0 auto;
    /* Center horizontally */
    display: flex;
    flex-direction: column;
    align-items: center;
    /* Center content inside the div */
}

h2 {
    text-align: center;
}

table {
    width: 100%;
    border-collapse: separate;
    /* Changed from collapse to separate */
    border-spacing: 0;
    border: 2px solid #ccc;
    /* Ensure table has a border */
    border-radius: 8px;
    overflow: hidden;
}

thead {
    background-color: #f2f2f2;
}

thead th {
    padding: 10px;
    border-bottom: 2px solid #ccc;
    /* Ensure there is a border at the bottom of the header */
}

tbody tr:nth-child(odd) {
    background-color: #f9f9f9;
}

tbody tr:nth-child(even) {
    background-color: #fff;
}

tbody td {
    padding: 10px;
    border-top: 1px solid #ddd;
    /* Ensure cells have borders */
    border-left: 1px solid #ddd;
    /* Ensure cells have borders */
}

tbody td:first-child {
    border-left: none;
    /* Remove left border for the first column */
}

tbody td:last-child {
    border-right: none;
    /* Remove right border for the last column */
}

tbody tr:hover {
    background-color: #f1f1f1;
}