# Treino Adaptativo

Monta treinos de academia pelo seu objetivo, troca o plano a cada 3 semanas e recalcula cardio, séries e meta de kcal a partir dos treinos registrados (kcal, minutos, esforço e peso).

- `index.html`: fonte do app (também publicado como artifact do Claude).
- `docs/`: versão instalável (PWA) servida pelo GitHub Pages. Funciona offline e guarda os dados no aparelho.

Depois de editar `index.html`, rode `python3 scripts/build-pwa.py` para atualizar `docs/index.html`.
