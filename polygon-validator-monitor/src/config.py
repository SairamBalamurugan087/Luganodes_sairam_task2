import yaml

class Config:
    def __init__(self, config_path: str):
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)

        self.validator_address = config['validator_address']
        self.rpc_endpoint = config['rpc_endpoint']
        self.checkpoint_api = config['checkpoint_api']
        self.heimdall_api = config['heimdall_api']
        self.telegram_bot_token = config['telegram_bot_token']
        self.telegram_chat_id = config['telegram_chat_id']
        self.check_interval = config['check_interval']
        self.max_height_difference = config['max_height_difference']
