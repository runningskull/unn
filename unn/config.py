editor = 'open {} -a /Applications/iA\ Writer.app'
compass_path = '/Library/Ruby/Gems/1.8/gems/compass-0.12.2/frameworks/compass/stylesheets/'
deploy_command = 's3cmd put --recursive _public/ s3://www.juanpatten.com'


import os, sys
try:
    cwd = os.getcwd()
    sys.path.append(cwd)
    from config_local import *
except:
    pass
