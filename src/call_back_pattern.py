from typing import List, Dict, Any, Callable
import pandas as pd

class Input:
    def __init__(self, df: pd.DataFrame, targets: List[Any]):
        self.df = df
        self.targets = targets

Inputs = List[Input]
run = Callable[[Inputs], Dict[str, Any]]

def Kindergarten(inputs_list: Inputs) -> Dict[str, Any]:
    df = inputs_list[0].df
    targets = inputs_list[0].targets
    store = {
        "kindergarten_df": df,
        "kindergarten_targets": targets
    }
    return store
   
def Over18Months(inputs_list: Inputs) -> Dict[str, Any]:
    df = inputs_list[0].df
    targets = inputs_list[0].targets
    store = {
        "over18months_df": df,
        "over18months_targets": targets
    }
    return store
        
def Under18Months(inputs_list: Inputs) -> Dict[str, Any]:
    df = inputs_list[0].df
    targets = inputs_list[0].targets
    store = {
        "under18months_df": df,
        "under18months_targets": targets
    }
    return store

class Build:
    def __init__(self):
        self.build: Inputs = []
        
    def add_inputs(self, df, targets):
        self.build.append(Input(df, targets))
    
    def process_interface(self, run):
        results = run(self.build)
        keys = list(results.keys())
        print("df:\n", results.get(keys[0]))
        print("targets:\n", results.get(keys[1]))

df = pd.DataFrame({'names': 
                        ["hans", "grete", "martin", "jens"],
                   'score':
                        [5, 10, 4, 3]
                 })

targets = ["hans", "grete", "jens"]
build = Build()
build.add_inputs(df, targets)
build.process_interface(Under18Months)