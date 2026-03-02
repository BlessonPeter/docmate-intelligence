import yaml

def load_config(config_path: str = "config/config.yaml") -> dict:
    """
    Load and return the configuration from a YAML file.
    """
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
        #print(f"Config loaded from {config_path}: {config}")
        print(config)
    return config
   

load_config( "config/config.yaml")