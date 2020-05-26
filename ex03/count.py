import re
import string


def text_analyzer(*str_text):
    """
        My magnifyque copié-collé
        Thisfunction counts the number of upper characters,
        lower characters,punctuationand spaces in a given text.
    """

    total_args = len(str_text)
    if total_args > 1:
        print('ERROR')
        return
    if total_args == 1:
        evaluate_str = str_text[0]
    else:
        print('What is the text to analyze?')
        evaluate_str = input()
    str_spaces = len(re.findall('[ \t\n\r\f\v]', evaluate_str))
    str_len = len(evaluate_str)
    str_uppers = len(re.findall('[A-Z]', evaluate_str))
    str_lowers = len(re.findall('[a-z]', evaluate_str))
    str_p = len(re.findall(r"[\"!#$%&'(),-./:;<=>?@[\]^_`{|}~]", evaluate_str))
    result = f"""The text contains {str_len} characters:
    \n- {str_uppers} upper letters
    \n- {str_lowers} lower letters
    \n- {str_p} punctuation marks
    \n- {str_spaces} spaces"""
    print(result)
