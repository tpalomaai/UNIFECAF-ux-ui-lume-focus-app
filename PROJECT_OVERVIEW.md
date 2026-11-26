# ✦ Project Overview — Lume

> Abra este arquivo ao iniciar o dia, ao voltar de uma pausa longa ou quando se perder.
> Ao fim de cada sessão (2 min): atualize 🧭 Agora, 📍 Continuar daqui, marque as tarefas feitas e adicione 1 linha no 📓 Registro.

---

## 🧭 Agora
| | |
|---|---|
| **Fase atual** | F6 — Textos (README e roteiro prontos; falta só Paloma cronometrar) · slides do vídeo pitch prontos no Canva p/ F7 |
| **Próxima ação** | Paloma: ler o roteiro em voz alta e cronometrar (≤ 4 min); depois F7 (gravar a narração slide por slide + a tela do protótipo, conforme docs/05-slides-narracao.md, e montar com o mascote: Feliz na abertura, Focado na navegação, Comemorando nos diferenciais/encerramento) |
| **Bloqueios** | Nenhum |
| **Prazo final** | **30/11/2026 (seg)** · faltam 4 dias · meta interna: tudo pronto na **sex 27/11** |
| **Última atualização** | 26/11/2026 (slides do vídeo pitch renderizados em HTML e colados no deck do Canva) |

## 📍 Continuar daqui
> F0 concluída: nome **Lume**, direção visual travada (fundo Creme lunar #FFF8EC, Lexend + Sniglet) e repositório no GitHub com toda a estrutura.
> F1 revisada com a pesquisa: o app virou **cronômetro progressivo sem pressão** + histórico por tarefa + "Onde parei / Próximo passo" + "Lembrar depois".
> Trabalho migrado para o **Claude Code** (terminal), com o repositório clonado no computador.
> **F1 aprovada** ✅ (fluxo com cronômetro progressivo, docs/02-fluxo.md).
> **F2 concluída** ✅: arquivo [Lume — UX/UI](https://www.figma.com/design/z7C1XSWQhlIpYry549Ba3Q) com 3 páginas + seções (limite do Starter), 6 wireframes + 04b (pausada) em cinza e 14 ligações no Prototype.
> Revisão aplicada (docs/revisoes/f2-wireframes.md): Retomar virou primário no Início, rótulos visíveis nos campos, pausa como estado da tela 04.
> **F3 em andamento:** Variables prontas (`Primitivos` 11 · `Tokens` 13 · `Medidas` 10) e 7 Text Styles. Lexend sem números tabulares → cronômetro em caixa fixa 180 px.
> Fundamentos à mão: Etapa 1 (frame + título) ✅ · Etapa 2 (13 cores, grid conferido por metadata — sem sobreposição) ✅.
> **25/11:** assinado **Figma Professional** (vaga Full) → MCP de volta, com política de uso (lote, leitura barata, IDs em docs/figma-ids.md, aviso de custo, placar, limite 40/dia). Plano recalibrado até 30/11 aprovado (ver 📅 Cronograma).
> **F3 concluída e congelada** ✅ 25/11: Fundamentos (paleta, tipografia, medidas), 4 componentes atômicos, 7 compostos e Mascote — tudo via MCP, auditoria limpa (254 nós). Screenshots em docs/screenshots/.
> **F4 iniciada** 25/11: os 7 wireframes foram duplicados para a página 📱 Telas (wireframes originais intactos). Telas **04** e **04b** montadas com instâncias reais (Chip, Cronômetro, Botão) e os frames "Espaço" trocados por spacers flexíveis (Auto Layout FILL). No processo, corrigi um bug de contraste no componente `Cronômetro` (já congelado — exceção documentada).
> **F4 — as 7 telas concluídas** ✅ 25/11: telas 01, 02, 03, 05 e 06 montadas com o mesmo método (instâncias reais: Mascote, Header/Saudação, Card/ContinuarDaqui, Card/Tarefa, Card/Lembrete, Card/Métrica, Input, Barra/Topo, Botão). Encontrei e corrigi 2 bugs no processo: (1) `layoutSizingHorizontal = 'FILL'` setado antes de inserir a instância no frame pai derruba o script inteiro — corrigir a ordem; (2) `Card/Métrica` expõe as 3 properties de valor em toda variante (não uma exclusiva por tipo) — "pegar a primeira property de texto" setou a errada e a tela 06 mostrou "47 min" em vez de "45 min" no card "Tempo de hoje"; corrigido setando pelo nome exato.
> **F4 — protótipo ligado** ✅ 25/11: 14 interações criadas (navegação entre as 7 telas, Pausar/Continuar como Change to com Smart Animate entre 04 e 04b, botões "voltar" com ação Back), ponto de partida do fluxo definido na tela 01. Conferido lendo as reactions de volta — tudo salvo certo.
> **Correção na página 📱 Telas:** as 7 telas tinham sido duplicadas soltas no canvas (nunca filhas de nenhuma *section*), sobrepondo a section "📖 Capa". Corrigido: agora são filhas de fato da section "📱 Telas finais" (redimensionada), lado a lado, sem sobrepor nada.
> Paloma testou no Present e perguntou se dá pra digitar de verdade nos Inputs — expliquei que o Figma não suporta teclado real em prototipagem (limitação da ferramenta) e propus simular com Change to entre os estados Vazio/Foco/Preenchido do componente `Input`. Decisão: **não fazer agora** (ficou pra "Estacionamento de ideias").
> Na tela 03, adicionei navegação direta: clicar num Card/Tarefa de "Tarefas recentes" leva pra tela 04, igual ao botão "Começar".
> **F4 concluída** ✅ 25/11: Paloma testou o fluxo completo no Present, aprovou, e gerou o link público do protótipo (colado em 🔗 Links de acesso).
> **F5 concluída** ✅ 25/11: contraste recalculado via WCAG fora do Figma — `vermelho/600` corrigido (#D23C3C → #C23434, falhava sobre `bg/app`). Auditoria das 7 telas finais: zero valor solto, zero palavra não-gentil, único problema real foi `Barra/Topo` com 47px (corrigido pra 48px). Seções 1.4 e 1.5 escritas em docs/01-teorico.md. Prompts de todas as fases registrados em docs/prompts.md.
> **F6 em andamento** 25/11: README completo (links, objetivo, fluxo, decisões de design, 3 screenshots das telas) e roteiro do vídeo escrito (docs/04-roteiro-video.md), calibrado pros 4 minutos.
> **Reforço do documento teórico** 25/11: Paloma revisou o enunciado do trabalho — ele pede pra **estruturar a experiência do usuário**, não só entregar a interface pronta. Li todos os resumos de aula dela no Obsidian (Matriz CSD, Mapa de Empatia, Persona, Journey Map, Pain Points, HMW, Duplo Diamante, Arquitetura da Informação, User Flow, Matriz de Impacto×Esforço) e incorporei essas ferramentas formais nas seções 1.1–1.3 do `docs/01-teorico.md` e no `docs/02-fluxo.md` (que ganhou um ponto de decisão real, virando um User Flow de verdade).
> **Página "🧠 Processo UX" criada no Figma** 25/11: além do documento teórico, montei os mesmos 8 artefatos (CSD, Mapa de Empatia, Persona, Pain Points+HMW, Journey Map, Sitemap, User Flow, Matriz de Impacto×Esforço) como uma página visual dentro do próprio arquivo Figma — já que o enunciado pede pra projetar a UX "utilizando Figma". Encontrei e corrigi um bug real no processo (texto sobrepondo texto por causa da ordem errada entre `resize()` e `.characters`), documentado em docs/figma-ids.md.
> **Ambiente de vídeo + mascote animado** 26/11: montado `video-editor/` com FFmpeg, MoviePy, faster-whisper e auto-editor (todos testados). PNGs do mascote organizados em `video-editor/entrada/mascote/` (feliz/focado/comemorando, 1254×1254, transparentes). Animação testada (pop de entrada, flutuação, troca de expressão com fade, pulinho de comemoração) em tela dividida creme/noite — `video-editor/saida/teste-mascote.mp4` — **aprovada pela Paloma, sem rodada de ajuste**. Vira o padrão pro vídeo pitch: Feliz na abertura, Focado na navegação pelo protótipo, Comemorando nos diferenciais e no encerramento (com o pulinho).
> **Deck de slides no Canva reprovado e refeito em HTML** 26/11: o primeiro deck gerado por IA no Canva ("Lume — Vídeo Pitch (slides)") foi reprovado por Paloma — títulos pequenos, celular minúsculo, símbolos de texto no lugar de ícones, prints da Library ilegíveis. Novo caminho: os 11 slides passaram a ser montados em HTML/CSS (Playwright renderiza cada um como PNG 1920×1080) em `video-editor/slides-src/` — fontes Lexend/Sniglet e ícones Tabler baixados localmente, recortes ampliados do Figma (paleta, Botão, Card/ContinuarDaqui, telas 03/05) via MCP (5 chamadas). Teste de estilo (slides 5 e 10) aprovado, depois os 11 completos aprovados em grade única. Self-Refine corrigiu uma linha pontilhada cruzando texto e cores de estrelinha fora da paleta.
> **Slides colados de volta no Canva** 26/11: a pedido da Paloma, as 11 páginas do mesmo deck do Canva (ID `DAHb_Q3KpO4`) foram substituídas pelos PNGs renderizados (upload via MCP, 1 imagem de página inteira por slide) e as anotações do apresentador passaram a ter a narração de `docs/05-slides-narracao.md`. Aprovado por Paloma antes do commit.
> **docs/05-slides-narracao.md criado** 26/11: tabela com narração, nome do áudio (`narracao/slide-NN.m4a` / `narracao/prototipo.m4a`) e duração estimada por bloco — total ~3:46, dentro do alvo de 3:45 (limite 3:55). É a fonte da verdade da gravação.
> **Parei aqui:** falta a Paloma gravar a narração slide por slide (conforme docs/05) e a tela do protótipo, depois montar o vídeo com MoviePy usando o mascote aprovado. Histórico completo e detalhado em **[PONTO-DE-RETOMADA.md](PONTO-DE-RETOMADA.md)**.

---

## 📅 Cronograma até a entrega
> Janela de trabalho: seg–sex 8:00–14:50. Sábado = BellMart (sem projeto). Nenhum dia passa de 40 chamadas de Figma MCP. Plano recalibrado e aprovado em 25/11 após o diagnóstico da F3.

| Dia | Tarefas | Tempo | Quem faz | Chamadas est. | Critério de pronto |
|---|---|---|---|---|---|
| Ter 24/11 | F0 + F1 | ✅ feito | — | — | Conceito, pesquisa e fluxo |
| Qua 25/11 | Fundamentos Etapas 3–5 (Tipografia, Medidas, Conferência) | 25 min | Paloma à mão | 0 | Seção Fundamentos completa |
| Qua 25/11 | Componentes atômicos: `Botão`, `Chip/Tarefa`, `Input` | ~1 h | Claude MCP (1 lote) | ~12 | 3 componentes com variantes, Auto Layout, só tokens |
| Qua 25/11 | `Mascote` (Feliz · Focado · Comemorando) | ~30 min | Claude MCP (1 lote) | ~6 | 3 variantes simples, Auto Layout |
| Qui 26/11 | Componentes compostos: 4 Cards + `Cronômetro` + `Header/Saudação` + `Barra/Topo` | ~1h30 | Claude MCP (1 lote) | ~20 | 7 componentes compostos usando os atômicos |
| Qui 26/11 | Auditoria rápida + **congelar Library** (portão F3) | ~20 min | Claude MCP | ~3 | Sem tokens soltos, nomes padronizados |
| Qui 26/11 | F4: duplicar wireframes → 📱 Telas, montar com instâncias, trocar "Espaço" por Auto Layout, pausa como interactive component | ~2h30 | Claude MCP (lotes ≤15, com aviso) | ~25 | 6 telas finais só com instâncias |
| Qui 26/11 | F4: interações do protótipo | ~1 h | Claude MCP | ~15 | Fluxo clicável completo |
| Qui 26/11 | Testar no Present/Preview + gerar link público | ~20 min | Paloma à mão | 0 | Link público funcionando |
| Sex 27/11 | F5: auditoria de contraste/toque via MCP + correções | ~45 min | Claude MCP | ~8 | Checklist 100% |
| Sex 27/11 | Doc 1.4–1.5 (texto com apoio do Claude) | ~45 min | Paloma + Claude | 0 | Seções escritas |
| Sex 27/11 | F6: README + roteiro do vídeo | ~1h30 | Paloma + Claude (texto) | 0 | README completo, roteiro ≤ 4 min |
| Sex 27/11 | F7: gravar vídeo pitch | ~1 h | Paloma à mão | 0 | Vídeo ≤ 4 min, YouTube não listado |
| Sáb 28/11 | — BellMart — | — | — | — | — |
| Dom 29/11 | Reserva para imprevistos | 0–2 h | — | — | — |
| Seg 30/11 | F8 Entrega (manhã) | 30 min | Paloma à mão | 0 | Trabalho enviado 🎉 |

---

## 🔗 Links de acesso
| Item | Link | Status |
|---|---|---|
| 🐙 Repositório GitHub | [UNIFECAF-ux-ui-lume-focus-app](https://github.com/tpalomaai/UNIFECAF-ux-ui-lume-focus-app) | ✅ |
| 🎨 Arquivo Figma | [Lume — UX/UI](https://www.figma.com/design/z7C1XSWQhlIpYry549Ba3Q) | ✅ |
| 🔗 Protótipo (link público) | [Protótipo - Preview](https://www.figma.com/proto/z7C1XSWQhlIpYry549Ba3Q/Lume-%E2%80%94-UX-UI?node-id=43-3&p=f&viewport=217%2C273%2C0.21&t=U2qWueE7FQUYMI9P-1&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=43%3A3&page-id=2%3A3) | ✅ |
| 🖼️ Slides do vídeo pitch (Canva) | [Lume — Vídeo Pitch (slides)](https://canva.link/3b4h0m8m7m54uqv) | ✅ (11 slides renderizados em HTML, narração nas anotações) |
| 🎬 Vídeo pitch | (a gravar na F7) | ⏳ |
| 📄 Enunciado do trabalho | (salvar PDF no Vault) | ⏳ |

---

## 🗺️ Visão geral das etapas
| Fase | Entrega | Timebox | Status | Entregável vinculado |
|---|---|---|---|---|
| F0 Setup | Tema, direção visual, estrutura, repo | 30 min | ✅ Concluída | — |
| F1 UX | Problema, persona, jornada, fluxo | 2 h | ✅ Concluída | Documento teórico (1,5) |
| F2 Wireframe | 6 telas em cinza + arquivo Figma organizado | 1–2 h | ✅ Concluída | Protótipo (3,5) |
| F3 Library | Variables, Text Styles, Componentes | 2 h | ✅ Concluída | Protótipo — Design System |
| F4 Telas + Protótipo | 6 telas finais + interações | 3 h | ✅ Concluída (fluxo aprovado, link público gerado) | Protótipo — Navegação |
| F5 Acessibilidade | Checklist WCAG + doc 1.4–1.5 | 1 h | ✅ Concluída | Documento teórico |
| F6 Textos | README + roteiro do vídeo + revisão do doc | 2 h | 🔵 Quase pronta (falta só Paloma cronometrar o roteiro) | Protótipo — README |
| F7 Vídeo | Gravação ≤ 4 min + upload | 1 h | ⚪ | Vídeo pitch (2,0) |
| F8 Entrega | Conferência final + envio no portal | 30 min | ⚪ | Todos |

Legenda: ✅ concluída · 🔵 em andamento · ⚪ não iniciada · 🔴 travada
**Total estimado:** ~13 h

---

## 📋 Etapas detalhadas

### F0 — Setup · 30 min · ✅
**Objetivo:** projeto definido e pronto para trabalhar sem reabrir decisões.
- [x] Ler o enunciado e listar os 3 entregáveis
- [x] Escolher o tema (app de sessão de foco)
- [x] Definir conceito, diferenciais e fluxo das 6 telas
- [x] Travar direção visual (cores, fundo, tipografia)
- [x] Definir estrutura da Library do Figma
- [x] Definir o nome (Lume)
- [x] Criar estrutura local (CLAUDE.md, README, docs/, Project Overview)
- [x] Criar repositório `UNIFECAF-ux-ui-lume-focus-app` no GitHub
- [x] Enviar arquivos para o GitHub e preencher o link acima
- [x] Preencher o prazo final (30/11/2026)
- [ ] Salvar o PDF do enunciado no Vault

**Pronto quando:** repositório online com a estrutura e prazo preenchido.

### F1 — UX · 2 h · ✅
**Objetivo:** entender a usuária e validar o fluxo antes de desenhar qualquer coisa.
- [x] Rodar o Prompt F1 no Claude Code
- [x] Definir o público (universitários EAD, home office, estudantes de idiomas)
- [x] Entrevista: distrações, apps anteriores, retomada, contexto de uso
- [x] Revisar conceito com base na pesquisa (cronômetro progressivo)
- [x] Escrever a persona (Camila, 29)
- [x] Escrever 4 dores e 4 necessidades
- [x] Escrever a jornada (7 etapas)
- [x] Fluxo em Mermaid + tabela das telas e interações (docs/02-fluxo.md)
- [x] 7 decisões de UX ligadas a princípios (Zeigarnik, Fitts, Hick, pico-fim, Jakob…)
- [x] **Aprovar o fluxo** (portão)
- [x] **Reforço 25/11** (a pedido da Paloma, revisando o enunciado — ele pede pra estruturar a UX, não só desenhar a UI): Problem Statement, Matriz CSD, Mapa de Empatia, Journey Map formal (curva de emoção), Pain Points (impacto × frequência), perguntas HMW, processo mapeado no Duplo Diamante, Arquitetura da Informação, User Flow com ponto de decisão real, Matriz de Impacto × Esforço — tudo baseado nos resumos de aula da Paloma (Obsidian) e incorporado em docs/01-teorico.md e docs/02-fluxo.md

**Pronto quando:** seções 1.1, 1.2 e 1.3 do documento teórico escritas e fluxo aprovado.

### F2 — Wireframe · 1–2 h · ✅
**Objetivo:** validar hierarquia e navegação sem cor.
- [x] Criar o arquivo "Lume — UX/UI" no Figma
- [x] Criar as páginas (Starter = 3): 🧩 Library · 🔲 Wireframes · 📱 Telas, com seções (docs/03-design-system.md)
- [x] Rodar o Prompt F2 (tabela de elementos por tela)
- [x] Desenhar os 6 frames em cinza (390×844), com nomes `01 - Boas-vindas` … `06 - Sessão concluída`
- [x] Ligar as telas com navegação simples (modo Prototype) — 14 ligações + ponto de partida "Fluxo principal"
- [x] Testar o fluxo clicando do início ao fim (Prototype Preview)
- [x] Revisão da F2 aplicada: hierarquia do Início, rótulos visíveis, frame 04b - Sessão pausada (docs/revisoes/f2-wireframes.md)
- [x] Colar o link do Figma acima

**Pronto quando:** as 6 telas existem, têm os nomes certos e navegam.

### F3 — Library · 2 h (rígido) · 🔵
**Objetivo:** criar todas as peças padronizadas antes das telas finais.
- [x] Variables, coleção `Primitivos` (cores cruas) — 10 cores, ocultas dos seletores
- [x] Variables, coleção `Tokens` (cores com função) — 12 aliases, cada um no seletor certo
- [x] Variables, coleção `Medidas` (espaço, raio, toque mínimo 48) — 10 medidas
- [x] Text Styles (7 estilos: Display, Títulos, Corpo, Legenda, Cronômetro)
- [x] Números estáveis no cronômetro: Lexend não tem tabulares → caixa fixa 180 px centralizada no componente `Cronômetro`
- [x] Instalar/ativar as fontes Lexend e Sniglet no Figma (já disponíveis via Google Fonts)
- [x] Seção 🎨 Fundamentos (página 🧩 Library) montada: paleta, tipografia (7 estilos) e medidas (espaço/raio/toque) — via MCP, padding/gap do frame corrigido para `espaco/xl`
- [x] Componentes atômicos via MCP: `Botão` (18 variantes), `Chip/Tarefa` (2), `Input` (4) — token `destaque/erro` criado (conferir contraste na F5)
- [x] Componentes compostos via MCP: `Card/Tarefa`, `Card/ContinuarDaqui` (com instância de Botão), `Card/Métrica`, `Card/Lembrete`, `Cronômetro`, `Header/Saudação` (com instância de Mascote), `Barra/Topo` — 2 bugs de sizing encontrados e corrigidos (ver docs/figma-ids.md)
- [x] `Mascote` (Feliz · Focado · Comemorando) — placeholder vetorial trocado por imagens PNG geradas no ChatGPT, upload via MCP
- [x] Tudo em Auto Layout e usando só variables — auditado via MCP (254 nós, 0 problemas reais)
- [x] **Congelar a Library** (portão) ✅ 25/11/2026 — screenshots em docs/screenshots/

**Pronto quando:** todos os componentes existem na seção 🧩 Componentes (página 🧩 Library).

### F4 — Telas finais + Protótipo · 3 h · ✅
**Objetivo:** protótipo navegável completo, montado só com instâncias.
- [x] Duplicar os wireframes para a página 📱 Telas (via MCP, wireframes originais intactos)
- [x] Tela 04 e 04b: instâncias de Chip/Tarefa, Cronômetro (Rodando/Pausado) e Botão (Secundário, Destaque, Primário) + fundo `bg/foco` + "Espaço" trocado por spacer flexível (Auto Layout FILL)
- [x] Telas 01, 02, 03, 05, 06: substituídas por instâncias da Library (mesmo método das 04/04b) — **as 7 telas estão prontas**
- [x] Interações: Começar (01) → Início (02); Nova sessão (02) → Escolher tarefa (03); Começar (03) → Sessão (04)
- [x] Interação: "Lembrar depois" (04 e 04b) → tela 05; botão e Barra/Topo da 05 voltam com ação **Back** (volta pra 04 ou 04b, conforme de onde veio)
- [x] Interação: Início "Retomar" (dentro do Card/ContinuarDaqui) → Sessão (04), atalho
- [x] Interação: "Concluir" (04 e 04b) → Sessão concluída (06) → "Salvar e sair" volta ao Início (02)
- [x] Pausa como interactive component: Pausar (04→04b) e Continuar (04b→04) ligados com **Smart Animate** (200 ms)
- [x] Definido o frame inicial (flow starting point): tela 01, fluxo "Fluxo principal"
- [x] Transições: Dissolve 300 ms nas navegações normais, Smart Animate 200 ms só na pausa (conferido lendo as reactions de volta — tudo salvo certo)
- [x] **Paloma à mão:** testar o fluxo inteiro em modo apresentação (Present/Preview) — aprovado
- [x] **Paloma à mão:** gerar o link público do protótipo e colar na tabela 🔗 Links de acesso acima
- [x] Tela 03: cards de "Tarefas recentes" navegam direto pra tela 04 (Sessão), além do botão "Começar"

**Pronto quando:** o fluxo principal funciona do início ao fim pelo link público. ✅

### F5 — Acessibilidade · 1 h · ✅
**Objetivo:** garantir e documentar acessibilidade e inclusão.
- [x] Prompt usado: ver [docs/prompts.md](docs/prompts.md)
- [x] Verificar contraste AA de todos os pares de cor usados (docs/03-design-system.md) — `vermelho/600` corrigido de #D23C3C para #C23434
- [x] Conferir áreas de toque ≥ 48 px — `Barra/Topo` corrigido de 47px para 48px
- [x] Conferir texto do corpo ≥ 14 px, legendas nunca < 12 px — 100% conforme
- [x] Conferir que nada depende só de cor (ícone + texto) — confirmado (legenda "Pausado"/"Em andamento", `acao/borda` e `destaque/retomar` só em bordas, nunca em texto)
- [x] Conferir linguagem gentil (nada de "falhou", "atrasou") — varredura nas 7 telas, zero ocorrências
- [x] Cronômetro com caixa fixa (180px) e leitura textual de apoio — confirmado
- [x] Corrigir o que falhou (via Library, em lote) — `vermelho/600` e `Barra/Topo`
- [x] Escrever doc 1.4 (Decisões de UI) e 1.5 (Acessibilidade e Inclusão) em docs/01-teorico.md

**Pronto quando:** checklist 100% e seções 1.4 e 1.5 escritas. ✅

### F6 — Textos · 2 h · 🔵
**Objetivo:** reaproveitar o documento teórico para o README e o vídeo.
- [x] Documento teórico completo (1.1 a 1.5) — revisado na F5
- [ ] Exportar o documento teórico no formato pedido pelo portal
- [x] Prompt usado: ver [docs/prompts.md](docs/prompts.md)
- [x] README: links em tabela no topo, objetivo, fluxo, decisões de design
- [x] Adicionar 2–3 imagens das telas no README (02 Início, 04 Sessão, 06 Concluída)
- [x] Roteiro do vídeo em tabela (tempo · fala · tela) — docs/04-roteiro-video.md
- [ ] **Paloma à mão:** ler o roteiro em voz alta e cronometrar (≤ 4 min) — ajustar o texto se passar
- [x] Enviar tudo para o GitHub

**Pronto quando:** README completo no GitHub e roteiro dentro do tempo.

### F7 — Vídeo pitch · 1 h · ⚪
**Objetivo:** apresentar problema, protótipo, decisões e diferenciais.
- [ ] Preparar a tela: Figma em modo apresentação + abas fechadas
- [ ] Gravar (Loom, OBS ou gravador do sistema)
- [ ] Conferir: problema/usuário · navegação · decisões UX/UI · diferenciais
- [ ] Conferir duração ≤ 4 min
- [ ] Subir no YouTube como **não listado**
- [ ] Colar o link aqui e no README

**Pronto quando:** link do vídeo funcionando em aba anônima.

### F8 — Entrega final · 30 min · ⚪
**Objetivo:** não perder ponto por detalhe.
- [ ] Abrir todos os links em aba anônima (Figma, protótipo, vídeo, GitHub)
- [ ] Conferir o ✅ Checklist de entrega abaixo, item por item
- [ ] Enviar no portal da UniFECAF
- [ ] Guardar comprovante/print do envio
- [ ] Atualizar o portfólio (GitHub pinado, YouTube)

**Pronto quando:** trabalho enviado e comprovante salvo. 🎉

---

## ✅ Checklist de entrega (critérios do enunciado)
**Documento teórico (1,5)**
- [x] 1.1 Problema e Usuário (reforçada com Problem Statement, Matriz CSD, Mapa de Empatia)
- [x] 1.2 Jornada do Usuário (reforçada com Journey Map formal, Pain Points, HMW)
- [x] 1.3 Estrutura da Solução (UX) (reforçada com Duplo Diamante, Arquitetura da Informação, User Flow, Matriz de Impacto×Esforço)
- [x] 1.4 Decisões de Interface (UI)
- [x] 1.5 Acessibilidade e Inclusão

**Protótipo Figma (3,5)**
- [x] 4–6 telas com fluxo principal completo
- [x] Interações configuradas e navegação funcional
- [x] Design system: cores, tipografia, componentes reutilizáveis
- [x] Telas nomeadas e arquivo organizado
- [x] Link público + README (objetivo, fluxo, decisões)

**Vídeo pitch (2,0)**
- [ ] Problema e usuário
- [ ] Navegação pelo protótipo
- [ ] Decisões de UX e UI
- [ ] Diferenciais
- [ ] ≤ 4 min + link público/não listado

---

## 🔒 Decisões tomadas
| Data | Decisão | Motivo |
|---|---|---|
| 24/11 | Tema: app de sessão de foco | Usuária real (eu), fluxo simples |
| 24/11 | Nome: **Lume** (luz pequena e constante) | Simples, adulto, combina com o tema céu/estrelas |
| 24/11 | 6 telas, mobile 390×844 | Atende 4–6 telas do enunciado |
| 24/11 | Direção "Céu de estrelas" + fundo Creme lunar #FFF8EC | Lúdico, acolhedor, bom contraste |
| 24/11 | Lexend (texto) + Sniglet (só saudação/logo) | Lexend melhora leitura → argumento de acessibilidade |
| 24/11 | Library no Figma antes das telas | Padronização e zero retrabalho |
| 24/11 | Repositório `UNIFECAF-ux-ui-lume-focus-app` | Mesmo padrão de nome dos outros projetos da faculdade |
| 24/11 | Público: universitários EAD, home office, estudantes de idiomas | Todos estudam/trabalham sozinhos, em casa, com tempo fragmentado |
| 24/11 | **Cronômetro progressivo** no lugar das durações fixas 15/25/45 | Pesquisa: contagem regressiva gera ansiedade; medir o tempo e otimizar no próprio ritmo funciona melhor |
| 24/11 | "Continuar daqui" com Onde parei + Próximo passo + botão Retomar | Retomada levava 30 min–1 h |
| 24/11 | "Me distraí" virou "Lembrar depois" | Maior distração = outras tarefas em paralelo |
| 24/11 | Continuar o projeto pelo Claude Code | CLAUDE.md carrega sozinho, arquivos locais, commits diretos |
| 24/11 | F1 aprovada | Fluxo com cronômetro progressivo validado |
| 24/11 | Figma com 3 páginas + seções (Library · Wireframes · Telas) | Plano Starter limita a 3 páginas |
| 24/11 | Retomar como botão primário no Início | Doc 1.3: retomar é a ação mais importante (Fitts; retomada levava 30 min–1 h) |
| 24/11 | `estrela/900` #3D2F00 + token `texto/sobre-destaque` | Texto do botão "Lembrar depois" estava fora da Library |
| 24/11 | Cronômetro em caixa fixa 180 px (Lexend sem números tabulares) | Mantém a fonte travada e evita o número "pular" |
| 24/11 | Figma à mão (sem MCP) até o fim do projeto | Limite do Starter; plano pago só para isso não compensa |
| 24/11 | Pausa como estado da tela 04 (04b no wireframe; Change to na F4) | Pausar não troca de contexto; componente interativo conta em "componentes reutilizáveis" |
| 25/11 | Upgrade para **Figma Professional** (vaga Full) | Créditos do MCP no Starter acabaram; Professional libera volume suficiente para fechar F3–F4 no prazo |
| 25/11 | **Política de uso do MCP:** lote por tarefa, leitura barata antes de screenshot, IDs salvos em docs/figma-ids.md, aviso de custo acima de 15 chamadas, placar por sessão, limite 40/dia, parar na hora em 429 | Evitar reincidir no limite e manter o trabalho repetitivo (componentes, telas, interações) com o Claude, deixando ajustes pontuais para Paloma à mão |
| 25/11 | **Library congelada** (F3 ✅) — auditoria via MCP (254 nós: 0 sem Auto Layout, 0 cor solta fora das seções de organização) | Portão antes de montar as telas finais (F4); mudanças na Library a partir daqui exigem motivo forte, como as demais Decisões travadas |
| 25/11 | Exceção à Library congelada: legenda do `Cronômetro` trocada de `texto/secundario` para `texto/sobre-acao` | Achado na montagem da tela 04b — baixo contraste sobre `bg/foco` (tela escura); motivo forte = acessibilidade |
| 25/11 | Botões "voltar" (Barra/Topo e "Guardar e voltar") usam a ação **Back** do Figma, não um destino fixo | Telas 05 e 03 são acessadas a partir de mais de um ponto do fluxo (04 ou 04b); Back volta sempre pra tela de origem, sem precisar duplicar lógica |
| 25/11 | As 7 telas reparentadas pra dentro da section "📱 Telas finais" (antes soltas no canvas) | Sobrepunham a section "📖 Capa"; `clone()` + `page.appendChild()` nunca posiciona dentro de uma section |
| 25/11 | Não simular digitação nos Inputs (Change to Vazio→Foco→Preenchido) por enquanto | Exigiria editar o componente `Input`, já congelado; Paloma decidiu que não precisa agora |
| 25/11 | Documento teórico reforçado com o processo formal de UX estudado na disciplina (CSD, Mapa de Empatia, Journey Map, Pain Points, HMW, Duplo Diamante, IA, User Flow, Matriz de Impacto×Esforço) | O enunciado pede pra estruturar a UX, não só entregar a UI pronta — o documento precisa mostrar o processo |
| 25/11 | Arquitetura da informação do app: sem menu global/abas, navegação linear e rasa | O app resolve uma tarefa por vez; cada clique extra custa caro pra quem já tem pouco tempo (Princípio das Escolhas e da Navegação Focada, Dan Brown) |
| 25/11 | **F4 concluída** — fluxo aprovado por Paloma no Present, link público gerado | Portão antes da F5; critério "fluxo clicável completo" atendido |
| 25/11 | Reforçado o documento teórico (1.1–1.3) com as ferramentas formais de UX estudadas na disciplina (Matriz CSD, Mapa de Empatia, Problem Statement, Journey Map, Pain Points, HMW, Duplo Diamante, Arquitetura da Informação, User Flow com decisão, Matriz de Impacto × Esforço) | Paloma revisou o enunciado: ele pede pra **estruturar a UX**, não só entregar a interface pronta — o documento precisa mostrar o processo, não só o resultado |
| 25/11 | `vermelho/600` corrigido de #D23C3C pra #C23434 (contraste AA) | O valor antigo falhava sobre `bg/app` (4,47); novo valor passa nos dois fundos usados pelo `destaque/erro` com folga (≥5,0) |
| 25/11 | `Barra/Topo` corrigido de 47px pra 48px de altura | Único problema real da auditoria da F5 — abaixo do toque mínimo e é clicável (ação Back) nas telas 03 e 05 |
| 25/11 | **F5 concluída** — checklist 100%, docs 1.4 e 1.5 escritos | Portão antes da F6; nenhuma pendência de acessibilidade restante |
| 25/11 | Criada a página "🧠 Processo UX" dentro do próprio arquivo Figma, espelhando os artefatos de UX (CSD, Mapa de Empatia, Persona, Journey Map, Pain Points+HMW, Sitemap, User Flow, Matriz de Impacto×Esforço) | O enunciado pede pra projetar a UX "utilizando Figma" — manter o processo só no documento teórico deixaria essa parte de fora do arquivo de entrega |
| 26/11 | Slides antes do áudio: primeiro montar e aprovar os 11 slides do vídeo pitch, só depois gravar a narração | Permite gravar cada narração já olhando pro slide certo e calibrar a duração por bloco antes de gastar tempo de gravação |
| 26/11 | Numeração por slide substitui cenas: qualquer estrutura antiga de "cena-XX"/storyboard de vídeo fica obsoleta — tudo se organiza por slide (1 a 11) ou pelo bloco "protótipo" | Evita ambiguidade entre dois sistemas de referência para o mesmo vídeo pitch |
| 26/11 | Deck do Canva descartado por qualidade (gerado por IA) — slides passaram a ser feitos em HTML renderizado com Playwright | Canva: títulos pequenos, celular minúsculo, símbolos de texto no lugar de ícones, prints da Library ilegíveis — HTML/CSS deu controle fino de tipografia, ícones reais e recortes legíveis do Figma |

---

## 📓 Registro de sessões (1 linha por sessão)
| Data | O que fiz | Tempo |
|---|---|---|
| 24/11 | Tema, plano, direção visual, Library definida, nome, estrutura F0 | ~50 min |
| 24/11 | F1: público, entrevista, conceito revisado (cronômetro progressivo), 1.1–1.3 | ~40 min |
| 24/11 | Prazo e cronograma definidos; migração para o Claude Code | ~10 min |
| 24/11 | F1 aprovada · F2: arquivo Figma (3 páginas), 6 wireframes em cinza, navegação ligada | ~30 min |
| 24/11 | Revisão F2: Retomar primário, rótulos nos campos, 04b pausada, 14 ligações · F2 ✅ | ~20 min |
| 24/11 | F3: Variables (3 coleções), 7 Text Styles, solução do cronômetro · parou no limite do Figma MCP | ~25 min |
| 24/11 | F3 à mão: Fundamentos Etapas 1–2 (frame, título, 13 cores) · criado PONTO-DE-RETOMADA.md | ~1 h |
| 25/11 | Upgrade Figma Professional confirmado (whoami) · política de uso do MCP registrada no CLAUDE.md · diagnóstico F3 via metadata (Componentes vazia) · docs/figma-ids.md criado · plano recalibrado até 30/11 aprovado | ~25 min |
| 25/11 | Componentes atômicos via MCP: `Botão` (18 var.), `Chip/Tarefa` (2), `Input` (4) · corrigido bug de property fundida entre variantes · token `destaque/erro` criado · 10 chamadas Figma MCP usadas | ~40 min |
| 25/11 | `Mascote` via MCP (3 variantes Humor) · 12 chamadas Figma MCP usadas na sessão | ~10 min |
| 25/11 | Mascote trocado por imagens PNG (Paloma gerou no ChatGPT; uma reprovada e refeita como "Determinada") · upload via MCP · 15 chamadas na sessão | ~15 min |
| 25/11 | Fundamentos Etapas 3–5 via MCP (a pedido da Paloma, mudando a divisão original): Tipografia (7 linhas) + Medidas (espaço/raio/toque) + correção do padding/gap para `espaco/xl` · F3 Library = Fundamentos 100% completo · 16 chamadas na sessão | ~10 min |
| 25/11 | 7 componentes compostos via MCP (Cards, Cronômetro, Header/Saudação, Barra/Topo) · 2 bugs de sizing encontrados e corrigidos no self-refine (texto cortado, número deslocado) · 30 chamadas na sessão | ~35 min |
| 25/11 | Auditoria completa (254 nós) + **Library congelada** ✅ · F3 concluída · screenshots salvos em docs/screenshots/ · 32 chamadas na sessão | ~10 min |
| 25/11 | F4 iniciada: 7 telas duplicadas · telas 04 e 04b montadas com instâncias (Chip, Cronômetro, Botão) + Espaço trocado por spacer flexível · corrigido contraste da legenda do Cronômetro (exceção à Library congelada) · 39 chamadas na sessão — parado no limite de hoje | ~20 min |
| 25/11 | Retomado após pausa · telas 01, 02, 03, 05 e 06 montadas com instâncias reais (Mascote, Header/Saudação, Card/ContinuarDaqui, Card/Tarefa×5, Card/Lembrete×2, Card/Métrica×3, Input×4, Barra/Topo×2, Botão×5) · **F4: as 7 telas concluídas** · 2 bugs corrigidos (ordem do layoutSizing FILL; property errada no Card/Métrica) · ~28 chamadas nesta sessão | ~35 min |
| 25/11 | 14 interações do protótipo ligadas (navegação entre as 7 telas, pausa como Change to/Smart Animate, botões voltar com ação Back) + frame inicial definido na tela 01 · conferido lendo as reactions de volta · **F4 praticamente concluída**, falta só Paloma testar e gerar o link público · ~10 chamadas neste bloco | ~15 min |
| 25/11 | Corrigidas as 7 telas pra dentro da section "Telas finais" (estavam soltas, sobrepondo a Capa) · Paloma testou no Present, perguntou sobre digitar nos Inputs — expliquei a limitação do Figma e a opção de simular com Change to; decidiu não fazer agora | ~10 min |
| 25/11 | Cards de "Tarefas recentes" na tela 03 ganharam navegação direta pra tela 04 · Paloma aprovou o fluxo completo no Present e gerou o link público · **F4 concluída** ✅ | ~10 min |
| 25/11 | F5: proposto e aprovado novo hex pro `vermelho/600` (#C23434, calculado via WCAG fora do Figma) · auditoria das 7 telas finais (1 chamada) · corrigido `Barra/Topo` (47→48px) · docs 1.4–1.5 escritos · docs/prompts.md criado · **F5 concluída** ✅ · ~4 chamadas Figma MCP neste bloco | ~40 min |
| 25/11 | F6: README completo (objetivo, fluxo, decisões, 3 screenshots das telas) · roteiro do vídeo escrito e calibrado pra 4 min (docs/04-roteiro-video.md) · 3 chamadas Figma MCP (só screenshots) | ~20 min |
| 25/11 | Lidos todos os resumos de UX do Obsidian da Paloma (vault da disciplina) · documento teórico (1.1–1.3) reforçado com o processo formal de UX (CSD, Mapa de Empatia, Problem Statement, Journey Map, Pain Points, HMW, Duplo Diamante, IA, User Flow, Matriz de Impacto×Esforço) · docs/02-fluxo.md ganhou um ponto de decisão real · 0 chamadas Figma MCP | ~30 min |
| 25/11 | Criada a página "🧠 Processo UX" no Figma com os mesmos 8 artefatos, em forma de board visual · bug de texto sobrepondo texto encontrado e corrigido (ordem resize/characters) · ~12 chamadas Figma MCP | ~30 min |
| 26/11 | Ambiente `video-editor/` montado e testado: FFmpeg, MoviePy, faster-whisper, auto-editor · contornado bug PyAV/Python 3.14 decodificando áudio via FFmpeg · 0 chamadas Figma MCP | ~30 min |
| 26/11 | PNGs do mascote organizados em `entrada/mascote/` (feliz/focado/comemorando, 1254×1254, transparentes) · teste de animação (pop, flutuação, fade de expressão, pulinho) em tela dividida creme/noite · `teste-mascote.mp4` + 4 frames gerados · **aprovado pela Paloma** ✅, sem ajuste · vira padrão do mascote pro vídeo pitch (Feliz abertura · Focado navegação · Comemorando diferenciais/encerramento) · 0 chamadas Figma MCP | ~25 min |
| 26/11 | Deck de slides gerado no Canva (IA, 1 geração) · **reprovado pela Paloma** (títulos pequenos, celular minúsculo, símbolos de texto, prints ilegíveis, muito vazio) · 0 chamadas Figma MCP | ~25 min |
| 26/11 | Novo caminho: 11 slides montados em HTML/CSS + Playwright (`video-editor/slides-src/`) · fontes Lexend/Sniglet e ícones Tabler baixados localmente · 5 chamadas Figma MCP (recortes ampliados: paleta, Botão, Card/ContinuarDaqui, telas 03/05) · teste de estilo (slides 5 e 10) aprovado · os 11 completos aprovados em grade única, 1 rodada de correção (linha cruzando texto, cor de estrelinha fora da paleta) | ~1h30 |
| 26/11 | docs/05-slides-narracao.md criado (narração, áudio, duração por slide — total ~3:46) · as 11 páginas do deck do Canva substituídas pelos PNGs renderizados (upload via MCP) e anotações atualizadas com a narração · aprovado pela Paloma antes do commit · 0 chamadas Figma MCP | ~30 min |
| 26/11 | Bug reportado por Paloma: título grudado na grade de cartões no slide 10 · corrigido o espaçamento em `build.py` (cartões descidos de 400→470px e 660→730px) · reexportado e recolado no Canva | ~10 min |

---

## 🅿️ Estacionamento de ideias (para depois da entrega)
- Animação do mascote ao concluir sessão
- Modo escuro completo
- Simular digitação nos Inputs (Change to entre os estados Vazio → Foco → Preenchido do componente `Input`) — exigiria editar a Library congelada; avaliar depois da entrega
