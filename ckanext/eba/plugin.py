import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from flask import Blueprint, render_template

def hello_plugin():
    return u'Hello from the EBA Theme extension'

class EbaPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.IAuthFunctions)
    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('assets',
            'eba')

    def get_blueprint(self):
        u'''Return a Flask Blueprint object to be registered by the app.'''
        # Create Blueprint for plugin
        blueprint = Blueprint(self.name, self.__module__)
        blueprint.template_folder = u'templates'
        # Add plugin url rules to Blueprint object
        blueprint.add_url_rule('/hello_plugin', '/hello_plugin', hello_plugin)
        return blueprint

#     def get_auth_functions(self):
#         """ Override the 'related' auth functions.
#         """
#         auth_functions = {
#             "user_list": auth.user_list
#         }

# def user_list(context, data_dict=None):
#     """ Check whether access to the user list is authorized
#     """
#     return {'success': _request_is_admin(context)}

# def _request_is_admin(context):
    
#     requester = context.get('user')
#     return _has_user_permission_for_some_group(requester, )

@toolkit.auth_allow_anonymous_access
def custom_user_list_auth(context, data_dict):
    # Only sysadmins should be able to see the user list
    return {'success': False}