import sublime, sublime_plugin, json
from pprint import pprint


class OpenlocationPromptCommand(sublime_plugin.WindowCommand):

    def run(self):
        settings = sublime.load_settings('OpenLocation.sublime-settings')
        with open(settings.get('settingsPath')) as json_data:
            self.settings_json = json.load(json_data)
            json_data.close()
            d = self.settings_json['folderAliases'].copy()
            d.update(self.settings_json['fileAliases'])
            self.aliasKeys = sorted(d.keys())
            sublime.active_window().show_quick_panel(self.aliasKeys, self.on_done)

    def on_done(self, selected):
        if self.aliasKeys[selected] in self.settings_json['folderAliases']:
            path = self.settings_json['folderAliases'][self.aliasKeys[selected]]
            sublime.run_command("new_window")
            d = {'folders': [{'follow_symlinks': True, 'path': path}]}
            sublime.active_window().set_project_data(d)
        else:
            path = self.settings_json['fileAliases'][self.aliasKeys[selected]]
            self.window.open_file(path)
