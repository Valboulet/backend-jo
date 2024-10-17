#!/bin/sh

if [ "$DATABASE" = "jo2024" ]; then
    echo "Checking if database is running..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
        sleep 0.1
    done 

    echo "The database is up and running :)"
fi

# Apply migrations
if [ "$RUN_MIGRATIONS" = "true" ]; then
    python manage.py makemigrations
fi
python manage.py migrate

# Execute the command passed as arguments (like `runserver`)
exec "$@"