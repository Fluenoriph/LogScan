from app_code.modules.argument_parser import ArgumentParser
from app_code.modules.program_process import ProgramProcess


if __name__ == '__main__':
    argument_parser = ArgumentParser()

    app_core = ProgramProcess(argument_parser.arguments.logfile, argument_parser.arguments.apikey,
                              argument_parser.arguments.output, argument_parser.arguments.format)
