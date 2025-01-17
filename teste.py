import pymnz


@pymnz.utils.errors.retry_on_failure(10)
def main():
    print('Vou dar erro em seguida')
    raise Exception('Erro de exemplo')


if __name__ == "__main__":
    pymnz.models.Script('Bot test', main).run()
