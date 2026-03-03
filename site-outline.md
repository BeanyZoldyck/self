# Personal Dev Site Outline

## Design System

- Background: Black (#000000)
- Text: Purple (#A855F7 / #9333EA)
- Font: JetBrains Mono (nerdy, monospace)

## Project Structure

```
dev-site/
├── src/
│   ├── routes/
│   │   ├── +layout.svelte          # Root layout (nav + global styles)
│   │   ├── +page.svelte            # Homepage
│   │   ├── +page.css               # Global styles (black bg, purple text)
│   │   ├── about/
│   │   │   └── +page.svelte        # About page
│   │   ├── projects/
│   │   │   └── +page.svelte        # Projects list
│   │   └── contact/
│   │       └── +page.svelte        # Contact info
│   └── lib/
│       └── components/
│           ├── Header.svelte       # Simple nav header
│           └── Footer.svelte       # Simple footer
├── static/
└── package.json
```

## Pages Overview

### Homepage (`/`)

- Hero: "Hi, I'm [Name]"
- One-liner: "I build things for the web"
- Links: [About] [Projects] [Contact]

### About (`/about`)

- Brief bio
- Skills/tech stack
- Maybe a photo (optional)

### Projects (`/projects`)

- List of projects
- Each project: name, description, link

### Contact (`/contact`)

- Email
- GitHub link
- LinkedIn or other social
- Simple, minimal

## Typography & Style

```
Font: JetBrains Mono

Colors:
- Background: bg-black
- Primary text: text-purple-400
- Hover/links: text-purple-300 hover:text-purple-200
- Borders: border-purple-800
```

## Notes

- Extremely minimal
- No fancy animations
- Focus on content
- Dark theme only
- Monospaced everything for that hacker vibe
