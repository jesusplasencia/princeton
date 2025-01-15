import helpers;

__all__ = ['helpers']

import logging;

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Define package metadata
__version__ = '1.0.0'
__author__ = 'Jesus Plasencia'
__description__ = 'A collection of helper and more functions'

# Option 4: Initialize package-wide resources
GLOBAL_CONFIG = {
    'debug_mode': False,
    'max_random_number': 1000,
    'default_list_size': 10
}

def setup_package():
    """Initialize any package-wide resources or configurations"""
    print(f"Initializing package version {__version__}")
    # Add any initialization code here

# Run setup when package is imported
setup_package()