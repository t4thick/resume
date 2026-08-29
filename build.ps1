# Build resume.tex and exit with error if build fails.
# Usage: .\build.ps1
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
Write-Host "Building resume.tex ..."
& pdflatex -interaction=nonstopmode -halt-on-error resume.tex
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& pdflatex -interaction=nonstopmode -halt-on-error resume.tex
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Write-Host "Build OK. Output: resume.pdf"
