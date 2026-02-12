from pyscf import gto, dft

print("--- INICIANDO CÁLCULO: ÂNION BENZOATO (C6H5COO-) ---")

# 1. Definir a Molécula (Sem o Hidrogênio ácido!)
mol = gto.M(
    atom = '''
        C   0.0000   0.0000   0.0000
        C   1.3900   0.0000   0.0000
        C   2.0850   1.2038   0.0000
        C   1.3900   2.4075   0.0000
        C   0.0000   2.4075   0.0000
        C  -0.6950   1.2038   0.0000
        H   1.9300  -0.9353   0.0000
        H   3.1650   1.2038   0.0000
        H   1.9300   3.3428   0.0000
        H  -0.5400   3.3428   0.0000
        H  -1.7750   1.2038   0.0000
        C  -0.7500  -1.2990   0.0000
        O  -0.1288  -2.3751   0.0000
        O  -2.1000  -1.2990   0.0000
        # O Hidrogênio ácido foi removido aqui
    ''',
    basis = 'sto-3g',
    charge = -1,   # <--- MUITO IMPORTANTE: Carga negativa
    spin = 0,      # Todos os elétrons emparelhados (Singleto)
    verbose = 0
)

print(f"Molécula montada! Elétrons: {mol.nelectron}")
# Dica: O neutro tinha 64 elétrons.
# Removemos 1 H (1 elétron), ficamos com 63.
# Adicionamos carga -1 (mais 1 elétron), voltamos para 64.
# O sistema continua "closed shell".

# 2. Configurar o Método (DFT - B3LYP)
metodo = dft.RKS(mol)
metodo.xc = 'b3lyp'

# 3. Rodar o Cálculo
print("Calculando energia do ânion...")
energia_anion = metodo.kernel()

print("-" * 30)
print(f"ENERGIA ANION: {energia_anion:.5f} Hartree")
print("-" * 30)
