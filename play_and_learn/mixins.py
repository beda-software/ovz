from main.mixins import MainNavigateMixin

__author__ = 'jackdevil'


class PlayAndLearnNavigateMixin(MainNavigateMixin):
    navbar_active = 'play_and_learn'


class ProfessionsNavigateMixin(PlayAndLearnNavigateMixin):
    sub_navbar_active = 'professions'
