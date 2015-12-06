import sublime, sublime_plugin

class NumberfyPromptCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.window.show_input_panel("Start Index:", "0", self.on_done, None, None)
        pass

    def on_done(self, text):
        try:
            dec = text.endswith("-")
            if dec:
                text = text[:len(text)-1]
            idx = int(text)
            if self.window.active_view():
                self.window.active_view().run_command("numberfy", {"idx": idx, "dec": dec} )
        except ValueError:
            pass

class NumberfyCommand(sublime_plugin.TextCommand):

    def run(self, edit, idx, dec):
        for region in self.view.sel():
            self.view.replace(edit, region, str(idx))
            idx = idx - 1 if dec else idx + 1
