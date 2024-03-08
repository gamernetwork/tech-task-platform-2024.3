# Technical Task - Developer, Platform team, ReedPop

Hello,

In this task you will be working on a simple data platform for a news website.

The project is built in Python and uses the Django framework (v3.2).

The aim is to develop a tagging feature for articles. You will be asked to:

  - Extend the models to include tags.
  - Make the tags creatable on the admin site.
  - Create a method that could be used to list tags.
  - Add some tests for your work.

The task is designed to demonstrate your ability to use new technology, to interpret specifications, solve programming problems, and show an understanding of test coverage.

The task is intended to take no more than 2 or 3 hours. If you overrun significantly then please get in touch as we may have misjudged the timing of the task.

## Getting set up

Install **Python 3** if you don't already have it (should be fine on macOS and Linux).

Then, in a shell, run the following to set up the project:

```bash
git clone https://github.com/gamernetwork/tech-task-platform-2024.3.git
cd tech-task-platform-2024.3

# set up a python virtual environment
python3 -m venv .env

# install Django into this environment
.env/bin/pip install -r requirements.txt

# set up the database
.env/bin/python manage.py migrate
```

You will now have a `db.sqlite3` file in your project directory. This is your database.

To access the admin site, create yourself a superuser account:
```bash
# set yourself up as a user for the backend of this site
.env/bin/python manage.py createsuperuser
```

Then run this command to load in a set of basic data:
```bash
# import 3 starting articles
.env/bin/python manage.py loaddata youreagamer_starting_articles
```

Now start a local development server (errors and access logs will show here):
```bash
.env/bin/python manage.py runserver
```

Point your browser at [http://127.0.0.1:8000](http://127.0.0.1.8000) and you should see a list of 3 posts, which can be clicked.

Finally, access the backend here: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in using the superuser account you created. This is where you can edit the data for the mock news site.

### Note regarding the database

If you get into a mess with migrations, etc, you can just move/delete the `db.sqlite3` file and re-run the `migrate` and `createsuperuser` steps again to get back to a fresh installation.

## Tasks

Please do the following:

  1. Add a `Tag` model with the following fields:
     * Name (up to 200 characters, unique)
     * Created at (date/time, automatically set when model is created)

      Also give the `Tag` model a `__str__` method that returns the `Tag`'s name.
  1. Add a field to the `Post` model allowing a post to be associated with zero or more tags.
  1. Make your DB reflect these above changes. Refer to the [Workflow section](https://docs.djangoproject.com/en/3.2/topics/migrations/#workflow) on migrations for steps to get your model changes into the database.
  1. Make it so you can add tags to articles on the admin site (HINT: All this requires is adding a `TagAdmin` class to `cms/admin.py` - use the `PostAdmin` class as a guide. Don't forget to import your `Tag` model here too!).
  1. Add a method or property to `Post` that returns a single string containing the name of all tags associated with the post, in alphabetical order.
     * For example, if a post is tagged with "Gaming", "Featured" and "Xbox", the output might be "Featured, Gaming, Xbox"
     * Ensure that this method can handle a post that has no tags.
  1. Add suitable test cases for the method you created in the previous step. Refer to ["Writing our first test"](https://docs.djangoproject.com/en/3.2/intro/tutorial05/#writing-our-first-test) for information about writing and running tests. 

## Submitting your completed task

You should submit your work by email either as a zip of code, or as a patch against the original repo.

Please do not file a pull request against the original repo - other candidates will see your work!

Feel free to provide any explanatory notes in along with you submission.

If anything is unclear, please do not hesitate to get in touch!
