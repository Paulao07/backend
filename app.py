from flask import Flask
from routes.main_routes import main_bp
from routes.usuario_routes import usuario_bp

app = Flask(_name_)
app.secret_key = 'yahoo'

# Registrar os blueprints
