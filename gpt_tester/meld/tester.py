from typing import Optional
import tiktoken
from Levenshtein import ratio as levenshtein_ratio
from gpt_tester.helper import generate


class MELDTest:
    """
    Creates a MELD test case object from a single text string question: q
    test method generates:
        l: Levenshtein distance-based ratio between actual and predicted text
    """

    def __init__(self, q: str, a: str, openai_model: str):
        self.q = q
        self.a = a
        self.openai_model = openai_model
        self.encoding = tiktoken.encoding_for_model(openai_model)

    def _test(self):
        """
        Split q into two halves: q1 and q2;
        Tokenize q2 using T: t2 = T(q2);
        model response g with q1 as context, temp = 0K;
        Generates k tokens from g where k = |t2|;
        Calculates distance-based ratio between q2 and generated text g:
        """
        self.q1, self.q2 = self.q[: len(self.q) // 2], self.q[len(self.q) // 2 :]
        self.t2 = self._tokenize(self.q2)
        self.g = self._openai_complete(self.q1, len(self.t2))
        self.l = self._distance_function(self.q2, self.g)
        return self.l

    def get_MELD_threshold(self, Y) -> bool:
        """
        Return true if l is greater than test threshold Y
        """
        self.meld_threshold = self.l > Y
        return self.meld_threshold

    def _distance_function(self, s1, s2):
        """
        Caclulate distance ratio between two strings
        s1, s2
        """
        l = levenshtein_ratio(s1, s2)
        return l

    def _tokenize(self, text):
        """
        Return list of byte strings from tiktoken encoder
        """
        encoded_text = self.encoding.encode(text)
        return [
            str(self.encoding.decode_single_token_bytes(token))
            for token in encoded_text
        ]

    def _openai_complete(self, prompt, num_tokens):
        return generate(prompt, gpt_model_name=self.openai_model, max_tokens=num_tokens)
