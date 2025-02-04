import json
import os

CONFIG_FILE_PATH = "/etc/device_config.json"

def load_device_config(config_path=CONFIG_FILE_PATH):
    """
    Loads the device configuration from a JSON file.

    :param config_path: Path to the configuration file.
    :return: A dictionary containing the configuration.
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    with open(config_path, "r") as config_file:
        try:
            config = json.load(config_file)
            return config
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding configuration file: {e}")

def save_device_config(config, config_path=CONFIG_FILE_PATH):
    """
    Saves the device configuration to a JSON file.

    :param config: A dictionary containing the configuration.
    :param config_path: Path to the configuration file.
    """
    try:
        with open(config_path, "w") as config_file:
            json.dump(config, config_file, indent=4)
    except Exception as e:
        raise IOError(f"Error saving configuration file: {e}")

def get_config_value(key, config_path=CONFIG_FILE_PATH):
    """
    Retrieves a specific configuration value.

    :param key: The key of the configuration value to retrieve.
    :param config_path: Path to the configuration file.
    :return: The value of the specified key.
    """
    config = load_device_config(config_path)
    return config.get(key)

def set_config_value(key, value, config_path=CONFIG_FILE_PATH):
    """
    Sets a specific configuration value.

    :param key: The key of the configuration value to set.
    :param value: The value to set for the specified key.
    :param config_path: Path to the configuration file.
    """
    config = load_device_config(config_path)
    config[key] = value
    save_device_config(config, config_path)
