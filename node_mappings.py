try:
    from .nodes.nodes_lora import *
except ImportError:
    print("\033[34mComfyroll Studio: \033[92mFailed to load Essential nodes\033[0m")

NODE_CLASS_MAPPINGS = {
    ### LoRA Nodes    
    "CR Load LoRA": CR_LoraLoader,    
    "CR LoRA Stack": CR_LoRAStack,
    "CR Random LoRA Stack": CR_RandomLoRAStack,
    "CR Random Weight LoRA": CR_RandomWeightLoRA,
    "CR Apply LoRA Stack": CR_ApplyLoRAStack,  
}

NODE_DISPLAY_NAME_MAPPINGS = {
    ### LoRA Nodes    
    "CR Load LoRA": "💊 CR Load LoRA",    
    "CR LoRA Stack": "💊 CR LoRA Stack",
    "CR Random LoRA Stack": "💊 CR Random LoRA Stack",
    "CR Random Weight LoRA": "💊 CR Random Weight LoRA",
    "CR Apply LoRA Stack": "💊 CR Apply LoRA Stack",  
}
