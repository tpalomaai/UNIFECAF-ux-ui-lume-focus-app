# Design System / Library Figma — Lume

## Regras de ouro
- Nenhum hex, tamanho de fonte ou espaçamento "solto" nas telas: só **Variables** e **Text Styles**.
- Toda tela é montada só com **instâncias** de componentes.
- Tudo em **Auto Layout**.
- Nomes em português, padrão `Categoria/Nome`.

## Páginas do arquivo
| Página | Conteúdo |
|---|---|
| 📖 Capa | Nome, versão, link do README |
| 🎨 Fundamentos | Paleta, tipografia, espaçamento, raios, ícones |
| 🧩 Componentes | Todos os componentes com variantes |
| 🔲 Wireframes | 6 telas em cinza |
| 📱 Telas | 6 telas finais |
| 🗂 Arquivo | Versões descartadas |

## Variables — `Primitivos`
| Variável | Valor |
|---|---|
| `indigo/700` | #3730A3 |
| `indigo/900` | #1B1846 |
| `indigo/300` | #6E69D6 |
| `estrela/400` | #FFD43B |
| `estrela/100` | #FFF3BF |
| `rosa/400` | #EC6FA8 |
| `rosa/800` | #A3215F |
| `neutro/0` | #FFFFFF |
| `neutro/500` | #5A5784 |
| `fundo/creme-lunar` | #FFF8EC |

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
| `destaque/progresso` | estrela/400 | Timer, conquistas, "Me distraí" |
| `destaque/progresso-fundo` | estrela/100 | Chips de duração |
| `destaque/retomar` | rosa/400 | Barra do "Continuar daqui" |
| `destaque/retomar-texto` | rosa/800 | Título do "Continuar daqui" |

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
| `Timer/Número` | Lexend | 38 / Medium / 100% |

## Componentes
| Componente | Propriedades / Variantes |
|---|---|
| `Botão` | Tipo: Primário · Secundário · Destaque — Estado: Padrão · Pressionado · Desabilitado — Ícone: sim/não |
| `Botão/Grande` | Ação principal "Nova sessão" |
| `Input` | Estado: Vazio · Preenchido · Foco · Erro |
| `Chip/Duração` | Valor: 15 · 25 · 45 — Selecionado: sim/não |
| `Card/Tarefa` | Texto + Chip/Duração |
| `Card/ContinuarDaqui` | Com texto · Vazio |
| `Card/Métrica` | Tipo: Minutos · Distrações |
| `Timer` | Progresso: 0 · 25 · 50 · 75 · 100 |
| `Header/Saudação` | Mascote + saudação + subtítulo |
| `Mascote` | Humor: Feliz · Focado · Comemorando |
| `Barra/Topo` | Com voltar · Sem voltar |

## Ordem de construção
1. Variables (Primitivos → Tokens → Medidas)
2. Text Styles
3. Componentes atômicos: Botão, Chip, Input
4. Componentes compostos: Cards, Timer, Header
5. Montar as 6 telas com instâncias

## Contraste (verificar na F5)
| Par | Uso |
|---|---|
| indigo/900 sobre creme #FFF8EC | texto principal |
| branco sobre indigo/700 | botão primário |
| #3D2F00 sobre estrela/400 | botão "Me distraí" |
| rosa/800 sobre branco | título "Continuar daqui" |
