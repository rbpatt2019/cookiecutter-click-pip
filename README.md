# cookiecutter-pip-click

A Python cookiecutter template for creating command-line tools.

## Information

I love command line tools and open-source software, so I create this template for use with future projects. It creates a well-structured - but hopefully not too opinionated - project for developing command line tools using [Click](https://click.palletsprojects.com/en/7.x/). This [cookiecutter](https://cookiecutter.readtehdocs.io) template should handle (nearly) all your project setup for you, using [poetry](https://eustace.poetry.io).

## Using the template

When starting a new project, always create a new virtual environment. I use pyenv for all my env/venv control, so I would do:

```sh
pyenv virtualenv project_name
pyenv virtualenv activate project_name
pip install -U cookiecutter
```

Use whatever method is already part of your workflow. Now, we initialise the project:

```sh
cookiecutter https://github.com/rbpatt2019/cookiecutter-pip-click
```

You'll be walked through some prompts to provide the necessary information. And, viola! Your project is set-up! 

## Final Steps

Let's take a peek around. To do that, move into the directory and view it's contents.

```sh
cd project_name
ls
```

Poetry uses a pyproject.toml for all of its settings, so let's look at that.

```sh
cat pyproject.toml
```

Here is where you can modify any settings for the package that you'd like to. The eagle-eyed among you might have noticed that pytest does not have its own section. Currently, pytest does not parse pyproject.toml for settings, so all options are manually passed to pytest in the Makefile.

I think `make` is the greatest thing since sliced bread, so let's check that out.

```sh
cat Makefile
```

Some useful commands here to handle everything from linting to version control to packaging. Since we are going to be developing this tool, run:

```sh
make develop
```

*DO THIS BEFORE ANYTHING ELSE*. I considered adding it to the post-generation hook, but elected not to. This was, you can create a venv however you want to, and I won't bork your python install if you forget to before creating a new project.

Now, create a repo on git hub, and push your new project there.

```sh
git remote add origin https://github.com/YOUR_USER/project_name
git push origin master
```

The project is designed to coordinate with [Travis CI](https://travis-ci.org), [codecov](https://codecov.io), [readthedocs](https://readthedocs.org), and [pyup](https://pyup.io). All the necessary files are there, you just need to add your new project to their websites, and they should just work.

Happy Coding!
