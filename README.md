# ComfyUI Prompt & Filename Tools

A collection of nodes designed to enhance your workflow with realistic filename generation, randomized wildcards, and keywords.

## Prompt Wildcards ✨

A text generation node that parses specific tags and replaces them with random values from curated lists. It is useful for building dynamic, varied prompts.

### Usage
Simply include tags in your prompt text. 
*   **Text Replacement**: `<tag>` is replaced by a random line from the corresponding CSV.
*   **Date Logic**: 
    *   Ranges: `<1980-1990>` picks a random year between the two.
    *   Patterns: `<19xx>`, `<2xxx>`, `<xxxx>` generates random years matching the pattern.

### Supported Tags
| Category | Tags |
| :--- | :--- |
| **Character** | `<nlt>` (Nationality), `<species>`, `<out>` (Outfit), `<outn>` (NSFW Outfit), `<makeup>`, `<exp>` (Expression), `<pose>` |
| **World** | `<loc>` (Location), `<locw>` (Weird Location), `<time>`, `<light>` (Lighting) |
| **Style/Art** | `<style>` (Assorted styles), `<medi>` (Medium), `<color>` (Colors), `<color2>` (Alt-colors) |
| **Pop Culture** | `<celeb>`, `<film>`, `<game>`, `<media>` |
| **Misc** | `<wordk>` (Photo keyword), `<word>` (Random word), `<wordp>` (Power word), `<wordn>` (NSFW word), `<pass>` (random password) |

---

## Filename Generator 📁

Generates realistic filenames and folder paths for 30+ different devices and platforms. These strings can be used as prompts to induce specific aesthetic effects (e.g., adding `DSC_0123.JPG` to a prompt).

### Parameters
1.  **Prompt**: Text to incorporate into the file path (spaces converted to underscores).
2.  **Format**:
    *   📷 **Cameras**: Nikon, Canon, Sony, Fujifilm, etc.
    *   📱 **Mobile**: iPhone (HEIC/JPEG), Android, Pixel, Samsung.
    *   🎥 **Video/Social**: TikTok, Instagram, Snapchat, GoPro, CCTV, Dashcam.
    *   🔬 **Specialty**: Thermal, Macro, Underwater, Astro, 3D Scan.
3.  **Path**: 
    *   `Disabled`: Filename only.
    *   `Simple`: Basic folder structure.
    *   `Complex`: Realistic, deep system paths (e.g., Windows/User directories).

### Examples
*   **Input**: `Format: 📷 Nikon`
    *   **Output**: `DSC_0123.JPG`
*   **Input**: `Prompt: "Party", Format: 📸 Instagram, Path: Complex`
    *   **Output**: `D:\Users\Pictures\Party\insta4567.jpg`
*   **Input**: `Prompt: "France", Format: 🌡️ Thermal`
    *   **Output**: `InfraredImage_20240117.jpg`

