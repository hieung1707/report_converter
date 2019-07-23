class Branch:
    def __init__(self, index, intent, meaning):
        self.index = index
        self.intent = intent
        self.next_branches = []
        self.meaning = meaning

    def add_next_branch(self, next_branch):
        self.next_branches.append(next_branch)

    def get_intent(self):
        return self.intent

    def get_next_branch(self, intent):
        for branch in self.next_branches:
            if intent == branch.get_intent():
                return branch
        return None
