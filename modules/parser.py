from recognizers.program import Program


class Parser:

    def __init__(self, lexical_reclassifier):
        self.lexical = lexical_reclassifier

    def parse(self):
        reuse_token = False
        stack = []
        machine = Program()

        while True:
            if not reuse_token:
                token = self.lexical.get_token()
                if token.value == 'EOF':
                    break
            reuse_token = False

            print('token: {} | state: ({}, {}) | stack len: {}'
                  .format(token.value, machine.__class__.__name__,
                          machine.get_state(), len(stack)))

            try:
                while True:
                    sub_machine = machine.process_atom(token)
                    # print('sub machine = {}'.format(sub_machine.__class__.__name__))
                    if sub_machine:
                        stack.append(machine)
                        machine = sub_machine
                    else:
                        break

            except ValueError as ex:
                if machine.accept():
                    reuse_token = True
                    try:
                        machine = stack.pop()
                    except IndexError:
                        print('Syntax error.')
                        return False
                else:
                    # Unexpected error
                    print(ex)
                    return False

        stack.append(machine)
        for m in stack:
            if not m.accept():
                return False
        return True
