from enum import Enum, auto


class Role(Enum):
    """Employee roles."""

    CTO = auto()
    SOFTWARE_ARCHITECT = auto()
    SOFTWARE_ENGINEER = auto()
    SOFTWARE_TESTER = auto()


class Employee:
    # defines class variables with identifier and their datatype
    name: str
    # role: str # better use an enum here
    role: Role
    vacation_days: int = 30


# the order is important. The command would not work if it is above
# the class definition for Employee.
employee_inst = Employee()

# Calling that without initialisation raises an AttributeError
# print(employee_inst.name)
