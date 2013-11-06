#!/usr/bin/env python
import os
from flask_boilerplate import main

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    main.app.run(port=port)
