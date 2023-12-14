import re

# Arreglo de reglas o hechos
facts = {}
rules = {}

# Funcion para comprobar si una expresion es un atomo
def is_atom(expression):
    return re.match("^[a-z][a-zA-Z0-9]*$", expression) is not None

# Funcion para comprobar si una expresion es una variable
def is_variable(expression):
    return re.match("^[A-Z][a-zA-Z0-9]*$", expression) is not None

# Funcion para comprobar si una expresion es una estrucura
def is_structure(expression):
    return "(" in expression and ")" in expression and is_atom(expression.split("(")[0])

# Funcion para aplicar las reglas de la query
def apply_rule(rule, query):

    rule_args, antecedents = rule
    unifications = unify(query, ("structure", None, rule_args))

    if unifications is None:
        return None
    return unifications

# Funcion para parsear expresiones (to fix espacios en blanco)
def parse_expression(expression):
    if is_atom(expression):
        return ("atom", expression)
    elif is_variable(expression):
        return ("variable", expression)
    elif is_structure(expression):
        functor, args = expression.split("(", 1)
        args = args[:-1]
        args = [arg.strip() for arg in args.split(",")]
        parsed_args = [parse_expression(arg) for arg in args]
        return ("structure", functor, parsed_args)
    else:
        raise ValueError("Error aqui")

# Funcion que define un hecho o una regla
def define_fact_or_rule(expression, antecedents):
    expr_type, functor, args = parse_expression(expression)
    if expr_type != "structure":
        raise ValueError("Error dios ya basta")

    if not antecedents:
        facts[functor] = [("structure", functor, args)]
        print(f"Se definió el hecho '{expression}'")
    else:
        parsed_antecedents = [parse_expression(ant) for ant in antecedents]
        if functor not in rules:
            rules[functor] = []
        rules[functor].append((("structure", functor, args), parsed_antecedents))
        print(f"Se definió la regla '{expression} :- {' '.join(antecedents)}'")

# Unifica Expresiones con sus hechos
def unify(expression, fact):
    _, _, expr_args = expression
    _, _, fact_args = fact

    if len(expr_args) != len(fact_args):
        return None

    unifications = {}
    for expr_arg, fact_arg in zip(expr_args, fact_args):
        expr_arg_type, expr_arg_value = expr_arg
        fact_arg_type, fact_arg_value = fact_arg

        if expr_arg_type == "variable":
            unifications[expr_arg_value] = fact_arg_value
        elif expr_arg_value != fact_arg_value:
            return None

    return unifications

        
# Funcion para manejar las querys
def handle_query(expression):
    expr_type, functor, args = parse_expression(expression)
    if expr_type != "structure":
        raise ValueError("LMAOOOOOOOOOOOOOOOO")

    query = (expr_type, functor, args)

    # Buscar en los hechos
    if functor in facts:
        for fact in facts[functor]:
            unifications = unify(query, fact)
            if unifications is not None:
                print(f"Satisfacible, cuando {', '.join(f'{k} = {v}' for k, v in unifications.items())}.")
                return

    # Buscar en las reglas
    if functor in rules:
        unifications = apply_rule(rules[functor], query)
        if unifications is not None:
            print(f"Satisfacible, cuando {', '.join(f'{k} = {v}' for k, v in unifications.items())}.")
            return

    print("No es satisfacible.")


# Interfaz de usuario
def main():
    while True:
        user_input = input("Ingrese una acción (DEF, ASK, SALIR): ")
        if "DEF" in user_input:
            _, expression, *antecedents = user_input.split()
            print(expression)
            define_fact_or_rule(expression, antecedents)
        elif "ASK" in user_input:
            _, expression = user_input.split(maxsplit=1)
            handle_query(expression)
        elif user_input == "SALIR":
            break
        else:
            print("Acción no reconocida")

if __name__ == "__main__":
    main()