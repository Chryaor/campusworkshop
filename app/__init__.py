"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpqlf8u9tun42u47ntg-a.oregon-postgres.render.com",
        database="tasks_8cyr",
        user="tasks_8cyr_user",
        password="Dc4RTyW54iu3VRGLs8ijbjwGaymfI1Nj")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
