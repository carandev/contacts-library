# Contacts Library

- requirements:
    - docker or mysql
    - python
    - virtual env

1. Clone repository
2. `python -m venv venv`
3. Windows: `.\venv\Scripts\activate` - Unix: `source ./venv/bin/activate`
4. If you didn't installed mysql you could use docker: `docker run --name mysql-server -p 3306:3306 -e MYSQL_ROOT_PASSWORD=admin -d mysql`
5. You can access to mysql with `docker exec -it mysql-server bash` and `mysql -u root -padmin`
6. Create database and table
7. Install python libraries: `pip install -r requirements`
8. Execute python script: `python main.py`