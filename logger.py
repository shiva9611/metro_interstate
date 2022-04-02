import logging as lg

lg.basicConfig(filename='app.log', filemode='a', level=logging.DEBUG,format='%(levelname)s:%(asctime)s %(message)s')