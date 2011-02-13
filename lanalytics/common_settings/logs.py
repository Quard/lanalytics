import logging
import os

DIRNAME = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) +  '/../')

#Configure logging
LOGFILE = "./../project.log"
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.path.join(DIRNAME, LOGFILE),
                    filemode='w')

logging.info("Project Started")
