import codecs
from . import ca_runner, msa_runner, tn_runner, ma_runner
from random import randint


class LastNTokens(object):
    def __init__(self, n):
        # last number of token to be reserved
        self.n = n
        self.session = 0
        self.tokens = list()
        for i in range(n):
            self.tokens.append('بدايةجملة')

    def get_n_tokens(self):
        # return self.tokens[-self.n:]
        return " _ ".join(self.tokens[:])

    def add_tokens_list(self, tokens, sessionid):
        if self.session == sessionid:
            self.tokens.append(tokens)
        else:
            self.session = sessionid
            self.tokens = tokens[:]
        if len(self.tokens) > self.n:
            self.tokens = self.tokens[-self.n:]


def run_diac(gomla, dialect):
    token_list_7 = LastNTokens(7)
    fname = randint(0, 100000)
    with codecs.open(f'diacritizer/userdata/{dialect}/{fname}.fmt', mode='w', encoding='utf-8') as infile:
        for token in gomla.strip().split():
            t = ' '.join(token)
            token_list_7.add_tokens_list(t, 0)
            infile.write(token_list_7.get_n_tokens() + '\n')
        else:
            token_list_7.add_tokens_list('نهايةجملة', 0)
            infile.write(token_list_7.get_n_tokens() + '\n')

            token_list_7.add_tokens_list('نهايةجملة', 0)
            infile.write(token_list_7.get_n_tokens() + '\n')

            token_list_7.add_tokens_list('نهايةجملة', 0)
            infile.write(token_list_7.get_n_tokens() + '\n')

            token_list_7.add_tokens_list('نهايةجملة', 0)
            infile.write(token_list_7.get_n_tokens() + '\n')

            token_list_7.add_tokens_list('نهايةجملة', 0)
            infile.write(token_list_7.get_n_tokens() + '\n')

            token_list_7.add_tokens_list('نهايةجملة', 0)
            infile.write(token_list_7.get_n_tokens() + '\n')

    if dialect == 'ca':
        ca_runner.infer(f"diacritizer/userdata/ca/{fname}.fmt", predictions_file=f"diacritizer/userdata/ca/{fname}.rlt",
            checkpoint_path=None, log_time=False)
    elif dialect == 'msa':
        msa_runner.infer(f"diacritizer/userdata/msa/{fname}.fmt", predictions_file=f"diacritizer/userdata/msa/{fname}.rlt",
            checkpoint_path=None, log_time=False)
    elif dialect == 'tun':
        tn_runner.infer(f"diacritizer/userdata/tun/{fname}.fmt", predictions_file=f"diacritizer/userdata/tun/{fname}.rlt",
            checkpoint_path=None, log_time=False)
    elif dialect == 'mor':
        ma_runner.infer(f"diacritizer/userdata/mor/{fname}.fmt", predictions_file=f"diacritizer/userdata/mor/{fname}.rlt",
            checkpoint_path=None, log_time=False)

    with codecs.open(f'diacritizer/userdata/{dialect}/{fname}.rlt', mode='r', encoding='utf-8') as outfile:
        diacritized_tokens = list()
        for line in outfile:
            diacritized_tokens.append((line.strip().split(' _ ')[-1]).replace(' ', ''))
        else:
            return ' '.join(diacritized_tokens[:-6])






