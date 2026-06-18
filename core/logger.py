from logging.config import dictConfig

def set_logger():
    dictConfig(
        {
            'version': 1,
            'disable_existing_loggers': False,
            "formatters": {
                "default": {
                    "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s "
                }
            },
            "handlers":{
                "file":{
                    "class":"logging.FileHandler",
                    "filename":"app.log",
                    "formatter":"default",
                    "level":"INFO"
                }
            },
            "root":{
                "handlers":["file"],
                "level":"INFO"
            }
        }
    )