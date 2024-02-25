from gpt_tester.env import Env
import openai
from tenacity import retry, wait_random_exponential, stop_after_attempt


@retry(wait=wait_random_exponential(min=1, max=10), stop=stop_after_attempt(2))
def generate(prompt: str, gpt_model_name: str, *args, **kwargs) -> str:

    env = Env()
    openai.api_key = env.OPENAI_API_KEY

    response = openai.ChatCompletion.create(
        model=gpt_model_name,
        messages=[{"role": "user", "content": prompt}],
        *args,
        **kwargs
    )
    return response["choices"][0]["message"]["content"]
