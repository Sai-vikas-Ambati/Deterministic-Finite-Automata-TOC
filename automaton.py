class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def accepts(self, input_string):
        state = self.start_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False  # reject invalid symbols
            state = self.transition_function.get((state, symbol))
            if state is None:
                return False
        return state in self.accept_states


if __name__ == "__main__":
    # Example DFA: accepts binary strings ending with '01'
    states = {"q0", "q1", "q2"}
    alphabet = {"0", "1"}
    transition_function = {
        ("q0", "0"): "q1",
        ("q0", "1"): "q0",
        ("q1", "0"): "q1",
        ("q1", "1"): "q2",
        ("q2", "0"): "q1",
        ("q2", "1"): "q0",
    }
    start_state = "q0"
    accept_states = {"q2"}

    dfa = DFA(states, alphabet, transition_function, start_state, accept_states)

    # Run test cases
    test_strings = ["01", "101", "001", "111", "1001"]
    for s in test_strings:
        print(f"{s}: {'ACCEPTED' if dfa.accepts(s
