#!/usr/bin/env node
"use strict";

const childProcess = require("child_process");
const fs = require("fs");
const os = require("os");
const path = require("path");

const pkg = require("../package.json");

const ALL_SKILL_PATHS = [
  "skills/codex-workflows",
  "skills/codex-backend-pack",
  "skills/codex-frontend-pack",
  "skills/codex-security-pack",
  "skills/codex-qa-pack",
  "skills/codex-node-validation-pack",
  "skills/codex-python-validation-pack",
  "skills/codex-rust-validation-pack"
];

const CORE_SKILL_PATHS = ["skills/codex-workflows"];

const WORKFLOW_EXAMPLES = [
  ["/brainstorm", "Explore options before coding"],
  ["/plan", "Build phased implementation plan"],
  ["/create", "Implement from approved plan"],
  ["/enhance", "Evolve existing implementation safely"],
  ["/debug", "Diagnose, isolate and fix defects"],
  ["/test", "Strengthen tests and quality gates"],
  ["/deploy", "Prepare release and rollout flow"],
  ["/preview", "Generate demos and previews"],
  ["/status", "Summarize progress and remaining work"],
  ["/orchestrate", "Coordinate multi-domain execution phases"],
  ["/game-dev", "Design and build game systems"],
  ["/roblox-game-dev", "Build secure Roblox game workflows"],
  ["/ui-ux-pro-max", "Professional UI/UX execution flow"]
];

function printHelp() {
  console.log(`cw ${pkg.version}

Usage:
  npx @codex-workflow/cw                  Install all packs (all-in-one)
  npx @codex-workflow/cw install          Install all packs (explicit command)
  npx @codex-workflow/cw --core-only      Install only core skill
  npx @codex-workflow/cw doctor           Check local prerequisites
  npx @codex-workflow/cw /help            Show this help
  npx @codex-workflow/cw /examples        Show prompt examples

Install flags:
  --repo <owner/repo>         Default: helberfmelo/codex-workflows
  --ref <git-ref>             Default: main
  --method <auto|download|git> Default: auto
  --dest <skills-dir>         Custom destination skills directory
  --python-exec <bin>         Python executable override
  --installer-script <path>   install-skill-from-github.py override
  --core-only                 Install only skills/codex-workflows
  --force                     Reinstall even if already present
  --dry-run                   Print command only

Prompt usage (inside Codex chat, not terminal):
  cw /orchestrate <objective>
  cw /debug <objective>
  cw /plan <objective>`);
}

function printExamples() {
  console.log("Available workflows:");
  for (const [workflow, summary] of WORKFLOW_EXAMPLES) {
    console.log(`  ${workflow.padEnd(18, " ")} ${summary}`);
  }
  console.log("");
  console.log("Prompt examples:");
  console.log("  cw /orchestrate evolve this repository with phase gates");
  console.log("  cw /plan break this feature into milestones");
  console.log("  cw /debug investigate this failing integration test");
  console.log("  Use codex-workflows em /create para implementar a API");
}

function codexHome() {
  return path.resolve(process.env.CODEX_HOME || path.join(os.homedir(), ".codex"));
}

function installerScriptPath(home) {
  return path.join(home, "skills", ".system", "skill-installer", "scripts", "install-skill-from-github.py");
}

function unique(values) {
  return [...new Set(values.filter(Boolean))];
}

function commandLabel(candidate) {
  const parts = [candidate.command, ...(candidate.prefixArgs || [])];
  return parts.join(" ");
}

function buildPythonCandidates(options, platform = process.platform) {
  const isWindows = platform === "win32";
  const raw = [];

  if (options.pythonExec) {
    raw.push({ command: options.pythonExec, prefixArgs: [] });
  }
  if (process.env.PYTHON) {
    raw.push({ command: process.env.PYTHON, prefixArgs: [] });
  }

  if (isWindows) {
    raw.push({ command: "python", prefixArgs: [] });
    raw.push({ command: "py", prefixArgs: ["-3"] });
    raw.push({ command: "py", prefixArgs: [] });
    raw.push({ command: "python3", prefixArgs: [] });
  } else {
    raw.push({ command: "python3", prefixArgs: [] });
    raw.push({ command: "python", prefixArgs: [] });
  }

  const seen = new Set();
  const candidates = [];
  for (const item of raw) {
    if (!item || !item.command) {
      continue;
    }
    const key = `${item.command}::${(item.prefixArgs || []).join(" ")}`;
    if (seen.has(key)) {
      continue;
    }
    seen.add(key);
    candidates.push(item);
  }
  return candidates;
}

function looksLikePythonLauncherIssue(text) {
  const lower = String(text || "").toLowerCase();
  return (
    lower.includes("python was not found") ||
    lower.includes("microsoft store") ||
    lower.includes("python nao foi encontrado") ||
    lower.includes("python n") && lower.includes("microsoft store")
  );
}

function parseInstallArgs(args) {
  const options = {
    repo: "helberfmelo/codex-workflows",
    ref: "main",
    method: "auto",
    dest: null,
    pythonExec: null,
    installerScript: null,
    coreOnly: false,
    force: false,
    dryRun: false
  };

  for (let i = 0; i < args.length; i += 1) {
    const token = args[i];
    if (token === "--repo") {
      options.repo = args[++i];
    } else if (token === "--ref") {
      options.ref = args[++i];
    } else if (token === "--method") {
      options.method = args[++i];
    } else if (token === "--dest") {
      options.dest = args[++i];
    } else if (token === "--python-exec") {
      options.pythonExec = args[++i];
    } else if (token === "--installer-script") {
      options.installerScript = args[++i];
    } else if (token === "--core-only") {
      options.coreOnly = true;
    } else if (token === "--force") {
      options.force = true;
    } else if (token === "--dry-run") {
      options.dryRun = true;
    } else if (token === "-h" || token === "--help") {
      printHelp();
      process.exit(0);
    } else {
      throw new Error(`Unknown argument: ${token}`);
    }
  }

  if (!["auto", "download", "git"].includes(options.method)) {
    throw new Error(`Invalid --method value: ${options.method}`);
  }

  return options;
}

function selectSkillPaths(skillPaths, destRoot, forceInstall) {
  if (forceInstall) {
    return { installPaths: skillPaths, skipped: [] };
  }
  const installPaths = [];
  const skipped = [];
  for (const skillPath of skillPaths) {
    const skillName = path.basename(skillPath);
    if (fs.existsSync(path.join(destRoot, skillName))) {
      skipped.push(skillName);
    } else {
      installPaths.push(skillPath);
    }
  }
  return { installPaths, skipped };
}

function buildInstallCommand(options, installPaths, installer, destRoot) {
  const cmdArgs = [
    installer,
    "--repo",
    options.repo,
    "--ref",
    options.ref,
    "--method",
    options.method,
    "--path",
    ...installPaths
  ];

  if (options.dest) {
    cmdArgs.push("--dest", destRoot);
  }

  return cmdArgs;
}

function runPythonCommand(candidate, args) {
  const spawnArgs = [...(candidate.prefixArgs || []), ...args];
  const proc = childProcess.spawnSync(candidate.command, spawnArgs, { encoding: "utf8" });
  const output = `${proc.stdout || ""}${proc.stderr || ""}`;
  if (proc.stdout) {
    process.stdout.write(proc.stdout);
  }
  if (proc.stderr) {
    process.stderr.write(proc.stderr);
  }
  if (proc.error && proc.error.code === "ENOENT") {
    return { code: null, output };
  }
  if (proc.error) {
    console.error(`Failed to execute ${commandLabel(candidate)}: ${proc.error.message}`);
    return { code: 1, output };
  }
  return { code: proc.status == null ? 1 : proc.status, output };
}

function selectAvailablePythonCandidates(options, platform = process.platform) {
  const candidates = buildPythonCandidates(options, platform);
  return candidates.filter((candidate) =>
    hasWorkingCommand(candidate.command, [...(candidate.prefixArgs || []), "--version"])
  );
}

function runInstall(options) {
  const home = codexHome();
  const installer = path.resolve(options.installerScript || installerScriptPath(home));
  const destRoot = path.resolve(options.dest || path.join(home, "skills"));
  const basePaths = options.coreOnly ? CORE_SKILL_PATHS : ALL_SKILL_PATHS;

  if (!fs.existsSync(installer)) {
    console.error(`Installer script not found: ${installer}`);
    console.error("Install/enable Codex skill-installer first.");
    return 1;
  }

  const { installPaths, skipped } = selectSkillPaths(basePaths, destRoot, options.force);
  if (skipped.length > 0) {
    console.log(`Skipping already installed skills: ${skipped.sort().join(", ")}`);
  }

  if (installPaths.length === 0) {
    console.log("All selected skills are already installed.");
    return 0;
  }

  const cmdArgs = buildInstallCommand(options, installPaths, installer, destRoot);
  const pythonCandidates = selectAvailablePythonCandidates(options);

  if (options.dryRun) {
    const previewCandidate = pythonCandidates[0] || { command: "python", prefixArgs: [] };
    console.log("Dry run command:");
    console.log([commandLabel(previewCandidate), ...cmdArgs].join(" "));
    return 0;
  }

  if (pythonCandidates.length === 0) {
    console.error("No working Python executable found. Install Python and retry.");
    return 1;
  }

  let launcherFallbackTriggered = false;
  for (const candidate of pythonCandidates) {
    const result = runPythonCommand(candidate, cmdArgs);
    if (result.code === null) {
      continue;
    }
    if (result.code === 0) {
      return 0;
    }
    if (looksLikePythonLauncherIssue(result.output)) {
      launcherFallbackTriggered = true;
      continue;
    }
    return result.code;
  }

  if (launcherFallbackTriggered) {
    console.error("Python launcher alias failed across candidates. Use --python-exec python as fallback.");
    return 1;
  }
  console.error("No working Python executable found. Install Python and retry.");
  return 1;
}

function hasWorkingCommand(command, args) {
  const proc = childProcess.spawnSync(command, args, {
    stdio: ["ignore", "pipe", "pipe"],
    encoding: "utf8"
  });
  if (proc.error && proc.error.code === "ENOENT") {
    return false;
  }
  return proc.status === 0;
}

function runDoctor() {
  const home = codexHome();
  const installer = installerScriptPath(home);
  const pythonCandidates = selectAvailablePythonCandidates({});
  const pythonOk = pythonCandidates[0] ? commandLabel(pythonCandidates[0]) : null;

  console.log("cw doctor");
  console.log(`- codex_home: ${home}`);
  console.log(`- installer_script: ${installer}`);
  console.log(`- installer_exists: ${fs.existsSync(installer)}`);
  console.log(`- python: ${pythonOk || "not found"}`);

  if (!fs.existsSync(installer)) {
    console.log("- fix: ensure Codex skill-installer is installed at ~/.codex");
    return 1;
  }
  if (!pythonOk) {
    console.log("- fix: install Python and ensure it is in PATH");
    return 1;
  }
  return 0;
}

function run() {
  const args = process.argv.slice(2);

  if (args.includes("-v") || args.includes("--version")) {
    console.log(pkg.version);
    return 0;
  }

  if (args[0] === "help" || args[0] === "/help" || args[0] === "-h" || args[0] === "--help") {
    printHelp();
    return 0;
  }

  if (args[0] === "examples" || args[0] === "/examples") {
    printExamples();
    return 0;
  }

  if (args[0] === "doctor") {
    return runDoctor();
  }

  if (args[0] && args[0].startsWith("/") && args[0] !== "/help" && args[0] !== "/examples") {
    console.log("Workflow slash commands are prompt intents for Codex chat, not terminal commands.");
    console.log(`Use in chat: "cw ${args[0]} <objective>"`);
    return 0;
  }

  try {
    const installArgs = args[0] === "install" ? args.slice(1) : args;
    const options = parseInstallArgs(installArgs);
    return runInstall(options);
  } catch (err) {
    console.error(String(err.message || err));
    console.error("Run `npx @codex-workflow/cw /help` for usage.");
    return 1;
  }
}

if (require.main === module) {
  process.exit(run());
}

module.exports = {
  buildPythonCandidates,
  looksLikePythonLauncherIssue,
  selectAvailablePythonCandidates
};
