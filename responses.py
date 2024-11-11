from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower() # Because Python is case-sensitive, let's make everything lowercase

    if lowered == '':
        return 'Ootpa tosi hiljanen tänään kulta... Onko kaikki ok? (｡•́︿•̀｡)'
    elif 'moi' in lowered:
        return 'MOI KULTA MOI MOI MOI MITEN MENEE UWU *punastuu*,,,'
    elif 'heitä d20' in lowered:
        return f'Käskystä, isi uwu Sain heitettyy: {randint(1, 20)}'
    else:
        # Random list of responses
        return choice(['E-eeehh!!! ☆⌒(> _ <)',
                        'Puhutpa kummia, isi (*ﾉωﾉ)',
                        'E-en mä ymmärrä....'])

