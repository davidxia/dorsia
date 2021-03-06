
Setup instructions for local environment
====================================================================================================

Django1.4. Server's running python 2.6.5

Clone repo, setup virtualenv, and install prerequisite modules:
----------------------------------------------------------------------------------------------------

    git clone git@github.com:davidxia/dorsia.git
    cd dorsia/dorsia
    virtualenv env
    source env/bin/activate
    ./pip/install.py


To install virtualenv:
----------------------------------------------------------------------------------------------------

    (sudo) pip install virtualenv

To install pip:
----------------------------------------------------------------------------------------------------

    curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
    (http://www.pip-installer.org/en/latest/installing.html)

Install postgres
----------------------------------------------------------------------------------------------------

If you're using Mac OS X, first install Homebrew:

    /usr/bin/ruby -e "$(/usr/bin/curl -fksSL https://raw.github.com/mxcl/homebrew/master/Library/Contributions/install_homebrew.rb)"

Then install PostgreSQL:

    brew install postgresql

Testing
====================================================================================================

Yes, we have tests. We sleep really well at night. To run the tests:

    ./manage.py tests
