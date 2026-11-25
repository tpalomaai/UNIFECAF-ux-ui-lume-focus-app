# Design System / Library Figma — Lume

## Regras de ouro
- Nenhum hex, tamanho de fonte ou espaçamento "solto" nas telas: só **Variables** e **Text Styles**.
- Toda tela é montada só com **instâncias** de componentes.
- Tudo em **Auto Layout**.
- Nomes em português, padrão `Categoria/Nome`.

## Páginas do arquivo
> O plano Starter do Figma permite só 3 páginas: o conteúdo é dividido em **seções** dentro delas.

| Página | Seções | Conteúdo |
|---|---|---|
| 🧩 Library | 🎨 Fundamentos · 🧩 Componentes | Paleta, tipografia, espaçamento, raios, ícones · todos os componentes com variantes |
| 🔲 Wireframes | — | 6 telas + 04b (pausada) em cinza |
| 📱 Telas | 📱 Telas finais | 6 telas finais |

Capa (nome, versão, link do README) e Arquivo (versões descartadas) ficam para a **F8**, como seções na página 📱 Telas.

## Variables — `Primitivos`
| Variável | Valor |
|---|---|
| `indigo/700` | #3730A3 |
| `indigo/900` | #1B1846 |
| `indigo/300` | #6E69D6 |
| `estrela/400` | #FFD43B |
| `estrela/100` | #FFF3BF |
| `estrela/900` | #3D2F00 |
| `rosa/400` | #EC6FA8 |
| `rosa/800` | #A3215F |
| `neutro/0` | #FFFFFF |
| `neutro/500` | #5A5784 |
| `fundo/creme-lunar` | #FFF8EC |
| `vermelho/600` | #C23434 (corrigido na F5 — #D23C3C falhava contraste AA sobre `bg/app`: 4,47) |

## Variables — `Tokens` (as telas usam SÓ estes)
| Token | Aponta para | Uso |
|---|---|---|
| `bg/app` | fundo/creme-lunar | Fundo das telas |
| `bg/foco` | indigo/900 | Fundo da tela de sessão |
| `bg/card` | neutro/0 | Cards |
| `texto/principal` | indigo/900 | Texto padrão |
| `texto/secundario` | neutro/500 | Texto de apoio |
| `texto/sobre-acao` | neutro/0 | Texto em botão primário |
| `acao/primaria` | indigo/700 | Botão principal |
| `acao/borda` | indigo/300 | Botão secundário |
| `destaque/progresso` | estrela/400 | Cronômetro, conquistas, "Lembrar depois" |
| `destaque/progresso-fundo` | estrela/100 | Chip "última vez" |
| `destaque/retomar` | rosa/400 | Barra do "Continuar daqui" |
| `destaque/retomar-texto` | rosa/800 | Título do "Continuar daqui" |
| `texto/sobre-destaque` | estrela/900 | Texto sobre amarelo (botão "Lembrar depois") |
| `destaque/erro` | vermelho/600 | Borda + texto do Input em Estado=Erro — **criado na F3, conferir contraste AA na F5** |

## Variables — `Medidas`
| Variável | Valores |
|---|---|
| `espaco/` | xs 4 · sm 8 · md 16 · lg 24 · xl 32 |
| `raio/` | chip 999 · card 14 · botao 16 · tela 24 |
| `toque/minimo` | 48 |

## Text Styles
| Estilo | Fonte | Tamanho / Peso / Altura |
|---|---|---|
| `Display/Saudação` | Sniglet | 24 / Regular / 120% |
| `Título/Tela` | Lexend | 24 / SemiBold / 130% |
| `Título/Seção` | Lexend | 16 / Medium / 140% |
| `Corpo/Padrão` | Lexend | 14 / Regular / 150% |
| `Corpo/Destaque` | Lexend | 14 / SemiBold / 150% |
| `Legenda/Padrão` | Lexend | 12 / Regular / 140% |
| `Cronômetro/Número` | Lexend | 38 / Medium / 100% |

> **Números tabulares:** a Lexend não tem tabular numbers (dígitos de 19,9 a 24,2 px; "00:11:11" = 146 px, "00:00:00" = 162 px). Solução: no componente `Cronômetro`, o número fica numa caixa de **largura fixa 180 px, texto centralizado** — qualquer tempo ocupa o mesmo espaço e nada ao redor se mexe.

## Componentes
| Componente | Propriedades / Variantes |
|---|---|
| `Botão` | Tipo: Primário · Secundário · Destaque — Estado: Padrão · Pressionado · Desabilitado — Ícone: sim/não — Ação de sessão: Pausar · Continuar |
| `Botão/Grande` | "Nova sessão" no Início (secundário; o primário é Retomar, no Card/ContinuarDaqui) |
| `Input` | Estado: Vazio · Preenchido · Foco · Erro |
| `Chip/Tarefa` | Tipo: Nome da tarefa · Última vez |
| `Card/Tarefa` | Nome + "última vez: X min" — Estado: Padrão · Selecionado |
| `Card/ContinuarDaqui` | Onde parei + Próximo passo + botão Retomar — Estado: Com conteúdo · Vazio |
| `Card/Métrica` | Tipo: Tempo de hoje · Última vez · Lembretes |
| `Card/Lembrete` | Texto do lembrete anotado |
| `Cronômetro` | Estado: Rodando · Pausado (sem anel de prazo) — número em caixa fixa 180 px, centralizado |
| `Header/Saudação` | Mascote + saudação + subtítulo |
| `Mascote` | Humor: Feliz · Focado · Comemorando |
| `Barra/Topo` | Com voltar · Sem voltar |

> Na F4, a pausa vira **interactive component** (Change to): `Botão` Pausar ⇄ Continuar e `Cronômetro` Rodando ⇄ Pausado, sem trocar de tela.

## Ordem de construção
1. Variables (Primitivos → Tokens → Medidas)
2. Text Styles
3. Componentes atômicos: Botão, Chip/Tarefa, Input
4. Componentes compostos: Cards, Cronômetro, Header
5. Montar as 6 telas com instâncias

## Contraste — auditoria final (F5, 25/11)
Calculado via fórmula WCAG (luminância relativa), fora do Figma. Mínimo AA: 4,5 para texto normal, 3,0 para elementos gráficos/bordas.

| Par | Uso | Contraste | Resultado |
|---|---|---|---|
| `texto/principal` sobre `bg/app` | Texto padrão | 15,71 | ✅ passa com folga |
| `texto/secundario` sobre `bg/app` / `bg/card` | Texto de apoio | 6,35 / 6,71 | ✅ passa |
| Branco sobre `acao/primaria` | Botão primário | 9,93 | ✅ passa com folga |
| `estrela/900` sobre `estrela/400` / `estrela/100` | Botão e chip "Lembrar depois" | 9,18 / 11,73 | ✅ passa com folga |
| `rosa/800` sobre branco | Título "Continuar daqui" | 7,14 | ✅ passa |
| `estrela/400` sobre `bg/foco` | Progresso no modo foco | 11,64 | ✅ passa com folga |
| `destaque/erro` sobre branco | Borda/texto do Input em erro | 5,48 | ✅ passa com folga (corrigido — ver abaixo) |
| `destaque/erro` sobre `bg/app` | Idem, sobre fundo do app | 5,19 | ✅ passa com folga (corrigido — ver abaixo) |
| `indigo/300` sobre `bg/foco` / `bg/app` | Borda do botão secundário | 3,68 / 4,27 | ✅ passa como borda (mín. 3,0) — nunca usado como texto |
| `rosa/400` sobre branco | Barra decorativa do "Continuar daqui" | 2,84 | ✅ só decorativo, sem texto sobre essa cor |

**Correção aplicada na F5:** `vermelho/600` mudou de `#D23C3C` para **`#C23434`** — o valor antigo falhava sobre `bg/app` (4,47, abaixo do mínimo 4,5). O novo hex mantém o mesmo tom de vermelho e passa com folga nos dois fundos usados pelo `destaque/erro`.

**Conferido na auditoria:** `indigo/300` nunca é usado como cor de texto (só como borda, onde o mínimo é 3,0, não 4,5) e `rosa/400` nunca tem texto sobre si (só a barra decorativa do Card/ContinuarDaqui).
