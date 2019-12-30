MODEL OF THE WEB APP:
Table-1: Admins [People who do the server maintenance and/or Content Updations]
         [Id, Name, Hash, Role]
Table-2: Blogs [Table consisting of data related to all the blogs present on the webapp]
     [Id, Timestamp, Content, Cover(img), Title, Intro]
Table-3: Msgs [Table consisting of all the messages came from get in touch field]
 [Id, Name, Email, Subject, Msg]

VIEWS OF THE WEB APP:

*Layout.html : Homogeneous Layout consisting of responsive navbar and footer for all the                                                             pages of web app. All other views will share this layout(more precisely style).
    ALL VIEWS FROM HERE WILL BE GENERATED DYNAMICALLY!

*Index.html: This view corresponds with the home-page/default-page of the web-app and will consist Jumbotron(Greeter), Skills(Dynamic graph), and Contact(form) components
*Blog.html: This view corresponds with the list of all the posted blogs on the portal, will have design as one-jumbotron per blog (jumbotron contains blog title and introduction as body text)

    WHEN USER CLICKS ON A BLOG FROM BLOGLIST VIEW BELOW VIEW WILL BE RENDERED ACCORDING TO THE SELECTED BLOG FROM BLOGS TABLE

Blogcore.html: This view will display the blogs’ Content text + Cover image + Title
Blogadder.html: This view will consist of a form with one to one relationship with fields of the table-2 (blogs) this will add new blog to the portal!