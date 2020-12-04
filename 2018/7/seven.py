import sys
sys.path.append('../')

from list import *

class Instruction:
    def __init__(self, prereq, step):
        self.prereq = prereq
        self.step = step

class InstructionList(List):
    def __init__(self, file):
        super().__init__(file)

    def calculateSets(self):
        # create 3 sets, all the prerequisites, all the things the prereqs are
        # of, and all the steps that exist (union of the previous two)
        self.allPrereqs = set()
        self.allStepLabels = set()
        for instruction in self.list:
            self.allPrereqs.add(instruction.prereq)
            self.allStepLabels.add(instruction.step)
        self.allSteps = self.allPrereqs.union(self.allStepLabels)


    def load(self):
        # load each line into data field
        super().load()
        # print(self.data)
        for instruction in self.data:
            prereq = instruction[5]
            step = instruction[36]
            self.list.append(Instruction(prereq, step))

        self.calculateSets()

    def __str__(self):
        out = ''
        for inst in self.list:
            out += 'prerequisite: ' + inst.prereq + ', step: ' + inst.step + '\n'
        return out

    def solve(self):
        allPrereqs = self.allPrereqs
        allStepLabels = self.allStepLabels
        allSteps = self.allSteps

        print(f'prerequisites: {allPrereqs}')
        print(f'step labels: {allStepLabels}')
        print(f'all steps: {allSteps}')

        # make sure our sets are correct
        assert allSteps.issuperset(allStepLabels)
        assert allSteps.issuperset(allPrereqs)

        # create a list of the available instructions (instructions with no
        # prerequisites)
        availableInstructions = sorted(list(allPrereqs - allStepLabels))
        print(f'availableInstructions: {availableInstructions}')

        order = []

        # as long as there's an available instruction
        while availableInstructions != []:
            nextInst = availableInstructions[0]

            # add the available instruction to our order
            order.append(nextInst)

            # remove any instructions with a prerequisite of the available
            # instruction from the list
            for inst in self.list:
                if inst.prereq == nextInst:
                    self.list.remove(inst)

            # recalculate the sets
            self.calculateSets()

            # reset the available instructions
            availableInstructions = sorted(list(self.allPrereqs - self.allStepLabels))
            print(availableInstructions)

        print(f'prerequisites: {allPrereqs}')
        print(f'step labels: {allStepLabels}')
        print(f'all steps: {allSteps}')
        print(f'order:{order}')
        return order

class Step:
    def __init__(self, step, prereqs):
        self.step = step # a string 'A', 'B', 'C', etc.
        self.prereqs = prereqs # an array of these strings ^
    def __str__(self):
        return 'step: ' + str(self.step) + ', prereqs: ' + str(self.prereqs)

class StepList:
    def __init__(self, instructionList):
        self.list = []

        # make a set of all the step labels that there are
        steps = set()
        for instruction in instructionList.list:
            steps.add(instruction.prereq)
            steps.add(instruction.step)
        steps = sorted(list(steps))

        for step in steps:
            prereqs = []
            for instruction in instructionList.list:
                if instruction.step == step:
                    prereqs.append(instruction.prereq)
            self.list.append(Step(step, prereqs))

    def __str__(self):
        out = ''
        for item in self.list:
            out += str(item) + '\n'
        return out

    def __len__(self):
        length = 0
        for item in self.list:
            length += 1
        return length

    def solve(self):
        order = ''

        # as long as the
        while len(self.list) > 0:
            # find the first step with no prerequisites: the actionable step
            for step in self.list:
                if step.prereqs == []:
                    actionableStep = step.step
                    # remove it from the StepList (since it's being done)
                    self.list.remove(step)
                    break
            # add it to a string 'order' to mark that it's been done
            order += actionableStep
            print(f'order: {order}')
            # remove it from all the other prerequisites (it's completed)
            for step in self.list:
                if actionableStep in step.prereqs:
                    step.prereqs.remove(actionableStep)
        return order

if __name__ == '__main__':
    e = InstructionList('testInput.txt')
    e.load()
    print(e)
    f = StepList(e)
    print(f)
    print(f.solve())

    g = InstructionList('input.txt')
    g.load()
    print(g)
    h = StepList(g)
    print(h)
    print(h.solve())
