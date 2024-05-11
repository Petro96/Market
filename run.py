from market import app

import os

from dotenv import load_dotenv

load_dotenv()



if __name__ =='__main__':
    app.run(host=os.environ.get('APP_HOST'),
            port=os.environ.get('FLASK_DEVELOPMENT_PORT'),
            debug=os.environ.get('FLASK_DEBUG'))