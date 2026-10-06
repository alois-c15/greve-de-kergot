class Personnage:
    def __init__(self, nom: str, pv: int, force: int) -> None:
        self.nom = nom
        self.pv = pv
        self.force = force

    def attaquer(self, cible: "Personnage") -> None:
        print(f"{self.nom} a attaqué {cible.nom} et a infligé {self.force} dégats")
        cible.pv -= self.force


hero = Personnage("Hero", 50, 10)
monstre = Personnage("Monstre", 15, 5)

hero.attaquer(monstre)
monstre.attaquer(hero)
