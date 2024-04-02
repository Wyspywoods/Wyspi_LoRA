try:
    from .nodes.nodes_lora import *
except ImportError:
    print("\033[31mWyspi: \033[96mFailed to load Essential nodes\033[0m")

NODE_CLASS_MAPPINGS = {
    ### LoRA Nodes    
    "WW Load LoRA": WW_LoraLoader,    
    "WW LoRA Stack": WW_LoRAStack,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    ### LoRA Nodes    
    "WW Load LoRA": "👻 WW Load LoRA",    
    "WW LoRA Stack": "👻 WW LoRA Stack",
}
