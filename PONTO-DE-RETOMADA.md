# 📍 Ponto de retomada — Lume

> Última atualização: **26/11/2026**. Leia este arquivo primeiro; ele tem o histórico completo. Para o dia a dia (próxima ação, cronograma), use `PROJECT_OVERVIEW.md`.
> Arquivo Figma: [Lume — UX/UI](https://www.figma.com/design/z7C1XSWQhlIpYry549Ba3Q)

## 🧭 Onde parei exatamente
**F4, F5 e F6 concluídas (falta só Paloma cronometrar o roteiro). Teste de animação do mascote feito, aguardando aprovação.** As 7 telas e o protótipo estão prontos e aprovados, com link público gerado. A F5 (acessibilidade) fechou: contraste corrigido, toque mínimo corrigido, docs 1.4/1.5 escritos. Na F6, o README está completo (com 3 screenshots das telas) e o roteiro do vídeo está escrito e calibrado pros 4 minutos.

Depois disso, a Paloma revisou o enunciado de novo e notou que ele pede pra **estruturar a UX**, não só entregar a interface pronta — então o documento teórico (seções 1.1–1.3) e o docs/02-fluxo.md foram reforçados com o processo formal estudado na disciplina (Matriz CSD, Mapa de Empatia, Problem Statement, Journey Map, Pain Points, HMW, Duplo Diamante, Arquitetura da Informação, User Flow com decisão real, Matriz de Impacto×Esforço). E, como o enunciado também pede pra projetar a UX "utilizando Figma", os mesmos 8 artefatos foram recriados como uma página visual dentro do próprio arquivo Figma ("🧠 Processo UX") — pra essa parte do trabalho não existir só no markdown.

Em paralelo, foi montado em `video-editor/` (fora do Figma) o ambiente local pra editar o vídeo pitch — FFmpeg, MoviePy, faster-whisper e auto-editor, todos testados — e hoje (26/11) o teste de animação do mascote (Feliz · Focado · Comemorando: pop de entrada, flutuação, troca de expressão com fade, pulinho de comemoração) em `video-editor/saida/teste-mascote.mp4`, aguardando a aprovação da Paloma antes de virar padrão pro vídeo pitch.

**Falta só:** (1) Paloma aprovar o teste do mascote (ou pedir ajuste — máx. 2 rodadas); (2) Paloma ler o roteiro (`docs/04-roteiro-video.md`) em voz alta e cronometrar — se passar de 4 min, ajustar o texto (não a estrutura dos blocos de tempo). Depois disso, F6 fecha de vez e começa a F7 (gravar o vídeo, à mão).

**Chamadas do Figma MCP usadas hoje (25/11), somando todas as sessões: ~100.** Passou bem da meta própria de 40/dia (o limite real do plano Professional é 200/dia — ainda há folga real).

---

## 📖 Histórico — como chegamos até aqui

### 24/11 — F0, F1, F2 e início da F3
- **F0:** tema definido (app de sessão de foco), nome **Lume**, direção visual "céu de estrelas" travada, estrutura local criada, repositório no GitHub.
- **F1 (UX):** pesquisa revelou que contagem regressiva gera ansiedade → conceito virou **cronômetro progressivo sem pressão**. Persona Camila (29), jornada de 7 etapas, "Continuar daqui" (Onde parei + Próximo passo + Retomar) e "Lembrar depois" (em vez de "Me distraí"). F1 aprovada.
- **F2 (Wireframe):** arquivo Figma criado com 3 páginas (limite do plano Starter): 🧩 Library · 🔲 Wireframes · 📱 Telas. 6 wireframes em cinza + 04b (pausada), navegação ligada (14 ligações). Revisão aplicada: Retomar virou botão primário no Início, rótulos visíveis, pausa como estado da tela 04.
- **F3 início:** Variables (Primitivos, Tokens, Medidas) e 7 Text Styles criados. Solução para o cronômetro: como a Lexend não tem números tabulares, o número fica numa caixa de largura fixa 180px para não "pular".
- **Bloqueio:** o Figma MCP atingiu o limite do plano **Starter** (~20 chamadas/mês). Decisão: seguir o resto da F3 à mão, com o Claude guiando passo a passo. Criado o primeiro PONTO-DE-RETOMADA.md.
- À mão: Fundamentos Etapas 1 (frame + título) e 2 (paleta de 13 cores) concluídas.

### 25/11 — Upgrade, F3 completa e congelada, início da F4
- **Upgrade para Figma Professional** (vaga Full) — créditos do MCP liberados. Confirmado via `whoami`.
- **Política de uso do MCP** registrada no CLAUDE.md: lote por tarefa, leitura barata antes de screenshot, IDs salvos em `docs/figma-ids.md`, aviso de custo acima de 15 chamadas, placar por sessão, meta de 40 chamadas/dia (o plano real permite 200/dia — 40 é uma margem de segurança que você escolheu).
- **Diagnóstico da F3** via metadata: seção 🧩 Componentes ainda vazia. Plano recalibrado e aprovado para fechar tudo até 30/11.
- A seu pedido, as Etapas 3–5 dos Fundamentos (Tipografia, Medidas, Conferência) — que estavam planejadas para você fazer à mão — passaram para o Claude via MCP, por se encaixarem no critério de "lote" (listas repetitivas de elementos parecidos).
- **Componentes atômicos** (`Botão` 18 variantes, `Chip/Tarefa` 2, `Input` 4) criados via MCP. **Bug encontrado e corrigido:** dar o mesmo nome de property a variantes com texto padrão diferente funde a property — todas passam a mostrar o mesmo texto. Correção: nomes de property diferentes por propósito (`Label` vs `Legenda`, `Placeholder` vs `Valor`).
- Criado o token `destaque/erro` (não existia na Library) para o Input em estado de erro — **pendente conferir contraste na F5**.
- **Mascote**: 3 variantes (Feliz, Focado, Comemorando) geradas primeiro como ícone vetorial simples, depois **substituídas por imagens PNG** que você gerou no ChatGPT. Uma imagem ("de Olhar Sério") foi reprovada por fundo sujo e expressão de raiva; você refez como "Determinada" — ficou boa.
- **7 componentes compostos** via MCP: `Card/Tarefa`, `Card/ContinuarDaqui` (usa instância de `Botão`), `Card/Métrica`, `Card/Lembrete`, `Cronômetro`, `Header/Saudação` (usa instância de `Mascote`), `Barra/Topo`. **2 bugs de sizing encontrados e corrigidos:** `resize()` sempre reseta `primaryAxisSizingMode`/`counterAxisSizingMode` para `FIXED` — só restaurar `AUTO` **depois** do `resize()`, nunca antes (causou texto cortado no Card/Tarefa/Métrica e número deslocado no Cronômetro).
- **Auditoria completa da Library** (254 nós): 0 frames sem Auto Layout, 0 cor solta fora de nós de organização do Figma. **Library congelada** ✅ — F3 concluída. Screenshots salvos em `docs/screenshots/`.
- **F4 iniciada:** os 7 wireframes (01–06 + 04b) duplicados para a página 📱 Telas, sem alterar os wireframes originais. Telas **04** e **04b** montadas com instâncias reais (Chip/Tarefa, Cronômetro, Botão Secundário/Destaque/Primário), fundo `bg/foco`, e os frames placeholder "Espaço" trocados por spacers invisíveis com `layoutSizingVertical: FILL` (o equivalente real de Auto Layout ao que o "Espaço" simulava).
- **Exceção à Library congelada:** a legenda do `Cronômetro` ("Em andamento"/"Pausado") usava `texto/secundario`, pensado para fundo claro — sobre o `bg/foco` escuro ficava quase ilegível. Corrigido para `texto/sobre-acao` (motivo forte: acessibilidade).
- Parado em 39/40 chamadas do dia.

### 25/11 (retomada) — F4 completa: as 7 telas
- Montadas as telas **01 (Boas-vindas)**, **02 (Início)**, **03 (Escolher tarefa)**, **05 (Lembrar depois)** e **06 (Sessão concluída)** com o mesmo método das 04/04b: Auto Layout vertical no frame da tela, instâncias reais no lugar dos placeholders, "Espaço" → spacer flex, cores por Variables e texto por Text Styles.
- Componentes usados pela primeira vez em tela: `Mascote` (Feliz na 01, Comemorando na 06), `Header/Saudação`, `Card/ContinuarDaqui` (Com conteúdo), `Card/Tarefa` (Padrão), `Card/Lembrete`, `Card/Métrica` (3 tipos), `Input` (Vazio), `Barra/Topo` (Com voltar).
- **Bug encontrado:** `instance.layoutSizingHorizontal/Vertical = 'FILL'` só pode ser setado depois de a instância já estar inserida num frame com Auto Layout — setar antes lança erro e desfaz **o script inteiro** (nenhuma mutação anterior é salva, mesmo as que já tinham "rodado" antes do erro). Descoberto porque a 1ª tentativa das telas 01+05 voltou com tudo intacto apesar de o código parecer ter avançado bastante.
- **Bug encontrado:** o componente `Card/Métrica` expõe as 3 properties de valor (`ValorTempodehoje`, `ValorÚltimavez`, `ValorLembretes`) em **toda** variante, não uma exclusiva por tipo (cada variante só *exibe* a sua, mas as três existem no `componentProperties` da instância). Um helper que pegava "a primeira property de texto encontrada" setou a errada, e a tela 06 mostrou "47 min" em vez de "45 min" no card "Tempo de hoje". Corrigido setando pelo nome exato correspondente ao tipo da variante.
- **Construção da F4 (as 7 telas) concluída.**

### 25/11 (continuação) — Protótipo ligado + correção da section
- **14 interações do protótipo** criadas via `node.setReactionsAsync(...)`: navegação completa do fluxo principal (01→02→03→04→06→02), atalho "Retomar"→04, "Lembrar depois" (04 e 04b)→05, pausa 04⇄04b como **Change to + Smart Animate** (200ms), botões "voltar" (Barra/Topo da 03 e 05, "Guardar e voltar" da 05) usando a ação **Back** em vez de destino fixo — necessário porque essas telas são acessadas de mais de um ponto do fluxo. Ponto de partida do fluxo definido na tela 01. Conferido lendo as reactions de volta do Figma — tudo salvo certo.
- **Bug encontrado e corrigido:** as 7 telas tinham sido duplicadas mantendo as coordenadas originais dos wireframes, soltas no canvas da página 📱 Telas (nunca filhas de nenhuma *section*) — por isso telas 01/02/03 apareciam visualmente em cima da section "📖 Capa". Corrigido: as 7 telas viraram filhas de fato da section "📱 Telas finais" (redimensionada para 3200×1000), organizadas lado a lado com espaçamento de 50px; a section "🗂 Arquivo" (ainda vazia) foi deslocada para não sobrepor.
- **Esclarecimento sobre Capa e Arquivo:** as duas sections continuam vazias de propósito — só são preenchidas na F8 (Capa: nome/versão/link do README; Arquivo: só se alguma tela for descartada no futuro).
- Paloma testou o fluxo no modo Present e perguntou se dava pra digitar de verdade nos campos Input. Expliquei que o Figma não suporta teclado real em modo de apresentação (limitação da ferramenta de prototipagem, não um bug nosso) e propus simular com **Change to** entre os estados Vazio → Foco → Preenchido do componente `Input` — o que exigiria editar a Library congelada. **Decisão: não fazer agora** (foi para o 🅿️ Estacionamento de ideias do PROJECT_OVERVIEW.md).
- Adicionada navegação direta nos 3 `Card/Tarefa` de "Tarefas recentes" (tela 03) pra tela 04, além do botão "Começar". **Paloma testou o fluxo completo no Present, aprovou, e gerou o link público do protótipo.** F4 concluída ✅.

### 25/11 (continuação) — F5: Acessibilidade
- **Parte A:** calculei em Node (fórmula WCAG de luminância relativa) um novo hex pro primitivo `vermelho/600` — o valor antigo (#D23C3C) falhava contraste sobre `bg/app` (4,47, abaixo do mínimo 4,5). Confirmei que meu cálculo batia exatamente com a tabela que a Paloma trouxe pronta (validação cruzada). Proposta: **#C23434** (5,19 sobre `bg/app`, 5,48 sobre branco). **Aprovado e aplicado** na Variable — propagou automaticamente pro `destaque/erro` em toda a Library.
- **Parte B:** auditoria das 7 telas finais num script só (percorre toda a árvore de nós, inclusive dentro de instâncias) — muito mais barato e completo que 7 `get_metadata` separados, porque também capturou Text Style, conteúdo de texto, fills vinculados a variable e nós com reactions (toque). Achados: zero valor de cor solto, zero palavra não-gentil ("falhou"/"erro"/"atrasou" etc.), nenhum texto abaixo de 12px. Único problema real: `Barra/Topo` com 47px de altura (1px abaixo do mínimo de 48px), e é clicável (ação Back) nas telas 03 e 05.
- Verificação extra pedida pela Paloma: confirmei que `indigo/300` (via token `acao/borda`) e `rosa/400` (via token `destaque/retomar`) só aparecem como `stroke/border` nas 7 telas, nunca como fill de texto — rodando um segundo script que varre especificamente esses dois tokens.
- **Bug/lição:** a primeira tentativa dessa verificação buscou os nomes dos PRIMITIVOS (`indigo/300`, `rosa/400`) direto nas telas e voltou vazia — porque as telas nunca vinculam a primitivos, só aos TOKENS que apontam pra eles (`acao/borda`, `destaque/retomar`). Tive que refazer buscando pelo nome do token, não do primitivo.
- **Parte C:** corrigido `Barra/Topo` (ambas as variantes) de 47px pra 48px via padding +0,5px cada lado — conferido por metadata (altura exata 48 nas instâncias das telas 03 e 05, sem overflow).
- **Parte D:** escritas as seções 1.4 (Decisões de Interface) e 1.5 (Acessibilidade e Inclusão) em docs/01-teorico.md, no mesmo estilo das seções 1.1–1.3. Atualizada a tabela de Contraste em docs/03-design-system.md com os valores finais.
- **Parte E:** criado docs/prompts.md com o prompt de cada fase (F0–F4 reconstruídos a partir do histórico, F5 verbatim, F6–F8 como rascunho).
- **F5 concluída** ✅.

### 25/11 (continuação) — F6: Textos
- **README.md** reescrito: tabela de links (protótipo público já preenchido), objetivo do produto, fluxo principal (com diagrama em texto), decisões de design (cores por função, tipografia, design system único, linguagem gentil, acessibilidade), e 3 screenshots reais das telas (Início, Sessão em andamento, Sessão concluída) — peguei via MCP (3 chamadas, só leitura) e salvei em `docs/screenshots/`.
- **docs/04-roteiro-video.md** escrito por completo: a fala de cada bloco de tempo (0:00–0:40 problema/usuário, 0:40–2:20 navegação no protótipo, 2:20–3:20 decisões de UX/UI, 3:20–4:00 diferenciais), calibrada pra um ritmo de leitura confortável dentro de 4 minutos.
- **F6 quase concluída** — falta só Paloma cronometrar lendo em voz alta.

### 26/11 — Ambiente de vídeo + teste de animação do mascote
- **Ambiente local de edição de vídeo** montado em `video-editor/` (fora do Figma, sem usar o Figma MCP): FFmpeg 9.1, Python 3.14 + MoviePy 2.2.1, faster-whisper 1.2.1 e auto-editor 29.3.1 — todos instalados e testados com um vídeo sintético (corte, extração de frames, remoção de silêncio, transcrição). **Gotcha encontrado:** o PyAV compatível com Python 3.14 (19.x) removeu o argumento `metadata_errors` que o faster-whisper usa internamente para decodificar áudio — contornado decodificando o áudio via FFmpeg para array numpy antes de passar pro Whisper (ver `video-editor/scripts/testar_whisper.py`).
- **Organização dos PNGs do mascote:** copiados (não movidos) de `Downloads/mascote/` pra `video-editor/entrada/mascote/`, renomeados por expressão. As 3 imagens exportadas do Figma têm 1254×1254px, RGBA, fundo transparente — nenhuma precisou ser reexportada. Mapeamento por expressão visual (os nomes originais não usavam os termos do projeto): "Sorridente" (sorriso simples) → `feliz.png`; "Determinada" (sobrancelha séria) → `focado.png`; "Contente" (boca bem aberta, sorriso largo) → `comemorando.png` — **a confirmar com a Paloma**, já que "Sorridente" e "Contente" são sinônimos no nome do arquivo.
- **Teste de animação** em `video-editor/scripts/animar_mascote.py` (só MoviePy + PIL, nada novo instalado): clipe de 8s, 1080p, tela dividida (metade creme-lunar `#FFF8EC`, metade noite `#1B1846`) pra comparar o mascote nos dois fundos ao mesmo tempo. Sequência: pop de entrada (Feliz, escala 0→110%→100%) → flutuação suave (±7px, ciclo de 2s) → fade curto pra Focado → flutuação → fade curto pra Comemorando com pulinho (2 saltos amortecidos). Gerado em `video-editor/saida/teste-mascote.mp4`, com 4 frames extraídos (entrada, flutuando, troca de expressão, comemoração) e mostrados pra Paloma.
- **Aguardando aprovação da Paloma** antes de usar no vídeo pitch de verdade (timebox do mascote: 30 min no total, máx. 2 rodadas de ajuste).

---

## ✅ O que já está pronto
- **F0, F1, F2:** concluídas.
- **F3 (Library): concluída e congelada.** Variables (3 coleções, incluindo `vermelho/600` e `destaque/erro`), 7 Text Styles, Fundamentos completos (paleta + tipografia + medidas), 4 componentes atômicos + 7 compostos + Mascote, auditoria limpa.
- **F4 — as 7 telas e o protótipo: concluídos.** Telas organizadas dentro da section correta, 14 interações ligadas e conferidas, frame inicial definido, fluxo aprovado por Paloma, link público gerado.
- **F5 — Acessibilidade: concluída.** `vermelho/600` corrigido (#C23434), `Barra/Topo` corrigido (48px), auditoria das 7 telas 100% conforme, seções 1.4 e 1.5 escritas, docs/prompts.md criado.
- **F6 — Textos: quase concluída.** README completo com screenshots, roteiro do vídeo escrito e calibrado.

## ⏭️ O que falta (nesta ordem)
1. **Paloma à mão:** ler `docs/04-roteiro-video.md` em voz alta e cronometrar (≤ 4 min); ajustar o texto se passar. Isso fecha a F6.
2. **F7 — Vídeo pitch** (à mão, Paloma grava e sobe no YouTube não listado).
3. **F8 — Entrega** (à mão) — nesse ponto também preencher as sections "Capa" e "Arquivo" do Figma (se houver algo a arquivar).

Cronograma detalhado com estimativas de tempo e chamadas: ver `PROJECT_OVERVIEW.md` → 📅 Cronograma.

---

## 🧠 Lições aprendidas (para não repetir erro)
- **Nomes de property diferentes** quando variantes têm texto padrão diferente — mesmo nome funde a property.
- **`resize()` reseta sizing modes para `FIXED`** — só restaurar `AUTO`/`FILL` depois do `resize()`, nunca antes.
- **Frame-wrapper sem `resize()` nem sizing mode explícito** pode ficar preso no padrão do Figma (100×100 fixo), não em hug — setar `counterAxisSizingMode = 'AUTO'` explicitamente.
- **Tokens pensados para fundo claro** (como `texto/secundario`) podem falhar o contraste em telas de fundo escuro (`bg/foco`) — conferir caso a caso, não assumir que todo token serve em qualquer fundo.
- **"Espaço" placeholder → spacer com `layoutSizingVertical: FILL`** é o equivalente real em Auto Layout (em vez de um frame cinza vazio).
- **`layoutSizingHorizontal/Vertical = 'FILL'` só funciona depois que a instância já tem um pai em Auto Layout** — setar antes de `insertChild`/`appendChild` lança erro e desfaz o script inteiro (nenhuma mutação anterior é salva). Ordem certa: criar → inserir no pai → setar sizing.
- **Componentes com várias variantes podem expor todas as properties de texto em cada instância**, mesmo quando só uma é visualmente usada por variante (caso do `Card/Métrica`). Nunca assumir "a primeira property de texto encontrada" — sempre setar pelo nome exato correspondente à variante.
- **`clone()` + `page.appendChild()` nunca coloca um nó dentro de uma *section*** — mesmo que as coordenadas coincidam visualmente com a área da section, o nó fica solto no canvas. Para colocar de fato dentro, use `section.appendChild(node)` (que preserva a posição visual absoluta automaticamente) e só depois ajuste x/y se quiser reorganizar.
- **Figma não suporta digitação real em modo de apresentação** — é uma limitação da ferramenta (não dá pra "codar" isso). O truque possível é simular com **Change to** entre variantes de texto diferentes (ex. Input Vazio → Foco → Preenchido), mas isso precisa ser configurado nas reactions dos próprios variants do componente pra funcionar em toda instância automaticamente.
- **As telas nunca vinculam direto a um Primitivo, só a Tokens** — ao auditar uso de uma cor "crua" (ex. `indigo/300`), buscar pelo nome do Primitivo retorna vazio mesmo que ela esteja em uso; é preciso buscar pelo nome do Token que aponta pra ela (ex. `acao/borda`).
- **Um script de auditoria que percorre toda a árvore de nós (incluindo dentro de instâncias) é muito mais barato que vários `get_metadata`** — dá pra pegar Text Style, conteúdo de texto, fills vinculados e nós com reactions (toque) tudo de uma vez, numa chamada só.

## Prompt para retomar no Claude Code
> Leia CLAUDE.md, PROJECT_OVERVIEW.md e PONTO-DE-RETOMADA.md. README e roteiro do vídeo já estão escritos (F6 quase pronta), o documento teórico foi reforçado com o processo formal de UX e a página "🧠 Processo UX" já existe no Figma. Eu cronometrei o roteiro em voz alta — [resultado]. Me ajude a ajustar o texto se precisar, e depois vamos pra F7 (preparar a gravação do vídeo).
