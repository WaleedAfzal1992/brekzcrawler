# To address the issue of examples not displaying correctly, we will adjust the formatting and ensure proper line breaks and spacing.
import os
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Git Commands Explained with Examples', 0, 1, 'C')
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_command(self, title, body):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(body)

pdf = PDF()
pdf.set_left_margin(10)
pdf.set_right_margin(10)
pdf.add_page()

commands = [
    {
        "title": "1. git init",
        "body": "Initializes a new Git repository.\n\nExample:\n    git init my-repo"
    },
    {
        "title": "2. git clone",
        "body": "Clones an existing repository into a new directory.\n\nExample:\n    git clone https://github.com/user/repo.git"
    },
    {
        "title": "3. git status",
        "body": "Shows the working directory status.\n\nExample:\n    git status"
    },
    {
        "title": "4. git add",
        "body": "Adds files to the staging area.\n\nExample:\n    git add file.txt"
    },
    {
        "title": "5. git commit",
        "body": "Records changes to the repository.\n\nExample:\n    git commit -m 'Initial commit'"
    },
    {
        "title": "6. git log",
        "body": "Shows the commit history.\n\nExample:\n    git log"
    },
    {
        "title": "7. git branch",
        "body": "Lists branches, creates a new branch, or deletes a branch.\n\nExamples:\n    git branch\n    git branch new-feature\n    git branch -d old-feature"
    },
    {
        "title": "8. git checkout",
        "body": "Switches branches or restores working directory files.\n\nExamples:\n    git checkout new-feature\n    git checkout -- file.txt"
    },
    {
        "title": "9. git merge",
        "body": "Merges branches.\n\nExample:\n    git merge new-feature"
    },
    {
        "title": "10. git pull",
        "body": "Fetches and integrates changes from a remote repository.\n\nExample:\n    git pull origin main"
    },
    {
        "title": "11. git push",
        "body": "Updates remote refs along with associated objects.\n\nExample:\n    git push origin main"
    },
    {
        "title": "12. git remote",
        "body": "Manages set of tracked repositories.\n\nExamples:\n    git remote -v\n    git remote add origin https://github.com/user/repo.git\n    git remote remove origin"
    },
    {
        "title": "13. git fetch",
        "body": "Downloads objects and refs from another repository.\n\nExample:\n    git fetch origin"
    },
    {
        "title": "14. git reset",
        "body": "Resets current HEAD to the specified state.\n\nExamples:\n    git reset --soft HEAD~1\n    git reset --mixed HEAD~1\n    git reset --hard HEAD~1"
    },
    {
        "title": "15. git revert",
        "body": "Reverts an existing commit by creating a new commit.\n\nExample:\n    git revert HEAD"
    },
    {
        "title": "16. git diff",
        "body": "Shows changes between commits, commit and working tree, etc.\n\nExample:\n    git diff"
    },
    {
        "title": "17. git stash",
        "body": "Stashes changes in a dirty working directory.\n\nExamples:\n    git stash\n    git stash apply"
    },
    {
        "title": "18. git tag",
        "body": "Creates, lists, deletes or verifies a tag object signed with GPG.\n\nExamples:\n    git tag v1.0\n    git tag -d v1.0"
    },
    {
        "title": "19. git config",
        "body": "Gets and sets repository or global options.\n\nExamples:\n    git config --global user.name 'Your Name'\n    git config --global user.email 'your.email@example.com'"
    },
    {
        "title": "20. git rm",
        "body": "Removes files from the working tree and from the index.\n\nExample:\n    git rm file.txt"
    }
]

for command in commands:
    pdf.add_command(command['title'], command['body'])

output_path = "E:\git_repository\pdfGit_Commands_Explained_v2.pdf"
pdf.output(output_path)

output_path
