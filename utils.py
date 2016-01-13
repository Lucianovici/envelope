# -*- coding: utf-8 -*-
"""
Utils.
"""
from lxml import etree
import re
import settings


class ConfirmationPageParser(object):

    @staticmethod
    def get_edit_last_response_form_params(html):
        edit_last_record_params = ''

        parser = etree.HTMLParser()
        tree = etree.fromstring(html, parser)
        element_list = tree.xpath('//a[contains(@href,"edit")]/@href')
        if element_list:
            match_params = re.search(r'\?(.*?)$', element_list[0])
            if match_params:
                edit_last_record_params = match_params.groups()[0]

        return edit_last_record_params

    @staticmethod
    def is_entry_recorded_for(html_response):
        return settings.GOOGLE_DOCS_FORM_SUCCESSFUL_RESPONSE_MESSAGE in html_response
