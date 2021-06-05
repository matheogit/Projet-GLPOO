from model.database import DatabaseEngine
from model.store import Store
from exceptions import ResourceNotFound
from model import *

from view.main_view import MainView


def main():
   # Init db
    database_engine = DatabaseEngine(url='sqlite:///shop.db')
    database_engine.create_database()

    # Database session is created when opening the app. All data will be commit in database at the end of the program.
    with database_engine.new_session() as db_session:
        # Init store object
        logiciel = Store(db_session)

        # Feed admin
        try:
            logiciel.user().get_by_username('admin')
        except ResourceNotFound:
            admin = Admin(username="admin", firstname="admin", lastname="admin", email="contact@shop.fr", password="AZERTY", gender="admin", age="20")
            db_session.add(admin)

        try:
            # Run main view
            MainView(logiciel).show()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
