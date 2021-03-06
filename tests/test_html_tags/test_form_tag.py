# -*- coding: utf-8 -*-

import pytest

from ..fixtures import parametrize

from korona.html.tags import Form
from korona.templates.html.tags import form
from korona.exceptions import TagAttributeError


@parametrize('attributes', [
    ({'text': 'abcd'}),
    ({'action': 'demo.asp',
      'method': 'get',
      'name': 'name1',
      'target': '_top'}),
    ({'novalidate': True}),
    ({'method': 'post', 'enctype': 'text/plain'})
])
def test_construct_form_tag(attributes):
    """Test for validating whether the form tag is constructed correctly or
    not.
    """
    form_ = Form(**attributes)
    assert form_.construct() == form.render(attributes)


@parametrize('attributes,exception,error_msg', [
    ({'enctype': 'text/plain', 'method': 'get'},
     AttributeError,
     'enctype attribute can be used/set only if method'),
    ({'method': 'post', 'enctype': 'plain'},
     TagAttributeError,
     'attribute values should be one of these'),
    ({'autocomplete': 'false'},
     TagAttributeError,
     'attribute values should be one of these'),
    ({'method': 'PUT'},
     TagAttributeError,
     'attribute values should be one of these')
])
def test_construct_form_tag_error(attributes, exception, error_msg):
    """Test for validating form tag's attributes."""
    with pytest.raises(exception) as exc:
        Form(**attributes)

    assert error_msg in str(exc)
