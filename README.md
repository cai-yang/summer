# summer

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

```
brew install rabbitmq
```

add ```PATH=$PATH:/usr/local/sbin``` to .profile

```
(sudo )pip install -r requirements.txt
```

```
cd summer
celery -A summer worker --loglevel=info
```

```
cd summer
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

go to ```127.0.0.1:8000/```





