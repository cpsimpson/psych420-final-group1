from .concepts.short_term import ShortTermMemory


class Hippocampus:

    def __init__(self, cortex, data_monitor, fuzzy_threshold=0.03):
        self.cortex = cortex
        self.short_term_memory = ShortTermMemory(self, data_monitor)
        self.data_monitor = data_monitor
        self._fuzzy_threshold = fuzzy_threshold

    def __str__(self):
        return f"Short Term Memory: \n {self.short_term_memory} \n"

    @property
    def fuzzy_threshold(self):
        return self._fuzzy_threshold

    @fuzzy_threshold.setter
    def fuzzy_threshold(self, fuzzy_threshold):
        self._fuzzy_threshold = fuzzy_threshold

    def time_tick(self):
        self.short_term_memory.time_tick()

    def end_simulation(self):
        self.short_term_memory.end_simulation()

    def process_sensory_input(self, sensory_input):
        self.short_term_memory.add(sensory_input)

    def send_to_long_term_storage(self, memory):
        self.cortex.store_memory(memory)

    def retrieve_from_long_term_storage(self, valence, arousal, dominance):
        return self.cortex.retrieve_memory(valence, arousal, dominance)
