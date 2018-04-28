import logging
from django.template.loader import *
from django.template.loader import get_template as _get_single_template
from django.template.loader import _dirs_undefined

log = logging.getLogger(__name__)


def get_template(template_name, dirs=_dirs_undefined, using=None, extension_name=None):
    if extension_name:
        try:
            full_name = "{}/{}".format(extension_name, template_name)
            return _get_single_template(full_name, dirs=dirs, using=using)
        except TemplateDoesNotExist as e:
            log.error("Failed to found template '{}' for extension '{}'".format(template_name, extension_name))
    return _get_single_template(template_name, dirs=dirs, using=using)
