#---------------------------------------------------------------------------------------------------------------------#
# Wyspywoods                                             
#---------------------------------------------------------------------------------------------------------------------#

import os
import sys
import comfy.sd
import comfy.utils
import folder_paths
import hashlib
from ..categories import icons

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "comfy"))

#---------------------------------------------------------------------------------------------------------------------#
# LoRA Nodes
#---------------------------------------------------------------------------------------------------------------------#
# This is a load lora node with an added switch to turn on or off.  On will add the lora and off will skip the node.
class WW_LoraLoader:
    def __init__(self):
        self.loaded_lora = None

    @classmethod
    def INPUT_TYPES(cls):
        loras = ["None"] + folder_paths.get_filename_list("loras")
    
        return {"required": {
            "lora_name_1": (loras,),
            "switch_1": (["🤍💤🤍","❤️💚❤️"],),
            "model_weight_1": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.05}),

            "lora_name_2": (loras,),
            "switch_2": (["🤍💤🤍","❤️💚❤️"],),
            "model_weight_2": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.05}),

            "lora_name_3": (loras,),
            "switch_3": (["🤍💤🤍","❤️💚❤️"],),
            "model_weight_3": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.05}),

            "lora_name_4": (loras,),
            "switch_4": (["🤍💤🤍","❤️💚❤️"],),
            "model_weight_4": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.05}),

            "lora_name_5": (loras,),
            "switch_5": (["🤍💤🤍","❤️💚❤️"],),
            "model_weight_5": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.05}),

            "lora_name_6": (loras,),
            "switch_6": (["🤍💤🤍","❤️💚❤️"],),
            "model_weight_6": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.05}),

            "lora_name_7": (loras,),
            "switch_7": (["🤍💤🤍","❤️💚❤️"],),
            "model_weight_7": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.05}),

            "lora_name_8": (loras,),
            "switch_8": (["🤍💤🤍","❤️💚❤️"],),
            "model_weight_8": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.05}),

            "lora_name_9": (loras,),
            "switch_9": (["🤍💤🤍","❤️💚❤️"],),
            "model_weight_9": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.05}),

            "lora_name_10": (loras,),
            "switch_10": (["🤍💤🤍","❤️💚❤️"],),
            "model_weight_10": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.05}),
        },
            "optional": {"lora_stack": ("LORA_STACK",)
            },
    }

    RETURN_TYPES = ("LORA_STACK", "STRING", )
    RETURN_NAMES = ("LORA_STACK", "show_help", )
    FUNCTION = "load_lora"
    CATEGORY = icons.get("Wyspi/LoRA")

    def load_lora(self, lora_name_1, model_weight_1, switch_1, lora_name_2, model_weight_2, switch_2, lora_name_3, model_weight_3, switch_3, lora_name_4, model_weight_4, switch_4, lora_name_5, model_weight_5, switch_5, lora_name_6, model_weight_6, switch_6, lora_name_7, model_weight_7, switch_7, lora_name_8, model_weight_8, switch_8, lora_name_9, model_weight_9, switch_9, lora_name_10, model_weight_10, switch_10, lora_stack=None):
        clip_weight = 1.0  # Set clip_weights to 1 by default

        # Initialise the list
        lora_list=list()

        if lora_stack is not None:
            lora_list.extend([l for l in lora_stack if l[0] != "None"])

        if lora_name_1 != "None" and  switch_1 == "❤️💚❤️":
            lora_list.extend([(lora_name_1, model_weight_1, clip_weight)]),

        if lora_name_2 != "None" and  switch_2 == "❤️💚❤️":
            lora_list.extend([(lora_name_2, model_weight_2, clip_weight)]),

        if lora_name_3 != "None" and  switch_3 == "❤️💚❤️":
            lora_list.extend([(lora_name_3, model_weight_3, clip_weight)]),

        if lora_name_4 != "None" and  switch_4 == "❤️💚❤️":
            lora_list.extend([(lora_name_4, model_weight_4, clip_weight)]),

        if lora_name_5 != "None" and  switch_5 == "❤️💚❤️":
            lora_list.extend([(lora_name_5, model_weight_5, clip_weight)]),

        if lora_name_6 != "None" and  switch_6 == "❤️💚❤️":
            lora_list.extend([(lora_name_6, model_weight_6, clip_weight)]),

        if lora_name_7 != "None" and  switch_7 == "❤️💚❤️":
            lora_list.extend([(lora_name_7, model_weight_7, clip_weight)]),

        if lora_name_8 != "None" and  switch_8 == "❤️💚❤️":
            lora_list.extend([(lora_name_8, model_weight_8, clip_weight)]),

        if lora_name_9 != "None" and  switch_9 == "❤️💚❤️":
            lora_list.extend([(lora_name_9, model_weight_9, clip_weight)]),

        if lora_name_10 != "None" and  switch_10 == "❤️💚❤️":
            lora_list.extend([(lora_name_10, model_weight_10, clip_weight)]),

        show_help = "💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚"           

        return (lora_list, show_help, )

#---------------------------------------------------------------------------------------------------------------------#
# Based on Efficiency Nodes
# This is a lora stack where a single node has 3 different loras each with their own switch
class WW_LoRAStack:

    @classmethod
    def INPUT_TYPES(cls):
        loras = ["None"] + folder_paths.get_filename_list("loras")
    
        return {"required": {
            "lora_name_1": (loras,),
            "switch_1": (["🤍💤🤍","❤️💚❤️"],),
            "model_weight_1": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.05}),
            "text_box_1": ("STRING", {"default": "TriggerW"}),

            "lora_name_2": (loras,),
            "switch_2": (["🤍💤🤍","❤️💚❤️"],),
            "model_weight_2": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.05}),
            "text_box_2": ("STRING", {"default": "TriggerW"}),

            "lora_name_3": (loras,),
            "switch_3": (["🤍💤🤍","❤️💚❤️"],),
            "model_weight_3": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.05}),
            "text_box_3": ("STRING", {"default": "TriggerW"}),

            "lora_name_4": (loras,),
            "switch_4": (["🤍💤🤍","❤️💚❤️"],),
            "model_weight_4": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.05}),
            "text_box_4": ("STRING", {"default": "TriggerW"}),

            "lora_name_5": (loras,),
            "switch_5": (["🤍💤🤍","❤️💚❤️"],),
            "model_weight_5": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.05}),
            "text_box_5": ("STRING", {"default": "TriggerW"}),

            "lora_name_6": (loras,),
            "switch_6": (["🤍💤🤍","❤️💚❤️"],),
            "model_weight_6": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.05}),
            "text_box_6": ("STRING", {"default": "TriggerW"}),

            "lora_name_7": (loras,),
            "switch_7": (["🤍💤🤍","❤️💚❤️"],),
            "model_weight_7": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.05}),
            "text_box_7": ("STRING", {"default": "TriggerW"}),

            "lora_name_8": (loras,),
            "switch_8": (["🤍💤🤍","❤️💚❤️"],),
            "model_weight_8": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.05}),
            "text_box_8": ("STRING", {"default": "TriggerW"}),

            "lora_name_9": (loras,),
            "switch_9": (["🤍💤🤍","❤️💚❤️"],),
            "model_weight_9": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.05}),
            "text_box_9": ("STRING", {"default": "TriggerW"}),

            "lora_name_10": (loras,),
            "switch_10": (["🤍💤🤍","❤️💚❤️"],),
            "model_weight_10": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.05}),
            "text_box_10": ("STRING", {"default": "TriggerW"}),
        },
            "optional": {"lora_stack": ("LORA_STACK",)
            },
    }

    RETURN_TYPES = ("LORA_STACK", "STRING", )
    RETURN_NAMES = ("LORA_STACK", "show_help", )
    FUNCTION = "lora_stacker"
    CATEGORY = icons.get("Wyspi/LoRA")

    def lora_stacker(self, lora_name_1, model_weight_1, switch_1, text_box_1, lora_name_2, model_weight_2, switch_2, text_box_2, lora_name_3, model_weight_3, switch_3, text_box_3, lora_name_4, model_weight_4, switch_4, text_box_4, lora_name_5, model_weight_5, switch_5, text_box_5, lora_name_6, model_weight_6, switch_6, text_box_6, lora_name_7, model_weight_7, switch_7, text_box_7, lora_name_8, model_weight_8, switch_8, text_box_8, lora_name_9, model_weight_9, switch_9, text_box_9, lora_name_10, model_weight_10, switch_10, text_box_10, lora_stack=None):
        clip_weight = 1.0  # Set clip_weights to 1 by default

        # Initialise the list
        lora_list=list()

        if lora_stack is not None:
            lora_list.extend([l for l in lora_stack if l[0] != "None"])

        if lora_name_1 != "None" and  switch_1 == "❤️💚❤️":
            lora_list.extend([(lora_name_1, model_weight_1, clip_weight)]),

        if lora_name_2 != "None" and  switch_2 == "❤️💚❤️":
            lora_list.extend([(lora_name_2, model_weight_2, clip_weight)]),

        if lora_name_3 != "None" and  switch_3 == "❤️💚❤️":
            lora_list.extend([(lora_name_3, model_weight_3, clip_weight)]),

        if lora_name_4 != "None" and  switch_4 == "❤️💚❤️":
            lora_list.extend([(lora_name_4, model_weight_4, clip_weight)]),

        if lora_name_5 != "None" and  switch_5 == "❤️💚❤️":
            lora_list.extend([(lora_name_5, model_weight_5, clip_weight)]),

        if lora_name_6 != "None" and  switch_6 == "❤️💚❤️":
            lora_list.extend([(lora_name_6, model_weight_6, clip_weight)]),

        if lora_name_7 != "None" and  switch_7 == "❤️💚❤️":
            lora_list.extend([(lora_name_7, model_weight_7, clip_weight)]),

        if lora_name_8 != "None" and  switch_8 == "❤️💚❤️":
            lora_list.extend([(lora_name_8, model_weight_8, clip_weight)]),

        if lora_name_9 != "None" and  switch_9 == "❤️💚❤️":
            lora_list.extend([(lora_name_9, model_weight_9, clip_weight)]),

        if lora_name_10 != "None" and  switch_10 == "❤️💚❤️":
            lora_list.extend([(lora_name_10, model_weight_10, clip_weight)]),

        show_help = "💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚"           

        return (lora_list, show_help, )
#---------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------------------------#
# MAPPINGS
#---------------------------------------------------------------------------------------------------------------------#
# For reference only, actual mappings are in __init__.py
'''
NODE_CLASS_MAPPINGS = {
    "WW Load LoRA": WW_LoraLoader,
    "WW LoRA Stack":WW_LoRAStack,
}
'''
