from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:blog_id>')
def show_post(blog_id):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    
    # Find the specific blog post by its ID
    blog_post = next((post for post in all_posts if post['id'] == blog_id), None)
    
    # If post is found, render it
    if blog_post:
        return render_template("post.html", post=blog_post)
    else:
        return "Post not found", 404

if __name__ == "__main__":
    app.run(debug=True)
