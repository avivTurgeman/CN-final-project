from PL_player import PL_player

# [name,rating,Team, position, goals, assists]
data = [
    # Manchester City F.C.
    PL_player("Erling Haaland", 7.8, "MCFC", "CF", 5, 0),
    PL_player("Julián Álvarez", 7.2, "MCFC", "CF", 2, 2),
    PL_player("Jack Grealish", 7.3, "MCFC", "LF", 0, 0),
    PL_player("Ilkay Gündoğan", 7.2, "MCFC", "CM", 0, 1),
    PL_player("Rodri Hernández", 6.8, "MCFC", "CM", 0, 0),
    PL_player("Phil Foden", 7.4, "MCFC", "AM", 1, 0),
    PL_player("Rico Lewis", 7.2, "MCFC", "RB", 1, 0),
    PL_player("Nathan Aké", 7.0, "MCFC", "CB", 0, 0),
    PL_player("Ruben Dias", 7.2, "MCFC", "CB", 1, 0),
    PL_player("Manuel Akanji", 7.0, "MCFC", "CB", 0, 0),
    PL_player("Ederson Moraes", 7.0, "MCFC", "GK", 0, 0),

    # Liverpool F.C.
    PL_player("Mohamed Salah", 8.0, "Liverpool", "RF", 8, 2),
    PL_player("Roberto Firmino", 7.1, "Liverpool", "CF", 2, 1),
    PL_player("Cody Gakpo", 7.1, "Liverpool", "LF", 0, 1),
    PL_player("James Milner", 6.1, "Liverpool", "CM", 0, 0),
    PL_player("Jordan Henderson", 6.9, "Liverpool", "CM", 0, 1),
    PL_player("Fabinho", 6.5, "Liverpool", "CM", 0, 0),
    PL_player("Alexander Arnold", 7.2, "Liverpool", "RB", 1, 0),
    PL_player("Virgil van Dijk", 6.8, "Liverpool", "CB", 0, 0),
    PL_player("Joel Matip", 7.2, "Liverpool", "CB", 1, 0),
    PL_player("Andrew Robertson", 7.0, "Liverpool", "LB", 0, 2),
    PL_player("Alisson Becker", 6.5, "Liverpool", "GK", 0, 0),

    # Real Madrid F.C.
    PL_player("Vinicius Júnior", 7.7, "RMFC", "LF", 6, 2),
    PL_player("Karim Benzema", 7.6, "RMFC", "CF", 2, 1),
    PL_player("Rodrygo", 7.8, "RMFC", "RF", 3, 2),
    PL_player("Luka Modric", 7.4, "RMFC", "CM", 2, 1),
    PL_player("Camavinga", 6.5, "RMFC", "CM", 0, 0),
    PL_player("Valverde", 7.9, "RMFC", "CM", 2, 2),
    PL_player("David Alaba", 6.9, "RMFC", "CB", 0, 0),
    PL_player("Antonio Rüdiger", 7.0, "RMFC", "CB", 1, 0),
    PL_player("Éder Militão", 7.1, "RMFC", "CB", 1, 0),
    PL_player("Daniel Carvajal", 6.9, "RMFC", "RB", 0, 2),
    PL_player("Thibaut Courtois", 7.2, "RMFC", "GK", 0, 0),

    # Paris Saint-Germain F.C.
    PL_player("Kylian Mbappe", 7.8, "PSG", "CF", 7, 3),
    PL_player("Lionel Messi", 8.4, "PSG", "RF", 4, 4),
    PL_player("Neymar", 7.6, "PSG", "LF", 2, 2),
    PL_player("Carlos Soler", 7.1, "PSG", "CM", 1, 0),
    PL_player("Marco Verratti", 6.5, "PSG", "CM", 0, 1),
    PL_player("Fabián Ruiz", 6.6, "PSG", "CM", 0, 0),
    PL_player("Nuno Mendes", 6.8, "PSG", "LB", 1, 0),
    PL_player("Sergio Ramos", 6.9, "PSG", "CB", 0, 0),
    PL_player("Marquinhos", 6.8, "PSG", "CB", 0, 0),
    PL_player("Achraf Hakimi", 6.7, "PSG", "RB", 0, 2),
    PL_player("Donnarumma", 6.7, "PSG", "GK", 0, 0),

    # FC Bayren Munich
    PL_player("Choupo-Moting", 7.3, "FCBM", "CF", 3, 0),
    PL_player("Sadio Mané", 7.5, "FCBM", "LF", 3, 1),
    PL_player("Kingsley Coman", 7.7, "FCBM", "LF", 1, 1),
    PL_player("Leroy Sané", 7.9, "FCBM", "RF", 4, 1),
    PL_player("Leon Goretzka", 7.3, "FCBM", "CM", 2, 3),
    PL_player("Joshua Kimmich", 7.9, "FCBM", "CM", 0, 3),
    PL_player("João Cancelo", 7.3, "FCBM", "RB", 0, 3),
    PL_player("João Cancelo", 7.1, "FCBM", "CB", 0, 0),
    PL_player("Dayot Upamecano", 7.1, "FCBM", "CB", 0, 0),
    PL_player("Benjamin Pavard", 7.3, "FCBM", "RB", 2, 0),
    PL_player("Yann Sommer", 7.9, "FCBM", "GK", 0, 0),

    # FC Porto
    PL_player("Mehdi Taremi", 8.0, "Porto", "CF", 5, 2),
    PL_player("Wenderson Galeno", 7.3, "Porto", "LF", 2, 1),
    PL_player("Pepê", 6.7, "Porto", "LF", 0, 0),
    PL_player("Otavio", 6.3, "Porto", "CM", 0, 2),
    PL_player("Mateus Uribe", 6.7, "Porto", "CM", 1, 0),
    PL_player("Marko Grujić", 6.9, "Porto", "CM", 0, 0),
    PL_player("Iván Marcano", 6.3, "Porto", "CB", 0, 0),
    PL_player("Pepe", 6.9, "Porto", "CB", 0, 0),
    PL_player("Joao Mario", 6.3, "Porto", "LB", 0, 0),
    PL_player("Zaidu Sanusi", 6.9, "Porto", "LB", 1, 0),
    PL_player("Diogo Costa", 7.7, "Porto", "GK", 0, 0)
]
