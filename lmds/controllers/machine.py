# Put settings in this file that will change depending on the
# machine, such as database hosts and external resource paths.
# One of these files exist for each enviornment this app will run in.

debug = True
cache = 'dummy' # or 'redis', 'locmem', 'database', or 'memcache'.

session_store = 'database' # or a `keyvalue` object.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'database.sqlite3',             # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}
