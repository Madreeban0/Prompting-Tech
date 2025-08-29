from datetime import datetime

class TokenLogger:
    def __init__(self, log_file='token_usage.log'):
        self.log_file = log_file

    def log_tokens(self, prompt, token_count):
        timestamp = datetime.now().isoformat()
        log_entry = f"{timestamp} | Prompt: {prompt} | Tokens Used: {token_count}\n"
        with open(self.log_file, 'a') as f:
            f.write(log_entry)

    def get_token_usage(self):
        try:
            with open(self.log_file, 'r') as f:
                return f.readlines()
        except FileNotFoundError:
            return []

    def clear_log(self):
        open(self.log_file, 'w').close()