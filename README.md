# Claire By The Algorithm Website

Multi-page website for Claire By The Algorithm, a digital labor platform for healthcare. The site features an interactive conversational demo as the hub, with deep-dive SEO content pages as spokes.

## Repository Structure

```
claire-website/
├── public/
│   ├── index.html                          # Interactive hub (conversational demo)
│   └── healthcare/
│       ├── mcp-security.html               # MCP & data security deep dive
│       ├── phone-tree-alternative.html     # Reasoning vs scripts
│       ├── insurance-verification.html     # Automated insurance verification
│       ├── ehr-integration.html            # FHIR/Epic/Cerner integration
│       ├── hipaa-compliance.html           # HIPAA compliance & audit trails
│       └── cost-analysis.html              # ROI calculator & cost comparison
├── vercel.json                             # Vercel deployment configuration
├── package.json                            # NPM scripts and metadata
└── README.md                               # This file
```

## Features

### Interactive Hub (index.html)
- Conversational demo with typing effects
- Dark to light theme transition
- Industry selection (Healthcare focused)
- Collapsible chat sidebar
- Main content reveal with navigation
- Fully responsive design

### SEO Content Pages
Each spoke page includes:
- 1,800-2,200 words of deep technical content
- Schema.org Article markup
- Semantic HTML5 structure
- Internal linking structure
- Mobile-responsive layout
- Table of contents sidebar
- Related topics navigation

## Technical Stack

- **Frontend:** Vanilla JavaScript (no frameworks)
- **Styling:** Pure CSS with CSS custom properties
- **Typography:** System fonts (-apple-system, SF Pro Display)
- **Deployment:** Vercel (static hosting)
- **Performance Target:** Lighthouse score 95+ on all metrics

## Local Development

### Prerequisites
- Node.js 18+ (for http-server)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd Claire
```

2. Run local development server:
```bash
npm run dev
```

3. Open your browser:
```
http://localhost:3000
```

The site will be served from the `public/` directory.

### Development Commands

- `npm run dev` - Start local development server on port 3000
- `npm run build` - No build step needed (static site)
- `npm start` - Start production-like server

## Deployment

### Vercel Deployment

The site is configured for automatic deployment to Vercel:

1. Connect your GitHub repository to Vercel
2. Vercel will automatically detect `vercel.json` configuration
3. Deploy from the `claude/build-claire-website-SQvrj` branch
4. Site will be live at your Vercel domain

### Manual Deployment

To deploy manually:

```bash
vercel --prod
```

### Environment Configuration

No environment variables needed - this is a static site.

## Design System

### Colors

**Healthcare Mode (Light - Default for content pages):**
- Primary Background: `#f8fafc`
- Secondary Background: `#ffffff`
- Primary Text: `#0f172a`
- Secondary Text: `#64748b`
- Accent: `#2563eb`
- Border: `#e2e8f0`

**Dark Mode (Interactive hub initial state):**
- Primary Background: `#0a0a0a`
- Secondary Background: `#1a1a1a`
- Primary Text: `#ffffff`
- Secondary Text: `#999999`
- Accent: `#ffffff`
- Border: `#333333`

### Typography

- **Body:** 1.0625rem / 1.8 line-height
- **H1:** 2.5rem, font-weight 600
- **H2:** 2rem, font-weight 600
- **H3:** 1.5rem, font-weight 600

### Responsive Breakpoints

- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: > 1024px

## SEO Optimization

### Content Strategy

Each spoke page targets specific long-tail keywords:
- `mcp-security.html` → "is my data being used to train chatgpt"
- `phone-tree-alternative.html` → "how to make ai voice not sound like a robot"
- `insurance-verification.html` → "can ai handle insurance verification automatically"
- `ehr-integration.html` → "best virtual assistant for epic cerner integration"
- `hipaa-compliance.html` → "hipaa compliant ai chatbot"
- `cost-analysis.html` → "medical receptionist cost per hour vs ai"

### Meta Tags

All pages include:
- Title tags (< 60 characters)
- Meta descriptions (155 characters)
- Open Graph tags
- Canonical URLs
- Schema.org Article markup

### Internal Linking

Each spoke page links to 3-5 other spoke pages, creating a web of interconnected content that improves:
- SEO authority distribution
- User navigation
- Content discovery

## Performance Optimization

### Targets
- First Contentful Paint: < 1.5s
- Largest Contentful Paint: < 2.5s
- Time to Interactive: < 3.5s
- Cumulative Layout Shift: < 0.1
- Total Blocking Time: < 200ms

### Optimizations Applied
- Inline critical CSS
- Vanilla JS (no framework overhead)
- System fonts (zero font download time)
- Minimal external dependencies
- Efficient CSS selectors
- No JavaScript frameworks

## Browser Support

- Chrome (last 2 versions)
- Firefox (last 2 versions)
- Safari (last 2 versions)
- Edge (last 2 versions)

## Accessibility

- WCAG 2.1 AA compliant
- Semantic HTML5 elements
- ARIA labels where needed
- Keyboard navigation support
- Sufficient color contrast ratios
- Responsive text sizing

## Content Guidelines

### Brand Voice
- 70% Professional contractor/technical documentation
- 30% Claire speaking directly ("I handle...", "I reason through...")
- Position as "teammate" not "tool"
- Avoid AI buzzwords
- Focus on labor outcomes

### Writing Style
- Answer real questions healthcare decision-makers search for
- Include technical depth for CTO/IT directors
- Provide business context for CMO/COO
- Use concrete examples and data
- Link to authoritative sources (.gov, .edu)

## File Structure Details

### index.html
- Hero section with grid pattern overlay
- Conversational typing animation
- User name input collection
- Industry selection (Healthcare + Financial Services disabled)
- Theme switcher (dark → healthcare light)
- Chat panel collapse to sidebar
- Main content reveal with sections

### Spoke Pages Template
All healthcare spoke pages follow:
```
- Navigation (fixed)
- Breadcrumb
- H1 (primary question)
- Introduction (200 words)
- Problem section (400 words)
- Technical deep dive (800 words)
- Claire's solution (400 words)
- Implementation (200 words)
- CTA box
- Sidebar (TOC + Related topics)
```

## Maintenance

### Adding New Content Pages

1. Create new HTML file in `public/healthcare/`
2. Follow the spoke page template structure
3. Add internal links from related pages
4. Update navigation if needed
5. Test responsive layout
6. Validate HTML5 and accessibility

### Updating Existing Content

1. Read the file first to understand current structure
2. Maintain existing CSS classes and layout
3. Preserve internal linking structure
4. Test on mobile and desktop breakpoints
5. Re-validate SEO meta tags

## License

UNLICENSED - Private repository for Claire By The Algorithm

## Contact

For questions or issues, contact the development team.

---

Built with vanilla HTML, CSS, and JavaScript. No frameworks, maximum performance.
