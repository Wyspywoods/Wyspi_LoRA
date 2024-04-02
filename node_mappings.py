try:
    from .nodes.nodes_lora import *
except ImportError:
    print("\033[34mComfyroll Studio: \033[92mFailed to load Essential nodes\033[0m")

NODE_CLASS_MAPPINGS = {
    ### LoRA Nodes    
    "WW Load LoRA": WW_LoraLoader,    
    "WW LoRA Stack": WW_LoRAStack,
    "CR Apply LoRA Stack": WW_ApplyLoRAStack,  
}

NODE_DISPLAY_NAME_MAPPINGS = {
    ### LoRA Nodes    
    "WW Load LoRA": "👻 WW Load LoRA",    
    "WW LoRA Stack": "👻 WW LoRA Stack",
    "CR Apply LoRA Stack": "👻 WW Apply LoRA Stack",  
}
