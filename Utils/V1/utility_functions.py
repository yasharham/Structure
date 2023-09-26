import os
from Constant.general import COMPLIANCE
from Utils.V1.config_reader import configure
import datetime


def getPath(path):
    '''
    get directory path

    :param path:
    :return directory path:
    '''
    loc = os.getcwd().split(COMPLIANCE)
    directory = os.path.join(loc[0],configure.get('PATH',path))
    return directory


def dateConverter(date, input_format, output_format):
    '''
    convert date to specific format

    :param date:
    :param input_format:
    :param output_format:
    :return fomated date:
    '''
    if type(date) == type("date"):
        date_obj = datetime.datetime.strptime(date, input_format)
        date_output = date_obj.strftime(output_format)
    else:
        date_output = date.strftime(output_format)
    return date_output

current_date = datetime.date.today()
now = datetime.datetime.now()