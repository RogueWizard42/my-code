#user code efficiency analyzer - because why not right?

import ast

def code_analyzer(user_code):
    
    def get_complexity_rating(complexity_score):
        if complexity_score <= 3:
            return "Simple: Your code is as clean as a well-maintained sword. Simple and effective!"
        elif complexity_score <=6:
            return "Moderate: Your code has some depth, like a seasoned adventurer facing their first real challenge."
        elif complexity_score <=9:
            return "Complex: Your code is a strategic battlefield, filled with layers of complexity. If this is by design, well played! If not, consider reforging your approach for a cleaner fight."
        else:
            return "Very Complex: Your code harnesses immense power, like an ancient tome of forgotten spells. If the complexity is necessary, then you wield it well. But beware—such magic can be dangerous if left unchecked!"
    
    coder = ast.parse(user_code) #looking through the code input by the user
    #setting the stuff i'm looking for to zero
    loop_count = 0
    function_count = 0
    if_count = 0
    recursion_count = 0
    complexity_score = 0  #complexity score is the sum of the weights of the different elements we're counting
    
    for node in ast.walk(coder):
        if isinstance(node, (ast.For, ast.While)):
            loop_count += 1
        elif isinstance(node, ast.FunctionDef):
            function_count += 1
            for child_node in ast.walk(node):
                if isinstance(child_node, ast.Call):
                    if isinstance(child_node.func, ast.Name) and child_node.func.id == node.name:
                        recursion_count += 1
        elif isinstance(node, ast.If):
            if_count += 1
     
    #complexity score weighting is based on an arbitrary combination of Big O complexity and Cyclomatic complexity       
    complexity_score = (loop_count *2) + (function_count *1) + (if_count * 1) + (recursion_count * 3) 
    complexity_rating = get_complexity_rating(complexity_score)
    
    print(f"Loops: {loop_count}, Functions: {function_count}, Ifs: {if_count}, Recursion: {recursion_count}, Complexity Score: {complexity_score}")
    return complexity_rating


test_code_5 = """
def summon_demon(power):
    if power > 100:
        return "Demon Lord"
    else:
        return summon_demon(power + 10)

def dungeon_escape():
    for i in range(5):
        while i < 5:  # ✅ Adding a while loop to push complexity above 10
            if i % 2 == 0:
                print("Turn left")
            else:
                print("Turn right")
            i += 1
"""

print(code_analyzer(test_code_5))






            
    










