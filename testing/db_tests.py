from database.db import Database
from core.utils import dict_factory


def test_init_db(db: Database = None) -> tuple:
    """
    Tests that the database is initialized correctly.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/store_records.db") if db is None else db

    if db.database_path != "database/store_records.db":
        error = f"Error in test_init_db: Database path is not correct.\n  - Actual: {db.database_path}"
        return False, error
    else:
        return True, "Database path is correct."


def test_get_inventory_exists(db: Database = None) -> tuple:
    """
    Tests that the inventory is not empty.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/store_records.db") if db is None else db
    full_inventory = db.get_full_inventory()

    if len(full_inventory) == 0:
        error = f"Error in test_get_full_inventory: Full inventory is empty.\n  - Actual: {len(full_inventory)}"
        return False, error
    else:
        return True, "Full inventory is not empty."


def test_dict_factory_link(db: Database = None) -> tuple:
    """
    Tests that the row factory is linked to dict_factory.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string,
    """
    db = Database("database/store_records.db") if db is None else db
    row_factory = db.connection.row_factory

    if row_factory != dict_factory:
        error = f"Error in test_dict_factory_link: Row factory is not linked to dict_factory.\n  - Expected: {dict_factory}\n  - Actual: {row_factory}"
        return False, error
    else:
        return True, "Row factory is linked to dict_factory."


def test_check_connection_threaded(db: Database = None) -> tuple:
    """
    Tests that the database connection is not single threaded.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string,
    """

    db = Database("database/store_records.db") if db is None else db
    connection_is_threaded = db.connection.isolation_level is None

    if connection_is_threaded:
        error = f"Error in test_check_connection_single_thread: Connection is single threaded.\n  - Actual: {connection_is_threaded}"
        return False, error
    else:
        return True, "Connection is not single threaded."
    
def test_wadi_rum_description(db: Database = None) -> tuple:
    """
    Tests that the description of wadi rum is correct.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string,
    """
    
    expected_description ="Climb desert dunes to see gorgeous sunsets over Wadi Rum."
    db = Database("database/store_records.db") if db is None else db

    wadi_rum_hike = [item for item in db.get_full_inventory() if item["item_name"] == "Wadi Rum Hike"][0]
    actual = wadi_rum_hike["info"]
    if wadi_rum_hike["info"] != expected_description:
        error = f"Error in test_wadi_rum_description: descrition does not match.\n  - Actual: {actual}"
        return False, error
    else:
        return True, "description is match."
    
def test_petra_description(db: Database = None) -> tuple:
    """
    Tests that the description of petra is correct.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string,
    """
    expected_description ="Visit the the lost city of Petra in all its glory."
    db = Database("database/store_records.db") if db is None else db

    petra = [item for item in db.get_full_inventory() if item["item_name"] == "Trek to Petra"][0]
    actual = petra["info"]
    if petra["info"] != expected_description:
        error = f"Error in test_petra_description: descrition does not match.\n  - Actual: {actual}"
        return False, error
    else:
        return True, "description is match."
    
def test_dana_description(db: Database = None) -> tuple:
    """
    Tests that the description of dana is correct.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string,
    """
    expected_description ="Gaze upon the diverse ecosystems of the Dana Biosphere."
    db = Database("database/store_records.db") if db is None else db

    dana = [item for item in db.get_full_inventory() if item["item_name"] == "Dana Biosphere Hike"][0]
    actual = dana["info"]
    if dana["info"] != expected_description:
        error = f"Error in test_dana_description: descrition does not match.\n  - Actual: {actual}"
        return False, error
    else:
        return True, "description is match."
    
    
    
