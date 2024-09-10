# Hack the North 2024 ~ HTMX-Workshop

Presentation and supporting materials for my Hack the North 2024 workshop "Hypermedia & HTMX - A Different Approach to Full Stack Development"  
Created and presented by [Jeremie Bornais](https://github.com/jere-mie).

## Slides

Slides will be released soon!

## Resources

### HTMX Resources

- [Main HTMX.org website](https://htmx.org/)
- [HTMX Docs](https://htmx.org/docs)
- [HTMX Code Snippets](https://htmx.org/examples) (HIGHLY recommend checking this one out)
- [HTMX Essays](https://htmx.org/essays) (Check this out if you want to learn the nerdy theory behind HTMX - I had a lot of fun going through these)
- [Hypermedia Systems Book](https://hypermedia.systems) (A more complete look into the theory behind Hypermedia and HTMX. Freely available online)

### Flask Resources

- [My Flask Workshop](https://github.com/jere-mie/flask-workshop) (I've given this talk several times - if you're newer to Flask and/or web development, you may want to check this out)
- [Official Flask Website](https://flask.palletsprojects.com/en/3.0.x/)

## How to Run This App

1. Make sure you have Python and pip installed
2. Clone this git repository
```sh
git clone https://github.com/jere-mie/flask-workshop
```

3. Install Python libraries
```sh
python3 -m pip install -r requirements.txt
```

4. Run the Flask server
```sh
python3 app.py
```

5. Head to http://127.0.0.1:5000/ to preview the web app!

### Using GitHub Codespaces

If you'd like to use GitHub Codespaces instead of running the application locally, you can skip the first two steps. Instead, ensure you're signed into GitHub, then navigate to this repository and click `Code > Codespaces > Create Codespace on main`. This will open up a web version of VSCode with access to a full Linux shell.

## Sample Code Overview

### app.py

This is the main Flask app, containing all of the routes and backend logic

### .gitignore

This file contains all of the files and folders you do not want added to the git repository. Generally you include things like config files, database files, the venv folder, and the pycache folder.

### static/

This folder contains all static files you want to use in your Flask app. This would include css files, images, javascript files, etc. In our case, it includes HTMX and Bootstrap.

### templates/

This folder contains all of your HTML templates. Usually you use a layout.html for things like metadata and a navbar, and then you create other templates that extend this template.

### instance/db.sqlite3

This is the SQLite database for our application. It will be automatically created if it doesn't exist when running `app.py`. If you want to start your database from scratch, simply delete this file.

### requirements.txt

Lists the third-party Python libraries used in our application.
