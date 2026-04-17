import numpy as np
import matplotlib.pyplot as plt

# =========================
# PARÂMETROS
# =========================
N = 42              # número de pontos no círculo
K = 5               # passo modular
ITER = 5000         # número de conexões

# =========================
# PONTOS NO CÍRCULO
# =========================
theta = np.linspace(0, 2*np.pi, N, endpoint=False)
points = np.stack([np.cos(theta), np.sin(theta)], axis=1)

# =========================
# GERAR CONEXÕES
# =========================
edges = []

x = 0
for i in range(ITER):
    y = (x + K) % N
    edges.append((x, y))
    x = y

# =========================
# MÉTRICA 1 — DENSIDADE ANGULAR
# =========================
density = np.zeros(N)

for a, b in edges:
    density[a] += 1
    density[b] += 1

density /= np.max(density)

# =========================
# MÉTRICA 2 — SIMETRIA
# =========================
symmetry_error = 0
for i in range(N//2):
    symmetry_error += abs(density[i] - density[(i + N//2) % N])

symmetry_error /= (N//2)

# =========================
# MÉTRICA 3 — COMPLEXIDADE
# =========================
unique_edges = len(set(edges))
complexity = unique_edges / ITER

# =========================
# VISUALIZAÇÃO
# =========================
plt.figure(figsize=(8,8), facecolor="black")

# desenhar conexões
for a, b in edges:
    x1, y1 = points[a]
    x2, y2 = points[b]
    plt.plot([x1, x2], [y1, y2], color="cyan", alpha=0.02)

# desenhar pontos
plt.scatter(points[:,0], points[:,1], c=density, cmap="plasma", s=30)

plt.axis("off")
plt.title(f"N={N} | K={K} | SymErr={symmetry_error:.4f} | Comp={complexity:.4f}", color="white")

plt.show()

# =========================
# OUTPUT NUMÉRICO
# =========================
print("=== RESULTADOS ===")
print("Simetria (erro):", symmetry_error)
print("Complexidade:", complexity)
print("Densidade média:", np.mean(density))
