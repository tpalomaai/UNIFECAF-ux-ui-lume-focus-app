# Documento Teórico — Lume

> Status: **rascunho F1** (seções 1.1–1.3). Seções 1.4 e 1.5 serão escritas na F5.

---

## 1.1 Problema e Usuário

### Qual problema o produto resolve?
Pessoas que estudam ou trabalham **sozinhas e de forma remota** não têm uma estrutura externa que as ajude a manter o foco: não há professor, colega ou horário fixo que "puxe" a atenção de volta. O resultado é um ciclo conhecido: demora para começar, distração no meio da tarefa e, ao voltar, tempo perdido para lembrar onde parou.

Os apps de foco existentes costumam piorar o cenário para iniciantes: pedem muita configuração antes da primeira sessão, punem a distração (em vez de ajudá-la) e não guardam o contexto da tarefa. Isso gera **baixa adesão e abandono nas primeiras interações** — exatamente o problema descrito pela startup.

O **Lume** resolve isso com sessões curtas que começam em poucos toques, um jeito rápido de "estacionar" distrações sem sair do foco e um registro de uma frase sobre onde a pessoa parou, que aparece na próxima sessão.

### Quem é o usuário?
Adultos que **aprendem ou trabalham por conta própria, em casa**, com tempo fragmentado:

| Perfil | Contexto |
|---|---|
| Universitários EAD | Assistem aulas e fazem atividades sozinhos, muitas vezes à noite, depois do trabalho |
| Profissionais em home office | Alternam tarefas, reuniões e interrupções da casa sem a estrutura do escritório |
| Estudantes de idiomas | Estudam em blocos curtos e frequentes (lições, flashcards, leitura), em geral sem professor ao lado |

#### Persona principal
**Camila, 29 anos** — cursa graduação EAD e trabalha em home office. Estuda inglês no tempo livre.
- **Rotina:** trabalha durante o dia; estuda em janelas de 20 a 40 minutos, à noite ou no começo da manhã.
- **Ferramentas:** celular sempre por perto, notebook para trabalho e faculdade.
- **Frase:** *"Quando finalmente sento para estudar, gasto metade do tempo tentando lembrar onde parei."*
- **Objetivo:** usar bem as poucas janelas de tempo que tem e sentir que está avançando.
- **Frustração:** já baixou apps de pomodoro, mas desistiu em poucos dias porque eram complicados de configurar ou faziam ela se sentir culpada quando se distraía.

### Quais dores e necessidades existem?
| Dores | Necessidades |
|---|---|
| **Dificuldade de começar:** muitas decisões antes de iniciar (quanto tempo? qual tarefa? quais configurações?) | **Começar em segundos**, com poucas escolhas |
| **Distração sem supervisão:** celular, pensamentos soltos ("preciso responder aquela mensagem") e interrupções da casa | **Lidar com a distração sem culpa** e sem perder a ideia que surgiu |
| **Perda de contexto ao retomar:** tempo gasto para lembrar onde parou depois de uma pausa ou de um dia para o outro | **Retomar de onde parou**, sem precisar reconstruir o raciocínio |

> 🔎 **Hipóteses a validar com a autora (perguntas 2–5):**
> 1. A principal fonte de distração é o celular e pensamentos soltos, mais do que ruído externo.
> 2. Apps de foco anteriores foram abandonados por excesso de configuração ou gamificação punitiva.
> 3. Retomar uma tarefa depois de uma interrupção custa vários minutos.
> 4. O uso principal é no celular, em sessões de 15 a 45 minutos.

---

## 1.2 Jornada do Usuário

### Fluxo principal
Boas-vindas → Início → Configurar sessão → Sessão em andamento ⇄ Estacionamento de distrações → Resumo da sessão → Início

### Etapas e objetivos em cada interação
| Etapa | Objetivo da usuária | Ação no app | Tela | Sentimento | Oportunidade de design |
|---|---|---|---|---|---|
| 1. Primeiro acesso | Entender rápido para que serve | Lê uma frase e toca em "Começar" | 01 - Boas-vindas | Curiosa, mas impaciente 😐 | Uma tela só, sem cadastro obrigatório |
| 2. Decidir o que fazer | Saber por onde começar | Vê o card "Continuar daqui" e toca em "Nova sessão" | 02 - Início | Aliviada por não ter que lembrar 🙂 | Ação principal grande e óbvia |
| 3. Preparar a sessão | Definir tarefa e tempo sem pensar muito | Escreve a tarefa e escolhe 15, 25 ou 45 min | 03 - Configurar sessão | Decidida 🙂 | Só 3 opções de duração |
| 4. Focar | Trabalhar sem interrupções | Acompanha o timer | 04 - Sessão em andamento | Concentrada 😌 | Tela escura e limpa, só o essencial |
| 5. Distrair-se | Tirar o pensamento da cabeça sem perder o foco | Toca em "Me distraí", anota e volta | 05 - Estacionamento | Culpada → aliviada 😟→🙂 | Distração tratada como algo normal, não como erro |
| 6. Concluir | Sentir que avançou e registrar onde parou | Vê o resumo e escreve 1 frase em "Continuar daqui" | 06 - Resumo da sessão | Orgulhosa 😄 | Final positivo, com celebração |
| 7. Voltar outro dia | Retomar sem esforço | Abre o app e lê onde parou | 02 - Início | Confiante 🙂 | O ciclo recomeça com contexto |

---

## 1.3 Estrutura da Solução (UX)

### Organização das telas
O app tem **6 telas** e um único fluxo principal, organizado em três momentos:

| Momento | Telas | Papel |
|---|---|---|
| **Antes do foco** | 01 Boas-vindas · 02 Início · 03 Configurar sessão | Começar rápido, com contexto |
| **Durante o foco** | 04 Sessão em andamento · 05 Estacionamento de distrações | Manter a atenção e lidar com interrupções |
| **Depois do foco** | 06 Resumo da sessão | Fechar o ciclo e preparar a próxima vez |

### Lógica de navegação
- **Linear e previsível:** cada tela tem **uma ação principal**, que leva à próxima etapa.
- **Um único desvio:** da Sessão, o botão "Me distraí" abre o Estacionamento, que sempre volta para a mesma sessão, com o timer preservado.
- **Ciclo fechado:** o Resumo sempre leva de volta ao Início, onde o "Continuar daqui" mostra a frase registrada.
- **Sem menus escondidos:** não há abas, menu lateral ou configurações obrigatórias no fluxo principal.

### Decisões tomadas para facilitar o uso
| Decisão | Princípio (Laws of UX) | Como aparece no Lume |
|---|---|---|
| Só 3 durações fixas | **Lei de Hick:** quanto mais opções, mais tempo para decidir | Chips de 15, 25 e 45 min, sem campo de minutos livre |
| Botão "Nova sessão" grande e na parte de baixo da tela | **Lei de Fitts:** alvos grandes e próximos são mais rápidos de tocar | Botão de destaque ao alcance do polegar |
| "Continuar daqui" | **Efeito Zeigarnik:** tarefas inacabadas ficam na mente; registrá-las alivia essa carga e facilita a retomada | Frase registrada no fim da sessão aparece no Início |
| "Me distraí" em vez de bloquear ou punir | **Carga cognitiva:** tirar o pensamento da cabeça libera atenção para a tarefa | Anotação rápida e volta imediata ao timer |
| Celebração no Resumo | **Regra do pico-fim:** as pessoas lembram de uma experiência pelo seu ponto alto e pelo final | Resumo com tempo focado, mascote comemorando e tom positivo |
| Timer circular e botões conhecidos (Pausar/Play) | **Lei de Jakob:** usuários preferem padrões que já conhecem de outros apps | Nada a aprender: o timer funciona como os outros |

---

## 1.4 Decisões de Interface (UI)
*(F5)*

## 1.5 Acessibilidade e Inclusão
*(F5)*

---

### Referências
- Laws of UX — https://lawsofux.com
- Nielsen Norman Group — https://www.nngroup.com
- Material Design — https://m3.material.io
- WCAG — https://www.w3.org/WAI/standards-guidelines/wcag/
