#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : tql-App.
# @File         : app_run
# @Time         : 2020/11/5 4:48 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  :
"""
'console_scripts': [
    'app-run=iapp.app_run.run:run'
]
"""
import os
import fire
from pathlib import Path
from iapp.utils import get_module_path


class AppRun(object):
    """doc"""

    def __init__(self, **kwargs):
        pass

    def apps_list(self, apps='apps'):
        """
        apps apps_streamlit
        """
        return list(Path(get_module_path(f'../{apps}', __file__)).glob('*app.py'))

    def fastapi(self, app_name, nohup=0):
        app_file = list(Path(get_module_path('../apps', __file__)).glob(f'*{app_name}*'))[0]
        cmd = f"python {app_file}"
        self._run_cmd(cmd, nohup)

    def streamlit(self, app_name, port=8888, nohup=0):
        app_file = list(Path(get_module_path('../apps_streamlit', __file__)).glob(f'*{app_name}*'))[0]
        cmd = f"streamlit run {app_file} --server.baseUrlPath web --server.port {port}"
        self._run_cmd(cmd, nohup)

    def _run_cmd(self, cmd, nohup=0):
        cmd = f"nohup {cmd} &" if nohup else cmd
        return os.system(cmd)


def cli():
    fire.Fire(AppRun)


if __name__ == '__main__':
    print(AppRun().apps_list())
