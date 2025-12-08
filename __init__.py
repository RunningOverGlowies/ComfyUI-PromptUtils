from .filename_generator import FilenameGenerator
from .prompt_wildcards import PromptWildcards

NODE_CLASS_MAPPINGS = {
    "FilenameGenerator": FilenameGenerator,
    "PromptWildcards": PromptWildcards,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FilenameGenerator": "Filename Generator 📁",
    "PromptWildcards": "Prompt Wildcards ✨",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

