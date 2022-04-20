import json


def find_preferred_source(json_file):
    f = open(json_file)
    resource_file = json.load(f)
    f.close()
    preferred_source = []
    for item in resource_file:
        if resource_file[item]['preferred_source'] == "yes":
            preferred_source.append(item)
    return preferred_source
