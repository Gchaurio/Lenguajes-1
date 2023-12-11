# Importaciones necesarias
import re

# Estructuras de datos para almacenar hechos y reglas
facts = {}
rules = {}

# Funciones de utilidad para análisis y validación de expresiones
def is_atom(expression):
    return re.match("^[a-z][a-zA-Z0-9]*$", expression) is not None

def is_variable(expression):
    return re.match("^[A-Z][a-zA-Z0-9]*$", expression) is not None

def is_structure(expression):
    return "(" in expression and ")" in expression and is_atom(expression.split("(")[0])

def apply_rule(rule, query):
    """Aplica una regla a una consulta, si es posible."""
    # Esta es una implementación muy simplificada.
    # No maneja la recursión ni las reglas más complejas.
    rule_args, antecedents = rule
    unifications = unify(query, ("structure", None, rule_args))

    if unifications is None:
        return None

    # Aquí deberías expandir la lógica para manejar antecedentes de reglas.
    return unifications

def parse_expression(expression):
    if is_atom(expression):
        return ("atom", expression)
    elif is_variable(expression):
        return ("variable", expression)
    elif is_structure(expression):
        functor, args = expression.split("(", 1)
        args = args[:-1]  # Remove closing parenthesis
        args = [arg.strip() for arg in args.split(",")]
        parsed_args = [parse_expression(arg) for arg in args]
        return ("structure", functor, parsed_args)
    else:
        raise ValueError("Invalid expression")

def define_fact_or_rule(expression, antecedents):
    expr_type, functor, args = parse_expression(expression)
    if expr_type != "structure":
        raise ValueError("Only structures can be facts or rules")

    if not antecedents:
        facts[functor] = [("structure", functor, args)]
        print(f"Se definió el hecho '{expression}'")
    else:
        parsed_antecedents = [parse_expression(ant) for ant in antecedents]
        if functor not in rules:
            rules[functor] = []
        rules[functor].append((("structure", functor, args), parsed_antecedents))
        print(f"Se definió la regla '{expression} :- {' '.join(antecedents)}'")

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

        
# Función para manejar consultas
def handle_query(expression):
    expr_type, functor, args = parse_expression(expression)
    if expr_type != "structure":
        raise ValueError("Queries must be structures")

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

def test():
    define_fact_or_rule('padre(juan, jose)', [])
    define_fact_or_rule('padre(jose, pablo)', [])
    define_fact_or_rule('padre(pablo, gaby)', [])
    define_fact_or_rule('ancestro(X, Y)', ['padre(X, Y)'])
    define_fact_or_rule('ancestro(X, Y)', ['padre(X, Z)', 'ancestro(Z, Y)'])

    print("\nRealizando consultas:")
    handle_query('ancestro(gaby, X)')
    handle_query('padre(juan, jose)')
    handle_query('ancestro(juan, X)')

# Interfaz de usuario
def main():
    while True:
        user_input = input("Ingrese una acción (DEF, ASK, SALIR): ")
        if user_input.startswith("DEF"):
            _, expression, *antecedents = user_input.split()
            print(expression)
            define_fact_or_rule(expression, antecedents)
        elif user_input.startswith("ASK"):
            _, expression = user_input.split(maxsplit=1)
            handle_query(expression)
        elif user_input == "SALIR":
            break
        elif user_input == "test":
            test()
        else:
            print("Acción no reconocida")

if __name__ == "__main__":
    main()