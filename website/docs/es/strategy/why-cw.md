# Por Que Usar `cw` en GPT Codex + VS Code

Si, esto es habitual en websites de repositorios GitHub profesionales.

Un portal de documentacion debe explicar:

- que problema resuelve el proyecto;
- que ventaja real aporta;
- cuando no es necesario.

Esta pagina lo cubre sin metricas artificiales.

## Problema que Resuelve `cw`

Sin un modelo operativo, el uso de Codex en proyectos grandes suele tener:

- prompts inconsistentes entre personas;
- transicion debil entre planificacion, implementacion y validacion;
- pasos de release y gobernanza omitidos bajo presion;
- trabajo repetido de setup entre repositorios.

## Que Aporta `cw`

`cw` agrega un modelo repetible de ejecucion sobre Codex:

- activacion explicita de workflow (`cw /orchestrate`, `cw /debug`, etc.);
- contratos codex-native para comportamiento de workflows;
- packs de validacion por dominio y stack (Node, Python, Rust);
- automatizacion de CI y release alineada con operacion real;
- docs multilanguage y playbooks operativos.

## Comparativo: Con y Sin `cw`

| Dimension | Sin `cw` | Con `cw` |
| --- | --- | --- |
| Inicio de tarea | El estilo de prompt varia por persona | Trigger explicito de workflow y objetivo |
| Trabajo multi-dominio | Coordinacion ad hoc | `/orchestrate` con fases estructuradas |
| Disciplina de validacion | Facil omitir checks | Rutinas de validacion y gates de CI |
| Higiene de release | Manual y propenso a errores | Flujo automatizado de tag/changelog/release |
| Onboarding | Conocimiento disperso en chats | Docs, ejemplos y comandos centralizados |
| Repetibilidad | Depende de memoria individual | Convenciones y checks de repositorio |

## Cuando `cw` No es Necesario

Para tareas muy pequenas y puntuales, prompts directos pueden ser suficientes.

`cw` aporta mas cuando necesitas:

- consistencia entre colaboradores;
- gates de calidad auditables;
- operacion y release a escala.

## Recomendacion Practica

Usa un modelo mixto:

1. Tareas simples: prompt directo.
2. Trabajo de producto: workflows `cw` + validaciones.
3. Ciclos de release: automatizacion de checks y pipeline.
