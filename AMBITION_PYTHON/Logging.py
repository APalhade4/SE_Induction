# r – open for reading
# w – open for writing, creates a new file if it does not exist or truncates the file if it exists.
# x - Opens a file for exclusive creation. If the file already exists, the operation fails.
# a – Opens a file for appending at the end of the file without truncating it.


import logging

logging.basicConfig(filename="Ambition.log", format='%(asctime)s %(message)s', filemode='a')
logging = logging.getLogger("Loggings")

function = lambda a : a + 5

logging.setLevel(1)

logging.debug ("This is Dubug msg")
logging.info ("This is Info  msg")
logging.warning (f"This is Warning msg due to lack of information in {function}")
logging.error ("This is error msg")
logging.critical ("This is critical msg")

# By default level is set to Warning.




















