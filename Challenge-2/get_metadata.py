import requests
import json
import logging
import argparse
import os

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)


def expand_tree(url, arr):
    output = {}
    for item in arr:
        new_url = url + item
        r = requests.get(new_url)
        text = r.text
        if item[-1] == "/":
            list_of_values = r.text.splitlines()
            output[item[:-1]] = expand_tree(new_url, list_of_values)
        elif is_json(text):
            output[item] = json.loads(text)
        else:
            output[item] = text
    return output


def get_metadata():
    initial = ["meta-data/"]
    result = expand_tree(metadata_url, initial)
    return result


def get_metadata_json():
    metadata = get_metadata()
    metadata_json = json.dumps(metadata, indent=2, sort_keys=True)
    return metadata_json


def is_json(my_json):
    try:
        json.loads(my_json)
    except ValueError:
        return False
    return True


def gen_dict_extract(func_key, var):
    if hasattr(var, 'items'):
        for k, v in var.items():
            if k == func_key:
                yield v
            if isinstance(v, dict):
                for result in gen_dict_extract(func_key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in gen_dict_extract(func_key, d):
                        yield result


def find_key(func_key):
    metadata = get_metadata()
    return list(gen_dict_extract(func_key, metadata))


def run(user_input, local_key=None):
    if user_input == "all":
        logger.info("===> triggering get_metadata_json function")
        net_data = get_metadata_json()
    elif user_input == "key":
        logger.info("===> triggering find_key function")
        net_data = find_key(local_key)
    else:
        net_data = "None"
        logger.info("Action Unknown")
    logger.info("===> run function completed.")
    return net_data


if __name__ == '__main__':
    metadata_url = 'http://169.254.169.254/latest/'
    parser = argparse.ArgumentParser(description='AWS EC2 Meta Data Key Parser')
    parser.add_argument('-o',
                        choices=['all', 'key'], dest='action_type',
                        help='list meta data for all or specific key (default: %(default)s)', required=True)
    parser.add_argument('-k', action='store', type=str, dest='key',
                        help='''Specific Key , example "ami-id"  ''', required=False)
    parser.add_argument('-v', action='version', version=os.path.basename(__file__) + ' 1.0')
    options = parser.parse_args()
    if options.key:
        key = str(options.key)
    else:
        key = None
    action_type = options.action_type
    logger.info("action_type: " + str(action_type))
    logger.info("key : " + str(key))
    print(run(action_type, key))
