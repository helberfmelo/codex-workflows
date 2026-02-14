# Por Que Usar `cw` no GPT Codex + VS Code

Sim, isso e comum em websites de repositorios GitHub mais profissionais.

Um portal de documentacao deve explicar:

- qual problema o projeto resolve;
- qual vantagem real ele entrega;
- quando ele nao e necessario.

Esta pagina faz isso sem metricas artificiais.

## Problema que o `cw` Resolve

Sem um modelo operacional, o uso do Codex em projetos maiores tende a ter:

- prompts inconsistentes entre pessoas;
- transicao fraca entre planejamento, implementacao e validacao;
- etapas de release e governanca puladas sob pressao;
- retrabalho de setup em repositorios diferentes.

## O que o `cw` Adiciona

O `cw` adiciona um modelo repetivel de execucao sobre o Codex:

- ativacao explicita de workflow (`cw /orchestrate`, `cw /debug`, etc.);
- contratos codex-native para comportamento dos fluxos;
- packs de validacao por dominio e stack (Node, Python, Rust);
- automacao de CI e release alinhada com operacao real;
- docs multilanguage e playbooks operacionais.

## Comparativo: Com e Sem `cw`

| Dimensao | Sem `cw` | Com `cw` |
| --- | --- | --- |
| Inicio de tarefa | Estilo de prompt varia por pessoa | Trigger explicito de workflow e objetivo |
| Trabalho multi-dominio | Coordenacao ad hoc | `/orchestrate` com fases estruturadas |
| Disciplina de validacao | Facil pular checks | Rotinas de validacao e gates de CI |
| Higiene de release | Manual e sujeito a erro | Fluxo automatizado de tag/changelog/release |
| Onboarding | Conhecimento disperso no chat | Docs, exemplos e comandos centralizados |
| Repetibilidade | Depende da memoria individual | Convencoes e checks de repositorio |

## Quando o `cw` Nao e Necessario

Para tarefas muito pequenas e pontuais, prompts diretos no Codex podem bastar.

O `cw` passa a valer quando voce precisa de:

- consistencia entre colaboradores;
- gates de qualidade auditaveis;
- operacao e release em escala.

## Recomendacao Pratica

Use modelo misto:

1. Tarefa simples: prompt direto.
2. Trabalho de produto: workflows `cw` + validacoes.
3. Ciclo de release: automacao de checks e pipeline.
