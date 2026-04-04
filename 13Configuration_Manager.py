def add_setting(settings_dict, pair_tupls):
    key, value = pair_tupls
    key = key.lower()
    value = value.lower()
    #checkking existence of the key in settings
    if key in settings_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings_dict[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"
# function to update user settings
def update_setting(settings_dict, pair_tupls):
    key, value = pair_tupls
    key = key.lower()
    value = value.lower()
    #checkking existence of the key in settings
    if key in settings_dict:
        settings_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
#deleting a setting
def delete_setting(settings_dict, passed_key):
    key = passed_key
    key = key.lower()
    if key in settings_dict:
        del settings_dict[key] 
        return f"Setting '{key}' deleted successfully!"
    return f"Setting not found!"
#To view the settings
def view_settings(settings_dict):
    if not settings_dict:
        return "No settings available."
    output = 'Current User Settings:'
    for key, value in settings_dict.items():
        output += f"\n{key.capitalize()}: {value}"
    return output + '\n'
    

test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}

add_setting({'theme': 'light'}, ('THEME', 'dark')) 










      
