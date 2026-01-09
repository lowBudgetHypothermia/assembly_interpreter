
class ASMARM:
    def __init__(self, path: str):
        self.source = path
        self.R = [0] * 16  # TODO: fill with i32s
        self.SP = self.R[13]
        self.LR = self.R[14]
        self.PC = self.R[15]
        # TODO: load all lines
        # ex:
        # self.program[n] = ["mov", "acc", "#42"]
        self.program = None  

    def step(self):
        # TODO: single line step
        pass

    def run(self):
        # TODO
        while self.PC != "SWI"

        pass

    def stop(self):
        # TODO
        pass

if __name__ == "__main__":
    inter = Interpreter("example.asm")
