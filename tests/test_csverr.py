import pytest

from utils.csverror import InstantiateCSVError


def test_csv_err_raise():
    with pytest.raises(InstantiateCSVError):
        raise InstantiateCSVError()
    with pytest.raises(InstantiateCSVError, match="Файл поврежден"):
        raise InstantiateCSVError("Файл поврежден")
