import mysql.connector

connection_config_dict = {
    'user': 'vova',
    'password': 'Frag#12345',
    'host': '3.122.239.30',
    'database': 'dbrealtor',
    'raise_on_warnings': True,
    #'use_pure': True,
    'autocommit': True,
    'pool_size': 5
}

connection = mysql.connector.connect(**connection_config_dict)