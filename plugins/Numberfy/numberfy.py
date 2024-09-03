import sublime, sublime_plugin

class NumberfyPromptCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.window.show_input_panel("Start Index:", "0", self.on_done, None, None)
        pass

    def on_done(self, text):
        try:
            dec = text.endswith("-")
            leftpad = None
            rmax = None
            if dec:
                text = text[:len(text)-1]
            if "%" in text:
                pparts = text.split("%")
                text = pparts[0]
                leftpad = int(pparts[1])
            if ":" in text:
                rparts = text.split(":")
                idx = int(rparts[0])
                rmax = int(rparts[1])
            else:
                idx = int(text)
            if self.window.active_view():
                self.window.active_view().run_command("numberfy", {"idx": idx, "dec": dec, "leftpad": leftpad, "rmin": idx, "rmax": rmax} )
        except ValueError:
            pass

class NumberfyCommand(sublime_plugin.TextCommand):

    def run(self, edit, idx, dec, leftpad, rmin, rmax):
        for region in self.view.sel():
            self.view.replace(edit, region, str(idx).zfill(leftpad) if leftpad else str(idx))
            idx = idx - 1 if dec else idx + 1
            if (rmax):
                if dec:
                    if idx < rmax:
                        idx = rmin
                else:
                    if idx > rmax:
                        idx = rmin

