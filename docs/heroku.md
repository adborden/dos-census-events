---
title: Heroku
---

# {{ page.title }}

This document describes how to get the Census Events application running on
[Heroku](https://www.heroku.com) in production.

1. Fork the repo on GitHub
1. Create the Heroku application
1. Configure the application settings
1. Login for final configuration


## Fork the repo on GitHub

_We are working to remove this step, since forking code makes it harder to keep
up with the latest features and updates from Census Events. See
[#81](https://github.com/openoakland/dos-census-events/issues/81) for discussion._

Follow [GitHub's instructions](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) to fork [Census Events](https://github.com/openoakland/dos-census-events).


## Create the Heroku application

From the [Heroku Dashboard](https://dashboard.heroku.com/apps), click New ->
Create new app. Enter a name for your application and click Create app.

Next, setup [GitHub integration](https://devcenter.heroku.com/articles/github-integration) to connect your forked GitHub repository.

From the integration, you can [deploy the master branch](https://devcenter.heroku.com/articles/github-integration#manual-deploys).


## Configure the application settings

From the [Heroku Dashboard](https://dashboard.heroku.com/apps), click the Resources
tab. Under add-ons, search for Heroku Postgres and click Provision.

Click the Settings tab. Under Config Vars, click Reveal Config Vars.

Add `DEBUG` key with value `0`.

Add `ALLOWED_HOSTS` key with value `<your-heroku-app-name>.herokuapp.com`.

Add `SECRET_KEY` key with a string of 50 random characters.

Add `GOOGLE_CALENDAR_ID` key with value of your Google Calendar Id.

Add `GOOGLE_SERVICE_ACCOUNT_INFO` key and paste the content of your
google-account.json file into the value field.


## Login for final configuration

Create an admin account with the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

    $ heroku run python manage.py createsuperuser

Open the app in your web browser.

    $ heroku open

Login with the admin user you just created.
