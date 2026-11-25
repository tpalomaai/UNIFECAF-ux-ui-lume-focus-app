# CLAUDE.md — Lume (App de Sessão de Foco)

> Leia este arquivo inteiro antes de qualquer tarefa. Ele é a fonte única de verdade do projeto.

## Contexto
- Trabalho UniFECAF: **"Da Ideia à Experiência: Projetando e Prototipando uma Interface Digital com Figma"** (Design de Interação e Interface UX/UI).
- Entregáveis (7,0 pts):
  1. Documento teórico — 1,5 pt (1.1 Problema e Usuário · 1.2 Jornada · 1.3 Estrutura UX · 1.4 Decisões UI · 1.5 Acessibilidade)
  2. Protótipo navegável no Figma + README — 3,5 pts (4–6 telas, interações, design system, organização, link público)
  3. Vídeo pitch ≤ 4 min — 2,0 pts (YouTube não listado)
- Fontes de referência: Figma Learn, Nielsen Norman Group, Material Design, Laws of UX, WCAG.

## Prazo
Entrega: **30/11/2026**. Meta interna: tudo pronto na sex 27/11 (ver cronograma no PROJECT_OVERVIEW.md).

## Repositório
https://github.com/tpalomaai/UNIFECAF-ux-ui-lume-focus-app

## Produto
**Lume** — app mobile de foco **sem pressão**: em vez de contagem regressiva, um cronômetro progressivo mede quanto tempo cada tarefa leva. Com o histórico, a pessoa melhora no próprio ritmo. O app guarda onde ela parou e o próximo passo, para retomar em segundos.

### Público
Universitários EAD, profissionais em home office e estudantes de idiomas — adultos que estudam ou trabalham sozinhos, em casa, com tempo fragmentado. Persona principal: Camila, 29 (ver docs/01-teorico.md).

### Diferenciais
1. **Cronômetro sem pressão** — conta o tempo para cima, sem prazo nem alarme; a sessão termina quando a usuária toca em "Concluir".
2. **Histórico por tarefa** — cada tarefa mostra "última vez: X min"; comparação gentil ao concluir.
3. **Continuar daqui** — "Onde parei" + "Próximo passo" registrados no fim; botão "Retomar" no Início.
4. **Lembrar depois** — anota uma tarefa paralela em 1 toque e volta para a sessão.

### Fluxo principal (6 telas)
01 - Boas-vindas → 02 - Início → 03 - Escolher tarefa → 04 - Sessão em andamento ⇄ 05 - Lembrar depois → 06 - Sessão concluída → 02 - Início
(Atalho: 02 "Retomar" → 04 — **Retomar é o botão primário do Início**)
(Pausa: 04 "Pausar" ⇄ "Continuar" — estado da tela 04; no wireframe é o frame 04b - Sessão pausada, na F4 vira interactive component)

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
| Tempo | Cronômetro progressivo — **nunca** contagem regressiva, alarme ou cor de alerta |
| Linguagem | Gentil, sem cobrança ("e tudo bem"); nunca "falhou" ou "atrasou" |

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
| F1 UX | docs/01-teorico.md (1.1–1.3) + docs/02-fluxo.md | 2 h | ✅ concluída (fluxo aprovado) |
| F2 Wireframe | 6 telas em cinza no Figma | 1–2 h | ✅ concluída (revisada) |
| F3 Library | Variables, Text Styles, Componentes (docs/03-design-system.md) | 2 h | componentes prontos |
| F4 Telas + Protótipo | 6 telas só com instâncias + interações | 3 h | fluxo clicável completo |
| F5 Acessibilidade | Checklist WCAG + doc 1.4–1.5 | 1 h | checklist 100% |
| F6 Textos | README + roteiro do vídeo (reaproveitar doc teórico) | 2 h | revisado |
| F7 Vídeo | Gravação ≤ 4 min | 1 h | link público |
| F8 Entrega | Conferência final + envio no portal | 30 min | trabalho enviado |

## Library Figma — resumo
Detalhes completos em `docs/03-design-system.md`.
- Variables: `Primitivos` → `Tokens` (telas usam só tokens) → `Medidas`.
- Text Styles: `Display/Saudação`, `Título/Tela`, `Título/Seção`, `Corpo/Padrão`, `Corpo/Destaque`, `Legenda/Padrão`, `Cronômetro/Número`.
- Componentes: Botão, Botão/Grande, Input, Chip/Tarefa, Card/Tarefa, Card/ContinuarDaqui, Card/Métrica, Card/Lembrete, Cronômetro, Header/Saudação, Mascote, Barra/Topo.
- Tudo em Auto Layout. Nenhum valor solto nas telas.

## Como trabalhar comigo (Claude)
- Faça no máximo 5 perguntas antes de começar uma fase.
- Uma proposta por vez, sem oferecer várias alternativas visuais.
- Ao fim de cada sessão, atualize PROJECT_OVERVIEW.md ("Onde estou" + "Continuar daqui").
- Textos: claros, curtos, sem enrolação.

### 💳 Política de uso do Figma MCP
Limite do plano: 200 chamadas/dia e 10/min. Meta: no máximo 40 por dia.

| Claude via MCP (repetitivo, em lote, precisão de tokens) | Paloma à mão (poucos cliques, ajuste pontual) |
|---|---|
| Criar componentes com variantes (Botão, Chip, Input, Cards, Cronômetro) | Renomear, mover ou alinhar 1 elemento |
| Ligar variables/tokens em vários elementos de uma vez | Trocar 1 texto, 1 cor ou 1 ícone |
| Montar as telas finais com instâncias | Ajustar o tamanho de seções e frames |
| Criar as interações do protótipo (muitas ligações) | Testar o protótipo no Present/Preview |
| Auditoria do arquivo (tokens soltos, nomes, Auto Layout) | Gerar o link público e configurar o compartilhamento |
| Qualquer tarefa com mais de ~10 elementos parecidos | Qualquer tarefa com menos de ~5 cliques |

Na dúvida: se eu levo menos de 3 minutos à mão, me passe o passo a passo em vez de usar o MCP.

Como economizar:
1. **Lote:** junte o máximo de trabalho numa única chamada de escrita, e não uma por peça.
2. **Leitura barata primeiro:** get_metadata antes de screenshot; leia só o nó que vai editar.
3. **IDs guardados:** use e mantenha atualizado o docs/figma-ids.md (páginas, seções, frames, componentes); não busque de novo um ID que já está lá.
4. **Aviso de custo:** antes de cada bloco, informe "custo estimado: N chamadas". Se passar de 15, espere a minha aprovação.
5. **Placar:** ao fim de cada bloco, informe "chamadas usadas nesta sessão: X / meta diária 40".
6. **Erro de limite (429):** pare na hora, sem tentar de novo em loop, e me passe o restante como passo a passo à mão.
7. Nunca use o MCP para conferir algo que eu já confirmei, nem para testar a conexão.

### 🔁 Self-Refine em toda execução
A cada tarefa (Figma, documentos ou repositório):
1. **Gerar:** faça a tarefa.
2. **Criticar:** confira com a lista abaixo. No Figma, comece pela metadata e tire no máximo 1 screenshot por bloco (não por item).
   - Segue as decisões travadas e a Lista do NÃO?
   - No Figma: toda cor é token, todo texto tem Text Style, todo frame com filhos tem Auto Layout, nomes no padrão `Categoria/Nome`, nada vazando ou sobreposto, nenhum valor solto?
   - Acessibilidade: contraste AA, toque mínimo de 48 px, rótulos visíveis, linguagem gentil (nunca "falhou" ou "atrasou")?
   - Atende ao critério de pronto e bate com docs/01-teorico.md e docs/02-fluxo.md?
3. **Refinar:** corrija e critique de novo. No máximo 2 rodadas; se ainda falhar, pare e me explique.
4. **Relatar:** primeiro o resultado (o que fez, o que a crítica encontrou, o que corrigiu, o que ficou pendente, chamadas usadas) e só depois a próxima ação ou os comandos.
