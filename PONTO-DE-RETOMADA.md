# 📍 Ponto de retomada — Lume

> Última atualização: **25/11/2026**. Leia este arquivo primeiro; ele tem o histórico completo. Para o dia a dia (próxima ação, cronograma), use `PROJECT_OVERVIEW.md`.
> Arquivo Figma: [Lume — UX/UI](https://www.figma.com/design/z7C1XSWQhlIpYry549Ba3Q)

## 🧭 Onde parei exatamente
**A F4 está praticamente concluída.** As 7 telas (01, 02, 03, 04, 04b, 05, 06) estão montadas com instâncias reais da Library, dentro da section "📱 Telas finais" (corrigido — ver histórico), e as 14 interações do protótipo estão todas ligadas e conferidas (navegação completa, pausa como Change to/Smart Animate, botões voltar com ação Back, frame inicial na tela 01).

**Falta só:**
1. Paloma testar o fluxo inteiro no Present/Preview.
2. Paloma gerar o link público do protótipo e colar no `PROJECT_OVERVIEW.md` (tabela 🔗 Links de acesso).

Depois disso a F4 fecha de vez e seguimos para a F5 (Acessibilidade).

**Chamadas do Figma MCP usadas hoje (25/11), somando todas as sessões: ~80.** Passou bem da meta própria de 40/dia (o limite real do plano Professional é 200/dia — ainda há folga real).

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

---

## ✅ O que já está pronto
- **F0, F1, F2:** concluídas.
- **F3 (Library): concluída e congelada.** Variables (3 coleções, incluindo `vermelho/600` e `destaque/erro`), 7 Text Styles, Fundamentos completos (paleta + tipografia + medidas), 4 componentes atômicos + 7 compostos + Mascote, auditoria limpa.
- **F4 — as 7 telas e o protótipo: concluídos.** Telas organizadas dentro da section correta, 14 interações ligadas e conferidas, frame inicial definido.

## ⏭️ O que falta (nesta ordem)
1. **Paloma à mão:** testar o fluxo inteiro no Present/Preview.
2. **Paloma à mão:** gerar o link público do protótipo e colar no `PROJECT_OVERVIEW.md` (🔗 Links de acesso). Isso fecha a F4.
3. **F5 — Acessibilidade:** auditoria de contraste AA (incluindo o token novo `destaque/erro`), toque ≥ 48px, doc 1.4–1.5.
4. **F6 — Textos:** README + roteiro do vídeo.
5. **F7 — Vídeo pitch** (à mão).
6. **F8 — Entrega** (à mão) — nesse ponto também preencher as sections "Capa" e "Arquivo" (se houver algo a arquivar).

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

## Prompt para retomar no Claude Code
> Leia CLAUDE.md, PROJECT_OVERVIEW.md e PONTO-DE-RETOMADA.md. A F4 está pronta (telas + protótipo); só falta eu testar no Present e gerar o link público. Depois disso, me ajude a começar a F5 (acessibilidade: contraste AA, toque mínimo, doc 1.4–1.5).
