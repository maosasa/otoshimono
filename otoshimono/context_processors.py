import environ
import os

def export_vars(request):
    env = environ.Env()
    if not os.environ.get('HEROKU_ENV'):
        env.read_env('.env.local')
    data = {}
    data['GMAP_APIKEY'] = env('GMAP_APIKEY')
    return data