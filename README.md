# Courses catalog
1. Run command
    ```
    git clone https://github.com/Gekol/course_catalog.git
    ```
2. Install `virtualenv` package with command
   ```
   pip install virtualenv
   ```
3. Create virtual environment with command
    ```
    virtualenv name_of_the_venv
    ```
Virtual environment should be at the same level as `courses` and `course_catalog` folders
3. Activate the venv with command
    ```
    source mypython/bin/activate
    ```
if you use Mac OS or Linux. For Windows, use the following command
    ```
    name_of_the_venv/Scripts/activate
    ```
4. Install the requirements with the following command
    ```
    pip install -r requirements.txt
    ```
5. Run the command
   ```
   python manage.py makemigrations
   ```
6. Run the command
   ```
   python manage.py migrate
   ```
7. Run the command
   ```
   python manage.py runserver
   ```
8. Open the ```http://127.0.0.1:8000/``` in browser