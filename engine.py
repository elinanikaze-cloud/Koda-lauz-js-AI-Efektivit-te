"""Koda lauzēja algoritma funkcijas (binārā meklēšana).

Šajā failā ir tikai aprēķini - bez input() un print().
"""


def aprekinat_minejumu(apaksa, augsa):
    """Atgriež diapazona vidējo skaitli - nākamo minējumu."""
    return (apaksa + augsa) // 2


def atjaunot_robezas(apaksa, augsa, minejums, atbilde):
    """Atgriež jaunās robežas pēc spēlētāja atbildes.

    "l" - skaitlis ir lielāks, tāpēc apakšējā robeža ir minejums + 1.
    "m" - skaitlis ir mazāks, tāpēc augšējā robeža ir minejums - 1.
    """
    if atbilde == "l":
        apaksa = minejums + 1
    elif atbilde == "m":
        augsa = minejums - 1
    return apaksa, augsa


def ir_pretruna(apaksa, augsa):
    """Atgriež True, ja diapazonā vairs nav neviena skaitļa."""
    return apaksa > augsa
