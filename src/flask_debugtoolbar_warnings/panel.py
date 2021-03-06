# -*- utf-8 -*-
"""
    flask_debugtoolbar_warnings.panel
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Warnings tracking panel

    :copyright: (c) 2018 the FlaskBB Team
    :license: MIT, see LICENSE for more details
"""

import jinja2
from flask_debugtoolbar.panels import DebugPanel


class WarningsPanel(DebugPanel):
    name = "Warnings"

    def __init__(self, *args, **kwargs):
        super(WarningsPanel, self).__init__(*args, **kwargs)
        self.jinja_env.loader = jinja2.ChoiceLoader(
            [
                self.jinja_env.loader,
                jinja2.PrefixLoader(
                    {
                        "debug_tb_warnings": jinja2.PackageLoader(
                            __name__, "templates"
                        )
                    }
                ),
            ]
        )

    @property
    def has_content(self):
        return True

    def nav_title(self):
        return "Warnings"

    def nav_subtitle(self):
        count = 0
        title = "Warning" if 0 < count < 2 else "Warnings"
        return "{} {}".format(count, title)

    def title(self):
        return "Warnings Captured"

    def url(self):
        return ""

    def content(self):
        self.render("debug_tb_warnings/warnings-panel.html", context={})

    def process_request(self, request):
        pass

    def process_response(self, request, response):
        pass
