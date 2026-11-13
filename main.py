"""Spēle "Koda lauzējs": dators min spēlētāja iedomāto skaitli."""

from engine import aprekinat_minejumu, atjaunot_robezas, ir_pretruna


def spelet():
    """Izspēlē vienu spēles partiju terminālī."""
    apaksa = 1
    augsa = 100
    minejumi = 0

    print("=== Koda lauzējs: AI Efektivitāte ===")
    print("Iedomājies veselu skaitli no 1 līdz 100, un es to uzminēšu.")
    print("Atbildi ar vienu burtu:")
    print("  l - tavs skaitlis ir lielāks")
    print("  m - tavs skaitlis ir mazāks")
    print("  p - pareizi, es uzminēju")
    print()

    while True:
        minejums = aprekinat_minejumu(apaksa, augsa)
        atbilde = input(f"Vai tavs skaitlis ir {minejums}? (l/m/p): ")
        atbilde = atbilde.strip().lower()

        if atbilde != "l" and atbilde != "m" and atbilde != "p":
            print("Nederīga atbilde!")
            continue

        minejumi = minejumi + 1

        if atbilde == "p":
            print(f"Uzminēju! Tavs skaitlis ir {minejums}.")
            print(f"Man vajadzēja {minejumi} minējumus.")
            break

        apaksa, augsa = atjaunot_robezas(apaksa, augsa, minejums, atbilde)

        if ir_pretruna(apaksa, augsa):
            print("Tavas atbildes bija pretrunīgas - šķiet, ka tu krāpies!")
            print("Spēle beigusies.")
            break


if __name__ == "__main__":
    spelet()
