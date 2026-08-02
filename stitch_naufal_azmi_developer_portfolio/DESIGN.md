---
name: Lumina Tech Portfolio
colors:
  surface: '#0b1326'
  surface-dim: '#0b1326'
  surface-bright: '#31394d'
  surface-container-lowest: '#060e20'
  surface-container-low: '#131b2e'
  surface-container: '#171f33'
  surface-container-high: '#222a3d'
  surface-container-highest: '#2d3449'
  on-surface: '#dae2fd'
  on-surface-variant: '#bcc9cd'
  inverse-surface: '#dae2fd'
  inverse-on-surface: '#283044'
  outline: '#869397'
  outline-variant: '#3d494c'
  surface-tint: '#4cd7f6'
  primary: '#4cd7f6'
  on-primary: '#003640'
  primary-container: '#06b6d4'
  on-primary-container: '#00424f'
  inverse-primary: '#00687a'
  secondary: '#c0c1ff'
  on-secondary: '#1000a9'
  secondary-container: '#3131c0'
  on-secondary-container: '#b0b2ff'
  tertiary: '#ffb873'
  on-tertiary: '#4b2800'
  tertiary-container: '#e89337'
  on-tertiary-container: '#5b3200'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#acedff'
  primary-fixed-dim: '#4cd7f6'
  on-primary-fixed: '#001f26'
  on-primary-fixed-variant: '#004e5c'
  secondary-fixed: '#e1e0ff'
  secondary-fixed-dim: '#c0c1ff'
  on-secondary-fixed: '#07006c'
  on-secondary-fixed-variant: '#2f2ebe'
  tertiary-fixed: '#ffdcbf'
  tertiary-fixed-dim: '#ffb873'
  on-tertiary-fixed: '#2d1600'
  on-tertiary-fixed-variant: '#6a3b00'
  background: '#0b1326'
  on-background: '#dae2fd'
  surface-variant: '#2d3449'
  bg-slate-900: '#0f172a'
  text-slate-100: '#f8fafc'
  text-slate-400: '#94a3b8'
  border-slate-800: '#1e293b'
  surface-slate-800: '#1e293b'
typography:
  display:
    fontFamily: Geist
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  display-mobile:
    fontFamily: Geist
    fontSize: 36px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Geist
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  max-width: 1200px
---

## Brand & Style

This design system is built for high-end developer portfolios, emphasizing technical precision and creative clarity. The aesthetic follows a **Modern Minimalism** approach with a strong **developer-centric** tilt, utilizing a deep slate background to reduce eye strain while making content pop with high-contrast accents.

The emotional response should be one of "sophisticated competence"—it’s quiet, professional, and fast. Key visual markers include generous negative space, crisp typography, and subtle interactive states that provide immediate, low-friction feedback. The UI avoids unnecessary decorative elements, allowing the work and the code to remain the focal point.

## Colors

The palette is anchored in a deep **Slate-900** background to provide a premium "pro-tool" feel. The primary accent is a vibrant **Cyan**, used sparingly for call-to-actions and interactive highlights to maintain a technical, energetic vibe. 

**Secondary Indigo** is used for secondary actions or to categorize different project types. Neutral tones transition from Slate-800 for surface elevations to Slate-100 for primary text, ensuring high legibility and a soft, accessible contrast ratio that prevents the "pure black" vibration common in dark modes.

## Typography

The typography system uses a tri-font strategy to differentiate intent. **Geist** provides a clean, technical edge for headings with its tight apertures and geometric construction. **Inter** handles body copy for maximum readability across various screen types. **JetBrains Mono** is reserved for labels, tags, and snippets to lean into the developer aesthetic.

Headlines should use tight letter-spacing to appear more impactful, while body text maintains a standard tracking to ensure long-form readability. For mobile, headline sizes scale down significantly to prevent awkward word breaks in narrow containers.

## Layout & Spacing

This design system uses a **12-column fluid grid** for desktop and a **single-column stack** for mobile. The layout is centered with a max-width of 1200px to prevent lines of text from becoming too long on ultra-wide monitors.

The spacing rhythm follows a base-4 system. Sections should be separated by large vertical gaps (80px to 120px) to allow the "minimalist" breathe room. Use 24px gutters for grid-based content like project cards. On mobile, margins reduce to 16px to maximize the limited screen real estate for content.

## Elevation & Depth

Depth is conveyed through **Tonal Layering** rather than traditional heavy shadows.
- **Level 0 (Background):** Slate-900.
- **Level 1 (Cards/Surfaces):** Slate-800 with a 1px solid border of Slate-700.
- **Level 2 (Hover States):** When a card is hovered, the border color transitions to Cyan, and a very soft, low-opacity (10%) Cyan outer glow is applied to simulate a technical "lit" effect.

Avoid blurs or heavy drop shadows. Keep edges crisp to maintain the professional, engineered look.

## Shapes

The shape language is **Soft (0.25rem)**. This slight rounding takes the edge off the brutalist origins of tech-style designs, making the UI feel modern and approachable without becoming "bubbly."

- **Buttons:** 4px radius for a standard sharp-technical look.
- **Cards:** 8px (rounded-lg) to provide enough curve to feel intentional.
- **Inputs:** 4px radius to match buttons.
- **Icons:** Use Lucide React icons with a 2px stroke width for consistency.

## Components

### Buttons
Primary buttons use a solid Cyan background with Slate-900 text. Secondary buttons use a Slate-800 background with a 1px Slate-700 border. All buttons should have a `transition: all 0.2s ease-in-out` for hover states.

### Cards
Project cards are the core component. Use a Slate-800 background with a 1px border. The title uses `headline-md`, and tags use `label-sm` with a secondary Indigo background at 10% opacity.

### Input Fields
Inputs should be Slate-900 with a 1px Slate-700 border. On focus, the border changes to Cyan. Placeholders use Slate-400.

### Chips/Tags
Tags use JetBrains Mono for a "code-tag" feel. They should be low-contrast (Slate-800 background) unless they indicate a specific high-priority skill, in which case use a subtle Cyan border.

### Transitions
Implement smooth, subtle transitions for all interactive elements. Page transitions should use a simple opacity fade (200ms) or a slight upward slide (4px) to emphasize the lightweight nature of the portfolio.