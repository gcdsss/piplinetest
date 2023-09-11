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


def modify_header1(
    test_class: BasePipLineTest, test_step: BaseTestStep, http_res_dict: dict = {}
):
    """modify http header

    Args:
        test_class (BasePipLineTest): _description_
        test_step (BaseTestStep): _description_
        http_res_dict (dict, optional): _description_. Defaults to {}.
    """
    test_step.headers["test1"] = "1"


def modify_header2(
    test_class: BasePipLineTest, test_step: BaseTestStep, http_res_dict: dict = {}
):
    """modify http header

    Args:
        test_class (BasePipLineTest): _description_
        test_step (BaseTestStep): _description_
        http_res_dict (dict, optional): _description_. Defaults to {}.
    """
    test_step.headers["test2"] = "2"


def modify_test_class_attribute(
    test_class: BasePipLineTest, test_step: BaseTestStep, http_res_dict: dict = {}
):
    test_class.user_name = "test1"
