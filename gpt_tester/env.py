import os
from dotenv import load_dotenv


class Env:

    def __init__(self):

        _ = load_dotenv()
        self.OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

        pass
