import numpy as np
from pyscf import gto, scf, dft

# Definição da Geometria (Coordenadas Cartesianas em Angstrom)
# Estrutura planar (Cs) construída com comprimentos de ligação padrão
benzoico_geom = '''
C   0.0000   0.0000   0.0000  # C1 (ligado ao carboxila)
C   1.3900   0.0000   0.0000  # C2 (anel)
C   2.0850   1.2038   0.0000  # C3 (anel)
C   1.3900   2.4075   0.0000  # C4 (oposto)
C   0.0000   2.4075   0.0000  # C5 (anel)
C  -0.6950   1.2038   0.0000  # C6 (anel)
H   1.9300  -0.9353   0.0000  # H (C2)
H   3.1650   1.2038   0.0000  # H (C3)
H   1.9300   3.3428   0.0000  # H (C4)
H  -0.5400   3.3428   0.0000  # H (C5)
H  -1.7750   1.2038   0.0000  # H (C6)
C  -0.7500  -1.2990   0.0000  # C (Carboxila)
O  -0.1288  -2.3751   0.0000  # O=C (Carbonila)
O  -2.1000  -1.2990   0.0000  # O-H (Hidroxila)
H  -2.4500  -2.2000   0.0000  # H (do OH)
'''

print("Construindo molécula de Ácido Benzoico...")

mol = gto.M(
    atom = benzoico_geom,
    basis = 'sto-3g',    # Base simples para teste rápido
    charge = 0,
    spin = 0,
    symmetry = True      # O PySCF tenta detectar a simetria (Cs)
)

print(f"Simetria detectada: {mol.topgroup}")
print(f"Número de elétrons: {mol.nelectron}")

# Cálculo DFT (Mais preciso que Hartree-Fock para orgânicos)
print("\nIniciando cálculo DFT (B3LYP)...")
mf = dft.RKS(mol)
mf.xc = 'b3lyp'  # O funcional mais famoso da química orgânica
energia = mf.kernel()

print(f"\nEnergia Total: {energia:.5f} Hartree")

# Análise de Cargas (Mulliken)
print("\nCargas de Mulliken (Onde estão os elétrons?):")
mf.analyze()

