import logging
LOG_FORMAT='%(levelname)s-%(asctime)s:%(message)s'
#LOG_FORMAT=f'{levelname}--{asctime}::{message}'
logging.basicConfig(filename='new.log',level=logging.DEBUG,
                    filemode='w',
                    format=LOG_FORMAT)
logger=logging.getLogger()

def run_func(r):
    '''
    r=r*10
    r=r**2
    r=str(r)
    '''
    logger.debug("multiplied by 10")
    r=r*10
    logger.debug("squred")
    r=r**2
    logger.debug("string conversion")
    r=r/0
    logger.debug("return statement")
    return r 
run_func(5)
    