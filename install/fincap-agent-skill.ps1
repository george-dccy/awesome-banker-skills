param(
    [ValidateSet("claude", "codex", "agents", "all")]
    [string]$Target = "all",
    [string]$RepoPath = "",
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PythonInstaller = Join-Path $ScriptDir "fincap_agent_skill.py"

$Args = @($PythonInstaller, "--target", $Target)
if ($RepoPath) {
    $Args += @("--repo-path", $RepoPath)
}
if ($DryRun) {
    $Args += "--dry-run"
}

python @Args
