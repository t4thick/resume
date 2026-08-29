# Richard Effah Yeboah - Resume (Jake's LaTeX Template)

LaTeX resume using [Jake's Resume Template](https://github.com/jakegut/resume) format.

## Compile to PDF

**Option 1: Overleaf (easiest)**
1. Go to [Overleaf](https://www.overleaf.com)
2. Create New Project → Upload Project
3. Upload `resume.tex` (and this folder)
4. Click Recompile

**Option 2: Local LaTeX**
```bash
pdflatex resume.tex
pdflatex resume.tex   # Run twice for references
```

**Option 3: VS Code / Cursor**
- Install "LaTeX Workshop" extension
- Open `resume.tex` and build (Ctrl+Alt+B or Cmd+Option+B)

## Live Preview

With **LaTeX Workshop** in Cursor/VS Code:
1. Open `resume.tex`
2. The extension auto-compiles on save
3. Click the preview icon or use "View LaTeX PDF" to see the PDF in a side panel
4. Edits to the .tex file will refresh the PDF preview

## Files

- `resume.tex` - LaTeX source (edit this with your info)
