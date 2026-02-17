#!/bin/bash
# Script to copy project to Documents/Projects

set -e

SOURCE="/Users/tushardhole/job-application-assistant"
TARGET="/Users/tushardhole/Documents/Projects/apply-job-claw"

echo "Copying project from $SOURCE to $TARGET..."

# Create target directory
mkdir -p "$TARGET"

# Copy all files excluding .git and __pycache__
rsync -av \
  --exclude='.git' \
  --exclude='__pycache__' \
  --exclude='*.pyc' \
  --exclude='.DS_Store' \
  "$SOURCE/" "$TARGET/"

echo ""
echo "Copy complete!"
echo ""
echo "Next steps:"
echo "  cd $TARGET"
echo "  git init"
echo "  git config user.name 'Tushar Dhole'"
echo "  git config user.email 'tushardhole@hotmail.com'"
echo "  git add ."
echo "  git commit -m 'feat(setup): initial project structure and Phase 1 foundation'"
echo "  git branch -M master"
echo "  git remote add origin git@github.com:tushardhole/apply-job-claw.git"
echo "  git push -u origin master"
echo ""
