from piplinetest import BasePipLineTest, BaseTestStep


def process_nothing(
    test_class: BasePipLineTest, test_step: BaseTestStep, http_res_dict: dict
):
    """_summary_

    Args:
        test_class (BasePipLineTest): test_class
        test_step (BaseTestStep): test_step
        http_res_dict (dict): http res json dict

    Returns:
        _type_: _description_
    """
    print(test_class.dict())
    print(test_step.dict())
    return ""


def add_something_to_test_step_header(
    test_class: BasePipLineTest, test_step: BaseTestStep, http_res_dict: dict
):
    """_summary_

    Args:
        test_class (BasePipLineTest): test_class
        test_step (BaseTestStep): test_step
        http_res_dict (dict): http res json dict

    Returns:
        _type_: _description_
    """
    test_step.headers = {"test": 1}
    return ""


def add_http_token_to_headers(
    test_class: BasePipLineTest, test_step: BaseTestStep, http_res_dict: dict
):
    """_summary_

    Args:
        test_class (BasePipLineTest): test_class
        test_step (BaseTestStep): test_step
        http_res_dict (dict): http res json dict

    Returns:
        _type_: _description_
    """
    token = http_res_dict["access_token"]
    test_step.headers = {"Authorization": f"bearer {token}"}
