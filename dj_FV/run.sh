#!/bin/bash

open_browser() {
    sleep 2
    xdg-open "http://127.0.0.1:8000/cale/"
}
python manage.py runserver & open_browser