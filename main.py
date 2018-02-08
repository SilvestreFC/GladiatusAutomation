# Imports;
from selenium import webdriver

import importlib
import sys
from functions import *
from objects import *

USER = __import__(sys.argv[1])
SCRIPT_STABLES = __import__('script_stables')
SCRIPT_EXPEDITIONS = __import__('script_expeditions')

# Create client driver;
puts("Creating web driver")
client = webdriver.Chrome()
client.get(USER.DEFAULT_GLADIATUS_URI)

# Login;
log_in(client,USER,"First time log in")

# 0 - 99 Job scripts;
# 100 - 199 Expedition scripts;

#SCRIPT_STABLES.loop(client, USER) # Work in stables
SCRIPT_EXPEDITIONS.loop(client, USER, 5, 4, 40, True) # Expeditions

