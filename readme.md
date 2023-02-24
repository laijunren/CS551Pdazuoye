## Project: Music Culture Project

This project is a test project. It is mainly used to learn the flask framework and some front-end knowledge.

It is not suitable for production environments because it lacks some security guarantees, such as csrf, xss, and so on.

Another reason for developing it is to explore the relationship between the data and deeply understand the relationship between the musician and his song style in the social background at that time.

## How to start it
+ First of all, you need to create a virtual environment venv. Here I use virtualenv, which is executed from the command line
  
    ```shell
    virtualenv venv
    source venv/bin/activate  # Activate virtual environment,windows: venv\Scripts\activate
    ```

+ then install the dependent package
      
     ```shell
     pip install -r requirements.txt
     ```
+ Initialize database data
    ```shell
    python setup_db.py
    ```
+ Run Project
    ```shell
    flask run
    ```
+ Browser access http://127.0.0.1:5000


## How to test it
First of all, you need to determine your browser and version. I'm using Chrome 109. If your version is different, there may be some problems.
Here is the download connection，http://chromedriver.storage.googleapis.com/index.html
+ Download the corresponding version of chromedriver，Then put it in the project directory `features/driver/`
+ Then execute
    ```shell
    behave
    ```
+ If you see the following output, congratulations, you have successfully tested this project
    ```shell
    ----------------------------------------
    1 feature passed, 0 failed, 0 skipped
    1 scenario passed, 0 failed, 0 skipped
    3 steps passed, 0 failed, 0 skipped, 0 undefined
    Took 0m0.281s
    ```
  