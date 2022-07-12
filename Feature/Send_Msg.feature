Feature: Envoie message en tant que administrateur vers un user

  Scenario: Connexion en tant que admin et envoie un message
    Given lancer le chrome Chrome browser
    When Page d'accueil s'affiche et faire le login
    Then Page Home s'affiche
    And Cliquer sur l'icone Mon Compte
    And Cliquer sur Messages personnels
    And Choisir un utilisateur
    And Envoie message
    And Cliquer sur le bouton Envoie message