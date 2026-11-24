# CLAUDE.md — Lume (App de Sessão de Foco)

> Leia este arquivo inteiro antes de qualquer tarefa. Ele é a fonte única de verdade do projeto.

## Contexto
- Trabalho UniFECAF: **"Da Ideia à Experiência: Projetando e Prototipando uma Interface Digital com Figma"** (Design de Interação e Interface UX/UI).
- Entregáveis (7,0 pts):
  1. Documento teórico — 1,5 pt (1.1 Problema e Usuário · 1.2 Jornada · 1.3 Estrutura UX · 1.4 Decisões UI · 1.5 Acessibilidade)
  2. Protótipo navegável no Figma + README — 3,5 pts (4–6 telas, interações, design system, organização, link público)
  3. Vídeo pitch ≤ 4 min — 2,0 pts (YouTube não listado)
- Fontes de referência: Figma Learn, Nielsen Norman Group, Material Design, Laws of UX, WCAG.

## Produto
**Lume** — app mobile de sessões curtas de foco para quem tem pouco tempo e se distrai fácil. Ajuda a começar rápido, voltar ao foco quando a mente foge e retomar de onde parou.

### Diferenciais
1. **Continuar daqui** — ao fim da sessão, 1 frase sobre onde parou; aparece na próxima.
2. **Estacionamento de distrações** — botão "Me distraí" anota o pensamento em 1 toque e volta ao timer.
3. **Zero configuração** — só 3 durações (15 / 25 / 45 min) e um botão grande para começar.

### Fluxo principal (6 telas)
01 - Boas-vindas → 02 - Início → 03 - Configurar sessão → 04 - Sessão em andamento ⇄ 05 - Estacionamento de distrações → 06 - Resumo da sessão → 02 - Início

## Decisões travadas (não reabrir sem motivo forte)
| Decisão | Valor |
|---|---|
| Nome | Lume |
| Plataforma | Mobile, frame 390×844 (iPhone 14) |
| Telas | 6 (máx. 7) |
| Direção visual | "Céu de estrelas" refinada |
| Fundo do app | Creme lunar #FFF8EC |
| Fundo modo foco | Noite #1B1846 |
| Ação principal | Índigo #3730A3 |
| Progresso / conquista | Estrela #FFD43B |
| Continuar daqui | Rosa #EC6FA8 (texto #A3215F) |
| Fonte principal | Lexend (criada para facilitar leitura) |
| Fonte de destaque | Sniglet — só logo e saudação |
| Mascote | Estrelinha simples (Feliz · Focado · Comemorando) |

## 🚫 Lista do NÃO
- Não mexer em cor/fonte fora da Library (só via Variables / Text Styles).
- Não criar tela extra sem motivo de fluxo.
- Não fazer animação/refinar mascote antes da F5.
- Não pesquisar referências visuais por mais de 20 min.
- Dúvida estética → opção mais simples + anotar em "Ideias para depois" (PROJECT_OVERVIEW.md).

## Fases
| Fase | Entrega | Timebox | Portão |
|---|---|---|---|
| F0 Setup | Repo e estrutura | 30 min | ✅ concluída |
| F1 UX | docs/01-teorico.md (1.1–1.3) + docs/02-fluxo.md | 2 h | fluxo aprovado |
| F2 Wireframe | 6 telas em cinza no Figma | 1–2 h | telas existem e navegam |
| F3 Library | Variables, Text Styles, Componentes (docs/03-design-system.md) | 2 h | componentes prontos |
| F4 Telas + Protótipo | 6 telas só com instâncias + interações | 3 h | fluxo clicável completo |
| F5 Acessibilidade | Checklist WCAG + doc 1.4–1.5 | 1 h | checklist 100% |
| F6 Textos | README + roteiro do vídeo (reaproveitar doc teórico) | 2 h | revisado |
| F7 Vídeo | Gravação ≤ 4 min | 1 h | link público |

## Library Figma — resumo
Detalhes completos em `docs/03-design-system.md`.
- Variables: `Primitivos` → `Tokens` (telas usam só tokens) → `Medidas`.
- Text Styles: `Display/Saudação`, `Título/Tela`, `Título/Seção`, `Corpo/Padrão`, `Corpo/Destaque`, `Legenda/Padrão`, `Timer/Número`.
- Componentes: Botão, Botão/Grande, Input, Chip/Duração, Card/Tarefa, Card/ContinuarDaqui, Card/Métrica, Timer, Header/Saudação, Mascote, Barra/Topo.
- Tudo em Auto Layout. Nenhum valor solto nas telas.

## Como trabalhar comigo (Claude)
- Faça no máximo 5 perguntas antes de começar uma fase.
- Uma proposta por vez, sem oferecer várias alternativas visuais.
- Ao fim de cada sessão, atualize PROJECT_OVERVIEW.md ("Onde estou" + "Continuar daqui").
- Textos: claros, curtos, sem enrolação.
