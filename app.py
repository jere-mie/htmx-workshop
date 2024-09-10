from flask import Flask, render_template, request, Request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from dotenv import load_dotenv
import os
import json
from datetime import datetime
import markdown

# init stuff
load_dotenv() # load environment variables from .env file
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for the articles - this represents the table in the database
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=func.now(), nullable=False)

# helper function to get article from request
def get_article_from_request(request: Request) -> Article:
    return Article(title=request.form.get("title"), content=request.form.get('content'))

# helper function to get all articles, showing newest first
def get_articles():
    articles = Article.query.all()
    articles = sorted(articles, key=lambda x: x.date, reverse=True)
    return articles

##########################################################
# Routes Section
# This is where we'll be working
##########################################################

# READ
@app.get('/')
def index():
    articles = get_articles()
    return render_template('index.html', articles=articles)

@app.get('/article/<int:id>')
def get_article(id):
    article = Article.query.get_or_404(id)
    article.content = markdown.markdown(article.content)
    return render_template('article.html', article=article)

##########################################################
# Start of new code
##########################################################

# DELETE
@app.delete("/article/<int:id>")
def delete_article(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    return """
    <div>
        <div class="m-2 p-2 bg-success rounded">Successfully Deleted Article!</div>
        <a href="/" class="btn btn-primary">Return Home</a>
    </div>
    """

# CREATE
@app.get("/article/new")
def create_article_form():
    return render_template("form_create.html")

@app.post("/article")
def create_article():
    article = get_article_from_request(request)
    db.session.add(article)
    db.session.commit()
    return render_template("articles_list.html", articles=get_articles())

# UPDATE
@app.get("/article/<int:id>/edit")
def edit_article_form(id):
    article = Article.query.get_or_404(id)
    return render_template("form_edit.html", article=article)

@app.put("/article/<int:id>")
def edit_article(id):
    existing_article = Article.query.get_or_404(id)
    new_article_data = get_article_from_request(request)
    existing_article.title = new_article_data.title
    existing_article.content = new_article_data.content
    db.session.commit()
    return render_template("article_details.html", article=existing_article)

##########################################################
# End of new code
##########################################################

##########################################################
# End of Routes Section
##########################################################

# Function to load articles from JSON and add to the database
def load_articles_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    for article_data in data['articles']:
        article = Article(
            id=article_data['id'],
            title=article_data['title'],
            content=article_data['content'],
            date=datetime.fromisoformat(article_data['date'])
        )
        db.session.add(article)
    db.session.commit()

def main():
    # create the database if it doesn't exist
    if not os.path.exists('instance/db.sqlite3'):
        with app.app_context():
            db.create_all()
            load_articles_from_json('static/articles.json')
            db.session.commit()
    # run the server
    app.run(debug=True, port=5000)

if __name__ == '__main__':
    main()
