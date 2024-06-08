import gettext
from const import LOCALES_DIR
_ = None
ngettext = None

# Assign localization functions
try:
    translation = gettext.translation('bla', localedir=LOCALES_DIR, languages=['uk'])
    print(f'Got translation: {translation}')
    if translation:
        translation.install()
        _ = translation.gettext
        ngettext = translation.ngettext
except FileNotFoundError:
    pass
if not _:
    _ = gettext.gettext
    ngettext = gettext.ngettext