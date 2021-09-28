# hierarchical-data-and-you

Sometimes when categorizing data, there are potentially infinite ways that the data can be organized. For example, a file path for an operating system includes all the parent folders and the the location of the item itself, like this:

```
/Users/jkaufeld/demo/test.py
```

If we're looking at an object called `test.py` and we want to find all of the "parent nodes", or the folders that contain this object, then we have to do a recursive call upwards. In a 'traditional' Django ORM setup, a naive example might look something like this:

```python
def get_complete_path(item):
    complete_path = list()

    while True:
        item = item.parent
        complete_path.prepend(item.path)
        if item.path == "/":
            break

    return os.path.join(complete_path)
```

This results in a database call for every single layer, which works out to three calls to get the complete path of our mythical object. We can do a lot better though... what if we could get that info in one call?

Using something called Modified Preorder Tree Traversal (MPTT), we can treat all our data like a gigantic tree, with a single starting point (the "root" object) and parents, siblings, and children galore. We can get the same data as above with a single call:

```
item.get_ancestors()
```

#### **Your Task**

The goal of this assignment is to learn about this type of database and different ways of working with it. Build a simple Django server that uses MPTT models from `django-mptt` to create a Dropbox-esque web interface where you can create "folders" and "files" in an arbitrary structure and then display that structure. We won't actually be uploading anything, just making model instances and using them to represent real data. See the rubric for more detailed information. Submit as link to your repo on Github.

In addition to creating this project, we're also going to practice including useful information in our README.md (yes, the file you are currently reading). We want anyone who hasn't run this project before to be able to run it locally on their machine. We want to update README.md include sections that explain 1) what the project does and 2) how to run the program. Here's a helpful resource on what a good README.md looks like: [https://www.makeareadme.com/](https://www.makeareadme.com/)

Resources:

*   [https://django-mptt.readthedocs.io/en/latest/overview.html](https://django-mptt.readthedocs.io/en/latest/overview.html)

Extra Credit:

*   3 BONUS POINTS: Add forms to create folders / "files" without using the admin panel.
*   5 BONUS POINTS: Add a basic authentication system where each user has their own tree. Login / logout pages / endpoints included.

#### **Submission**

Submit a link to your GitHub repo.

```
https://github.com/kenzie-se-q4/hierarchical-data-and-you-<github_username>/
```
