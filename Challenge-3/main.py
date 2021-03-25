import logging
import argparse
import os

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)


def dictionary_parser(input_1, key):
    try:
        val = input_1[key]
    except Exception as e:
        logger.info(e)
        val = None
    return val


def main(data, key_input):
    logger.info("===> data : " + str(data))
    if '/' in key_input:
        key_input = key_input.split('/')
    else:
        key_input = key_input.split()
    
    logger.info("===> key_input_list : " + str(key_input))
    data_type = True
    if not isinstance(data, dict):
        raise Exception("input data not a valid dictionary")
    while data_type is True:
        if isinstance(data, dict):
            for each in range(len(key_input)):
                data = dictionary_parser(data, key_input[each])
                if data is None:
                    data = "Not a valid key/ nested key"
                if each == 0:
                    data_type = False
        else:
            data_type = False
    return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Nested Key Parser')
    parser.add_argument('-o', action='store', type=str, dest='object',
                        help='''Nested Dictionary object Must be enclosed in double quotes, 
                        example "{'a': {'b': {'c': 'd'}}}"''', required=True)
    parser.add_argument('-k', action='store', type=str, dest='keychain',
                        help='''Key Chain must be separated by '/' or single key should be provided without '/',
                         example multiple = "a/b/c", single = "a" ''', required=True)
    parser.add_argument('-v', action='version', version=os.path.basename(__file__) + ' 1.0')
    options = parser.parse_args()
    local_data = eval(options.object)
    local_key_input = options.keychain
    total_data = main(local_data, local_key_input)
    logger.info("===> output : " + str(total_data))
