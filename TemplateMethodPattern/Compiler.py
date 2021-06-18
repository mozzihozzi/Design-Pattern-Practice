from abc import ABCMeta, abstractmethod


class Compiler(metaclass=ABCMeta):
    @abstractmethod
    def collectSource(self):
        pass

    @abstractmethod
    def compileToObject(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compileAndRun(self):
        self.run()


class IOSCompiler(Compiler):
    def collectSource(self):
        print("Collecting Swift Source Code!!")

    def compileToObject(self):
        print("Compiling Swift Code to LLVM Bitcode!!")

    def run(self):
        print("Program running on runtime environment")


if __name__ == "__main__":
    IOS = IOSCompiler()
    IOS.compileAndRun()

