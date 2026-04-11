@echo off
echo === GIT NUKE PUSH STARTING ===

:: move out of .dev into project root
cd ..

:: Set your repo URL
set REPO_URL=https://github.com/Clenner/nexora.git

:: Remove old git history (if exists)
if exist .git (
    echo Removing old .git folder...
    rmdir /s /q .git
)

:: Init new repo
echo Initializing new repo...
git init

:: Set branch to main
git branch -M main

:: Add remote
echo Adding remote...
git remote add origin %REPO_URL%

:: Add all files
echo Adding files...
git add .

:: Commit
echo Committing...
git commit -m "full overwrite (nuke push)"

:: FORCE PUSH
echo Pushing (this will overwrite EVERYTHING)...
git push -u origin main --force

echo === DONE ===
pause