from rasa.shared.core.slots import Slot
from typing import Any, Dict, List, Text, Optional

class CurrentContextSlot(Slot):

    type_name = "fact_about"
    
    def __init__(
        self,
        name: Text,
        mappings: List[Dict[Text, Any]],
        initial_value: Any = None,
        value_reset_delay: Optional[int] = None,
        influence_conversation: bool = True,
    ) -> None:

        super().__init__(
            name=name,
            initial_value=initial_value,
            mappings=mappings,
            value_reset_delay=value_reset_delay,
            influence_conversation=influence_conversation,
        )
        self.curr_context = ""

    def _feature_dimensionality(self):
        return 2

    def _as_feature(self):
        r = [0.0] * self.feature_dimensionality()
        if self.value:
            print("Received feature is... = ", self.value)
            if not self.curr_context:
                self.curr_context = self.value
            if self.curr_context == "fish_fun_facts":
                r[0] = 1.0
            elif self.curr_context == "pet_fun_facts":
                r[1] = 1.0
        return r