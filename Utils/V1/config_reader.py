from configparser import ConfigParser
import os
from Constant.general import COMPLIANCE


loc= os.getcwd().split(COMPLIANCE)
path= os.path.join(loc[0],f'{COMPLIANCE}/config.ini')

configure = ConfigParser()
configure.read(path)

