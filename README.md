Django boilerplate

## 1. Project Structure

```txt
project_root/
├── apps/                  # All Django apps live here
├── common/                # Shared models, utils, permissions
├── config/                # Django settings, urls, wsgi, asgi
├── templates/             # App templates (if any)
├── manage.py
├── .env
├── requirements.txt
```

## 2. Apps Structure
```txt
project_root/
├── apps/
│   ├── accounts
│   ├── next-app (in plural)
```

If you already have an app that has to be created in apps folder create the folder with the apps name.
Lets give an example with `accounts` app.

1. go to apps folder and create accounts empty folder
2. then type in this command to make apps registered in an empty folder

```
python manage.py startapp accounts apps/accounts
```

3. In settings part (core.configs.app) make sure to register an app like this `apps.accounts` in `PROJECT_APPS` list

4. In created folder there will we `apps.py` inside it the variable `name` has to also include the apps folder before the name of the app. `apps.accounts`

```txt
project_root/
├── apps/                         # all apps folder
│   └── accounts                  # individual app folder
│       └── user                  # sub-app for main model divisions
│           ├── repositories
│           ├── services
│           ├── tests
│           ├── __init__.py
│           ├── admin.py
│           ├── models.py
│           ├── serializers.py
│           ├── urls.py
│           └── admin.py
```

Command to create sub app:
```bash
python manage.py create_subapp user accounts
```

`user` - name of a sub app
`accounts` - name of the app

