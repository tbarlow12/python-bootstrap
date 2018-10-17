from dotenv import load_dotenv
# Enables loading of values into environment
# variables from .env file.
load_dotenv()

# Example .env file:
'''
KEY1=VALUE1
KEY2=VALUE2
'''
# Accessed as:
'''
>>> os.environ['KEY1']
>>> VALUE1
'''
