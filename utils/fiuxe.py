import pytest

@pytest.fixture(params=[[1,2],[2,3],[3,4]])
def test_data(request):

    return request.param

def test_not_2(test_data):
    print('test_data: %s' % test_data)
    assert test_data == [1,2]


