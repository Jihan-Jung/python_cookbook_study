import logging
def set_logger_to_show_info_level(mylogger):  
    mylogger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler('to_info.log')
    file_handler.setFormatter(formatter)
    mylogger.addHandler(file_handler)

def set_basic_config():  
    # Configure the logging system  
    logging.basicConfig(        
        filename='app.log',       
        level=logging.ERROR
    )

if __name__ == '__main__':
    set_basic_config()

    mylogger = logging.getLogger('to_info')
    set_logger_to_show_info_level(mylogger) 

    # Variables (to make the calls that follow work)   
    hostname = 'www.python.org'    
    item = 'spam'    
    filename = 'data.csv'   
    mode = 'r'

    # Example logging calls (insert into your program)    
    while True:
        message = input()

        if message == "debug":
            logging.debug('Got here')
            mylogger.debug('Got here')
        elif message == "info":
            logging.info('Opening file %r, mode=%r', filename, mode)    
            mylogger.info('Opening file %r, mode=%r', filename, mode)    
        elif message == "warning":
            logging.warning('Feature is deprecated')    
            mylogger.warning('Feature is deprecated')    
        elif message == "error":
            logging.error("Couldn't find %r", item)    
            mylogger.error("Couldn't find %r", item)    
        elif message == "criticla":
            logging.critical('Host %s unknown', hostname)    
            mylogger.critical('Host %s unknown', hostname)    