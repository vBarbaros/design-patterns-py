# source : https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_abstract_factory.htm
# with small adaptations to keep same style across examples


class Window:
    __toolkit = ""
    __purpose = ""

    def __init__(self, toolkit, purpose):
        self.__toolkit = toolkit
        self.__purpose = purpose

    def getToolkit(self):
        return self.__toolkit

    def getType(self):
        return self.__purpose


class GtkToolboxWindow(Window):
    def __init__(self):
        Window.__init__(self, "Gtk", "ToolboxWindow")


class GtkLayersWindow(Window):
    def __init__(self):
        Window.__init__(self, "Gtk", "LayersWindow")


class GtkMainWindow(Window):
    def __init__(self):
        Window.__init__(self, "Gtk", "MainWindow")


class QtToolboxWindow(Window):
    def __init__(self):
        Window.__init__(self, "Qt", "ToolboxWindow")


class QtLayersWindow(Window):
    def __init__(self):
        Window.__init__(self, "Qt", "LayersWindow")


class QtMainWindow(Window):
    def __init__(self):
        Window.__init__(self, "Qt", "MainWindow")


class AbstractFactoryUI:
    def getToolboxWindow(self): pass

    def getLayersWindow(self): pass

    def getMainWindow(self): pass


class GtkUIFactory(AbstractFactoryUI):
    def getToolboxWindow(self):
        return GtkToolboxWindow()

    def getLayersWindow(self):
        return GtkLayersWindow()

    def getMainWindow(self):
        return GtkMainWindow()


class QtUIFactory(AbstractFactoryUI):
    def getToolboxWindow(self):
        return QtToolboxWindow()

    def getLayersWindow(self):
        return QtLayersWindow()

    def getMainWindow(self):
        return QtMainWindow()


def client(factory: AbstractFactoryUI) -> None:
    main = factory.getMainWindow()
    layers = factory.getLayersWindow()
    toolbox = factory.getToolboxWindow()

    print(f"{main.getToolkit()} : {main.getType()}")
    print(f"{layers.getToolkit()} : {layers.getType()}")
    print(f"{toolbox.getToolkit()} : {toolbox.getType()}")


if __name__ == "__main__":
    print("\nClient: Testing client code with Factory Type GtkUIFactory:")
    client(GtkUIFactory())

    print("\nClient: Testing client code with Factory Type QtUIFactory:")
    client(QtUIFactory())