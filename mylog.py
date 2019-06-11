import logging
i = 0


# 循环写日志
while(i < 10000):
    i += 1
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                    #    datefmt='%Y-%m-%d,%H:%M:%S.%f',
                        filename='myapp.log',
                        filemode='w')


    logging.debug('This is debug message')
    logging.info('This is info message')
    logging.warning('This is warning message')





