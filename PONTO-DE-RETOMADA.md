# 📍 Ponto de retomada — Lume

> Última atualização: **25/11/2026**, antes de uma pausa. Leia este arquivo primeiro; ele tem o histórico completo. Para o dia a dia (próxima ação, cronograma), use `PROJECT_OVERVIEW.md`.
> Arquivo Figma: [Lume — UX/UI](https://www.figma.com/design/z7C1XSWQhlIpYry549Ba3Q)

## 🧭 Onde parei exatamente
Terminei de montar as telas **04 (Sessão em andamento)** e **04b (Sessão pausada)** com instâncias reais da Library, na página 📱 Telas. Faltam as telas **01, 02, 03, 05 e 06** (mesmo método), depois as interações do protótipo e o link público. Parei porque bati na meta de 40 chamadas do dia — nada quebrado, só uma pausa de orçamento.

**Chamadas do Figma MCP usadas hoje (25/11): 39 / 40.** Reinicia amanhã.

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

---

## ✅ O que já está pronto
- **F0, F1, F2:** concluídas.
- **F3 (Library): concluída e congelada.** Variables (3 coleções, incluindo `vermelho/600` e `destaque/erro`), 7 Text Styles, Fundamentos completos (paleta + tipografia + medidas), 4 componentes atômicos + 7 compostos + Mascote, auditoria limpa.
- **F4 (em andamento):** 7 telas duplicadas para 📱 Telas · telas **04** e **04b** montadas com instâncias.

## ⏭️ O que falta (nesta ordem)
1. **Telas 01, 02, 03, 05, 06** — montar com instâncias da Library, mesmo método das 04/04b (ver `docs/figma-ids.md` para todos os IDs de componentes e telas). Lotes sugeridos: 01+05 juntas (mais simples), depois 02, depois 03, depois 06.
2. **Interações do protótipo** — todas as ligações (Começar → Início → Configurar → Sessão; Lembrar depois → anotação → volta; Retomar → atalho; Concluir → Sessão concluída → Início; Pausar/Continuar entre 04 e 04b via Change to/Smart Animate); frame inicial; transições.
3. **Paloma à mão:** testar no Present/Preview e gerar o link público.
4. **F5 — Acessibilidade:** auditoria de contraste AA (incluindo o token novo `destaque/erro`), toque ≥ 48px, doc 1.4–1.5.
5. **F6 — Textos:** README + roteiro do vídeo.
6. **F7 — Vídeo pitch** (à mão).
7. **F8 — Entrega** (à mão).

Cronograma detalhado com estimativas de tempo e chamadas: ver `PROJECT_OVERVIEW.md` → 📅 Cronograma.

---

## 🧠 Lições aprendidas (para não repetir erro)
- **Nomes de property diferentes** quando variantes têm texto padrão diferente — mesmo nome funde a property.
- **`resize()` reseta sizing modes para `FIXED`** — só restaurar `AUTO`/`FILL` depois do `resize()`, nunca antes.
- **Frame-wrapper sem `resize()` nem sizing mode explícito** pode ficar preso no padrão do Figma (100×100 fixo), não em hug — setar `counterAxisSizingMode = 'AUTO'` explicitamente.
- **Tokens pensados para fundo claro** (como `texto/secundario`) podem falhar o contraste em telas de fundo escuro (`bg/foco`) — conferir caso a caso, não assumir que todo token serve em qualquer fundo.
- **"Espaço" placeholder → spacer com `layoutSizingVertical: FILL`** é o equivalente real em Auto Layout (em vez de um frame cinza vazio).

## Prompt para retomar no Claude Code
> Leia CLAUDE.md, PROJECT_OVERVIEW.md e PONTO-DE-RETOMADA.md. Estou na F4, preciso montar as telas 01, 02, 03, 05 e 06 com instâncias da Library (mesmo método usado nas telas 04/04b). Siga a política de uso do MCP (lote, aviso de custo, placar).
