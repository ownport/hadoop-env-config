import os
import pytest

from hadoop_env_config import env_config

def get_abspath_test_path():

    return os.path.dirname(os.path.abspath(__file__))

def get_settings_path():

    return os.path.join(get_abspath_test_path(), 'resources/settings/')


@pytest.fixture(params=['hdp-with-server.settings', 'hdp-wo-server.settings'])
def hdp_settings_path(request):

    return os.path.join(get_settings_path(), request.param)


@pytest.fixture(params=['hdp-with-server.settings', 'hdp-wo-server.settings'])
def hdp_settings_path(request):

    return os.path.join(get_settings_path(), request.param)


def test_env_config_undefined_settings():

    with pytest.raises(env_config.UndefinedSettingsFile):
        conf = env_config.HadoopEnvConfig(None)


def test_env_config_empty_settings():

    with pytest.raises(env_config.IncorrectJsonFormat):
        conf = env_config.HadoopEnvConfig(os.path.join(get_settings_path(), 'empty.settings'))

def test_env_config_incorrect_path_to_settings():

    with pytest.raises(env_config.IncorrectJsonFormat):
        conf = env_config.HadoopEnvConfig(os.path.join(get_settings_path(), 'shadow.settings'))


def test_hadoop_env_config_init(hdp_settings_path):

    conf = env_config.HadoopEnvConfig(hdp_settings_path)
