# -- coding: utf-8 --
"""

Created on: 19/10/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pytest


from application.app import create_app


@pytest.fixture
def app():
    app = create_app("testing")

    return app