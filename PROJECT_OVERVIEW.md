# ✦ Project Overview — Lume

> Abra este arquivo ao iniciar o dia, ao voltar de uma pausa longa ou quando se perder.
> Ao fim de cada sessão (2 min): atualize 🧭 Agora, 📍 Continuar daqui, marque as tarefas feitas e adicione 1 linha no 📓 Registro.

---

## 🧭 Agora
| | |
|---|---|
| **Fase atual** | F1 — UX (problema, persona, jornada, fluxo) |
| **Próxima ação (≤ 30 min)** | Preencher o prazo final → rodar o Prompt F1 e responder as perguntas sobre a usuária |
| **Bloqueios** | Nenhum |
| **Prazo final** | ____/____ (preencher) · faltam __ dias |
| **Última atualização** | 24/11/2026 |

## 📍 Continuar daqui
> F0 concluída: nome **Lume**, direção visual travada (fundo Creme lunar #FFF8EC, Lexend + Sniglet) e repositório no GitHub com toda a estrutura.
> Próximo: abrir o Claude Code na pasta do repositório e rodar o **Prompt F1**.

---

## 🔗 Links de acesso
| Item | Link | Status |
|---|---|---|
| 🐙 Repositório GitHub | [UNIFECAF-ux-ui-lume-focus-app](https://github.com/tpalomaai/UNIFECAF-ux-ui-lume-focus-app) | ✅ |
| 🎨 Arquivo Figma | (a criar na F2) | ⏳ |
| 🔗 Protótipo (link público) | (a gerar na F4) | ⏳ |
| 🎬 Vídeo pitch | (a gravar na F7) | ⏳ |
| 📄 Enunciado do trabalho | (salvar PDF no Vault) | ⏳ |

---

## 🗺️ Visão geral das etapas
| Fase | Entrega | Timebox | Status | Entregável vinculado |
|---|---|---|---|---|
| F0 Setup | Tema, direção visual, estrutura, repo | 30 min | ✅ Concluída | — |
| F1 UX | Problema, persona, jornada, fluxo | 2 h | ⚪ | Documento teórico (1,5) |
| F2 Wireframe | 6 telas em cinza + arquivo Figma organizado | 1–2 h | ⚪ | Protótipo (3,5) |
| F3 Library | Variables, Text Styles, Componentes | 2 h | ⚪ | Protótipo — Design System |
| F4 Telas + Protótipo | 6 telas finais + interações | 3 h | ⚪ | Protótipo — Navegação |
| F5 Acessibilidade | Checklist WCAG + doc 1.4–1.5 | 1 h | ⚪ | Documento teórico |
| F6 Textos | README + roteiro do vídeo + revisão do doc | 2 h | ⚪ | Protótipo — README |
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
- [ ] Preencher o prazo final
- [ ] Salvar o PDF do enunciado no Vault

**Pronto quando:** repositório online com a estrutura e prazo preenchido.

### F1 — UX · 2 h · ⚪
**Objetivo:** entender a usuária e validar o fluxo antes de desenhar qualquer coisa.
- [ ] Rodar o Prompt F1 no Claude Code
- [ ] Responder as até 5 perguntas sobre a usuária e as dores dela
- [ ] Revisar a persona (1 persona)
- [ ] Revisar 3 dores e 3 necessidades
- [ ] Revisar a jornada (tabela: etapa · objetivo · ação · sentimento)
- [ ] Revisar o fluxo em Mermaid das 6 telas (docs/02-fluxo.md)
- [ ] Revisar 3 decisões de UX com Laws of UX (Hick, Carga Cognitiva, Zeigarnik)
- [ ] **Aprovar o fluxo** (portão)

**Pronto quando:** seções 1.1, 1.2 e 1.3 do documento teórico escritas e fluxo aprovado.

### F2 — Wireframe · 1–2 h · ⚪
**Objetivo:** validar hierarquia e navegação sem cor.
- [ ] Criar o arquivo "Lume — UX/UI" no Figma
- [ ] Criar as páginas: 📖 Capa · 🎨 Fundamentos · 🧩 Componentes · 🔲 Wireframes · 📱 Telas · 🗂 Arquivo
- [ ] Rodar o Prompt F2 (tabela de elementos por tela)
- [ ] Desenhar os 6 frames em cinza (390×844), com nomes `01 - Boas-vindas` … `06 - Resumo da sessão`
- [ ] Ligar as telas com navegação simples (modo Prototype)
- [ ] Testar o fluxo clicando do início ao fim
- [ ] Colar o link do Figma acima

**Pronto quando:** as 6 telas existem, têm os nomes certos e navegam.

### F3 — Library · 2 h (rígido) · ⚪
**Objetivo:** criar todas as peças padronizadas antes das telas finais.
- [ ] Variables, coleção `Primitivos` (cores cruas)
- [ ] Variables, coleção `Tokens` (cores com função)
- [ ] Variables, coleção `Medidas` (espaço, raio, toque mínimo 48)
- [ ] Text Styles (7 estilos: Display, Títulos, Corpo, Legenda, Timer)
- [ ] Instalar/ativar as fontes Lexend e Sniglet no Figma
- [ ] Página 🎨 Fundamentos montada (paleta, tipografia, espaçamentos)
- [ ] Componentes atômicos: `Botão` (variantes), `Chip/Duração`, `Input`
- [ ] Componentes compostos: `Card/Tarefa`, `Card/ContinuarDaqui`, `Card/Métrica`, `Timer`, `Header/Saudação`, `Barra/Topo`
- [ ] `Mascote` (Feliz · Focado · Comemorando) — versão simples
- [ ] Tudo em Auto Layout e usando só variables
- [ ] **Congelar a Library** (portão)

**Pronto quando:** todos os componentes existem na página 🧩 Componentes.

### F4 — Telas finais + Protótipo · 3 h · ⚪
**Objetivo:** protótipo navegável completo, montado só com instâncias.
- [ ] Duplicar os wireframes para a página 📱 Telas
- [ ] Substituir os elementos cinza por instâncias da Library
- [ ] Tela 04 com fundo `bg/foco` (modo noite)
- [ ] Interações: Começar → Início → Configurar → Sessão
- [ ] Interação: "Me distraí" → Estacionamento → volta à Sessão
- [ ] Interação: fim da sessão → Resumo → Início
- [ ] Definir o frame inicial (flow starting point)
- [ ] Transições simples (Smart Animate ou Dissolve, 200–300 ms)
- [ ] Testar o fluxo inteiro em modo apresentação
- [ ] Gerar o link público do protótipo e colar acima

**Pronto quando:** o fluxo principal funciona do início ao fim pelo link público.

### F5 — Acessibilidade · 1 h · ⚪
**Objetivo:** garantir e documentar acessibilidade e inclusão.
- [ ] Rodar o Prompt F5
- [ ] Verificar contraste AA dos 4 pares de cor (docs/03-design-system.md)
- [ ] Conferir áreas de toque ≥ 48 px
- [ ] Conferir texto do corpo ≥ 14–16 px
- [ ] Conferir que nada depende só de cor (ícone + texto)
- [ ] Timer com indicação textual ("restam 16 minutos")
- [ ] Corrigir o que falhar (só via Library)
- [ ] Revisar doc 1.4 (Decisões de UI) e 1.5 (Acessibilidade e Inclusão)

**Pronto quando:** checklist 100% e seções 1.4 e 1.5 escritas.

### F6 — Textos · 2 h · ⚪
**Objetivo:** reaproveitar o documento teórico para o README e o vídeo.
- [ ] Revisão final do documento teórico (1.1 a 1.5)
- [ ] Exportar o documento teórico no formato pedido pelo portal
- [ ] Rodar o Prompt F6
- [ ] README: links em tabela no topo, objetivo, fluxo, decisões de design
- [ ] Adicionar 2–3 imagens das telas no README
- [ ] Roteiro do vídeo em tabela (tempo · fala · tela)
- [ ] Ler o roteiro em voz alta e cronometrar (≤ 4 min)
- [ ] Enviar tudo para o GitHub

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
- [ ] 1.1 Problema e Usuário
- [ ] 1.2 Jornada do Usuário
- [ ] 1.3 Estrutura da Solução (UX)
- [ ] 1.4 Decisões de Interface (UI)
- [ ] 1.5 Acessibilidade e Inclusão

**Protótipo Figma (3,5)**
- [ ] 4–6 telas com fluxo principal completo
- [ ] Interações configuradas e navegação funcional
- [ ] Design system: cores, tipografia, componentes reutilizáveis
- [ ] Telas nomeadas e arquivo organizado
- [ ] Link público + README (objetivo, fluxo, decisões)

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

---

## 📓 Registro de sessões (1 linha por sessão)
| Data | O que fiz | Tempo |
|---|---|---|
| 24/11 | Tema, plano, direção visual, Library definida, nome, estrutura F0 | ~50 min |

---

## 🅿️ Estacionamento de ideias (para depois da entrega)
- Animação do mascote ao concluir sessão
- Modo escuro completo
- 
