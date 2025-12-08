import random
import os
import json
from datetime import datetime, timedelta
from typing import Dict, Tuple

_CACHE = {}

def load_json_file(key, file_name):
    if file_name not in _CACHE:
        file_path = os.path.join(os.path.dirname(__file__), "data", file_name)
        with open(file_path, "r", encoding='utf-8') as file:
            _CACHE[file_name] = json.load(file)
    return _CACHE[file_name].get(key, []) if isinstance(_CACHE[file_name].get(key), list) else None

class FilenameGenerator:
    def __init__(self, seed: int = None):
        self.rng = random.Random(seed)
        self.start_date = datetime(1990, 1, 1)
        self.end_date = datetime.now()

    @classmethod
    def INPUT_TYPES(cls) -> Dict:
        return {
            "optional": {
                "prompt": ("STRING", {"multiline": True, "default": "", "forceInput": True}),
                "extra_prompt": ("STRING", {"multiline": True, "default": ""}),
                "format": (load_json_file("formats","filenames.json"), {"default": "📷 Nikon"}),
                "path": (["Disabled", "Simple", "Complex"], {"default": "Disabled"}),
                "seed": ("INT", {"default": random.randint(0, 30000), "min": 0, "max": 30000, "step": 1}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("Filename Only", "Prompt with Filename")
    FUNCTION = "generate_random"
    CATEGORY = "Prompt"

    def random_date(self) -> Tuple[int, datetime]:
        random_days = self.rng.randint(0, (self.end_date - self.start_date).days)
        return random_days, self.start_date + timedelta(days=random_days)

    def random_time(self) -> str:
        return f"{self.rng.randint(0, 23):02d}{self.rng.randint(0, 59):02d}{self.rng.randint(0, 59):02d}"

    def generate_path(self, extra_prompt: str, path: str) -> str:
        drives = load_json_file("drives","filenames.json")
        common_folders = (load_json_file("common_folders","filenames.json") if path == "Complex" else [])
        extras = (load_json_file("extras","filenames.json") if path == "Complex" else [])
        extra_prompt = extra_prompt.replace(' ', '_')
        
        def normalize_path(path: str) -> str:
            is_windows = ':' in path or '\\' in path
            normalized = path.replace('/' if is_windows else '\\', '\\' if is_windows else '/')
            separator = '\\' if is_windows else '/'
            while separator * 2 in normalized:
                normalized = normalized.replace(separator * 2, separator)
            return normalized

        all_paths = [normalize_path(f"{d}\\{f}") for d in drives for f in common_folders] + \
                    [normalize_path(f"{d}") for d in drives] + \
                    [normalize_path(p) for p in extras]
        base_path = self.rng.choice(all_paths).rstrip('/\\')
        components = [base_path] + ([extra_prompt] if extra_prompt else [])
        separator = '\\' if (':' in base_path or '\\' in base_path) else '/'
        return normalize_path(f"{separator.join(components)}{separator}")

    def generate_filename(self, choice: str) -> tuple[str, str]:
        number, number2 = f"{self.rng.randint(0, 9999):04d}", f"{self.rng.randint(0, 9999)}"
        _, random_dt = self.random_date()
        random_date_str, random_time_str = random_dt.strftime("%Y%m%d"), self.random_time()
        num_date_time = f"{self.rng.randint(10000, 99999)}_{random_date_str}_{random_time_str}"
        delim = self.rng.choice(['','-','_'])
        image_type = self.rng.choice(load_json_file("image_type","filenames.json"))
        suffix = self.rng.choice([f"{random_date_str}_{number}", f"{num_date_time}"])
        thermal_image_type = self.rng.choice(load_json_file("thermal_image_type","filenames.json"))
        misc_image_type = self.rng.choice(load_json_file("misc_image_type","filenames.json"))
        underwater_image_type = self.rng.choice(load_json_file("underwater_image_type","filenames.json"))
        astro_image_type = self.rng.choice(load_json_file("astro_image_type","filenames.json"))
        macro_image_type = self.rng.choice(load_json_file("macro_image_type","filenames.json"))
        sat_image_type = self.rng.choice(load_json_file("sat_image_type","filenames.json"))
        filenames = {
            "📷 Nikon": f"DSC_{number}.JPG", "📷 Canon": f"IMG_{number}.CR3", "📷 Fujifilm": f"DSCF_{number}.JPG",
            "📷 Sony": f"DSC0{number}.ARW", "📷 Panasonic": f"P{number}.JPG", "📷 Casio": f"CIMG{number}.JPG",
            "📷 Generic": f"IMG_{number}.JPG", "📱 Android": f"Photo_{number}.JPG", "📱 iPhone HEIC": f"IMG_{number}.HEIC",
            "📱 iPhone JPEG": f"IMG_{number}.JPG", "📱 Pixel": f"IMG_{random_date_str}_{number}.JPG",
            "📱 Samsung": f"{random_date_str}_{number}.JPG", "🖥️ Windows Screenshot": f"Screenshot ({number}).PNG",
            "🍏 macOS Screenshot": f"Screen Shot {random_date_str[:4]}-{random_date_str[4:6]}-{random_date_str[6:]} at {random_time_str[:2]}.{random_time_str[2:4]}.{random_time_str[4:]}.PNG",
            "🎥 VLC": f"vlcsnap-{random_date_str[:4]}-{random_date_str[4:6]}-{random_date_str[6:]}-{random_time_str}.PNG",
            "💬 WhatsApp": f"IMG-{random_date_str}-WA{number}.JPG", "📸 Instagram": f"insta{number}.JPG",
            "📘 Facebook": f"FB_IMG_{number}.JPG", "👻 Snapchat": f"snap{number}.JPG", "🎵 TikTok": f"VID_{number}.MP4",
            "🚁 DJI": f"DJI_{number}.JPG", "🚁 Mavic": f"MAVIC_{number}.JPG", "🎥 GoPro": f"GOPR{number}.MP4",
            "🔄 360": f"360Degree{delim+image_type}_{suffix}.MP4",
            "🚗 Dashcam": f"DASH{delim}CAM_{suffix}.MP4",
            "🛩 Aerial": f"Aerial{delim+image_type}_{suffix}.JPG",
            "🤿 Underwater": f"Underwater{delim+image_type}_{suffix}.JPG",
            "📹 Security Camera": f"SECURITY{delim}CAM_{suffix}.MP4",
            "📹 CCTV": f"CCTV_{suffix}.MP4",
            "🖼️ 3D Scan": f"3D{delim}Scan_{random_date_str}_Model{number2}_{number}.ply",
            "🌡️ Thermal Imaging": f"{thermal_image_type}_{suffix}.JPG",
            "🌌 Astro": f"{astro_image_type+delim+image_type}_{suffix}.JPG",
            "🛰 Satellite": f"{sat_image_type+delim+image_type}_{suffix}.JPG",
            "🔬 Macro": f"{macro_image_type+delim+image_type}_{suffix}.JPG",
            "❓ Misc": f"{misc_image_type+delim+image_type}_{suffix}.JPG",
        }
        if choice == "🎲 Random": 
            choice = self.rng.choice(list(filenames.keys()))
        return filenames.get(choice), ''.join(char for char in choice if char.isalnum()).strip()

    def generate_random(self, format: str, extra_prompt: str, path: str, prompt: str = "", seed: int = None) -> Tuple[str, str]:
        if seed is not None:
            self.rng.seed(seed)
        filename, choice = self.generate_filename(format)
        extra_prompt = f"{prompt} {extra_prompt}" if prompt else extra_prompt
        full_path = (self.generate_path(extra_prompt, path) + filename) if path != "Disabled" else f"{extra_prompt} {filename}"
        print(full_path, filename)
        return filename, full_path