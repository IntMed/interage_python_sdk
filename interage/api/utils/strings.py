def remove_lead_and_trail_slash(val):
    if val.startswith('/'):
        val = val[1:]
    if val.endswith('/'):
        val = val[:-1]
    return val
