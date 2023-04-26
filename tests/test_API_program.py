from src.main import analyse_responses
from src.main import get_response

def test_analyse_func():

    success = True

    results = analyse_responses(get_response("2021-01"))

    for result in results:
        if result == 0:
            success = False

    assert success

