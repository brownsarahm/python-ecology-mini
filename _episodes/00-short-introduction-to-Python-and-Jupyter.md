---
title: Short Introduction to Programming in Python
teaching: 10
exercises: 5
questions:
    - "What is Python?"
    - "Why should I learn Python?"
objectives:
    - "Describe the advantages of using programming vs. completing repetitive tasks by hand."
    - "Define the following data types in Python: strings, integers, and floats."
    - "Perform mathematical operations in Python using basic operators."
    - "Define the following as it relates to Python: lists, tuples, and dictionaries."
---

# The Basics of Python

Python is a general purpose programming language that supports rapid development
of scripts and applications.

Python's main advantages:

* Open Source software, supported by Python Software Foundation
* Available on all platforms
* It is a general-purpose programming language
* Supports multiple programming paradigms
* Very large community with a rich ecosystem of third-party packages

## Interpreter

Python is an interpreted language which can be used in two ways:

* "Interactive" Mode: It functions like an "advanced calculator" Executing
  one command at a time:

~~~
user:host:~$ python
Python 3.5.1 (default, Oct 23 2015, 18:05:06)
[GCC 4.8.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 2
4
>>> print("Hello World")
Hello World
~~~
{: .language-python}

* "Scripting" Mode: Executing a series of "commands" saved in text file,
  usually with a `.py` extension after the name of your file:

~~~
user:host:~$ python my_script.py
Hello World
~~~
{: .bash}

## Jupyter Notebooks

Jupyter notebooks allow us to work with the interactive interpreter that thas some extra features built into it and combine with text to build a narrative.  These are really good for research- you can disseminate work, share it with colleagues or use it like a lab notebook, until you figure out the right way of getting something done.  They're also useful for teaching, as you'll see here.

### Starting in the same spot

To help the lesson run smoothly, let's ensure everyone is in the same directory.
This should help us avoid path and file name issues. At this time please
navigate to the workshop directory. If you working in Jupyter Notebook be sure
that you start your notebook in the workshop directory.

A quick aside that there are Python libraries like [OS
Library](https://docs.python.org/3/library/os.html) that can work with our
directory structure, however, that is not our focus today.



### Extra notebook Magics to facilitate short time
This is a modification of the regular Data Carpentry Python Ecology Lessons,
designed to be able to use only 90 minutes total and still get to some interesting
activities, so we will use some extra jupyter notbeook magic this lesson includes
the content and then we can work from that.

First, we'll use the pycat magic to show some hints while we explore jupyter notbeooks a little more.

~~~
%pycat code/notebook_hints.md
~~~
{: .language-python}

The main magic that we will use is called `load`. It allows us to pull in excerpts
of code to the notebook.  In research, this might be useful if you have common
setup things that you do not want or need to call as a function, but this is
possibly most for exactly this purpose, teaching, live. We'll use it here, so we
can go a little faster and for some activities.

~~~
%load code/example.py
~~~
{: .language-python}

Then when we run the cell (shit + enter). it comments that line out and adds the
content of the file `example.py`

~~~
# %load code/example.py
a = 4
b = 3

c = a**2 + b**2
~~~
{: .language-python}

Also, we learned what a comment is: a line of python code starting with a `#`
will not run, so if we run the cell above, all it does is the other lines, it doesn't
reload the file.  This cell won't actually output anything, but we can use another
jupyter notebook feature to check what it did. Any variable on the last line of
a cell will be printed - in a nice format, often.

~~~
c
~~~
{: .language-python}

```
25
~~~
{: .output}

If we want to correct this to actually be pythagorean theorem, we will we can add
the sqrt function, but we'll get an error, because that's not a built in function
in python.
We can manually copy the code from the cell we imported, or practice
copying a cell. Use escape to get to command mode, then go up to the cell we want
to copy and press`c`, now arrow to the bottom and press `v`.


## About Libraries
A library in Python contains a set of tools (called functions) that perform
tasks on our data. Importing a library is like getting a piece of lab equipment
out of a storage locker and setting it up on the bench for use in a project.
Once a library is set up, it can be used or called to perform many tasks.



Python doesn't load all of the libraries available to it by default. We have to
add an `import` statement to our code in order to use library functions. To import
a library, we use the syntax `import libraryName`. If we want to give the
library a nickname to shorten the command, we can add `as nickNameHere`.  An
example of importing the pandas library using the common nickname `pd` is below.

Each time we call a function that's in a library, we use the syntax
`LibraryName.FunctionName`. Adding the library name with a `.` before the
function name tells Python where to find the function. In the example above, we
have imported Pandas as `pd`. This means we don't have to type out `pandas` each
time we call a Pandas function.
