import random
import string
import os
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import subprocess
import sys
import random
import json
import os
import re

class PromptWildcards:
    def __init__(self, seed: int = None):
        self.rng = random.Random(seed)
        
    @classmethod
    def INPUT_TYPES(cls) -> Dict:
        return {
            "optional": {
                "Prompt": ("STRING", {"multiline": True, "default": "Nationality: <nlt>\nSpecies: <species>\nOutfit: <out>\nOutfit (nsfw): <outn>\nMake-up: <makeup>\nExression: <exp>\nPose: <pose>\nLocation (mundane): <loc>\nLocation (weird): <locw>\nCelebrity: <celeb>\nMedia: <media>\nFilm: <film>\nGame: <game>\nWord: <word>\nPower-word: <wordp>\nPower-word (nsfw): <wordn>\nPassword: <pass>\nColor: <color>\nColor keyword: <color2>\nPhoto keyword: <wordk>\nMedium: <medi>\nTime of day: <time>\nLighting: <light>\nStyles: <style>\nYears: <69-79>, <19xx>, <2xxx>, <xxxx>"}),
                "seed": ("INT", {"default": random.randint(0, 30000), "min": 0, "max": 30000, "step": 1}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Prompt",)
    FUNCTION = "generate_pm"
    CATEGORY = "Prompt"
    
    def random_line_from_file(self, file_path):
        with open(file_path, encoding='utf-8') as f:
            line_count = sum(1 for _ in f)
            f.seek(0)
            random_line_index = self.rng.randint(0, line_count - 1)
            for current_index, line in enumerate(f):
                if current_index == random_line_index:
                    return line.strip()

    def generate_pm(self, Prompt: str, seed: int = None) -> Tuple[str]:
        if seed: self.rng.seed(seed)
        files = {tag: os.path.join(os.path.dirname(__file__), "data", f"{name}.csv") for tag, name in {
            "<celeb>": "celebrities", "<media>": "assorted_media", "<game>": "games", "<film>": "movies", "<species>": "species", "<nlt>": "nationalities", 
            "<loc>": "locations_mundane", "<locw>": "locations_weird", "<out>": "outfits", "<outn>": "outfits_nsfw",
            "<makeup>": "makeup", "<exp>": "expressions", "<time>": "times", "<pose>": "poses", 
            "<pass>": "passwords", "<word>": "words", "<wordp>": "power_words", "<wordn>": "power_words_nsfw", "<wordk>": "keywords", "<color>": "colors","<color2>": "color2","<medi>": "mediums","<light>":"lighting","<style>":"styles"}.items()}
        while any(tag in Prompt for tag in files):
            Prompt = re.sub("|".join(map(re.escape, files)), lambda m: self.random_line_from_file(files[m.group()]), Prompt, 1)
        return (re.sub(r"<(\d+)-(\d+)>|<(\d{2}xx|xxxx|\d{1}xxx)>", lambda m: str(self.rng.randint(1900 + int(m.group(1)), 1900 + int(m.group(2)))) if m.group(1) else str(self.rng.randint(1000, 9999) if m.group(3) == "xxxx" else self.rng.randint(int(m.group(3)[0] + "000"), int(m.group(3)[0] + "999")) if "xxx" in m.group(3) else self.rng.randint(int(m.group(3)[:2] + "00"), int(m.group(3)[:2] + "99"))), Prompt),)