from cs50 import SQL

db = SQL("sqlite:///portal.db")

tablerow = db.execute("SELECT * FROM Blogs WHERE blog_title='Blog-Title-1'")
print(tablerow[0]['blog_title'])