from behave import *

use_step_matcher("re")



@when("write a Hello world program")
def step_impl(context):
    global s
    """
    :type context: behave.runner.Context
    """
    s = "Hello world"
    print(s)
    # assert "Hello world", context
    raise NotImplementedError(u'STEP: When write a Hello world program')


@then("verify the Hello world string")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert s == "Hello world"
    raise NotImplementedError(u'STEP: Then verify the Hello world string')