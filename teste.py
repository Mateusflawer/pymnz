import pymnz


def soma(a, b):
    result = a + b
    print(f"A soma de {a} + {b} é {result}.")
    return result


def subtracao(a, b):
    result = a - b
    print(f"A subtração de {a} - {b} é {result}.")
    return result


if __name__ == "__main__":
    function_executor = pymnz.models.FunctionExecutor()
    function_executor.add_function(soma)
    function_executor.execute_all(b=1, a=2)
    function_executor.clear_results()

    # Executar funções
    function_executor.add_function(subtracao)
    function_executor.execute_all(10, 11)
    function_executor.clear_results()
