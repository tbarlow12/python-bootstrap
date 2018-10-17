# Enables 'from example_module import Multiplier'
# instead of 'from example_module.multiplier import Multiplier'
# The noqa comment next to the import tells flake8 to
# ignore the unused import
from .multiplier import Multiplier  # noqa: F401
