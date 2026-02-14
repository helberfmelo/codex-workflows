# Por que usar `cw` no GPT Codex + VS Code

O `cw` padroniza como você planeja, executa e valida tarefas com o Codex no VS Code.

Sem esse padrão, equipes tendem a ter prompts inconsistentes, validação fraca e releases manuais mais suscetíveis a erro.

Com `cw`, você ganha workflows explícitos, gates de qualidade, automação de release e onboarding mais rápido.

## Problema que o `cw` resolve

Sem um modelo operacional, o uso do Codex em projetos maiores tende a apresentar:

- prompts inconsistentes entre colaboradores;
- transição fraca entre planejamento, implementação e validação;
- etapas de release e governança puladas sob pressão;
- retrabalho de setup em repositórios diferentes.

## O que o `cw` adiciona

O `cw` adiciona um modelo repetível de execução sobre o Codex:

- ativação explícita de workflow (`cw /orchestrate`, `cw /debug`, etc.);
- contratos codex-native para o comportamento dos fluxos;
- packs de validação por domínio e stack (Node, Python e Rust);
- automação de CI e release alinhada com a operação real;
- documentação multilíngue e playbooks operacionais.

## Comparativo: com e sem `cw`

| Dimensão | Sem `cw` | Com `cw` |
| --- | --- | --- |
| Início de tarefa | Estilo de prompt varia por pessoa | Trigger explícito de workflow e objetivo |
| Trabalho multidomínio | Coordenação ad hoc | `/orchestrate` com fases estruturadas |
| Disciplina de validação | Fácil pular checks | Rotinas de validação e gates de CI |
| Higiene de release | Manual e sujeito a erro | Fluxo automatizado de tag/changelog/release |
| Onboarding | Conhecimento disperso no chat | Docs, exemplos e comandos centralizados |
| Repetibilidade | Depende da memória individual | Convenções e checks de repositório |

## Quando o `cw` não é necessário

Para tarefas muito pequenas e pontuais, prompts diretos no Codex podem bastar.

O `cw` passa a valer mais quando você precisa de:

- consistência entre colaboradores;
- gates de qualidade auditáveis;
- operação e release em escala.

## Recomendação prática

Use um modelo misto:

1. Tarefa simples: prompt direto.
2. Trabalho de produto: workflows `cw` + validações.
3. Ciclo de release: automação de checks e pipeline.
