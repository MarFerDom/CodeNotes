from dataclasses import dataclass
from farmAnimal import farmAnimal



farmAnimal_type_list: 'dict[str, callable[..., farmAnimal]]' = {}



def makeFromJson(**args: 'dict[str,any]'):
    args_ = args.copy()
    name_of_type = args_.pop('name_of_type','platypus')
    return makeAnimal(name_of_type=name_of_type, args=args_)



def makeAnimal(args: 'dict[str,any]', name_of_type: str = "platypus"):
    '''instantiate animal from registered class with arguments'''

    builder = farmAnimal_type_list.get(name_of_type, platypus)
    return builder(**args)



def registerAnimal(type_name: str, builder: 'callable[...,farmAnimal]'):
    '''register class by name'''

    farmAnimal_type_list[type_name] = builder



@dataclass
class platypus():
    '''Default random animal that follows the farmAnimal Protocol'''

    name: str = 'Plato'

    def do(self) -> None:
        print(f"I am {self.name} the platypus!! Kneel befor me!")