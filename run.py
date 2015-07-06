#!/usr/bin/env python

import os
from app import create_app
from app.models import db

# default to dev config because no one should use this in
# production anyway
env = os.environ.get('SETTINGS_STUDYING', 'prod')
app = create_app('app.settings.%sConfig' % env.capitalize(), env=env)

if __name__ == "__main__":
    app.run(debug=True)
