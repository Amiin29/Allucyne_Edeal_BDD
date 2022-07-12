Feature: Déconnexion d'une session a partir de la page d'accueil Moodle

  Scenario: je suis dans Moodle et je click sur le boutton de déconnexion
    Given Je suis dans la page moodle
    When CLiquer sur Déconnexion
    Then Session actuelle est fermée et la page d'accueil s'affiche