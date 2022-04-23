# Data Base Table creation command
# CREATE TABLE POSTS(ID INTEGER PRIMARY KEY AUTOINCREMENT,Title varchar(200),Description varchar(1000),Date text);

import sqlite3
from flask import request, Flask, render_template, redirect

app = Flask(__name__)


def get_all_blogs():
    """
    This is function, that receives and returns all the blogs in connected db;

    :return: list of all blogs in db;
    """
    connection = sqlite3.connect("blog.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM POSTS")
    blogs = cursor.fetchall()
    connection.close()
    return blogs


@app.route('/')
def main_page():
    """
    This is the main page of website that provides blog maintenance;

    :return: Website main page with enumeration of all blogs;
    """
    return render_template("blogs.html", blogs=get_all_blogs())


@app.route('/new')
def new_blog_page():
    """
    This is page that provides creation of new blogs in connected db;

    :return: Exception message or redirects user on main page if creation was success;
    """
    if not request.args.get('title') and not request.args.get('desc'):
        return "Wrong syntax buddy, try to use ?title='blog name'&desc='blog description' instead"
    blog_title = request.args.get('title')
    blog_desc = request.args.get('desc')
    if create_blog(blog_title, blog_desc):
        return redirect("/")
    return "Sorry buddy, i can't create that blog maybe it's wrong syntax or empty args"


def create_blog(blog_title: str, blog_desc: str):
    """
    This is additional function, that accepts params of future blog and then creates "create new blog" command for
    db and commits it;

    :param blog_title: Title of new blog;
    :param blog_desc: Description of new blog;
    :return: Boolean that means whether execution was successful;
    """
    if not blog_title or not blog_desc:
        return False
    connection = sqlite3.connect("blog.db")
    cursor = connection.cursor()
    cursor.execute(" INSERT INTO POSTS(Title, Description, Date) VALUES(?,?,date('now'))", (blog_title, blog_desc))
    connection.commit()
    connection.close()
    return True


@app.route('/delete')
def delete_blog_page():
    """
    This is page that provides deletion of chosen blogs in connected db;

    :return: Exception message or redirects user on main page whether deletion was success;
    """
    if not request.args.get('id'):
        return "Wrong syntax buddy, try to use ?id='blog_number' instead"
    try:
        blog_id = int(request.args.get('id'))
    except ValueError:
        return "Sorry buddy, but it must be a number of blog, not any letters"
    if blog_id not in get_ids():
        return "Sorry buddy, there are no any blog with that id"
    if delete_blog(blog_id):
        return redirect("/")
    return "Sorry buddy, i can't delete that blog maybe it's wrong syntax or empty args"


def delete_blog(blog_id: int):
    """
    This is additional function, that accepts ID of blog to delete and then creates "delete blog" command for
    db and commits it;

    :param blog_id: ID of blog to delete;
    :return: Boolean that means whether execution was successful;
    """
    if not blog_id:
        return False
    connection = sqlite3.connect("blog.db")
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM POSTS WHERE ID = ?", (blog_id,))
    connection.commit()
    connection.close()
    return True


def get_ids():
    """
    This is additional function that receives all the IDs from connected db and returns it

    :return: List of IDs in connected db
    """
    connection = sqlite3.connect("blog.db")
    cursor = connection.cursor()
    cursor.execute("SELECT ID FROM POSTS")
    ids = cursor.fetchall()
    connection.close()
    blog_ids_list = [blog_id[0] for blog_id in ids]
    return blog_ids_list


@app.route('/edit')
def edit_blog_page():
    """
    This is page that provides edition of chosen blogs in connected db;

    :return: Exception message or redirects user on main page whether deletion was success;
    """
    if not request.args.get('id') or (not request.args.get('title') and not request.args.get('desc')):
        return "Wrong syntax buddy, try to use ?id='blog_number'&title='new blog title'/desc='new blog desc' instead"
    try:
        blog_id = int(request.args.get('id'))
    except ValueError:
        return "Sorry buddy, but it must be a number of blog, not any letters"
    if blog_id not in get_ids():
        return "Sorry buddy, there are no any blog with that id"
    success_title_edit = False
    success_desc_edit = False
    new_blog_title = request.args.get('title')
    if new_blog_title is None:
        success_title_edit = True
    new_blog_desc = request.args.get('desc')
    if new_blog_desc is None:
        success_desc_edit = True
    if new_blog_title is not None:
        success_title_edit = edit_blog_title(new_blog_title, blog_id)
    if new_blog_desc is not None:
        success_desc_edit = edit_blog_desc(new_blog_desc, blog_id)
    if success_title_edit is True and success_desc_edit is True:
        return redirect("/")
    return "Sorry buddy, i can't edit that blog maybe it's wrong syntax or empty args"


def edit_blog_title(new_blog_title: str, blog_id: int):
    """
    This is additional function, that accepts ID of blog to edit and new title,
    and then creates "edit blog" command for db and commits it;

    :param new_blog_title: New title for chosen blog
    :param blog_id: ID of blog to change
    :return: Boolean that means whether execution was successful;
    """
    if not new_blog_title or not blog_id:
        return False
    connection = sqlite3.connect("blog.db")
    cursor = connection.cursor()
    cursor.execute(f"UPDATE POSTS SET Title = ? WHERE ID = ?", (new_blog_title, blog_id))
    connection.commit()
    connection.close()
    return True


def edit_blog_desc(new_blog_desc: str, blog_id: int):
    """
    This is additional function, that accepts ID of blog to edit and new description,
    and then creates "edit blog" command for db and commits it;

    :param new_blog_desc: New description for chosen blog
    :param blog_id: ID of blog to change
    :return: Boolean that means whether execution was successful;
    """
    if not new_blog_desc or not blog_id:
        return False
    connection = sqlite3.connect("blog.db")
    cursor = connection.cursor()
    cursor.execute(f"UPDATE POSTS SET Description = ? WHERE ID = ?", (new_blog_desc, blog_id))
    connection.commit()
    connection.close()
    return True


if __name__ == '__main__':
    app.run()
