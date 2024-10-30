# manage.py
from app import app, db
from flask_migrate import Migrate, upgrade, migrate

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run()