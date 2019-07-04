import codecs
from . import ca_runner, msa_runner, tn_runner, ma_runner
from random import randint
import pyarabic.araby as araby
from collections import defaultdict, Counter


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
        gomla = araby.normalize_ligature(gomla)
        gomla_list = araby.tokenize(gomla.replace('_', ''), conditions=araby.is_arabicrange, morphs=araby.strip_tashkeel)

        for token in gomla_list:
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
        counters = defaultdict(Counter)
        for i, line in enumerate(outfile):
            dtokens = line.strip().split(' _ ')
            # print(len(dtokens), dtokens)
            for j, _ in enumerate(dtokens):
                tk = dtokens[j - 1 - i % 7]

                if tk not in ['نهايةجملة', 'بدايةجملة']:
                    counters[j].update([tk])

                if sum(counters[j].values()) >= 7:
                    diacritized_tokens.append(counters[j].most_common(1)[0][0].replace(' ', ''))
                    counters[j].clear()
        else:
            return ' '.join(diacritized_tokens)






