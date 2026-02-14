#!/usr/bin/env node
"use strict";

const assert = require("assert");
const path = require("path");

const cw = require(path.join(__dirname, "..", "bin", "cw.js"));

function candidateLabels(candidates) {
  return candidates.map((item) => [item.command, ...(item.prefixArgs || [])].join(" "));
}

function testWindowsCandidatePriority() {
  const candidates = cw.buildPythonCandidates({}, "win32");
  const labels = candidateLabels(candidates);
  assert.deepStrictEqual(labels.slice(0, 4), ["python", "py -3", "py", "python3"]);
}

function testLinuxCandidatePriority() {
  const candidates = cw.buildPythonCandidates({}, "linux");
  const labels = candidateLabels(candidates);
  assert.deepStrictEqual(labels.slice(0, 2), ["python3", "python"]);
}

function testPythonLauncherIssueDetection() {
  assert.strictEqual(
    cw.looksLikePythonLauncherIssue(
      "Python was not found; run without arguments to install from the Microsoft Store."
    ),
    true
  );
  assert.strictEqual(
    cw.looksLikePythonLauncherIssue(
      "Python nao foi encontrado; executar sem argumentos para instalar da Microsoft Store."
    ),
    true
  );
  assert.strictEqual(cw.looksLikePythonLauncherIssue("fatal: installer script not found"), false);
}

function run() {
  testWindowsCandidatePriority();
  testLinuxCandidatePriority();
  testPythonLauncherIssueDetection();
  console.log("test_cw_cli_node.js: ok");
}

run();
