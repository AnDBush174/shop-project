# language.py
class LanguageMixin(object):

    def __init__(self):
        self.language = 'EN'

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'
