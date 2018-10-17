# Enables 'from example_module_2 import Adder'
# instead of 'from example_module_2.adder import Adder'
# The noqa comment next to the import tells flake8 to
# ignore the unused import
from .adder import Adder  # noqa: F401
