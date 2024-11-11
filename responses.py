from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower() # Because Python is case-sensitive, let's make everything lowercase

    # Default responses for when no specific match is found
    default_responses = [
        'E-eeehh!!! ☆⌒(> _ <)',
        'Puhutpa kummia, isi (*ﾉωﾉ)',
        'E-en mä ymmärrä....'
    ]

    # For empty messages
    if lowered == '':
        return 'Ootpa tosi hiljanen tänään kulta... Onko kaikki ok? (｡•́︿•̀｡)'

    # Match different keywords in messages
    match lowered:
        case s if 'moi' in s:
            return 'MOI KULTA MOI MOI MOI MITEN MENEE UWU *punastuu*,,,'
        case s if 'heitä d20' in s:
            return f'Käskystä, isi uwu Sain heitettyy: {randint(1, 20)}'
        case s if any(word in s for word in ['juomaan', 'juoda', 'yksille']):
            return choice(['Tietty! Aina voi ottaa yhden •̀⩊•́',
                           'T-taas... noh, jos nyt tämän kerran ( • ̀ω•́ )✧',
                           'Sinut tietäen menee yl- *yskii* *tukehtuu*'])
        case s if 'huomenta' in s:
            return 'OHAIJJOOO ONII-CHAN ❤ (ɔˆз(ˆ⌣ˆc) Tänäänkin on hyvä päivä alkaa myymään tavaraa!'
        case _:
            return choice(default_responses)




