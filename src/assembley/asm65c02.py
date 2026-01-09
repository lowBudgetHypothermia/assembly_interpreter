from dataclass import dataclass

@dataclass
class Registers:
    ACC: int  # 1 Byte

    # indexes
    X: int = 0    # 1 Byte
    Y: int = 0    # 1 Byte

    # stack pointer
    # addresses 256-Byte stack: $0100-$01FF
    S: int = 0    # 1 Byte
    PC: int = 0   # 2 Bytes

    # status register
    P: int = 0    # 1 Byte, 6 Bits used by ALU

class ASM65C02:
    def __init__(self, path: str):
        self.source = path
        self.regs = Registers()

        # TODO: load all lines
        self.program = None

    def step(self):
        # TODO: single line step
        pass

    def run(self):
        # TODO
        while self.PC != "STP":
            pass

    def stop(self):
        # TODO
        pass

if __name__ == "__main__":
    inter = Interpreter("example.asm")
