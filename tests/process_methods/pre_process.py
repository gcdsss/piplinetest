from piplinetest import BasePipLineTest, BaseTestStep


def process_nothing(
    test_class: BasePipLineTest, test_step: BaseTestStep, http_res_dict: dict = {}
):
    """_summary_

    Args:
        piplinetest_dict (dict): _description_
        test_step (dict): _description_

    Returns:
        _type_: _description_
    """
    print(test_class)
    print(test_step)
    return ""


def modify_body(
    test_class: BasePipLineTest, test_step: BaseTestStep, http_res_dict: dict = {}
):
    """_summary_

    Args:
        piplinetest_dict (dict): _description_
        test_step (dict): _description_

    Returns:
        _type_: _description_
    """
    test_step.body["test"] = 1


def send_http_token(
    test_class: BasePipLineTest, test_step: BaseTestStep, http_res_dict: dict = {}
):
    test_step.body["username"] = test_class.username
    test_step.body["password"] = test_class.password
