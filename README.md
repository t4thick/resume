# Richard Effah Yeboah — Software Engineering Resume

ATS-friendly, one-page resume focused on verified full-stack engineering work. The current version removes unsupported fellowship and project claims and links directly to deployed applications and public source code.

## Compile to PDF

**Option 1: Overleaf**
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

## Current files

- `resume.tex` — source of truth
- `resume.pdf` — generated application copy
- `RICHARD EFFAH YEBOAH RESUME.pdf` — same current resume with a human-readable filename

## Accuracy rule

Add a credential, employer, project, metric, or technology only when it can be supported by a repository, deployment, official record, or direct confirmation. Keep dates and titles consistent across the resume, GitHub, LinkedIn, and applications.
