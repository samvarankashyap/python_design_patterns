class LinchpinAPI(object):
    def __init__(self):
        self._state= None
        self._state_observers = []

    @property
    def state(self):
        """getter function for state property of the API obect."""
        print("getter of variable state called")
        return self._state

    @state.setter
    def state(self, value):
        # call run_hooks after state is being set
        print("setter of state variable called")
        self._state = value

        for callback in self._state_observers:
            callback(self._state)
            # currently supports only one observer call for each state
            # so popping out the observer object after the callback
            self._state_observers.pop()

    def bind_to_state(self, callback):
        print('bound to state')
        self._state_observers.append(callback)


class LinchpinHooks(object):
    def __init__(self, api):
        self.api = api
        self.api.bind_to_state(self.trigger_state_change)

    def trigger_state_change(self, state):
        print("state change triggered in linchpin api")
        print("Observed in LinchpinHooks :: "+str(state))


if __name__ == '__main__':
    print("Creating api object")
    api_obj = LinchpinAPI()
    print("Creating linchpin hooks object, and passing api to constructor")
    p = LinchpinHooks(api_obj)
    print("Changing the state of the api object")
    api_obj.state = "preup"
