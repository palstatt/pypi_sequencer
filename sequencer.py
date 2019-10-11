class Sequencer:

    bpm = 140
    sequence = []
    current_step = 0

    def __init__(self):
        self.sequence = [[], [], [], [], [], [], [], []]

    def get_tempo(self):
        return (60 / self.bpm) / 2

    def add_step(self, sound, at_step):
        self.sequence[at_step].append(sound)

    def add_steps(self, sound, at_steps):
        for step in at_steps:
            self.add_step(sound, step)

    def remove_step(self, sound, at_step):
        if sound in self.sequence[at_step]:
            self.sequence[at_step].remove(sound)

    def get_step(self):
        step = self.current_step % 8
        self.current_step += 1
        return self.sequence[step]

    def speed_up(self, increment_by):
        self.bpm += increment_by

    def slow_down(self, decrement_by):
        self.bpm -= decrement_by
