# Prompts por fase — Lume

> Registro dos prompts usados em cada fase do projeto, pelo Claude Code. **F0 a F4** são reconstruções fiéis a partir do histórico documentado em `PONTO-DE-RETOMADA.md` e `PROJECT_OVERVIEW.md` (as conversas originais não ficaram salvas como arquivo). **F5** é o prompt exato usado. **F6 a F8** são rascunhos para quando chegar a hora — ajustar conforme o que estiver pendente naquele momento.

---

## F0 — Setup
> Vamos começar um trabalho da UniFECAF de Design de Interação e Interface UX/UI: documento teórico + protótipo navegável no Figma + vídeo pitch. Me ajude a definir o tema, o nome, a direção visual e a estrutura do projeto (CLAUDE.md, docs/, Project Overview), e a criar o repositório no GitHub.

## F1 — UX
> Rode a pesquisa de UX: defina o público, faça uma entrevista comigo (como usuária real), escreva a persona, as dores e necessidades, a jornada do usuário (docs/02-fluxo.md) e as decisões de UX ligadas a princípios (Leis de UX, NN/g). Ao final, aprove o fluxo antes de passar pro wireframe.

## F2 — Wireframe
> Crie o arquivo "Lume — UX/UI" no Figma, com a estrutura de páginas definida (Library, Wireframes, Telas). Desenhe as 6 telas em cinza (390×844), nomeadas e na ordem do fluxo, e ligue a navegação básica entre elas no modo Prototype.

## F3 — Library
> Monte a Library do Figma: Variables (Primitivos → Tokens → Medidas), Text Styles, e todos os componentes com variantes (atômicos e compostos), tudo em Auto Layout e usando só tokens. Audite o arquivo inteiro antes de congelar a Library (portão antes da F4).

## F4 — Telas finais + Protótipo
> Duplique os wireframes para a página de Telas (sem alterar os originais), monte cada tela só com instâncias dos componentes da Library (trocando qualquer placeholder cinza), e ligue todas as interações do protótipo: navegação do fluxo principal, atalhos, pausa como interactive component, frame inicial e transições. Siga a Política de uso do Figma MCP e o Self-Refine do CLAUDE.md.

## F5 — Acessibilidade
*(prompt exato, usado em 25/11/2026)*

> Leia CLAUDE.md, PROJECT_OVERVIEW.md e PONTO-DE-RETOMADA.md antes de começar (git pull primeiro). Siga a Política de uso do Figma MCP e o Self-Refine do CLAUDE.md.
>
> ## F5 — Acessibilidade
> Objetivo: garantir e documentar acessibilidade e inclusão. Pronto quando: checklist 100% e seções 1.4 e 1.5 do docs/01-teorico.md escritas.
>
> ### Parte A — Contraste (já calculado fora do Figma; NÃO gaste chamadas recalculando)
> [tabela de contraste com os pares e resultados]
>
> Tarefas:
> 1. Proponha um novo hex para o primitivo `vermelho/600` que passe 4,5 sobre bg/app E sobre branco (com folga, ≥ 5,0), mantendo o tom de vermelho. Calcule em código (fórmula WCAG), não no Figma. Mostre o valor e os dois contrastes; espere eu aprovar antes de aplicar.
> 2. Na auditoria (Parte B), confirme que indigo/300 não é usado como cor de TEXTO em nenhum lugar, e que rosa/400 só aparece como barra decorativa (sem texto).
>
> ### Parte B — Auditoria das telas finais (1 lote via MCP, só get_metadata; máx. ~8 chamadas; avise o custo antes)
> [critérios: toque ≥48px, texto ≥14/12px, Text Style + token, rótulos visíveis, independência de cor, linguagem gentil, cronômetro]
>
> ### Parte C — Correções
> [repetitivo/Library → MCP em 1 lote; pontual → passo a passo pra Paloma à mão; Self-Refine ao final]
>
> ### Parte D — Documentação (sem MCP)
> [1.4 Decisões de Interface; 1.5 Acessibilidade e Inclusão; atualizar docs/03-design-system.md]
>
> ### Parte E — Registro
> [docs/prompts.md; PROJECT_OVERVIEW.md; PONTO-DE-RETOMADA.md; commit e push ao fim de cada parte]
>
> Ordem: A1 (proposta do vermelho) → espere aprovação → B → C → D → E. Relate o resultado antes de cada próxima etapa.

## F6 — Textos (README + roteiro do vídeo)
*(rascunho — ajustar antes de usar)*

> Com a F5 concluída, escreva o README do projeto (links em tabela no topo, objetivo, fluxo, decisões de design, 2–3 imagens das telas) reaproveitando docs/01-teorico.md. Depois monte o roteiro do vídeo pitch em tabela (tempo · fala · tela), cobrindo problema/usuário, navegação pelo protótipo, decisões de UX/UI e diferenciais, dentro de 4 minutos. Sem uso do Figma MCP.

## F7 — Vídeo pitch
*(rascunho — Paloma grava à mão; Claude ajuda a revisar o roteiro e a duração antes)*

> Revise comigo o roteiro do vídeo antes de eu gravar: confira se cobre problema/usuário, navegação, decisões de UX/UI e diferenciais, e se cabe em 4 minutos lendo em voz alta. Depois de eu gravar e subir no YouTube (não listado), me ajude a colar o link no README e no PROJECT_OVERVIEW.md.

## F8 — Entrega final
*(rascunho)*

> Antes de eu enviar no portal da UniFECAF, confira comigo o ✅ Checklist de entrega do PROJECT_OVERVIEW.md item por item (documento teórico, protótipo com link público, README, vídeo), e confirme que todos os links abrem em aba anônima.
