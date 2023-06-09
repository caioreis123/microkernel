# Core system
class Kernel:
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, plugin):
        self.plugins[name] = plugin

    def unregister_plugin(self, name):
        del self.plugins[name]

    def run(self):
        for name, plugin in self.plugins.items():
            print(f"Running plugin: {name}")
            plugin.run()


# Plugin module
class HelloWorldPlugin:
    def run(self):
        print("Hello World!")


class ByePlugin:
    def run(self):
        print("Bye!")


# Main program
if __name__ == "__main__":
    core = Kernel()
    core.register_plugin("HelloWorld", HelloWorldPlugin())
    core.register_plugin("Bye", ByePlugin())
    core.run()
