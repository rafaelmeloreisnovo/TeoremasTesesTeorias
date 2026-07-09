# Ponte Livro Vivo — Teoremas, Teses, Teorias e Conjecturas

> Modo: ponte operacional entre `TeoremasTesesTeorias` e o Livro Vivo RAFAELIA  
> Status inicial: `FORMALIZACAO_READY`  
> Regra: nenhuma afirmação sobe ao altar sem selo, domínio, evidência e limite

## Parábola do altar e dos degraus

O discípulo levou várias placas ao templo.

Em uma estava escrito: teorema.

Em outra: tese.

Em outra: teoria.

Em outra: conjectura.

Ele colocou todas no altar maior.

O mestre desceu as placas e disse:

— O altar não é para nomes altos. É para aquilo que suporta peso.

Depois construiu degraus:

```text
metáfora → definição → hipótese → conjectura → resultado → prova
```

E disse:

— Quem respeita o degrau chega mais alto sem quebrar a escada.

## Invariante

```text
afirmação → domínio → status epistemológico → evidência → limite → próximo teste
```

Forma compacta:

```math
Inv(TTT)=Claim\rightarrow Domain\rightarrow Status\rightarrow Evidence\rightarrow Falsifier
```

## Risco principal

| Risco | Correção |
|---|---|
| teorema sem prova | reclassificar como hipótese/conjectura |
| teoria sem modelo formal | criar domínio e variáveis |
| tese sem evidência | exigir artefato ou argumento |
| conjectura sem falsificador | criar teste ou contraexemplo possível |
| metáfora confundida com ciência | marcar `METAFORA_DIDATICA` |

## Próximos passos

1. Criar `CATALOGO_TEOREMAS_TESES_TEORIAS.md`.
2. Listar cada afirmação com selo epistemológico.
3. Separar matemática clássica de hipótese autoral.
4. Linkar scripts, provas, contraexemplos e artefatos.
5. Criar coluna `como pode falhar`.

## Ficha Livro Vivo

```yaml
repo: rafaelmeloreisnovo/TeoremasTesesTeorias
familia: Papers/Teoria
invariante: "afirmação → domínio → status epistemológico → evidência → limite → próximo teste"
selo: FORMALIZACAO_READY
risco: "afirmações fortes sem prova, domínio ou falsificador"
proximo_passo: "criar catálogo com status, evidência, limite e teste"
```

## Retroalimentar[3]

- **F_ok:** o repositório recebe ponte para separar teorema, tese, teoria, conjectura, hipótese e metáfora.
- **F_gap:** falta inventário real das afirmações e seus artefatos.
- **F_next:** criar `CATALOGO_TEOREMAS_TESES_TEORIAS.md`.
