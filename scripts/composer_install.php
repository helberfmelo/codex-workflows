<?php
declare(strict_types=1);

/**
 * Composer wrapper for codex-workflows skill installation.
 *
 * It delegates to the official Python installer from Codex:
 * ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py
 */

function fail(string $message): never
{
    fwrite(STDERR, "Error: {$message}\n");
    exit(1);
}

function codexHome(): string
{
    $fromEnv = getenv("CODEX_HOME");
    if (is_string($fromEnv) && $fromEnv !== "") {
        return $fromEnv;
    }

    if (stripos(PHP_OS_FAMILY, "Windows") === 0) {
        $profile = getenv("USERPROFILE");
        if (!is_string($profile) || $profile === "") {
            fail("USERPROFILE not available and CODEX_HOME not set.");
        }
        return $profile . DIRECTORY_SEPARATOR . ".codex";
    }

    $home = getenv("HOME");
    if (!is_string($home) || $home === "") {
        fail("HOME not available and CODEX_HOME not set.");
    }
    return $home . DIRECTORY_SEPARATOR . ".codex";
}

function parseArgs(array $argv): array
{
    $options = [
        "mode" => "all",
        "ref" => "main",
        "repo" => "helberfmelo/codex-workflows",
        "method" => "auto",
        "python" => "python",
        "dest" => null,
    ];

    foreach ($argv as $arg) {
        if (str_starts_with($arg, "--mode=")) {
            $options["mode"] = substr($arg, strlen("--mode="));
            continue;
        }
        if (str_starts_with($arg, "--ref=")) {
            $options["ref"] = substr($arg, strlen("--ref="));
            continue;
        }
        if (str_starts_with($arg, "--repo=")) {
            $options["repo"] = substr($arg, strlen("--repo="));
            continue;
        }
        if (str_starts_with($arg, "--method=")) {
            $options["method"] = substr($arg, strlen("--method="));
            continue;
        }
        if (str_starts_with($arg, "--python=")) {
            $options["python"] = substr($arg, strlen("--python="));
            continue;
        }
        if (str_starts_with($arg, "--dest=")) {
            $options["dest"] = substr($arg, strlen("--dest="));
            continue;
        }
    }

    if (!in_array($options["mode"], ["all", "core"], true)) {
        fail("Unsupported --mode. Use all or core.");
    }
    if (!in_array($options["method"], ["auto", "download", "git"], true)) {
        fail("Unsupported --method. Use auto, download or git.");
    }

    return $options;
}

function buildSkillPaths(string $mode): array
{
    $all = [
        "skills/codex-workflows",
        "skills/codex-backend-pack",
        "skills/codex-frontend-pack",
        "skills/codex-security-pack",
        "skills/codex-qa-pack",
        "skills/codex-node-validation-pack",
        "skills/codex-python-validation-pack",
        "skills/codex-rust-validation-pack",
    ];
    if ($mode === "core") {
        return ["skills/codex-workflows"];
    }
    return $all;
}

function runInstaller(array $options): int
{
    $installer = codexHome()
        . DIRECTORY_SEPARATOR . "skills"
        . DIRECTORY_SEPARATOR . ".system"
        . DIRECTORY_SEPARATOR . "skill-installer"
        . DIRECTORY_SEPARATOR . "scripts"
        . DIRECTORY_SEPARATOR . "install-skill-from-github.py";

    if (!file_exists($installer)) {
        fail("Codex installer script not found at {$installer}");
    }

    $paths = buildSkillPaths((string)$options["mode"]);
    $cmd = [
        (string)$options["python"],
        $installer,
        "--repo",
        (string)$options["repo"],
        "--ref",
        (string)$options["ref"],
        "--method",
        (string)$options["method"],
        "--path",
    ];
    foreach ($paths as $path) {
        $cmd[] = $path;
    }
    if (is_string($options["dest"]) && $options["dest"] !== "") {
        $cmd[] = "--dest";
        $cmd[] = $options["dest"];
    }

    $escaped = array_map("escapeshellarg", $cmd);
    $command = implode(" ", $escaped);
    passthru($command, $status);
    return (int)$status;
}

$options = parseArgs(array_slice($argv, 1));
exit(runInstaller($options));
