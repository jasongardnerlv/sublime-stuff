import sublime, sublime_plugin, uuid
from datetime import datetime

class DatagenPromptCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.cmdKeys = [
            ["Date","Outputs the current datetime in ISO 8601"],
            ["Guid","Outputs a Guid in RFC 4122"],
            ["Warm","Outputs the guid for Warm Springs location"]
        ]
        sublime.active_window().show_quick_panel(self.cmdKeys, self.on_done)

    def on_done(self, selected):
        self.window.active_view().run_command("datagen", {"selected": selected})


class DatagenCommand(sublime_plugin.TextCommand):

    def run(self, edit, selected):
        if selected == 0:
            dateStr = datetime.now().isoformat()
            for region in self.view.sel():
                self.view.replace(edit, region, dateStr)
        if selected == 1:
            for region in self.view.sel():
                self.view.replace(edit, region, str(uuid.uuid4()))
        if selected == 2:
            for region in self.view.sel():
                self.view.replace(edit, region, "63600e89-1eb7-444b-8163-41925110db94")
