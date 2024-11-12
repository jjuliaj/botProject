from random import choice, randint
from spotify_handler import get_random_track

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
        case s if any(word in s for word in ['musiikkia', 'biisi', 'musiikki', 'laulu', 'soundtrack']):
            try:
                track = get_random_track()
                return (f"Käskystä! Tässä päivän biisi uwu: "
                        f"*{track['name']}* artistilta {track['artists']}\n"
                        f"Linkki: {track['url']} (´ ω `♡)")
            except Exception as e:
                print(f"Error getting track: {e}")
                return "G-gomen... nyt en keksi biisiä... yritin kyllä (｡•́︿•̀｡)"
        case _:
            return choice(default_responses)




