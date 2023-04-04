import src.db.db_util as db_util

# db = db_init.create_connection_to_db()


def get_login_code_from_db(phone='0500000000'):
    """
    self explainatory
    :return:
    """
    db = db_util.create_connection_to_db()
    rec = db['users'].find_one({'phone': phone})
    code = rec.get('loginCode')

    return code


print(get_login_code_from_db(phone='0500000000'))


def get_value(collection, col, identifier):
    """
    get a value from a column within a collection
    :param collection:
    :param col:
    :return:
    """
    db = db_util.create_connection_to_db()
    rec = db[collection].find_one({col: identifier})
    value = rec.get(col)

    return value


def get_record(collection, col, identifier):
    db = db_util.create_connection_to_db()
    rec = db[collection].find_one({col: identifier})
    return rec

# print(get_value('products', 'name', 'OG Kush'))


def get_product_supplier(item_name):
    item_name = str(item_name)
    db = db_util.create_connection_to_db()
    rec = db['products'].find_one({'name': item_name})
    print(rec)
    return rec['storeId']


# print(get_product_supplier("OG Kush"))

def get_active_products():
    db = db_util.create_connection_to_db()
    rec = db['products'].find({'active': True}).limit(21)
    for r in rec:
        print(r)
    # db_util.pd.set_option('display.width', 1000)
    # db_util.pd.set_option('display.max_columns', 20)
    # df = db_util.pd.DataFrame(list(rec))
    # df = df.drop('_id', axis=1)
    # print(df)

# get_active_products()


def get_user_data(phone):
    db = db_util.create_connection_to_db()
    rec = db['users'].find_one({'phone': phone})
    print(rec)

# get_user_data(phone="0500000000")

# get_records('products', 'storeId', 'fhpplkka71tme')


def get_departments():
    db = db_util.create_connection_to_db()
    rec = db['departments'].find({'active': True})
    for r in rec:
        print(r)
