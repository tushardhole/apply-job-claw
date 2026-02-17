#!/bin/bash
# Git setup script for apply-job-claw

set -e

cd "$(dirname "$0")"

echo "Setting up git repository..."

# Remove existing .git if it exists and has issues
if [ -d .git ]; then
    echo "Removing existing .git directory..."
    rm -rf .git
fi

# Initialize git
git init

# Configure git user
git config user.name "Tushar Dhole"
git config user.email "tushardhole@hotmail.com"

# Add all files
git add .

# Create initial commit
git commit -m "feat(setup): initial project structure and Phase 1 foundation

- Set up project structure with clean architecture
- Define all core interfaces (browser, telegram, LLM, storage, etc.)
- Create domain models (UserProfile, JobApplication, FormField, etc.)
- Configure CI/CD with GitHub Actions
- Set up testing infrastructure (pytest, pytest-bdd)
- Add pre-commit hooks configuration
- Create logging utility module
- Write initial unit tests"

# Rename branch to master
git branch -M master

# Add remote (remove if exists first)
git remote remove origin 2>/dev/null || true
git remote add origin git@github.com:tushardhole/apply-job-claw.git

echo ""
echo "Git setup complete!"
echo ""
echo "To push to GitHub, run:"
echo "  git push -u origin master"
echo ""
