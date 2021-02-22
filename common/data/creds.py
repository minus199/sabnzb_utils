creds = {
    'addic7ed': {'u': "mrmarket", 'p': "xfpH0vAAO9"},
    'legendastv': {'u': "minus199", 'p': "4zwnDfY05W"},
    'opensubtitles': {'u': "N/A", 'p': "N/A"},
    'omdb_api_key': {'k': "9a741426"} # (minus199 email)    
}


def to_args():
    return [
        "--addic7ed", creds['addic7ed']['u'], creds['addic7ed']['p'], 
        "--legendastv", creds['legendastv']['u'], creds['legendastv']['p'],  
        "--opensubtitles", creds['opensubtitles']['u'], creds['opensubtitles']['p'], 
        "--omdb", creds['omdb_api_key']['k']
    ]