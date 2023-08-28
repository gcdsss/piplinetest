from piplinetest import BasePipLineTest, BaseTestStep


def process_nothing(piplinetest: BasePipLineTest, test_step: BaseTestStep):
    """_summary_

    Args:
        piplinetest_dict (dict): _description_
        test_step (dict): _description_

    Returns:
        _type_: _description_
    """
    print(piplinetest)
    print(test_step)
    return ""


def modify_body(piplinetest: BasePipLineTest, test_step: BaseTestStep):
    """_summary_

    Args:
        piplinetest_dict (dict): _description_
        test_step (dict): _description_

    Returns:
        _type_: _description_
    """
    test_step.body["test"] = 1
