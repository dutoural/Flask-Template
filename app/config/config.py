"""Global configuration file for the project"""

"""Variable used to configure the flask server"""
flask_config = {
    "host" : "127.0.0.1", #put 0.0.0.0 to broadcast
    # "host" : "0.0.0.0", #put 0.0.0.0 to broadcast
    "port" : 3000,
    "debug" : True
}


"""Database Configuration"""
DB_secretKey = ''
DB_path = 'sqlite:///database.db'

