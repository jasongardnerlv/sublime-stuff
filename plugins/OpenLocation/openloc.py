import sublime, sublime_plugin

class OpenlocationPromptCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.window.show_input_panel("Location Key:", "", self.on_done, None, None)
        pass

    def on_done(self, text):
        settings = sublime.load_settings('OpenLocation.sublime-settings')
        if settings.has(text):
            path = settings.get(text)
            sublime.run_command("new_window")
            d = {'folders': [{'follow_symlinks': True, 'path': path}]}
            sublime.active_window().set_project_data(d)
        else:
            sublime.error_message('Unrecognized location key: ' + text)
