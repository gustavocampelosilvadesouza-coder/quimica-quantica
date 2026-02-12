from pyscf import gto, scf
import numpy as np
import matplotlib.pyplot as plt
# Distâncias H–H (em Å)
distancias = np.linspace(0.5, 2.5, 9)

energias = []

for R in distancias:
    mol = gto.M(
        atom=f"H 0 0 0; H 0 0 {R}",
        basis="sto-3g"
    )

    mf = scf.RHF(mol)
    energia = mf.kernel()

    energias.append(energia)

    print(f"R = {R:.2f} Å | Energia = {energia}")
# Salvar resultados
with open("results/h2_curve.dat", "w") as f:
    f.write("# R (Å)    Energia (Hartree)\n")
    for R, E in zip(distancias, energias):
        f.write(f"{R:.6f}  {E:.10f}\n")
plt.plot(distancias, energias, marker="o")
plt.xlabel("Distância H–H (Å)")
plt.ylabel("Energia (Hartree)")
plt.title("Curva de dissociação do H₂ (HF/STO-3G)")
plt.grid(True)
plt.show()
