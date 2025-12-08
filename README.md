Two ComfyUI nodes designed to enhance your workflow with realistic filename generation and prompt generation.

## Filename Generator 📁

- Generates somewhat realistic filenames for 30+ different devices and platforms
- Creates authentic file paths in both simple and complex formats
- Supports multiple image and video formats (JPG, CR3, ARW, HEIC, MP4, etc.)
- Customizable through prompt text and random seed
- Includes specialized formats for scientific and professional imaging

Filenames as prompts are not a magic bullet, but they can produce sometimes produce interesting effects with certain models (add `DSC_0123.JPG` to any prompt and try yourself).

### Input Parameters

1. **Prompt**: (Optional) Text that will be incorporated into the file path
   - Spaces will be converted to underscores
   - Used to create topic-specific folders

2. **Extra Prompt**: (Optional) Additional text to be used in filename or path generation
   - Can be combined with the main prompt, useful for adding more context or metadata

3. **Format**: Choose from these categories:
   - 🎲 Random (randomly selects a format)
   - 📷 Camera Brands: Nikon, Canon, Fujifilm, Sony, Panasonic, Casio, Generic
   - 📱 Mobile Devices: Android, iPhone (HEIC/JPEG), Pixel, Samsung
   - 🖥️ Screenshots: Windows, macOS
   - 🎥 Video/Social: VLC, WhatsApp, Instagram, Facebook, Snapchat, TikTok
   - 🚁 Drones: DJI, Mavic
   - 📹 Action/Security: GoPro, Dashcam, Security Camera, CCTV
   - 🤿 Specialty: Underwater, Aerial, 360-Degree
   - 🔬 Scientific: Macro, Thermal Imaging
   - 🌌 Advanced Imaging: Astro Photography, Satellite Imagery
   - 🖼️ Special: 3D Scan
   - ❓ Misc: Various other 'formats' 

4. **Path**: Choose between:
   - Disabled: No path
   - Simple: Basic directory structures
   - Complex: More detailed folder hierarchies including common user directories

5. **Seed**: (Optional)

#### Outputs

1. **Filename Only**: Just the generated filename (e.g., `IMG_0123.CR3`)
2. **Filename With Path**: Complete file path (e.g., `C:\Users\Photos\IMG_0123.CR3`)

#### Examples
```
Prompt: Big fat Steve Mt Everest trip
Format: 📷 Nikon
Path: Simple
```
Possible output:
- Filename Only: `DSC_0123.JPG`
- Filename With Path: `C:\Big_fat_Steve_Mt_Everest_trip\DSC_0123.JPG`

```
Prompt: Crazy New Years Eve drunk party 1999
Format: 📸 Instagram
Path: Complex
```
Possible output:
- Filename Only: `insta4567.jpg`
- Filename With Path: `D:\Users\Pictures\Crazy_New_Years_Eve_drunk_party_1999\insta4567.jpg`

```
Prompt: Beautiful France Provence countryside
Format: 🌡️ Thermal Imaging
Path: Complex
```
Possible output:
- Filename Only: `InfraredImage_45678_20240117_143022.jpg`
- Filename With Path: `E:\Projects\Beautiful_France_Provence_countryside\InfraredImage_45678_20240117_143022.jpg`

---
