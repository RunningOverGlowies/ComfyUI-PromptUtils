from .filename_generator import FilenameGenerator
from .keyword_generator import KeywordGenerator
from .prompt_wildcards import PromptWildcards

NODE_CLASS_MAPPINGS = {
    "FilenameGenerator": FilenameGenerator, 
    "KeywordGenerator": KeywordGenerator,
    "PromptWildcards": PromptWildcards,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FilenameGenerator": "Filename Generator 📁", 
    "KeywordGenerator": "Keyword Generator 🔑",
    "PromptWildcards": "Prompt Wildcards ✨",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
