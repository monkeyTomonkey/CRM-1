from django.template import Library
from django.utils.safestring import mark_safe
from django.shortcuts import reverse

from thanos.service.crm import site

register = Library()


@register.inclusion_tag('thanos/add_change_form.html')
def show_form(config_obj, modelform):
    from django.forms.boundfield import BoundField
    from django.db.models.query import QuerySet
    from django.forms.models import ModelChoiceField, ModelMultipleChoiceField

    new_form = []
    for bound_field in modelform:
        info_dict = {"popUp": False, "popUp_url": None, "bound_field": bound_field}

        ## 只有符合条件的字段才能有添加按钮、使用popUp
        # 符合条件的字段在ModelForm中表现为ModelChoiceField或其子类，在Model中表现为FK和M2M类
        field_obj = bound_field.field
        if isinstance(field_obj, ModelChoiceField):
            rel_class_name = field_obj.queryset.model  # 例：models.Department
            if rel_class_name in site._registry:
                info = (rel_class_name._meta.app_label, rel_class_name._meta.model_name)
                base_url = reverse('%s_%s_add' % info)

                current_related_name = config_obj.model_class._meta.get_field(bound_field.name).rel.related_name
                current_model_name = config_obj.model_name

                popUp_url = '{}?popback_id={}&related_name={}&model_name={}'.format(base_url, bound_field.auto_id,
                                                                                    current_related_name,
                                                                                    current_model_name)

                info_dict["popUp"] = True
                info_dict["popUp_url"] = popUp_url

        new_form.append(info_dict)

    return {"add_change_form": new_form}
