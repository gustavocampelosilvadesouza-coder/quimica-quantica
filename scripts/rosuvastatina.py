from pyscf import gto, dft

print("--- ANÁLISE DA ROSUVASTATINA (Inibidor da HMG-CoA Redutase) ---")

# Coordenadas aproximadas da Rosuvastatina (Forma Ácida)
# Esta geometria representa a conformação bioativa (como ela fica na enzima)
rosuva_geom = '''
S   2.435   -1.162    0.198
O   2.186   -2.227    1.168
O   3.272   -0.038    0.697
N   0.970   -0.455   -0.129
C   3.239   -1.890   -1.198
C  -0.088   -0.563    0.781
N  -1.289   -0.046    0.505
C  -1.077    0.957   -0.413
N  -2.186    1.296   -0.966
C  -3.155    0.467   -0.347
C  -2.583   -0.366    0.575
C  -3.231   -1.425    1.408
C   1.146    0.282   -1.378
C   0.841    1.642   -1.442
C   1.621   -0.395   -2.493
C   1.018    2.327   -2.637
H   0.457    2.164   -0.570
C   1.791    0.289   -3.684
H   1.849   -1.453   -2.434
C   1.492    1.650   -3.757
H   0.776    3.385   -2.688
H   2.158   -0.240   -4.551
F   1.662    2.316   -4.912
C  -0.021    1.637   -0.893
C  -4.577    0.548   -0.707
C  -5.163    1.810   -0.654
C  -5.405   -0.583   -1.121
C  -6.526    1.936   -0.994
H  -4.538    2.695   -0.342
C  -6.767   -0.456   -1.464
H  -4.968   -1.572   -1.171
C  -7.332    0.803   -1.402
H  -6.963    2.923   -0.947
H  -7.394   -1.343   -1.785
H  -8.397    0.903   -1.674
C  -2.492   -1.365    2.756
H  -2.628   -2.392    0.916
H  -4.288   -1.164    1.503
H  -2.973   -2.126    3.385
H  -2.730   -0.407    3.228
H  -1.417   -1.491    2.607
H   4.225   -2.261   -0.905
H   2.607   -2.750   -1.455
H   3.332   -1.221   -2.054
'''

mol = gto.M(
    atom = rosuva_geom,
    basis = 'sto-3g',  # Base leve. Se usar 6-31g vai demorar muito!
    charge = -1,
    verbose = 0
)

print(f"Molécula construída! Elétrons: {mol.nelectron}")
print("Esta molécula é GRANDE. O cálculo pode levar 1 ou 2 minutos...")

# Cálculo de Energia
mf = dft.RKS(mol)
mf.xc = 'b3lyp'
energia = mf.kernel()

print("-" * 30)
print(f"Energia Total: {energia:.5f} Hartree")
print("-" * 30)

# Análise do Dipolo (A "polaridade" da chave)
dipolo = mf.dip_moment()
print(f"Momento de Dipolo (Debye): {dipolo}")
print("\nInterpretação:")
print("O vetor dipolo mostra para onde os elétrons estão sendo puxados.")
print("Isso orienta a molécula a entrar na enzima de frente ou de costas.")

# Análise de Cargas (Onde estão os pontos de contato?)
print("\nCargas Parciais (Mulliken) nos átomos principais:")
mf.analyze()
